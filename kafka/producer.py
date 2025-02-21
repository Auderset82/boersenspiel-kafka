from confluent_kafka import Producer

# Kafka-Config
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

def send_message(topic, message):
    """Sendet eine Nachricht an ein Kafka-Topic."""
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()
    print(f"✅ Nachricht gesendet an {topic}: {message}")

if __name__ == "__main__":
    topic_name = "test-topic"
    message = "Hallo von Python Producer!"
    send_message(topic_name, message)
