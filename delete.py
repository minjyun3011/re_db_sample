from db_config import Message

def delete_message(id):
    msg = Message.get_by_id(id)
    msg.delete_instance()

if __name__ == "__main__":
    delete_message(2)
