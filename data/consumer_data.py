import psycopg2
from pulsar import Client
import json
import os
from dotenv import load_dotenv

def persistir_no_postgres(mensagem):
    """Persiste a mensagem no banco de dados PostgreSQL."""
    try:
        # Configurações do PostgreSQL
        load_dotenv()

        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_USER = os.getenv("DB_USER") 
        DB_PASS = os.getenv("DB_PASS")
        DB_NAME = os.getenv("DB_NAME")

        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (mensagem['nome'], mensagem['idade']))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao persistir no PostgreSQL:", error)
    finally:
        cursor.close()
        conn.close()

def receber_mensagens():
    # Configurações do Pulsar
    topic_name = "persistent://public/default/pessoas-topic"
    subscription_name = "consumer-1"
    service_url = "pulsar://localhost:6650"

    client = Client(service_url)

    # Criando um consumidor para receber dados do tópico
    consumer = client.subscribe(topic_name, subscription_name)

    try:
        # Processando as mensagens recebidas e inserindo no banco de dados
        while True:
            msg = consumer.receive()
            try:
                dado = json.loads(msg.data().decode('utf-8'))
                persistir_no_postgres(dado)
                print("Dados inseridos:", (dado))
            except Exception as e:
                print(f"Erro ao processar mensagem: {e}")
            consumer.acknowledge(msg)
    finally:
        # Fechando o consumidor e o cliente
        consumer.close()
        client.close()


if __name__ == "__main__":
    receber_mensagens()

