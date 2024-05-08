from pulsar import Client, ConsumerType, InitialPosition

def receber_mensagens():
    # Configurações do Pulsar
    service_url = "pulsar://localhost:6650"  # URL do serviço Pulsar
    topic = "persistent://public/default/example-topic"  # Nome do tópico
    subscription_name = 'subscription-1'

    client = Client(service_url)

    # Configura a posição da inscrição para começar do início do tópico
    consumer = client.subscribe(
        topic,
        subscription_name=subscription_name,
        consumer_type=ConsumerType.Exclusive,
        initial_position=InitialPosition.Earliest
    )
    while True:
        msg = consumer.receive()
        try:
            print("Mensagem recebida: '{}' id='{}'".format(msg.data().decode('utf-8'), msg.message_id()))
            consumer.acknowledge(msg)
        except Exception as e:
            print("Erro ao processar mensagem:", e)
            consumer.negative_acknowledge(msg)

if __name__ == "__main__":
    receber_mensagens()
