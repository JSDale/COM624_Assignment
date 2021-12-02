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
    using System;
    using System.Text;
    using RabbitMQ.Client;

    /// <summary>
    /// Sends the messages to python backend
    /// </summary>
    public class Sender : IDisposable
    {
        /// <summary>
        /// The hostname for rabbitMQ
        /// </summary>
        private readonly string hostname;

        private IConnection connection;

        public Sender(string hostname)
        {
            this.hostname = hostname;
        }

        /// <summary>
        /// Initializes the rabbitMQ connection.
        /// </summary>
        public void Initialize()
        {
            try
            {
                 var factory = new ConnectionFactory() { HostName = this.hostname };
                this.connection = factory.CreateConnection();
            }
            catch
            {
                CustomEvents.CustomDisplayError.InvokeDisplayError("Could not connect to rabbitMQ, ensure service is running");
            }
        }

        /// <summary>
        /// Sends the messages to RabbitMQ
        /// </summary>
        /// <param name="messageAsJson">The message to publish.</param>
        public void GetPredictions(string messageAsJson)
        { 
            // ReSharper disable once ConvertToUsingDeclaration
            using (var channel = this.connection.CreateModel())
            {
                //// These settings must be the same as the ones in the back-end
                channel.QueueDeclare(queue: "StockExchange", durable: false, exclusive: false, autoDelete: true, arguments: null);

                var body = Encoding.UTF8.GetBytes(messageAsJson);

                channel.BasicPublish(exchange: string.Empty, routingKey: "StockExchange", basicProperties: null, body: body);
            }
        }

        /// <summary>
        /// Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        /// </summary>
        public void Dispose()
        {
            this.connection?.Dispose();
            this.connection = null;
        }
    }
}