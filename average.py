total_wishes = 0
recursion_reduction = 0
true_total_wishes = 0
price_of_wishes = 2


with open("number_of_wishes_experimental.txt", mode = "r", encoding = "UTF-8") as file:         ##reading the file into a variable then splitting into a list
    content = file.read()
    wish_list = content.split("\n")
    
recursion = int(len(wish_list) - 1)         ##last line is always '' hence last item in the list therefore can't be added to the list, this is my lazy way around it

for i in range(0, recursion):       ##totalling up the number of wishes used

    total_wishes += int(wish_list[int(i)])


print("this is how many total wishes were required " + str(total_wishes))       ##printing the total wishes and the amount of times the character was obtained
print("to get " + str(recursion) + " of the desired 5* character")
average = total_wishes/recursion            ##finding the average
cost = price_of_wishes*average              ##finding the average cost of the character

print("this is how many wishes it took on average: " + str(average) + "\n")     ##printing the average and then the cost
print("this would cost $" + str(cost))
