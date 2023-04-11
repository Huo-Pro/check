import simple.simple_pb2 as simple_pb2

# 创建一个 SimpleMessage 对象
simple_message = simple_pb2.SimpleMessage()
simple_message.name = "Lily"
simple_message.id = 5678
simple_message.email = "lily@example.com"

phone_number = simple_message.phones.add()
phone_number.number = "123-4567"
phone_number.type = simple_pb2.Person.WORK

# 创建一个 AddressBook 对象，并将 simple_message 添加到其中
address_book = simple_pb2.AddressBook()
address_book.people.append(simple_message)

# 将 AddressBook 对象写入二进制文件
with open("address_book.bin", "wb") as f:
    f.write(address_book.SerializeToString())

# 从二进制文件中读取 AddressBook 对象
with open("address_book.bin", "rb") as f:
    address_book = simple_pb2.AddressBook()
    address_book.ParseFromString(f.read())

# 打印出其中的 Person 对象
for person in address_book.people:
    print(f"Name: {person.name}")
    print(f"ID: {person.id}")
    print(f"Email: {person.email}")
    for phone_number in person.phones:
        print(f"Phone ({phone_number.type}): {phone_number.number}")