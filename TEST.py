
dumbpython = ("this", "is", "a", "tuple")
tuple2 = ("sphynx", "fox", "dog")
tuple3 = ("brown", "green", "red", "blue")
dicty = {dumbpython: "test 1", tuple2: "test 2", tuple3: "test 3"}
user = input("the test word")
for tupllle in dicty:
    if user in tupllle:
        print("yes", tupllle)
    else:
        print("test failed :(")