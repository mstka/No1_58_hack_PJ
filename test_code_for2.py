import sqlite3
import hashlib

# データベース接続のセットアップ
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# ユーザーテーブルの作成（初回実行時のみ）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# パスワードをハッシュ化する関数
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ユーザー登録関数
def register_user(name, email, password):
    hashed_password = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                       (name, email, hashed_password))
        conn.commit()
        print("✅ ユーザー登録が完了しました！")
    except sqlite3.IntegrityError:
        print("⚠️ このメールアドレスは既に登録されています。")

# ユーザー登録を実行
if __name__ == "__main__":
    name = input("名前を入力してください: ")
    email = input("メールアドレスを入力してください: ")
    password = input("パスワードを入力してください: ")

    register_user(name, email, password)
