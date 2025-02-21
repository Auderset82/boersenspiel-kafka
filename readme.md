# 📌 boersenspiel-kafka

Dieses Repository enthält den Kafka-Service für das Börsenspiel-Projekt.

## 📦 Enthaltene Dateien:
- `kafka/producer.py` - Sendet Nachrichten an Kafka
- `kafka/consumer.py` - Empfängt Nachrichten von Kafka
- `Dockerfile.kafka` - Dockerfile für Render
- `docker-compose.yml` - Zum lokalen Start von Kafka mit Docker
- `requirements.txt` - Python-Abhängigkeiten

## 🚀 Deployment auf Render
1. Erstelle auf [Render.com](https://render.com/) einen neuen **Private Service**
2. Wähle `boersenspiel-kafka` als Repository
3. Setze die **Build Command**:  
   ```sh
   docker build -t kafka-service -f Dockerfile.kafka .
