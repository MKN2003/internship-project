# Hashable objects
hashable_objects = { 42: "Integer",
                    "hello": "string",
                    (1, 2): "tuple",
                    frozenset([1, 2, 3]): "frozenset" 
                    }

print(hashable_objects)

# Unhashable objects
try:
    unhashable_objects = {
        [1, 2, 3]: "list"
    }
except TypeError as error:
    print(error)

try:
    unhashable_objects = {
        {1, 2, 3}: "set"
    }
except TypeError as error:
    print(error)

try:
    unhashable_objects = {
        {{1: 2}}:  "dictionary"
    }
except TypeError as error:
    print(error)