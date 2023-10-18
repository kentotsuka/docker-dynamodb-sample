import boto3
from boto3.dynamodb.conditions import Key

# パーミッションキーとソートキーを指定した一意検索
def fetch_by_unique(table):
  data = table.query(
           KeyConditionExpression = Key("Classroom").eq("1組") & Key("StudentNumber").eq(1)
         )
  return data

# 前方一致で検索
def fetch_by_prefix(table):
  data = table.query(
           KeyConditionExpression = Key("Classroom").eq("1組")
          )
  return data

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

print("一意検索")
print(fetch_by_unique(table))
print("-------------")
print("前方一致検索")
print(fetch_by_prefix(table))
print("-------------")
print(f"Table status: {table.table_status}")
