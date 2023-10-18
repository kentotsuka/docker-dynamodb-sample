import boto3

def insert_data(table):
  schools = [
    {
      "Classroom": "1組",
      "StudentNumber": 1,
      "StudentName": {"LastName": {"山田"}, "FirstName": {"太郎"}},
      "Gender": {"Male"},
      "FavoriteColor": {"Red"},
    },
    {
      "Classroom": "2組",
      "StudentNumber": 1,
      "StudentName": {"LastName": {"田中"}, "FirstName": {"花子"}},
      "Gender": {"Female"},
      "Subject": {"理科"},
    }
  ]

  # 複数書き込み
  with table.batch_writer() as batch:
    for school in schools:
      batch.put_item(Item=school)
      print(f'Adding school: {school["Classroom"]}, {school["StudentNumber"]}')


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
insert_data(table)
print(f"Table status: {table.table_status}")
