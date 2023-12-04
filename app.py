import time

from db_config import Message

def delete_message():
    msg_id = input("削除するメッセージのIDを入力してください > ")
    try:
        msg = Message.get_by_id(msg_id)
        msg.delete_instance()
        print(f"{msg.user}さんのメッセージを削除しました。")
    except Message.DoesNotExist:
        print("指定されたIDのメッセージは存在しません。")

def edit_message():
    msg_id = input("編集するメッセージのIDを入力してください > ")
    try:
        msg = Message.get_by_id(msg_id)
        print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")
        time.sleep(1)
        msg.content = input("新しいメッセージを入力してください > ")
        msg.save()
        print(f"{msg.user}さんのメッセージを編集しました。")
    except Message.DoesNotExist:
        print("指定されたIDのメッセージは存在しません。")

def is_user_message_exist(user_name):
    return Message.select().where(Message.user == user_name).exists()

def main():
    while True:
        user_name = input("ユーザーネームを入力してください > ")
        if user_name == "":
            print("名前が未入力です。入力をやり直してください.")
            continue
        message = ""  # 繰り返し条件の初期化
        
        while True:
            message = input("メッセージか専用コマンド(\\e, \\d, \\q)を入力してください > ")
            if message == "\\q":
                break

            if message == "\\d":
                if is_user_message_exist(user_name):
                    delete_message()
                else:
                    print("あなたはこのメッセージを削除できません")
                time.sleep(1)
                continue

            if message == "\\e":
                if is_user_message_exist(user_name):
                    edit_message()
                else:
                    print("あなたはこのメッセージを編集できません")
                time.sleep(1)
                continue

            if message.startswith("\\"):
                time.sleep(1)
                print("無効なコマンドです。正しいコマンドを入力してください.")
                time.sleep(1)
                continue

            if message == "":
                time.sleep(1)
                print("メッセージが未入力です。1文字以上入力してください.")
                time.sleep(1)
                continue

            Message.create(user=user_name, content=message)
            print(f"{user_name}としてメッセージの入力が完了しました！")
            time.sleep(1)
        break

if __name__ == "__main__":
    main()
