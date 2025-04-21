from kafka import KafkaConsumer
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['entreprise']
collection = db['ventes']

consumer = KafkaConsumer(
    'ventes',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("En attente de messages...")
for msg in consumer:
    vente = msg.value
    print(f"Insertion : {vente}")
    collection.insert_one(vente)
