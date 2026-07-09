#lists
amazon_cart = ["notebooks" , "laptop" , "mouse" , "keyboard"]
print(amazon_cart[0 :  : 2])
amazon_cart[0] = "files"
print(amazon_cart)
print(amazon_cart[1 : 3])
new_cart = amazon_cart[0 : 3]
new_cart[0] = "gum"
print(new_cart)

basket1 = [1 , 2 , 3 , 4 , 5]
basket1.append(100)
print(basket1)
basket2 = [11 , 12 , 13 , 14 , 15]
basket2.insert(2 , 100)
print(basket2)
basket3 = [8 , 9 , 10]
new_list = basket3.extend([100 , 101])    # this just modifies the list
print(new_list)

basket1.pop()
print(basket1)
basket2.pop(1)
print(basket2)
basket1.remove(4)
print(basket1)
basket2.clear()
print(basket2)

pulp1 = ["a" , "b" , "c" , "d" , "e" , "a"]
print(pulp1.index("d"))
print("d" in pulp1)
print("x" in pulp1)
print("i" in "hi hello bye")
print(pulp1.count("a"))
pulp2 = ["f" , "l" ,"g" , "h" , "i" , "j"]
pulp2.sort()
print(pulp2)
print(sorted(pulp1))
pulp1.reverse()
print(pulp1)
print(pulp2[  :   : -1])
print(list(range(1 , 100)))
sentence1 = ""
new_sentence1 = sentence1.join(["hi" , "hello" , "bye"])
print(new_sentence1)
sentence2 = " "
new_sentence2  = sentence2.join(["hi" , "hello" , "bye"])
print(new_sentence2)
sentence3 = " and "
new_sentence3 = sentence3.join(["hi" , "hello" , "bye"])
print(new_sentence3)
sentence4 = ",".join(["hi" , "hello" , "bye"])
print(sentence4)

a , b , c , *other , d = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(a)
print(b)
print(c)
print(other)
print(d)