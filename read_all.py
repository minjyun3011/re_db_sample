from db_config import Message

def display_all_message():
    for msg in Message.select():
        print(msg.id, msg.user, msg.content, msg.pub_date)

if __name__ == "__main__":
    display_all_message()
