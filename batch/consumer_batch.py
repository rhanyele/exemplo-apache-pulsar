import pulsar

def receber_mensagens():
    # Configurações do Pulsar
    client = pulsar.Client('pulsar://localhost:6650')
    topic = 'persistent://public/default/example-topic'
    subscription_name = 'subscription-1'
    batch_size = 10  # Definir o tamanho máximo do batch

    # Cria uma assinatura para começar do início do tópico
    consumer = client.subscribe(
        topic,
        subscription_name=subscription_name,
        consumer_type=pulsar.ConsumerType.Exclusive,
        InitialPosition=pulsar.InitialPosition.Earliest
    )

    batch = []
    while True:
        received_message = consumer.receive()
        batch.append(received_message)
        if len(batch) == batch_size:
            # Exibe as mensagens apenas quando o batch estiver cheio
            for msg in batch:
                print("Mensagem recebida: '{}' id='{}'".format(msg.data().decode('utf-8'), msg.message_id()))
            # Limpa o batch
            batch.clear()

if __name__ == "__main__":
    receber_mensagens()