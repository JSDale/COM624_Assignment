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
    using System.Text;
    using System.Threading.Tasks;

    using CustomEvents;

    using RabbitMQ.Client;
    using RabbitMQ.Client.Events;

    public class Consumer
    {
        public async Task Consume()
        {
            var factory = new ConnectionFactory() { HostName = "localhost" };
            // ReSharper disable once ConvertToUsingDeclaration
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.QueueDeclare(
                    queue: "resp_stock",
                    durable: false,
                    exclusive: false,
                    autoDelete: false,
                    arguments: null);

                var consumer = new EventingBasicConsumer(channel);
                consumer.Received += (model, ea) =>
                {
                    var body = ea.Body.ToArray();
                    var message = Encoding.UTF8.GetString(body);
                    UpdateGui.InvokeUpdateStock(message);
                };

                channel.BasicConsume(queue: "resp_stock", autoAck: true, consumer: consumer);
            }
        }
    }
}