

namespace MessageTemplates
{
    using Newtonsoft.Json;

    public static  class JsonSerializer
    {
        public static string SerializeMessageToSend(MessageToSend messageToSend)
        {
            return JsonConvert.SerializeObject(messageToSend);
        }
    }

    public class MessageToSend
    {
        public string Ticker { get; }

        public string Source { get; }

        public string ModelType { get; }

        public MessageToSend(string ticker, string source, string modelType)
        {
            this.Ticker = ticker;
            this.Source = source;
            this.ModelType = modelType;
        }
    }
}
