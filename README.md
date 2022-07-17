# FastAPI 入門


## メモ
### RESTful API
- アドレス可能性 URIでアクセス可能
- ステートレス性 セッション情報を持たない
- 接続性 リンクで飛べる
- 統一インターフェース　HTTPメソッド

APIを叩く上で必要な情報
- APIに接続するための情報
    - APIエンドポイント(URL)
    - APIキー(ID)
 - APIに送信する情報
    - HTTPメソッド(POST or GET)
    - ヘッダー(データの種類　APIキー などの認証情報)
    - ボディー(JSON 送受信したい情報)

Java Script Object Notation
```json
{"key":"value"}
```

HTTPメソッド
- GET 取得
- POST 送信
- PUT 編集
- DELETE 削除

