#!/usr/bin/env python
import pika
import sys
import os
import re
import time
import thread
import pp

from threading import Thread


class thread_it(Thread):
    def __init__ (self,param):
        Thread.__init__(self)
        self.param = param
    def run(self):
        mutex.acquire()
        output.append(self.param)
        mutex.release()   
  

threads = []
output = []
mutex = thread.allocate_lock()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='54.235.169.93'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
for x in range(0, 100):
    #multithread this loop in python
	current = thread_it(x)
    	threads.append(current)
    	current.start()
	message = ' '.join(sys.argv[1:]) or "This is a text message that is delivered to another program."
	channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode = 2))
	print " [x] Sent %r" % (message,)
	
for t in threads:
    t.join()
	
connection.close()
