# Projeto Exemplo Apache Pulsar

O Apache Pulsar é uma plataforma de mensageria e streaming de dados distribuída e escalável.

O projeto é uma aplicação Python utilizando o Apache Pulsar, criada para ser um exemplo das funcionalidades básicas do Pulsar. Este projeto tem como objetivo ser uma referência para projetos posteriores com a ferramenta.

Pulsar é construído no padrão publish–subscribe (publicar-assinar). Nesse padrão, os produtores publicam mensagens nos tópicos; os consumidores assinam esses tópicos, processam as mensagens recebidas e enviam confirmações ao broker quando o processamento é concluído.

![Visão Geral do Apache Pulsar](https://github.com/rhanyele/exemplo-apache-pulsar/assets/10997593/34ae226a-a200-47b2-84a9-2b6a9300ef3e)

### Documentação
- [Apache Pulsar](https://pulsar.apache.org/)

## Estrutura do projeto
```bash
- batch
  - consumer_batch.py
  - producer_batch.py
- database
  - .env
  - consumer_data.py
  - producer_data.py
- streaming
  - consumer.py
  - producer.py
- docker-compose.yml
```

## Funcionalidades
- **Consumer:** Faz a assinatura de um tópipco e consome/lê as mensagens de dentro do tópico.
- **Producer:** Produz e envia as mensagens para dentro de um tópico.

## Requisitos
- Python
- Poetry
- Docker

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/rhanyele/exemplo-apache-pulsar.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd exemplo-apache-pulsar
   ```

3. Instale as dependências usando Poetry:
   ```bash
   poetry install
   ```
   
4. Execute o Docker Composer:

   ```bash
   docker compose up -d
   ```

5. Na pasta database, crie um arquivo `.env` com as variáveis de conexão do seu banco de dados PostgreSQL:
   ```
   DB_HOST=seu_host
   DB_PORT=sua_porta
   DB_NAME=seu_banco_de_dados
   DB_USER=seu_usuario
   DB_PASS=sua_senha
   ```

## Uso
### Streaming
Cria um producer que vai enviar mensagens para um tópico.
```bash
poetry run python .\streaming\producer.py 
```

Cria um consumer que vai consumir/ler as mensagens de um tópico.
```bash
poetry run python .\streaming\consumer.py 
```

### Batch
Cria um producer que vai enviar um lote de mensagens para um tópico.
```bash
poetry run python .\batch\producer_batch.py 
```

Cria um consumer que vai consumir/ler as mensagens em lote de um tópico.
```bash
poetry run python .\batch\consumer_batch.py 
```

### Database
Cria um producer que vai enviar 10 mensagens seguidas para um tópico.
```bash
poetry run python .\database\producer_data.py 
```

Cria um consumer que vai consumir/ler as mensagens de um tópico e salvar no banco de dados PostreSQL.
```bash
poetry run python .\database\consumer_data.py 
```

## Autor
[Rhanyele Teixeira Nunes Marinho](https://github.com/rhanyele)

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
