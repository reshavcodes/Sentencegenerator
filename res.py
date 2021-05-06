from requests import get
import json

def data(num):
    z= get(f"https://random-word-api.herokuapp.com/word?number={num}")
    return json.loads(z.content)
if __name__=="__main__":
    print(data(5))