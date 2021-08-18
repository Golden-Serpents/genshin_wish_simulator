total_wishes = 0
recursion_reduction = 0
true_total_wishes = 0
price_of_wishes = 2


with open("number_of_wishes_experimental.txt", mode = "r", encoding = "UTF-8") as file:
    content = file.read()
    wish_list = content.split("\n")
    
recursion = int(len(wish_list) - 1)

for i in range(0, recursion):
    if int(wish_list[int(i)]) > 1:
        total_wishes += int(wish_list[int(i)])
        true_total_wishes += int(wish_list[int(i)])
        recursion_reduction += 1
        
    else:
        true_total_wishes += int(wish_list[int(i)])

adjusted_recursion = recursion - recursion_reduction

print("this is how many total wishes were required if you never hit first time " + str(total_wishes))
print("to get " + str(recursion) + " of the desired 5* character")
average = total_wishes/recursion
cost = price_of_wishes*average

print("this is how many wishes it took on average: " + str(average) + "\n")
print("this would cost $" + str())

print("this is how many total wishes were required " + str(true_total_wishes))
print("to get " + str(recursion) + " of the desired 5* character\n")
average = true_total_wishes/adjusted_recursion
cost = price_of_wishes*average

print("this is how many wishes it took on average: " + str(average))
print("this would cost $" + str())
