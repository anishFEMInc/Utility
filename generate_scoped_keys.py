from keen.client import KeenClient
from keen import scoped_keys
    
api_key='7EC010A4C033AF0EAC60B13AEA0EF1D7'
    
write_key = scoped_keys.encrypt(api_key, {"filters": [{
                                                      "property_name": "unit_domain",
                                                      "operator": "eq",
                                                      "property_value": "fem-inc.com"
                                                      }],"allowed_operations": ["write"]})
read_key = scoped_keys.encrypt(api_key, {"filters": [{
                                                     "property_name": "unit_domain",
                                                     "operator": "eq",
                                                     "property_value": "fem-inc.com"
                                                     }],"allowed_operations": ["read"]})


print(write_key)
print("=========")
print(read_key)
