import os
import datetime
import logging
from peewee import SqliteDatabase
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

# .envの読み込み
load_dotenv()

# データベースへの接続設定
db = SqliteDatabase("re_peewee_db.sqlite")  # SQLite固定の場合

# db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()

class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)
    user = CharField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = "messages"

db.create_tables([Message])



# カリキュラムのコードではエラーが解消されなかった
# import os
# import logging
# from playhouse.db_url import connect
# from dotenv import load_dotenv

# # .envの読み込み
# load_dotenv()

# # データベースへの接続設定
# # db = SqliteDatabase("peewee_db.sqlite")  # SQLite固定の場合
# db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# # db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# # 接続NGの場合はメッセージを表示
# if not db.connect():
#     print("接続NG")
#     exit()
# TypeError: 'host' is an invalid keyword argument for Connection()
