

namespace GuiController
{

    /// <summary>
    /// Contains the properties for stock messages.
    /// </summary>
    public class StockMessage
    {
        /// <summary>
        /// Gets or sets predictions received from backend.
        /// </summary>
        public string confidenceOfModel { get; set; }

        /// <summary>
        /// Gets or sets the file path of the graph image to load.
        /// </summary>
        public string GraphLocation { get; set; }
    }
}
