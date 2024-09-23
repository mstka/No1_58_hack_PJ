Running frontend: in Fronted folder -> In terminal run: "npm run dev" or "npm run build && npm run preview".

---

今回はこれをサーバーとフロントエンドとの通信用に使用→bomu.info:3000


!!attention!!
まだこのAPIは使える状態ではないので、APIを使える前提でフロントエンドを作っていただきたいです


「bomu.info:3000/img_list」
パズルに使用する画像のファイル名の一覧を取得する
一番最初の状態の時の画像の並べ方が取得できる
レスポンスはjson形式

{
    "pos":{
        "Y座標":{
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名"
        },"Y座標":{
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名"
        },"Y座標":{
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名",
            "X座標":"画像名"
        }
    }
}

「bomu.info:3000/画像名」
画像が取得できる

「bomu.info:3000/q_and_a」
問題文と答えの選択肢と、回答の開始時刻と終了時刻を取得することが出来る
レスポンスはjson形式

{
    "question":"問題文",
    "answer":[
        "回答の選択肢_1",
        "回答の選択肢_2",
        "回答の選択肢_3",
        "回答の選択肢_4"
    ],
    "start_time":{
        "hour":"何時",
        "minute":"何分"
    },
    "finish_time":{
        "hour":"何時",
        "minute":"何分"
    }
}



「bomu.info:3000/send_answer/choice_answer/user_name」
"ユーザー名"で指定されたユーザーの選択肢の回答番号が"選択肢の番号"であるとして送信する

メソッドはGETメソッド


レスポンスは以下のjson形式
{
    "result":"success"
}


「bomu.info:3000/ranking」
ゲームのランキングを取得する

{
    "ranking":[
            "1位のユーザー名",
            "2位のユーザー名",
            "3位のユーザー名"
        ]
}



=========ここから下はAPIとは別なのでフロントエンドで実装しなくてもいい=========

「bomu.info:3000/make_room/何秒後にゲーム開始するか」
ルームを新しく作成する

=======

