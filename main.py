from eds import EDSFile

file = EDSFile(filename="test.eds", key="qwe123")

file.write(data="test")
print(file.read())
