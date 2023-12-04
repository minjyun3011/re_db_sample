from db_config import Message


def display_all_message():
    for msg in Message.select():
        print(msg.id, msg.user, msg.content, msg.pub_date)


def update_message(id):
    msg = Message.get_by_id(id)
    msg.user = "So Sato"
    msg.save()

if __name__ == "__main__":
    update_message(1)

display_all_message()
