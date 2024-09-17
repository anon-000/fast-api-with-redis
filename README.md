# { Trying the Redis Queue with FAST API }
-------------------
## How to run/test it ?
```

* git clone
* create a virtual environment
* pip install -r requirements.py
* create a .env file and store your REDIS_DB_NO, REDIS_PASSWORD(if any), REDIS_QUEUE_NAME
* now we are ready with basic setup.

-------------- Running Producer Code ( Inside virtual env) --------------

* uvicorn producer_app.main:app --reload

---------------------------------------------------

-------------- Running Consumer/Worker Code ( Inside virtual env) --------------
( If you want multiple workers then follow the below for each worker, open separate terminal and run below code )

* python -m consumer_app.worker

---------------------------------------------------

-------------- How to Test --------------

Open a fresh terminal and hit your fast API end point : /start-message-queue

* Run the following curl command in terminal

curl --location 'localhost:8000/start-message-queue' \
--header 'Content-Type: application/json' \
--data '{
    "numberOfMessages": 3
}'

-----------------------------------------
```

-------------------


### 1. Setting up Producers and Consumers
-------------------




https://github.com/user-attachments/assets/dd606d8d-cee8-452f-8c3c-c547ea1310d1







### 2. Sending & Recieving 10 messages (with some fraction of delay 0.1)
-------------------




https://github.com/user-attachments/assets/95379c15-0e63-4d91-9952-3db3447d255f






### 3. Sending & Recieving 3000 & 30,000 messages (with no delay : You can see the speed) 
-------------------



https://github.com/user-attachments/assets/c5d9ab32-3371-463c-a131-769dcdd27d91








