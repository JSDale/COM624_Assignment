// --------------------------------------------------------------------------------------------------------------------
// <copyright file="Sender.cs" company="QinetiQ Ltd 2021">
//   Copyright (c) QinetiQ Ltd 2021. All rights reserved.
// </copyright>
// <summary>
//   Sends the messages.
// </summary>
// --------------------------------------------------------------------------------------------------------------------


namespace MessageBroker
{
    using System.Text;

    using RabbitMQ.Client;

    /// <summary>
    /// Sends the messages to python backend
    /// </summary>
    public class Sender
    {
        /// <summary>
        /// Sends the messages
        /// </summary>
        /// <param name="ticker">The abbreviation for the company used on the stock market</param>
        /// <param name="stockInfoSource">Where the stock information is gathered</param>
        public void Send(string ticker, string stockInfoSource)
        {
            var factory = new ConnectionFactory() { HostName = "localhost" };
            // ReSharper disable once ConvertToUsingDeclaration
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                //// These settings must be the same as the ones in the back-end
                channel.QueueDeclare(queue: "StockExchange", durable: false, exclusive: false, autoDelete: false, arguments: null);

                var message = JsonSerializer.SerializeMessageToSend(new MessageToSend(ticker, stockInfoSource));
                var body = Encoding.UTF8.GetBytes(message);

                channel.BasicPublish(exchange: string.Empty, routingKey: "StockExchange", basicProperties: null, body: body);
                
            }
        }
    }
}