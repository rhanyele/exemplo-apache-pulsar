from pulsar import Client
import json

def enviar_mensagens():
    # Configurações do Pulsar
    service_url = "pulsar://localhost:6650"  # URL do serviço Pulsar
    topic = "persistent://public/default/pessoas-topic"  # Nome do tópico

    client = Client(service_url)

    # Criando um produtor para publicar dados no tópico
    producer = client.create_producer(topic)

    # Dados a serem publicados
    dados = [
        {"nome": "Gabriel", "idade": 1},
        {"nome": "Gustavo", "idade": 4},
        {"nome": "Guilherme", "idade": 8}
    ]

    # Publicando os dados no tópico
    # Envia as mensagens em fomato JSON
    for dado in dados:
        producer.send(json.dumps(dado).encode('utf-8'))

    # Fechando o produtor e o cliente
    producer.close()
    client.close()

if __name__ == "__main__":
    enviar_mensagens()