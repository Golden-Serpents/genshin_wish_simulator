total_wishes = 0
price_of_wish = 2

with open("number_of_wishes_experimental.txt", mode = "r", encoding = "UTF-8") as file:
    content = file.read()
    wish_list = content.split("\n")
    
recursion = len(wish_list) - 1

for i in range(0, recursion):
    total_wishes += int(wish_list[int(i)])
    
print("this is how many total wishes were required " + str(total_wishes))
print("to get " + str(recursion) + " of the desired 5* character")
average = total_wishes/recursion

print("this is how many wishes it took on average: " + str(average))

dollars = average * price_of_wish

print("this is equal to $" + str(dollars))
