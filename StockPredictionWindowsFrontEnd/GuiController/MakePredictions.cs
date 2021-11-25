

namespace GuiController
{
    using System.Drawing;

    /// <summary>
    /// Abstracts the GUI from the BLL
    /// </summary>
    public class MakePredictions
    {
        private string ticker;

        private string informationSource;

        private string modelType;

        public MakePredictions(string ticker, string informationSource, string modelType)
        {
            this.ticker = ticker;
            this.informationSource = informationSource;
            this.modelType = modelType;
        }

        public void GetPredictions()
        {
            var mb = new MessageBroker.Sender();
            mb.Send(this.ticker, this.informationSource, this.modelType);
        }
    }
}
