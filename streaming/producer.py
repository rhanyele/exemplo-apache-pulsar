from pulsar import Client

def enviar_mensagens():
    # Configurações do Pulsar
    service_url = "pulsar://localhost:6650"  # URL do serviço Pulsar
    topic = "persistent://public/default/example-topic"  # Nome do tópico

    client = Client(service_url)
    producer = client.create_producer(topic)
    
    mensagem = "Mensagem de exemplo"
    producer.send(mensagem.encode('utf-8'))
    print("Mensagem enviada:", mensagem)
    producer.close()
    client.close()

if __name__ == "__main__":
    enviar_mensagens()
