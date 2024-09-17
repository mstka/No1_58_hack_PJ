今回はこれをサーバーとフロントエンドとの通信用に使用→bomu.info:60000


!!attention!!
まだこのAPIは使える状態ではないので、APIを使える前提でフロントエンドを作っていただきたいです


「bomu.info:60000/img_list」
パズルに使用する画像のファイル名の一覧を取得する
一番最初の状態の時の画像の並べ方が取得できる
レスポンスはjson形式

{
    "img_list":[
        "画像名",
        "画像名",
        "画像名",
        "画像名",
        "画像名"],
    "pos":{
        "X座標":{
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名"
        },"X座標":{
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名"
        },"X座標":{
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名",
            "Y座標":"画像名"
        }
    }
}

「bomu.info:60000/画像名」
画像が取得できる

「bomu.info:60000/q_and_a」
問題文と答えの選択肢を取得することが出来る
レスポンスはjson形式

{
    "question":"問題文",
    "answer":[
        "回答の選択肢_1",
        "回答の選択肢_2",
        "回答の選択肢_3",
        "回答の選択肢_4"
    ]
}


「bomu.info:60000/user/ユーザー名」
"ユーザー名"で指定されたユーザー名でサーバーに参加登録する

「bomu.info:60000/send_answer/ユーザー名/選択肢の番号」
"ユーザー名"で指定されたユーザーの選択肢の回答番号が"選択肢の番号"であるとして送信する

「bomu.info:60000/make_room」
ルームを新しく作成する
