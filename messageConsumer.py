import pika
import json
from SendMail import sendMessageMail
import json
params = pika.URLParameters('amqps://ziucaoki:sHXSNCgyMx6DAPMGgZNkiCe4jjR_7Fb6@jackal.rmq.cloudamqp.com/ziucaoki')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='nova_mensagem_ticket')

def callback(ch, method, properties, body):
    data = json.loads(body)
    sendMessageMail(data['nome'], data['ticket_id'], data['email'])

channel.basic_consume(queue='nova_mensagem_ticket', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()