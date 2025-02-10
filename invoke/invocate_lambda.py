import boto3
import json
 
# Inicializa o cliente Lambda
lambda_client = boto3.client('lambda')
 
# Define o ARN da função Lambda
lambda_arn = 'arn:aws:lambda:us-east-1:266549158321:function:invoke-dev-Invoke'
 
# Dados que você deseja enviar para a função Lambda
payload = {
    "nome": "teste",
    "idade": "10"
}
 
# Dispara a função Lambda
response = lambda_client.invoke(
    FunctionName=lambda_arn,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload),
)
 
# Lê a resposta
response_payload = json.loads(response['Payload'].read())
 
print('Resposta da Lambda:', response_payload)
