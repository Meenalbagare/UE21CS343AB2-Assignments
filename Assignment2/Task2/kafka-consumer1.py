#!/usr/bin/env python3
from kafka import KafkaConsumer
import json
import sys
import re
# Get the topic name from command line arguments
topic1 = sys.argv[1]

# Create a Kafka consumer
consumer = KafkaConsumer(topic1, bootstrap_servers='localhost:9092')

# Initialize a dictionary to store comments
comments_dict = {}
split_pattern=re.compile(r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)')
# Consume messages and extract comments
while True:  # Continue to poll until an "EOF" marker is encountered
    message = consumer.poll(timeout_ms=5000)  # Set a timeout (in milliseconds)

    if not message:
        # No new messages received within the timeout
        break  # Exit the loop

    for record in message.values():
        for msg in record:
            data = re.split(split_pattern,msg.value.decode('utf-8'))
            
            action = data[0]
            
            if action == 'EOF':
                break  # Exit the loop when the "EOF" marker is received

            if action == 'comment':
                username = data[2]
                comment =data[-1][1:-1] # Remove double quotes
                #comment=data[4]
               
                if username in comments_dict:
                    comments_dict[username].append(comment)
                else:
                    comments_dict[username] = [comment]

# Sort the dictionary by usernames
#sorted_comments_dict = {k: sorted(v) for k,v in comments_dict.items()}
sorted_comments_dict=dict(sorted(comments_dict.items(),key=lambda item:item[0]))
print(json.dumps(sorted_comments_dict, indent=4,ensure_ascii=False))

# Close the consumer
consumer.close()


