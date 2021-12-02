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

        /// <summary>
        /// The username to connect to RMQ with
        /// </summary>
        private readonly string username;

        /// <summary>
        /// The password to connect to RMQ with.
        /// </summary>
        private readonly string password;

        private IConnection connection;

        /// <summary>
        /// Initializes a new instance of the <see cref="Sender"/> class.
        /// </summary>
        /// <param name="hostname">The hostname of device running RMQ</param>
        /// <param name="username">The username to connect to RMQ with</param>
        /// <param name="password">The password to connect to RMQ with</param>
        public Sender(string hostname, string username, string password)
        {
            this.hostname = hostname;
            this.username = username;
            this.password = password;
        }

        /// <summary>
        /// Initializes the rabbitMQ connection.
        /// </summary>
        public void Initialize()
        {
            try
            {
                 var factory = new ConnectionFactory()
                 {
                     HostName = this.hostname,
                     UserName = this.username,
                     Password = this.password
                 };
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