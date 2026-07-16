file = open("example.txt", "w")
file.write("hello world\n")
file.write("my name is re\n")
file.write("this is file")
file.close()

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

file = open("example.txt", "a")
file.write("this is appended.\n")
file.close()

try:
    with open("missing file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
except IOError:
    print("An IO error occoured")

