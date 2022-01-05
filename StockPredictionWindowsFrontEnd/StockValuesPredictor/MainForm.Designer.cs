
namespace StockValuesPredictor
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.tabControlMenu = new System.Windows.Forms.TabControl();
            this.EnterStockInfoPage = new System.Windows.Forms.TabPage();
            this.panel1 = new System.Windows.Forms.Panel();
            this.comboBoxModelType = new System.Windows.Forms.ComboBox();
            this.richTextBoxPredictions = new System.Windows.Forms.RichTextBox();
            this.comboBoxInfoSource = new System.Windows.Forms.ComboBox();
            this.buttonPredict = new System.Windows.Forms.Button();
            this.textBoxEnterTicker = new System.Windows.Forms.TextBox();
            this.tabPageGraph = new System.Windows.Forms.TabPage();
            this.pictureBoxGraph = new System.Windows.Forms.PictureBox();
            this.tabPageConfiguration = new System.Windows.Forms.TabPage();
            this.labelPassword = new System.Windows.Forms.Label();
            this.textBoxPassword = new System.Windows.Forms.TextBox();
            this.labelUsername = new System.Windows.Forms.Label();
            this.textBoxUsername = new System.Windows.Forms.TextBox();
            this.buttonApplyConfig = new System.Windows.Forms.Button();
            this.labelHostname = new System.Windows.Forms.Label();
            this.textBoxHostname = new System.Windows.Forms.TextBox();
            this.tabControlMenu.SuspendLayout();
            this.EnterStockInfoPage.SuspendLayout();
            this.panel1.SuspendLayout();
            this.tabPageGraph.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxGraph)).BeginInit();
            this.tabPageConfiguration.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControlMenu
            // 
            this.tabControlMenu.Alignment = System.Windows.Forms.TabAlignment.Bottom;
            this.tabControlMenu.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControlMenu.Controls.Add(this.EnterStockInfoPage);
            this.tabControlMenu.Controls.Add(this.tabPageGraph);
            this.tabControlMenu.Controls.Add(this.tabPageConfiguration);
            this.tabControlMenu.Location = new System.Drawing.Point(0, 0);
            this.tabControlMenu.Name = "tabControlMenu";
            this.tabControlMenu.SelectedIndex = 0;
            this.tabControlMenu.Size = new System.Drawing.Size(847, 450);
            this.tabControlMenu.TabIndex = 0;
            // 
            // EnterStockInfoPage
            // 
            this.EnterStockInfoPage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.EnterStockInfoPage.Controls.Add(this.panel1);
            this.EnterStockInfoPage.Location = new System.Drawing.Point(4, 4);
            this.EnterStockInfoPage.Name = "EnterStockInfoPage";
            this.EnterStockInfoPage.Padding = new System.Windows.Forms.Padding(3);
            this.EnterStockInfoPage.Size = new System.Drawing.Size(839, 422);
            this.EnterStockInfoPage.TabIndex = 0;
            this.EnterStockInfoPage.Text = "Enter Stock To Predict";
            this.EnterStockInfoPage.UseVisualStyleBackColor = true;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.comboBoxModelType);
            this.panel1.Controls.Add(this.richTextBoxPredictions);
            this.panel1.Controls.Add(this.comboBoxInfoSource);
            this.panel1.Controls.Add(this.buttonPredict);
            this.panel1.Controls.Add(this.textBoxEnterTicker);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(3, 3);
            this.panel1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(831, 414);
            this.panel1.TabIndex = 0;
            // 
            // comboBoxModelType
            // 
            this.comboBoxModelType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxModelType.FormattingEnabled = true;
            this.comboBoxModelType.Items.AddRange(new object[] {
            "linear regression",
            "polynomial regression 2d",
            "polynomial regression 3d",
            "k nearest neighbour",
            "arima"});
            this.comboBoxModelType.Location = new System.Drawing.Point(37, 124);
            this.comboBoxModelType.Name = "comboBoxModelType";
            this.comboBoxModelType.Size = new System.Drawing.Size(233, 23);
            this.comboBoxModelType.TabIndex = 11;
            // 
            // richTextBoxPredictions
            // 
            this.richTextBoxPredictions.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.richTextBoxPredictions.Location = new System.Drawing.Point(319, 0);
            this.richTextBoxPredictions.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.richTextBoxPredictions.Name = "richTextBoxPredictions";
            this.richTextBoxPredictions.ReadOnly = true;
            this.richTextBoxPredictions.Size = new System.Drawing.Size(512, 415);
            this.richTextBoxPredictions.TabIndex = 10;
            this.richTextBoxPredictions.Text = "";
            // 
            // comboBoxInfoSource
            // 
            this.comboBoxInfoSource.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxInfoSource.FormattingEnabled = true;
            this.comboBoxInfoSource.Items.AddRange(new object[] {
            "yahoo"});
            this.comboBoxInfoSource.Location = new System.Drawing.Point(37, 180);
            this.comboBoxInfoSource.Name = "comboBoxInfoSource";
            this.comboBoxInfoSource.Size = new System.Drawing.Size(233, 23);
            this.comboBoxInfoSource.TabIndex = 9;
            // 
            // buttonPredict
            // 
            this.buttonPredict.Location = new System.Drawing.Point(93, 220);
            this.buttonPredict.Name = "buttonPredict";
            this.buttonPredict.Size = new System.Drawing.Size(115, 38);
            this.buttonPredict.TabIndex = 8;
            this.buttonPredict.Text = "Predict";
            this.buttonPredict.UseVisualStyleBackColor = true;
            this.buttonPredict.Click += new System.EventHandler(this.buttonPredict_Click);
            // 
            // textBoxEnterTicker
            // 
            this.textBoxEnterTicker.BackColor = System.Drawing.SystemColors.Window;
            this.textBoxEnterTicker.Location = new System.Drawing.Point(37, 151);
            this.textBoxEnterTicker.Name = "textBoxEnterTicker";
            this.textBoxEnterTicker.Size = new System.Drawing.Size(233, 23);
            this.textBoxEnterTicker.TabIndex = 7;
            this.textBoxEnterTicker.Text = "Enter Stock Ticker";
            // 
            // tabPageGraph
            // 
            this.tabPageGraph.Controls.Add(this.pictureBoxGraph);
            this.tabPageGraph.Location = new System.Drawing.Point(4, 4);
            this.tabPageGraph.Name = "tabPageGraph";
            this.tabPageGraph.Padding = new System.Windows.Forms.Padding(3);
            this.tabPageGraph.Size = new System.Drawing.Size(839, 422);
            this.tabPageGraph.TabIndex = 1;
            this.tabPageGraph.Text = "Prediction Graph";
            this.tabPageGraph.UseVisualStyleBackColor = true;
            // 
            // pictureBoxGraph
            // 
            this.pictureBoxGraph.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxGraph.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBoxGraph.Location = new System.Drawing.Point(3, 3);
            this.pictureBoxGraph.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.pictureBoxGraph.Name = "pictureBoxGraph";
            this.pictureBoxGraph.Size = new System.Drawing.Size(833, 416);
            this.pictureBoxGraph.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxGraph.TabIndex = 0;
            this.pictureBoxGraph.TabStop = false;
            // 
            // tabPageConfiguration
            // 
            this.tabPageConfiguration.Controls.Add(this.labelPassword);
            this.tabPageConfiguration.Controls.Add(this.textBoxPassword);
            this.tabPageConfiguration.Controls.Add(this.labelUsername);
            this.tabPageConfiguration.Controls.Add(this.textBoxUsername);
            this.tabPageConfiguration.Controls.Add(this.buttonApplyConfig);
            this.tabPageConfiguration.Controls.Add(this.labelHostname);
            this.tabPageConfiguration.Controls.Add(this.textBoxHostname);
            this.tabPageConfiguration.Location = new System.Drawing.Point(4, 4);
            this.tabPageConfiguration.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPageConfiguration.Name = "tabPageConfiguration";
            this.tabPageConfiguration.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPageConfiguration.Size = new System.Drawing.Size(839, 422);
            this.tabPageConfiguration.TabIndex = 2;
            this.tabPageConfiguration.Text = "Configuration";
            this.tabPageConfiguration.UseVisualStyleBackColor = true;
            // 
            // labelPassword
            // 
            this.labelPassword.AutoSize = true;
            this.labelPassword.Location = new System.Drawing.Point(52, 142);
            this.labelPassword.Name = "labelPassword";
            this.labelPassword.Size = new System.Drawing.Size(57, 15);
            this.labelPassword.TabIndex = 6;
            this.labelPassword.Text = "Password";
            // 
            // textBoxPassword
            // 
            this.textBoxPassword.Location = new System.Drawing.Point(52, 165);
            this.textBoxPassword.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.textBoxPassword.Name = "textBoxPassword";
            this.textBoxPassword.Size = new System.Drawing.Size(110, 23);
            this.textBoxPassword.TabIndex = 5;
            this.textBoxPassword.Text = "guest";
            // 
            // labelUsername
            // 
            this.labelUsername.AutoSize = true;
            this.labelUsername.Location = new System.Drawing.Point(52, 84);
            this.labelUsername.Name = "labelUsername";
            this.labelUsername.Size = new System.Drawing.Size(60, 15);
            this.labelUsername.TabIndex = 4;
            this.labelUsername.Text = "Username";
            // 
            // textBoxUsername
            // 
            this.textBoxUsername.Location = new System.Drawing.Point(52, 107);
            this.textBoxUsername.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.textBoxUsername.Name = "textBoxUsername";
            this.textBoxUsername.Size = new System.Drawing.Size(110, 23);
            this.textBoxUsername.TabIndex = 3;
            this.textBoxUsername.Text = "guest";
            // 
            // buttonApplyConfig
            // 
            this.buttonApplyConfig.Location = new System.Drawing.Point(358, 399);
            this.buttonApplyConfig.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.buttonApplyConfig.Name = "buttonApplyConfig";
            this.buttonApplyConfig.Size = new System.Drawing.Size(105, 22);
            this.buttonApplyConfig.TabIndex = 2;
            this.buttonApplyConfig.Text = "Apply";
            this.buttonApplyConfig.UseVisualStyleBackColor = true;
            this.buttonApplyConfig.Click += new System.EventHandler(this.buttonApplyConfig_Click);
            // 
            // labelHostname
            // 
            this.labelHostname.AutoSize = true;
            this.labelHostname.Location = new System.Drawing.Point(52, 27);
            this.labelHostname.Name = "labelHostname";
            this.labelHostname.Size = new System.Drawing.Size(62, 15);
            this.labelHostname.TabIndex = 1;
            this.labelHostname.Text = "Hostname";
            // 
            // textBoxHostname
            // 
            this.textBoxHostname.Location = new System.Drawing.Point(52, 50);
            this.textBoxHostname.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.textBoxHostname.Name = "textBoxHostname";
            this.textBoxHostname.Size = new System.Drawing.Size(110, 23);
            this.textBoxHostname.TabIndex = 0;
            this.textBoxHostname.Text = "localhost";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(846, 456);
            this.Controls.Add(this.tabControlMenu);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimumSize = new System.Drawing.Size(818, 495);
            this.Name = "MainForm";
            this.Text = "Stock Preditcting";
            this.tabControlMenu.ResumeLayout(false);
            this.EnterStockInfoPage.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.tabPageGraph.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxGraph)).EndInit();
            this.tabPageConfiguration.ResumeLayout(false);
            this.tabPageConfiguration.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControlMenu;
        private System.Windows.Forms.TabPage EnterStockInfoPage;
        private System.Windows.Forms.TabPage tabPageGraph;
        private System.Windows.Forms.PictureBox pictureBoxGraph;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.RichTextBox richTextBoxPredictions;
        private System.Windows.Forms.ComboBox comboBoxInfoSource;
        private System.Windows.Forms.Button buttonPredict;
        private System.Windows.Forms.TextBox textBoxEnterTicker;
        private System.Windows.Forms.ComboBox comboBoxModelType;
        private System.Windows.Forms.TabPage tabPageConfiguration;
        private System.Windows.Forms.Label labelHostname;
        private System.Windows.Forms.TextBox textBoxHostname;
        private System.Windows.Forms.Label labelPassword;
        private System.Windows.Forms.TextBox textBoxPassword;
        private System.Windows.Forms.Label labelUsername;
        private System.Windows.Forms.TextBox textBoxUsername;
        private System.Windows.Forms.Button buttonApplyConfig;
    }
}

