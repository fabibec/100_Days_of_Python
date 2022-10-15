with open("my_text.txt") as file:
    content = file.read()
    print(content)

with open("my_new_file.txt", mode="a") as file:
    file.write("I now try to work with files")