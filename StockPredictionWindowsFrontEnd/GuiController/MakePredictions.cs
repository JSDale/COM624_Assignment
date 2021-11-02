

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

        public MakePredictions(string ticker, string informationSource)
        {
            this.ticker = ticker;
            this.informationSource = informationSource;
        }

        public void GetPredictions()
        {
            var mb = new MessageBroker.Sender();
            mb.Send(this.ticker, this.informationSource);
        }
    }
}
