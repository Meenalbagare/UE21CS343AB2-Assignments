#!/usr/bin/env python3
from kafka import KafkaConsumer
import json
import sys

# Get the topic name from command line arguments
topic2 = sys.argv[2]

# Create a Kafka consumer
consumer = KafkaConsumer(topic2, bootstrap_servers='localhost:9092')

# Initialize a dictionary to store the number of likes for each user's post
likes_dict = {}

# Consume messages and count likes
while True:
    message=consumer.poll(timeout_ms=5000)
    if not message:
        break
    for record in message.values():
        for message in record:
            data = message.value.decode('utf-8').split()
            action = data[0]
            if action=="EOF":
                break
            if action == 'like':
                username = data[2]
                post_id = data[3]
                if username in likes_dict:
                    if post_id in likes_dict[username]:
                        likes_dict[username][post_id] += 1
                    else:
                        likes_dict[username][post_id] = 1
                else:
                    likes_dict[username] = {post_id: 1}
	   
# Sort the dictionary by usernames
sorted_likes_dict = dict(sorted(likes_dict.items()))

# Print the JSON representation of the sorted likes dictionary
print(json.dumps(sorted_likes_dict, indent=4))

# Close the consumer
consumer.close()


