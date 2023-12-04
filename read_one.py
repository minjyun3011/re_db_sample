from db_config import Message

def find_message():
    try:
        # msg = Message.get_by_id(id)
        msg = Message.get(Message.content == "Hello!!")
        print(msg.id, msg.user, msg.content, msg.pub_date)
    except:
        print("条件に一致するメッセージが見つかりませんでした。")

if __name__ == "__main__":
    find_message()
