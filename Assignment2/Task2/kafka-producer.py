#!/usr/bin/env python3
from kafka import KafkaProducer
import sys

# Get the topic names from command line arguments
topic1, topic2, topic3 = sys.argv[1:]

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Read data from standard input and produce to topics
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace
    if line == "EOF":
        break  # Exit the loop when EOF is encountered
    message_bytes=line.encode('utf-8')
    # Produce messages to the respective topics
    producer.send(topic1, value=message_bytes)
    producer.send(topic2, value=message_bytes)
    producer.send(topic3, value=message_bytes)

# Close the producer
producer.close()



