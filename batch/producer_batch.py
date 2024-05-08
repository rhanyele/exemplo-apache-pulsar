from pulsar import Client

# Função para enviar mensagens em lote
def enviar_mensagens():
    # Configurações do Pulsar
    service_url = "pulsar://localhost:6650"  # URL do serviço Pulsar
    topic = "persistent://public/default/example-topic"  # Nome do tópico
    batch_size = 5  # Tamanho do batch

    client = Client(service_url)
    producer = client.create_producer(topic, batching_enabled=True, batching_max_publish_delay_ms=10)
    
    batch = []
    for i in range(10):
        mensagem = "Mensagem de exemplo {}".format(i)
        batch.append(mensagem.encode('utf-8'))
        if len(batch) >= batch_size:
            for msg in batch:
                producer.send(msg)
            batch = []

    if batch:
        for msg in batch:
            producer.send(msg)

    producer.flush()
    producer.close()
    client.close()

if __name__ == "__main__":
    enviar_mensagens()
