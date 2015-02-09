from keen.client import KeenClient
from keen import scoped_keys
    
api_key='master api key'
    
write_key = scoped_keys.encrypt(api_key, {"allowed_operations": ["write"]})
read_key = scoped_keys.encrypt(api_key, {"allowed_operations": ["read"]})


print(write_key)
print("=========")
print(read_key)
