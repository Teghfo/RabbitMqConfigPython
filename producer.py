import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel =connection.channel()



# channel.queue_declare(queue = 'mapsa')
# channel.queue_declare(queue = 'ghom')
# channel.exchange_declare('korona1', exchange_type='fanout')


# channel.basic_publish(exchange = '',routing_key = 'mapsa', body="hello mapsa")


# channel.basic_publish(exchange = 'korona1',routing_key = '', body="hello mapsa")
# channel.queue_bind(exchange='korona1', queue='ghom')


channel.basic_publish(exchange='Namzadang',
                      routing_key='',
                      body="Darkhast Ezdevaj!")

connection.close()
print("task send!")