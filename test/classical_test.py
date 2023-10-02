import secrets
from src import classical

def test_gen():
    token = secrets.token_hex(5)
    result = classical.gen(token, 200)
    print(result)



    
