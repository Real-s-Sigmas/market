import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def add_value(key, value):
    if not r.exists(key):
        r.set(key, value)
        print(f"Добавлен новый ключ: {key} с значением: {value}")
    else:
        
        if r.type(key) == b'string':
            
            existing_value = r.get(key).decode('utf-8')
            
            r.delete(key)
            r.rpush(key, existing_value) 
            print(f"Ключ '{key}' преобразован в список с начальным значением: {existing_value}")
        
        existing_values = r.lrange(key, 0, -1)
        existing_values = [v.decode('utf-8') for v in existing_values]

        r.rpush(key, value)
        print(f"Добавлено значение '{value}' к ключу '{key}'")

# Пример использования
add_value('my_key', 'value1')
add_value('my_key', 'value2')
add_value('my_key', 'value1')