import boto3


def create_table(dynamodb=None):
  table = dynamodb.create_table(
    TableName="School",
    KeySchema=[
      # 教室(パーティションキー)
      {"AttributeName": "Classroom", "KeyType": "HASH"},
      # 出席番号(ソートキー)
      {"AttributeName": "StudentNumber", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
      {"AttributeName": "Classroom", "AttributeType": "S"},
      {"AttributeName": "StudentNumber", "AttributeType": "N"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
  )
  return table


dynamodb = boto3.resource(
  service_name="dynamodb",
  endpoint_url="http://localhost:8000",
  # ローカル環境の場合、適当な文字列指定でアクセス可
  aws_access_key_id="aaaaaaaaaa",
  aws_secret_access_key="aaaaaaaaaa",
  region_name="aaaaaaaaaa",
)
table = create_table(dynamodb)
print(f"Table status: {table.table_status}")
