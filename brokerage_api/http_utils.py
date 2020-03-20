def check_http_status(res):
    status = res.status_code
    if status == 200:
        return True
    if status == 400:
        print("BAD REQUEST")
        return False
    if status == 401:
        print("UNAUTHORIZED")
        return False
    if status == 403:
        print("FORBIDDEN")
        return False
    if status == 404:
        print("URL NOT FOUND")
        return False
    if status == 429:
        print("RATE LIMIT HIT, TOO MANY REQUESTS")
        return False   
    if status == 500:
        print("INTERNAL SERVER ERROR")
        return False 
    if status == 501:
        print("NOT IMPLEMENTED")
        return False
    if status == 502:
        print("BAD GATEWAY")
        return False

def attempt_json_decode(res):
    val = None
    try:
        val = res.json()['response']
    except json.JSONDecodeError:
        print(res)
        print("Failed Decoding JSON")
    return val