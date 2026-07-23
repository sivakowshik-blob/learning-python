i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("done")

i = 1
while i < 10:
    print(i)
    i += 1
    break
else:
    print("done")

while True :
     input("say something : ")
     break\
     
while True : 
    response = input("say something : ")
    if (response == "bye") :
        break