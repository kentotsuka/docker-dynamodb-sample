import boto3

def update_data(table):
  table.update_item(
    Key = {
      "Classroom": "1組",
      "StudentNumber": 1
    },
    UpdateExpression = "set " \
      + "Subject" + "=:" + "Subject" + "," \
      + "Club" + "=:" + "Club",
    ExpressionAttributeValues = {
      ":" + "Subject" : "数学",
      ":" + "Club" : "サッカー"
    },
    ReturnValues="UPDATED_NEW"
  )


dynamodb = boto3.resource(
  service_name="dynamodb",
  endpoint_url="http://localhost:8000",
  # ローカル環境の場合、適当な文字列指定でアクセス可
  aws_access_key_id="aaaaaaaaaa",
  aws_secret_access_key="aaaaaaaaaa",
  region_name="aaaaaaaaaa",
)
# テーブルの取得
table = dynamodb.Table("School")
update_data(table)
print(f"Table status: {table.table_status}")
