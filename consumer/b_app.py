import json
from kafka import KafkaConsumer

# Kafka yapılandırmasını güncelleyin
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'X'

# Kafka consumer'ı oluşturun
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Kafka'dan mesajları tüketen işlev
def consume_messages():
    for message in consumer:
        print(message.value)

# Ana işlemi başlat
if __name__ == '__main__':
    consume_messages()
