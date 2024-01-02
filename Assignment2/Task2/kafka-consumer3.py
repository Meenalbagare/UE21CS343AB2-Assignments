#!/usr/bin/env python3
from kafka import KafkaConsumer
import json
import sys

# Get the topic name from command line arguments
topic3 = sys.argv[3]

# Create a Kafka consumer
consumer = KafkaConsumer(topic3, bootstrap_servers='localhost:9092')

# Initialize a dictionary to store popularity scores
popularity_dict = {}

# Consume messages and calculate popularity
while True:  # Continue to poll until an "EOF" marker is encountered
    message = consumer.poll(timeout_ms=5000)  # Set a timeout (in milliseconds)

    if not message:
        # No new messages received within the timeout
        break  # Exit the loop

    for record in message.values():
        for msg in record:
            data = msg.value.decode('utf-8').split()
            action = data[0]
            username = data[2]

            if username not in popularity_dict:
                popularity_dict[username] = {
                    "likes": 0,
                    "shares": 0,
                    "comments": 0
                }

            if action == 'EOF':
                break  # Exit the loop when the "EOF" marker is received

            if action == 'like':
                popularity_dict[username]["likes"] += 1
            elif action == 'share':
                popularity_dict[username]["shares"] += len(data) - 4  # Number of people shared to
            elif action == 'comment':
                popularity_dict[username]["comments"] += 1

# Calculate popularity using the provided formula
for username, values in popularity_dict.items():
    likes = values["likes"]
    shares = values["shares"]
    comments = values["comments"]
    popularity = (likes + 20 * shares + 5 * comments) / 1000
    popularity_dict[username] = popularity

# Sort the dictionary by usernames
sorted_popularity_dict = dict(sorted(popularity_dict.items()))

# Print the JSON representation of the sorted popularity dictionary
print(json.dumps(sorted_popularity_dict, indent=4))

# Close the consumer
consumer.close()


