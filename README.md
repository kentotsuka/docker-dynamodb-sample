# docker-dynamodb-sample

## バージョン
- Python 3.11.6
- Docker v20.10.21

## ビルド

### Dynamodbローカル設定
```bash
docker-compose up
```

`http://localhost:8001/`に`dynamodb-admin`が立ち上がる
データの状況などを確認できる

## 操作
`function/`にデータ操作のファイルを配置

```bash
python function/***.py
```