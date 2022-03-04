import sys
from time import sleep

def dictionary():
    food_dict = {
        "brand":"pizza hut",
        "type":"cheese",
        "rating": True
    }

    print(food_dict)
    print(food_dict["brand"])
    print(food_dict.get("brand"))
    print(len(food_dict))

    if "rating" in food_dict:
        print("Yes, 'model' is in the food dictionary")

    for key in food_dict:
        print(key)
        print(food_dict[key])

    for value in food_dict.values():
        print(value)

    for key, value in food_dict.items():
        print(key, value)

def Nested_dict():
    family = {
        "Armaan": {
            "age":14,
            "Legal": "Mashuq"
        },
        
        "Mahfuza": {
            "age":43,
            "Legal":"Lima"
        },

        "Shafiqul": {
            "age":46,
            "Nickname":"Shafiq"
        }
    }

    for key in family:
        print(key)
        print(family[key])
        #! Or:
        print(f"Key: {key} Value: {family[key]}")

    print("\n")

    for key, value in family.items():
        print(key, value)
        print(f"Key: {key}, Value: {value}")

