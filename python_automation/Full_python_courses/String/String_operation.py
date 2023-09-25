str = "My Name Is Rahul Rahul Rahul"

str = str.replace("Rahul", "Rahul Verma", 2)
print(str)
str="My Name Is Parikh"
li=str.split()#Return a list of strings
print(li)

str="My,Name, Is, Parikh"
li=str.split(',')#delimiter
print(li)

str="My,Name, Is, Parikh"
li=str.split(',',1)
print(li)

str="My,Name, Is, Parikh"
li=str.split(',',2)
print(li)

str="My Name Is Parikh"
str=str.replace("Parikh","Rohan")
print(str)

str="My Name Is Parikh"
str=str.replace("Which","Rohan")
print(str)

str="My Name Is Parikh Parikh Parikh"
str=str.replace("Parikh","Rohan",2)
print(str)

str="My Name Is Parikh"
index=str.find("Na")
print(index)

str="My Name Is Parikh"
index=str.find("Nae")
print(index)

str="My Name Is Parikh Parikh"
index=str.find("Par")
print(index)

str="My Name Is Parikh Parikh"
index=str.find("Par",16,21)
print(index)

str="My Name Is Parikh"
str=str.lower()
print(str)
str=str.upper()
print(str)

str="My Name Is Parikh"
ans=str.startswith("My Na")
print(ans)

str="My Name Is Parikh"
ans=str.startswith("My Nae")
print(ans)

str="My Name Is Parikh"
ans=str.startswith("Pae",11,25)
print(ans)

str="My Name Is Parikh"
ans=str.startswith("Pa",11,25)
print(ans)