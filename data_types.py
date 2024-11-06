# ------- dictionaries --------

dict_1 = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "colors": ["red", "white", "blue"],
    "year": 1964,
    "year": 2020
}

print(dict_1.__class__) # <class 'dict>

# ----- using the dict constructor ------
dict_2 = dict(name="John", age=36, country="Norway")
print(dict_2)

# --- looping ---
for key in dict_2.keys():
    print(dict_2[key])


# --- check existence ---
print("age" in dict_2) 
# --- updating ---
dict_2.update({"name": "Nathen"})
dict_2["school"] = "harvard"


# --- deleting ---
del dict_1
del dict_2["country"]


