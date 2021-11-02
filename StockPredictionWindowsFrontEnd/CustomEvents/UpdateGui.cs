

namespace CustomEvents
{
    public static class UpdateGui
    {
        public delegate void UpdateStock(string stockPredictions);
        
        public static event UpdateStock UpdateStockEvent;

        public static void InvokeUpdateStock(string stockPredictions)
        {
            UpdateStockEvent.Invoke(stockPredictions);
        }
    }
}
