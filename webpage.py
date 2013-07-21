#!/usr/bin/env python
import pika
import sys
import os
import re
import time
import pp
import sys, thread, time, urllib, httplib, re
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def main():
    for url in sys.argv[1:]:
        thread.start_new(loadurl, (url,))
	message =url 
	channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode = 2))
	print " [x] Sent %r" % (message,)
    time.sleep(1000000)

def loadurl(url):
    f = urllib.urlopen(url)
    text = f.read()
    print len(text), url

main()
