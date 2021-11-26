

using MessageTemplates;

namespace CustomEvents
{
    /// <summary>
    /// Handles events for updating the GUI
    /// </summary>
    public static class UpdateGui
    {
        /// <summary>
        /// delegate for passing stock predictions to GUI
        /// </summary>
        /// <param name="returnedMessage">The predictions to pass</param>
        public delegate void UpdateStock(StockMessage returnedMessage);
        
        /// <summary>
        /// Event to handle when stock predictions are published
        /// </summary>
        public static event UpdateStock UpdateStockEvent;

        /// <summary>
        /// Invokes the <see cref="InvokeUpdateStock"/>.
        /// </summary>
        /// <param name="returnedMessage">the predictions to pass to GUI</param>
        public static void InvokeUpdateStock(StockMessage returnedMessage)
        {
            UpdateStockEvent.Invoke(returnedMessage);
        }
    }
}
