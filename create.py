from db_config import Message

def create_message():
    message = Message(user="Bob", content="Hello!!")
    message.save()
    Message.create(user="Tom", content="Hi!")

if __name__ == "__main__":
    create_message()
