from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

produits = ['Chaussures', 'T-shirt', 'Jeans', 'Montre', 'Sac']
regions = ['Île-de-France', 'Rhône-Alpes', 'Provence', 'Occitanie']

def generer_vente():
    return {
        'date_vente': fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        'montant_vente': round(random.uniform(10, 500), 2),
        'produit': random.choice(produits),
        'region': random.choice(regions)
    }

while True:
    vente = generer_vente()
    print(f"Envoi: {vente}")
    producer.send('ventes', vente)
    time.sleep(1)

