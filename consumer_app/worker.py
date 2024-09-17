import redis
import os
from dotenv import load_dotenv
import random
from json import loads
from time import sleep


# Load environment variables from the .env file
load_dotenv()

database = os.getenv("REDIS_DB_NO")
# required if you have setup password for redis, I don't have configured password so don't neeed it
secret_key = os.getenv("REDIS_PASSWORD")
queue_name = os.getenv("REDIS_QUEUE_NAME")


def redis_db():
    db = redis.Redis(
        host="localhost",
        port=6379,
        db=database,
        decode_responses=True
    )
    db.ping()
    return db


def redis_queue_push(db, message):
    db.lpush(queue_name, message)


def redis_queue_pop(db):
    # Use BRPOP to block until a task is available
    _, message = db.brpop(queue_name)
    return message


def processMessage(db, msg_json: str):
    message = loads(msg_json)
    print(
        f"\nMessage recieved : id -> {message['id']}, no. -> {message['messageIndex']}")

    # lets add some random logic to fail a few msgs to see how our system behaves
    is_success = random.choices((True, False), weights=(5, 1), k=1)[0]

    if is_success:
        print("Message processed ✅")
    else:
        print("Message processing failed ❌")
        redis_queue_push(db, msg_json)


def main():
    print("Started Listening...")
    db = redis_db()
    while True:
        message = redis_queue_pop(db)
        if message:
            processMessage(db, message)
        else:
            print("No tasks in the queue. Waiting...")


if __name__ == "__main__":
    main()
