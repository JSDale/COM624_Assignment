

namespace GuiController
{
    using System.Collections.Generic;

    /// <summary>
    /// Contains the properties for stock messages.
    /// </summary>
    public class StockMessage
    {
        /// <summary>
        /// Gets or sets predictions received from backend.
        /// </summary>
        public List<string> Predictions { get; set; }

        /// <summary>
        /// Gets or sets the file path of the graph image to load.
        /// </summary>
        public string GraphLocation { get; set; }
    }
}
