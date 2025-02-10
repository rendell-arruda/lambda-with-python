import boto3
import json
 
# Inicializa o cliente Lambda
lambda_client = boto3.client('lambda')
 
# Define o ARN da função Lambda
lambda_arn = 'arn:aws:lambda:us-east-1:266549158321:function:invoke-dev-Invoke'
 
# Dados que você deseja enviar para a função Lambda
# Define um JSON com os dados que serão enviados para a função Lambda.
payload = {
    "nome": "teste",
    "idade": "10"
}
 
# Dispara a função Lambda
	# FunctionName=lambda_arn → Especifica qual função Lambda será chamada.
	# •	InvocationType='RequestResponse' → Define que a chamada será síncrona, ou seja, o código aguardará a resposta da Lambda antes de continuar.
	# •	Payload=json.dumps(payload) → Converte o dicionário Python para um JSON antes de enviar.
response = lambda_client.invoke(
    FunctionName=lambda_arn,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload),
)
 
# # Lê a resposta
# O response['Payload'] contém a saída da função Lambda.
# 	•	O .read() lê os bytes retornados.
# 	•	json.loads(...) converte a string JSON de volta para um dicionário Python.
response_payload = json.loads(response['Payload'].read())
 
print('Resposta da Lambda:', response_payload)
