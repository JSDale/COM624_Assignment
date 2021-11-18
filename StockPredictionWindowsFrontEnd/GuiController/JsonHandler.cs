

namespace GuiController
{
    using Newtonsoft.Json;

    /// <summary>
    /// Serializes and Deserializes JSON
    /// </summary>
    public static class JsonHandler
    {
        /// <summary>
        /// Deserializes the JSON stock prediction message into objected.
        /// </summary>
        /// <param name="message">message to deserialize</param>
        /// <returns>The deserialized message</returns>
        public static StockMessage DeserializeStockMessage(string message)
        {
            //// message = message.Replace("\\\\", "\\");
            var obj = JsonConvert.DeserializeObject<StockMessage>(message);
            return obj;
        }
    }
}
