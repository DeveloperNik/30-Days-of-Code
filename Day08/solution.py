n = int(input())

phonebook = {}

for i in range(0, n):
    entry = str(input()).split(" ")

    name = entry[0]
    num = int(entry[1])
    phonebook[name] = num

a = 1
while a == 1:
    name = str(input())

    if (name == False):
        break
    if name in phonebook:
        phone = phonebook[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
