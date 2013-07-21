The webpage.py program was parallelized to 
•	Break up the task into smaller tasks[9]

URLs were entered via the command line. Each URL spawned a thread. The thread sent the URL to the worker nodes. 

•	Assign the smaller tasks to multiple workers that completed the tasks simultaneously[9]

Each worker node counted the number of words on the webpage of the URL that was passed via the Rabbit MQ messaging service.

•	Coordinate the workers and their communication [9]

Each task was passed in round-robin fashion via a load-balancer.

Please see code attachment files webpage.py and wp_worker.py for actual code.



message_send.py and message_rec.py
The code uses a thread for each message and distributed each message round-robin fashion to the worker nodes. 
Code was based on RabbitMQ examples. 


index.php (a WordPress index file) 
The index.php file in addition to the RabbitMQ example code for new_task.py and worker.py code were used for this example.
The example passes a visitor's url and a bit more information to worker nodes. 

-- author: amanda fouts