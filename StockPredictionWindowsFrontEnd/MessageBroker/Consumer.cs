// --------------------------------------------------------------------------------------------------------------------
// <copyright file="Consumer.cs" company="QinetiQ Ltd 2021">
//   Copyright (c) QinetiQ Ltd 2021. All rights reserved.
// </copyright>
// <summary>
//   
// </summary>
// --------------------------------------------------------------------------------------------------------------------


namespace MessageBroker
{
    using System;
    using System.Security.Cryptography;
    using System.Text;

    using CustomEvents;
    using MessageTemplates;
    using RabbitMQ.Client;
    using RabbitMQ.Client.Events;

    /// <summary>
    /// Class for consuming messages
    /// </summary>
    public class Consumer : IDisposable
    {
       /// <summary>
        /// The address of the rabbitMQ broker host.
        /// </summary>
        private readonly string hostName;

        /// <summary>
        /// The name of the queue to consume on.
        /// </summary>
        private readonly string queueName;

        /// <summary>
        /// The username to use with rabbitMQ. Must be an available user in RMQ
        /// </summary>
        private readonly string username;

        /// <summary>
        /// The password to use with RMQ. Must be an available user in RMQ
        /// </summary>
        private readonly string password;

        /// <summary>
        /// The rabbit MQ connection.
        /// </summary>
        private IConnection connection;

        /// <summary>
        /// The channel to communicate on.
        /// </summary>
        private IModel channel;

        /// <summary>
        /// Consumes messages on given queue.
        /// </summary>
        private EventingBasicConsumer consumer;

        /// <summary>
        /// Initializes a new instance of the <see cref="Consumer"/> class.
        /// </summary>
        /// <param name="hostName">The address of the rabbitMQ broker host.</param>
        /// <param name="queueName">The name of the queue to consume on.</param>
        public Consumer(string hostName, string queueName, string username, string password)
        {
            this.hostName = hostName;
            this.queueName = queueName;
            this.username = username;
            this.password = password;
        }

        /// <summary>
        /// Consumes messages on given queue
        /// </summary>
        public void Consume()
        {
            if (this.consumer == null)
            {
                return;
            }

            this.channel.BasicConsume(queue: this.queueName, autoAck: true, consumer: this.consumer);
        }

        /// <summary>
        /// Initializes the consumer
        /// </summary>
        public void Initialize()
        {
            try
            {
                var factory = new ConnectionFactory() 
                {
                    HostName = this.hostName,
                    UserName = this.username,
                    Password = this.password
                };

                // ReSharper disable once ConvertToUsingDeclaration
                this.connection = factory.CreateConnection();
            }
            catch
            {
               CustomDisplayError.InvokeDisplayError("Could not connect to RabbitMQ, ensure the service is running");
                return;
            }
            this.channel = this.connection.CreateModel();
            this.channel.QueueDeclare(
                queue: this.queueName,
                durable: false,
                exclusive: false,
                autoDelete: true,
                arguments: null);

            this.consumer = new EventingBasicConsumer(this.channel);
            this.consumer.Received += this.WhenConsumed;
        }

        /// <summary>
        /// Disposes objects.
        /// </summary>
        public void Dispose()
        {
            this.channel?.Dispose();
            this.channel = null;

            this.connection?.Dispose();
            this.connection = null;
        }

        private void WhenConsumed(object model, BasicDeliverEventArgs ea)
        {
            var body = ea.Body.ToArray();
            var message = Encoding.UTF8.GetString(body);
            var obj = JsonHandler.DeserializeStockMessage(message);
            if (message.ToLower().Contains("error"))
            {
                CustomDisplayError.InvokeDisplayError(obj.ModelConfidence);
                return;
            }

            UpdateGui.InvokeUpdateStock(obj);
        }
    }
}