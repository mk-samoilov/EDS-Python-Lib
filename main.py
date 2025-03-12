from eds import EDSFile

file = EDSFile(filename="exemple.eds", key="qwe123")

file.write(new_data="exemple data")
print(file.read())
