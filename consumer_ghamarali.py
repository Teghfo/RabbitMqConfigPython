import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel =connection.channel()



def Hello_Mapsa(ch, method, properties, body):
    print("ghamarAli ok dad")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    time.sleep(5)



# channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue = 'ghamarALi', on_message_callback = Hello_Mapsa)


print("worker is on!")


channel.start_consuming()