import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel =connection.channel()




# channel.queue_declare(queue = 'sakineh')
# channel.queue_declare(queue = 'ghamarALi')




channel.exchange_declare('Namzadang', exchange_type='fanout')



channel.queue_bind(exchange='Namzadang',
                   queue='sakineh')


channel.queue_bind(exchange='Namzadang',
                   queue='ghamarALi')