from confluent_kafka import Consumer

# Kafka-Config
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(["test-topic"])

print("📡 Warte auf Nachrichten...")

try:
    while True:
        msg = consumer.poll(1.0)  # Warte 1 Sekunde auf eine Nachricht
        if msg is None:
            continue
        if msg.error():
            print(f"❌ Fehler: {msg.error()}")
        else:
            print(f"📩 Nachricht erhalten: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("❌ Consumer beendet.")
finally:
    consumer.close()
