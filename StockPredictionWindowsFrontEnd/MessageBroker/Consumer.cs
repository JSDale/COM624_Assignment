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
    using System.Text;
    using System.Threading.Tasks;

    using CustomEvents;

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
        public Consumer(string hostName, string queueName)
        {
            this.hostName = hostName;
            this.queueName = queueName;
        }

        /// <summary>
        /// Consumes messages on given queue
        /// </summary>
        public async void Consume()
        {
            if (this.consumer == null)
            {
                throw new NullReferenceException("consumer was null.");
            }

            this.channel.BasicConsume(queue: this.queueName, autoAck: true, consumer: this.consumer);
            await Task.Delay(TimeSpan.FromMilliseconds(20));
        }

        /// <summary>
        /// Initializes the consumer
        /// </summary>
        public void Initialize()
        {
            var factory = new ConnectionFactory() { HostName = this.hostName };
            // ReSharper disable once ConvertToUsingDeclaration
            this.connection = factory.CreateConnection();
            this.channel = this.connection.CreateModel();
            this.channel.QueueDeclare(
                queue: this.queueName,
                durable: false,
                exclusive: false,
                autoDelete: false,
                arguments: null);

            this.consumer = new EventingBasicConsumer(this.channel);
            this.consumer.Received += (model, ea) =>
                {
                    var body = ea.Body.ToArray();
                    var wibble = ea.RoutingKey;
                    var message = Encoding.UTF8.GetString(body);
                    UpdateGui.InvokeUpdateStock(message);
                };
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
    }
}