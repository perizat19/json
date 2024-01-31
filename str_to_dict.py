import json

# The 1st example

str = '{"id": 2762, "brand": "Nike", "qty": 100, "status": {"isForSale": true} }'
sneakers = json.loads(str)

print(sneakers["id"])
print(sneakers["brand"])
print(sneakers["qty"])
print(sneakers["status"])

sneakers_str = json.dumps(sneakers, indent=1)
print(sneakers_str)

# The 2nd example

products_str = '{"apple": 140, "mango": 500, "banana": 170, "status": {"is_available": true} }'
products = json.loads(products_str)

print(products["apple"])
print(products["mango"])
print(products["banana"])
print(products["status"])

products_dict_to_str = json.dumps(products, indent=1)
print(products_dict_to_str)

# Example 3

costs = '{"shirts": 1000, "jackets": 2500, "shoes": 3700, "status": {"is_available": false} }'

costs_dict = json.loads(costs)
print(costs_dict["status"])
print(costs_dict)


costs_str = json.dumps(costs_dict, indent=1)
print(costs_str)