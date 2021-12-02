﻿

namespace Gui
{
    using System;
    using System.Diagnostics.CodeAnalysis;
    using System.Threading.Tasks;
    using System.Windows.Forms;

    using MessageBroker;

    using MessageTemplates;

    /// <summary>
    /// The main form for the application
    /// </summary>
    public partial class MainForm : Form
    {
        /// <summary>
        /// The publisher.
        /// </summary>
        private Sender rmqSender;

        /// <summary>
        /// Consumes messages.
        /// </summary>
        private Consumer consumer;

        /// <summary>
        /// Initializes a new instance of the <see cref="MainForm"/> class.
        /// </summary>
        public MainForm()
        {
            this.InitializeComponent();
            this.InitEventListeners();
            this.StartConsumer();
            this.rmqSender.Initialize();
        }

        /// <summary>
        /// Starts subscriber for predictions
        /// </summary>
        private void StartConsumer()
        {
            var hostName = this.textBoxUsername.Text;
            var username = this.textBoxUsername.Text;
            var password = this.textBoxPassword.Text;
            const string Queue = "resp_stock";
            this.consumer = new Consumer(hostName, Queue, username, password);
            this.consumer.Initialize();
            Task.Run(() => this.consumer.Consume());
        }

        /// <summary>
        /// Starts the sender.
        /// </summary>
        private void StartSender()
        {
            var hostname = this.textBoxHostname.Text;
            this.rmqSender = new Sender(hostname);
            this.rmqSender.Initialize();
        }

        /// <summary>
        /// Initializes the events to run methods when triggered.
        /// </summary>
        private void InitEventListeners()
        {
            CustomEvents.UpdateGui.UpdateStockEvent += this.UpdateGui;
            CustomEvents.CustomDisplayError.DisplayErrorEvent += this.ShowErrorMessage;
        }

        /// <summary>
        /// Updates GUI with new predictions.
        /// </summary>
        /// <param name="returnedMessage">the returned message from backend.</param>
        private void UpdateGui(StockMessage returnedMessage)
        {
            this.UpdateStockPredictions(returnedMessage.ModelConfidence);
            this.UpdateGraph(returnedMessage.GraphLocation);
        }

        /// <summary>
        /// Displays an error message in a message box.
        /// </summary>
        /// <param name="errorMessage">The message to display, it is stored in the model confidence parameter</param>
        private void ShowErrorMessage(string errorMessage)
        {
            const string Title = "Error";
            MessageBox.Show(errorMessage,acp Title);
        }

        /// <summary>
        /// Updates the GUI to display predictions
        /// </summary>
        /// <param name="confidenceOfModel">the confidence of the model used.</param>
        private void UpdateStockPredictions(string confidenceOfModel)
        {
            if (this.richTextBoxPredictions.InvokeRequired)
            {
                this.richTextBoxPredictions.Invoke((MethodInvoker)delegate
                {
                    var timeOfMessage = DateTime.Now.ToString("HH:mm:ss.fff");
                    this.richTextBoxPredictions.AppendText($"\nReceived at: {timeOfMessage}\n{confidenceOfModel}");
                });
            }
            else
            {
                this.richTextBoxPredictions.Text += DateTime.Now.ToString("mm:ss.fff");
                var timeOfMessage = DateTime.Now.ToString("HH:mm:ss.fff");
                this.richTextBoxPredictions.AppendText($"\nReceived at: {timeOfMessage}\n{confidenceOfModel}");
            }
        }

        /// <summary>
        /// updates the picture box with generated graph of predictions
        /// </summary>
        /// <param name="location">the file path of the graph</param>
        private void UpdateGraph(string location)
        {
            if (this.pictureBoxGraph.InvokeRequired)
            {
                this.pictureBoxGraph.ImageLocation = location;
                this.pictureBoxGraph.SizeMode = PictureBoxSizeMode.StretchImage;
            }
            else
            {
                this.pictureBoxGraph.ImageLocation = location;
                this.pictureBoxGraph.SizeMode = PictureBoxSizeMode.StretchImage;
            }
        }

        /// <summary>
        /// Hooks onto buttonPredict click event
        /// </summary>
        /// <param name="sender">The context</param>
        /// <param name="e">event arguments</param>
        [SuppressMessage("StyleCop.CSharp.NamingRules", "SA1300:ElementMustBeginWithUpperCaseLetter", Justification = "Auto-generated by IDE")]
        private void buttonPredict_Click(object sender, EventArgs e)
        {
            var ticker = this.textBoxEnterTicker.Text;
            var source = this.comboBoxInfoSource.Text;
            var modelType = this.comboBoxModelType.Text;
            if(!this.UserEnteredDataOk(ticker, source, modelType))
            {
                return;
            }
            var message = JsonSerializer.SerializeMessageToSend(new MessageToSend(ticker, source, modelType));
           
            this.rmqSender.GetPredictions(message);
        }

        /// <summary>
        /// Guard clauses for entering stock data.
        /// </summary>
        /// <param name="ticker">the ticker</param>
        /// <param name="source">the source</param>
        /// <param name="modelType">the model type</param>
        /// <returns>If the data is proceedable</returns>
        [SuppressMessage("StyleCop.CSharp.DocumentationRules", "SA1650:ElementDocumentationMustBeSpelledCorrectly", Justification = "Reviewed. Suppression is OK here.")]
        private bool UserEnteredDataOk(string ticker, string source, string modelType)
        {
            const string Title = "Error"; 

            if (ticker == string.Empty)
            {
                MessageBox.Show(@"Please enter a Ticker in the box, example: AAPL", Title);
                return false;
            }

            if (source == string.Empty)
            {
                MessageBox.Show(@"Please select an information source.", Title);
                return false;
            }

            if (modelType == string.Empty)
            {
                MessageBox.Show(@"Please select a model to use.", Title);
                return false;
            }

            return true;
        }

        /// <summary>
        /// The event handler for when the apply config button is pressed.
        /// </summary>
        /// <param name="sender">The context</param>
        /// <param name="e">The event arguments</param>
        [SuppressMessage("StyleCop.CSharp.NamingRules", "SA1300:ElementMustBeginWithUpperCaseLetter", Justification = "Reviewed. Suppression is OK here.")]
        private void buttonApplyConfig_Click(object sender, EventArgs e)
        {
            this.consumer.Dispose();
            this.rmqSender.Dispose();
            this.StartConsumer();
            this.StartSender();
        }
    }
}
