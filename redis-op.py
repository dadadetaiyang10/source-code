from redis import Redis

if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与redis服务器建立连接
        redis_conn = Redis(host="127.0.0.1", port=6379, db=0)
        # 1.set("key", "value")
        result = redis_conn.set("name", "Tom")
        print(result)

        # 2.get("key")
        result = redis_conn.get("name")
        print(result)

        # 3.set("key", "new value")
        result = redis_conn.set("name", "Alex")
        print(result)

        # 4.delete("key")
        # result = redis_conn.delete("name")
        # print(result)

        # 5.keys()
        result = redis_conn.keys()
        print(result)
    except Exception as e:
        print(e)
