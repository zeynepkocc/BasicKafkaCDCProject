import time
import json
from pymongo import MongoClient
from kafka import KafkaProducer

# MongoDB bağlantısı için gerekli bilgileri güncelleyin
mongo_host = 'mongodb://localhost:27017'
mongo_db = 'zeynep'
mongo_collection = 'kafkaproject'

# Kafka yapılandırmasını güncelleyin
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'X'

# Kafka producer'ı oluşturun
producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# MongoDB'ye bağlanın
client = MongoClient(mongo_host)
db = client[mongo_db]
collection = db[mongo_collection]

# Önceki çalışmadan sonra eklenmiş yeni dokümanları tespit eden ve Kafka'ya mesaj gönderen işlev
def process_new_documents():
    # Son çalışma sırasında alınan son dökümanın _id değerini alın
    last_document_id = None  # Dökümanı takip etmek için gereken bir mekanizma oluşturun

    while True:
        # Yeni dökümanları sorgula
        query = {}  # İsteğe bağlı sorgu filtreleri ekleyin
        if last_document_id:
            query['_id'] = {'$gt': last_document_id}

        new_documents = collection.find(query)

        for doc in new_documents:
            # Yeni dökümanı Kafka'ya gönder
            message = {'document': doc}
            producer.send(kafka_topic, value=message)

            # Son dökümanın _id değerini güncelle
            last_document_id = doc['_id']

        # 10 saniye bekle
        time.sleep(10)

# Ana işlemi başlat
if __name__ == '__main__':
    process_new_documents()
