from db_config import Message

def delete_message():
    msg_id = input("削除するメッセージのIDを入力してください > ")
    msg = Message.get_by_id(msg_id)
    if not msg.delete_instance():
        print("削除に失敗しました。IDを再度確認してください。")

def edit_message():
    msg_id = input("編集するメッセージのIDを入力してください > ")
    msg = Message.get_by_id(msg_id)
    print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")
    msg.content = input("新しいメッセージを入力してください > ")
    msg.save()
    return msg

def main():
    user_name = input("ユーザーネームを入力してください > ")
    message = ""  # 繰り返し条件の初期化

    while True:
        # for msg in Message.select():
        #     print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")

        message = input("メッセージを入力してください > ")
        if message == "\q":
            break
        
        if message == "\d":
            delete_message()
            continue
        
        if message == "\e":
            edit_message()
        
        Message.create(user=user_name, content=message)



if __name__ == "__main__":
    main()
