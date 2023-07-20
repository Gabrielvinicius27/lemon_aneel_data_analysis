# lemon_ANEEL_data_analysis
# Contexto

Desenvolver uma arquitetura para extrair dados públicos da ANEEL com objetivo de entender o cenário atual de geração de energia.

## Arquitetura utilizando AWS

![image](https://github.com/Gabrielvinicius27/lemon_aneel_data_analysis/blob/main/images/arquitetura_2.png)

1.	**API Gateway**: Configurar APIs e autenticação, por exemplo API da ANEEL.
2.	**Lambda**: Utilizando uma abordargem serverless podemos reduzir custos e aproveitar as integrações com outros serviços da AWS. 
3.	**AWS Lake Formation**: Governança e catálogo de dados. Dados armazenados no S3, o armazenamento é separado em três etapas, bronze com dados raw, silver com dados acurados e gold com dados prontos para serem consultados em sua melhor qualidade. As tabelas ficam registradas no AWS Glue Data Catalog. 
4.	**AWS Glue**: A transformação do dado é feita nesse serviço com o uso de spark e de forma serverles em jobs schedulados. 
5.	**Athena**: Serviço para criar queries SQL e consultas ad-hoc. 
6.	**Tableau**: Visualização dos dados. 
7.	**Kinesis**: Os dados do API gateway passam por esse serviço e a cada quantidade específica de registros aciona um gatilho para iniciar a Lambda Function. 
8.	**Lambda**: Envia os dados para o Dynamo DB. 
9.	**Dynamo DB**: Banco de dados NoSQL serverless para consulta e escrita rápida dos dados de stream.

## Arquitetura utilizando GCP

![image](https://github.com/Gabrielvinicius27/lemon_aneel_data_analysis/blob/main/images/arquitetura_1.png)

Aqui temos uma abordagem mais simples seguindo o modelo Serverless.
 
1.	**Cloud Functions**: Coleta de dados de API, ou csv em um endereço URL, a cloud function executa um código em python e armazena o resultado no cloud storage. Esta cloud function também pode executar um submit para o Dataproc.
2.	**Cloud Storage**: Dado armazenado e pronto para ser enviado ao Bigquery.
3.	**Dataproc**: Execução de lotes Serverless utilizando pyspark, exemplo de código de extração abaixo.
4.	**Bigquery**: Ambiente ideal para tratar dados em grandes volumes utilizando SQL, é integrado com ferramentas de visualização de dados.
5.	**Pub/Sub**: Serviço de mensageria, pode se conectar ao cloud logging e aguardar que a tabela seja criada, acionando um trigger para uma cloud function que extrai métricas de data quality. Por exemplo, timeliness (dado está atualizado?), completeness (dados faltando, quantidade de nulos), uniqueless (dados duplicados?), outliers (existem dados que estão fora do padrão dos últimos dias)?

## Exemplo de extração utilizando dataproc, GCS -> Bigquery

Para iniciar o lote Serverless é necessário enviar este comando, isso pode ser feito diretamente no cloud shell ou então através de cloud function:
![image](https://github.com/Gabrielvinicius27/lemon_aneel_data_analysis/images/carbon (1).png)

O arquivo Python está armazenado em um bucket:
![image](https://github.com/Gabrielvinicius27/lemon_aneel_data_analysis/images/carbon (2).png)

## Próximos passos
* Provisonar recursos utilizando terraform para termos infra as code.



