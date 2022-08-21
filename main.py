# a = "hello "
# c = "this world"
# b = a + c + " hi"
# print(b)

# a = "this"
# c = "hi"
# b = "hello {} world {}".format(a, c)
# print(b)
#
# a = "this"
# c = "hi"
# b = "hello {1} world {0}".format(a, c)
# print(b)

# a = "this"
# c = "hi"
# b = f"hello {c} world {a}"
# print(b)

a = "this"
c = "hi"
b = "hello %s world %s" % (a, c)
print(b)
