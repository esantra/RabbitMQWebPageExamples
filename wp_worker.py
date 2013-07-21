#!/usr/bin/env python
import pika
import time
import sys, thread, time, urllib, httplib, re

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
	thread.start_new(loadurl, (body,))
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

def loadurl(url):
    f = urllib.urlopen(url)
    text = f.read()
    wordcount=0
    for lines in text:
         f1=lines.split()
         wordcount=wordcount+len(f1)
    f.close()
    print url + ' word count:', str(wordcount)
    

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()