import pika
import json
from SendMail import sendMail
import json
params = pika.URLParameters('amqps://ziucaoki:sHXSNCgyMx6DAPMGgZNkiCe4jjR_7Fb6@jackal.rmq.cloudamqp.com/ziucaoki')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='novo_ticket_setor')

def callback(ch, method, properties, body):
    data = json.loads(body)
    sendMail(data['nome'], data['setor'], data['email'])

channel.basic_consume(queue='novo_ticket_setor', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()