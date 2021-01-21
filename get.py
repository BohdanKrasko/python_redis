import redis
from redis import Redis
host = 'localhost'
port = 6379
password = ''

def hello_redis():
    try:
        r = redis.Redis()
        r.set("msg:hello", "Hello Redis!!!")

        msg = r.get("msg:hello")

        print(msg)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    hello_redis()
