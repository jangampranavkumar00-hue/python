msg="HELLO PYTHON "
print(msg.lower())
print(msg.upper())
print(msg.capitalize())
print(msg.casefold())
print(msg.center(50))
print(msg.count("L"))
print(msg.endswith("PYTHON "))
print(msg.startswith("H"))
print(msg.startswith("HELLO"))
print(msg.find("L"))
print(len(msg))
print(msg.replace("PYTHON","JAVA"))
print(msg.replace("HELLO","hi"))
print(msg.split(" "))
print(msg.index("L"))
print(msg.find("L"))
print(msg.isalnum())
print(msg.isalpha())
print(msg.isnumeric())
msg="   hello python  "

print(msg.lstrip())
msg=["hello","python","java"]
s="myself"
m1=s.join(msg)
print(m1)
#string formating
#process of placing variables in a string
name="pranav"
clg="mrvtc"
rollno=123
#concatenation
print("my name is "+name+" my rollno is"+str(rollno))
#.format string
print("my name is {} my rollno is {}".format(name,rollno))
print("my name is{} my rollno is {}".format(rollno,name))
#fstring
print(f"my name is {name} my rollno is {rollno}")