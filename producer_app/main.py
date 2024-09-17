from fastapi import FastAPI, HTTPException
from data_models.queue_request_body import QueueRequestBody
import redis
import os
from dotenv import load_dotenv
from uuid import uuid4
from datetime import datetime
import random
from json import dumps
from time import sleep


# Load environment variables from the .env file
load_dotenv()

# fast api init
app = FastAPI()


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


def start_sending_messages_to_queue(message_count: int, delay: float = 0.1):
    try:
        db = redis_db()
        print("\n---------------------------------\n")
        for i in range(message_count):
            msg = {
                "id": str(uuid4()),
                "time_stamp":  datetime.utcnow().isoformat(),
                "messageIndex": i+1,
                "data": {
                    "x": random.randrange(0, 100),
                    "y": random.randrange(0, 100),
                }
            }
            msg_json = dumps(msg)
            print(f"\nSending msg : index -> {i+1}, id-> [ {msg.get('id')} ]")
            redis_queue_push(db, msg_json)
            if message_count < 100:
                sleep(delay)
        print("\n\n---------------------------------\n")
    except Exception as e:
        print("Error", e)
        raise HTTPException(status_code=400, detail=f"{e}")


@app.post("/start-message-queue")
async def start_queue(body: QueueRequestBody):
    start_sending_messages_to_queue(body.numberOfMessages)
    return {"sent": True}
