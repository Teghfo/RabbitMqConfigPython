import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel =connection.channel()



def Hello_Mapsa(ch, method, properties, body):
    print("ch : {}, method {}, property {} , body {}".format(ch, method, properties, body))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    time.sleep(5)



# channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue = 'mapsa', on_message_callback = Hello_Mapsa)


print("worker is on!")


channel.start_consuming()