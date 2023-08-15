"""
try:
    with open("../package_1/out.txt", "w") as file:
        file.write("hi")
except:
    print("Error file")
    """
"""
try:
    with open("../package_1/out.txt", "a+") as file:
        file.seek(0)
        file.write("world\n")
        s = file.readlines()
        print(s)

except:
    print("Error file")
"""
"""
import pickle

books = [
    ("name", "andrey"),
    ("surname", "oveshkov")
]
with open("../package_1/out.txt", "wb") as file:
    pickle.dump(books, file)
"""
"""
import pickle

books = [
    ("name", "andrey"),
    ("surname", "oveshkov")
]
with open("../package_1/out.txt", "rb") as file:
    bs = pickle.load(file)
print(bs)
# [('name', 'andrey'), ('surname', 'oveshkov')]
"""
"""
import pickle

book_1 = ["andre"]
book_2 = ["oveshkov"]

try:
    with open("../package_1/out.txt", "wb") as file:
        b1 = pickle.dump(book_1, file)
        b2 = pickle.dump(book_2, file)
except:
    print("Error file")
"""
"""
import pickle

try:
    with open("../package_1/out.txt", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
except:
    print("Error file")
print(b1, b2, sep="\n")
# ['andre']
# ['oveshkov']
"""