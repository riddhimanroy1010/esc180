string = "hello.This is my thing!this is something new."
string = string.replace("!", ".")
print(string.casefold())
print(string.split("."))

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave', 'Alice']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']