

namespace MessageBroker
{
    using System;
    using System.Dynamic;

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

        public MessageToSend(string ticker, string source)
        {
            this.Ticker = ticker;
            this.Source = source;
        }
    }
}
