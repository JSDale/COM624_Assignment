

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
        /// <param name="stockPredictions">The predictions to pass</param>
        public delegate void UpdateStock(string stockPredictions);
        
        /// <summary>
        /// Event to handle when stock predictions are published
        /// </summary>
        public static event UpdateStock UpdateStockEvent;

        /// <summary>
        /// Invokes the <see cref="UpdateStockEvent"/>.
        /// </summary>
        /// <param name="stockPredictions">the predictions to pass to GUI</param>
        public static void InvokeUpdateStock(string stockPredictions)
        {
            UpdateStockEvent.Invoke(stockPredictions);
        }
    }
}
