import random

exit_loop = False

number_of_wishes = 0
wish = []
desired = [0, 1]
guarantee = False

for i in range(0,854):
    wish.append(i)
    
for i in range(16):
    wish.append(2000)

for i in range(130):
    wish.append(1000)

for i in range(0, 100):
    
    result = random.choice(wish)
    
    if number_of_wishes % 90 == 0 and number_of_wishes > 0 and guarantee == False:
        result = 2000

    elif number_of_wishes % 10 == 0 and number_of_wishes > 0:
        result = 1000
        
    else:
        result = result
        
    if guarantee == False:
        
        featured = random.choice(desired)
        
        if result == 1000 and featured == 1:
            number_of_wishes += 1

        elif result == 1000 and featured == 0:
            guarantee = True
            number_of_wishes += 1

        elif result == 2000 and featured == 1:
            number_of_wishes += 1
            exit_loop = True

            with open("number_of_wishes_experimental.txt", mode = "a", encoding = "UTF-8") as file:
                file.write(str(number_of_wishes) + "\n")

            number_of_wishes = 0
            
        elif result == 2000 and featured == 0:
            guarantee = True
            number_of_wishes += 1
            
        else:
            number_of_wishes += 1

    else:
        
        if result == 1000:
            number_of_wishes += 1
            guarantee = False
            
        elif result == 2000:
            number_of_wishes += 1
            exit_loop = True

            with open("number_of_wishes_experimental.txt", mode = "a", encoding = "UTF-8") as file:
                file.write(str(number_of_wishes) + "\n")

            number_of_wishes = 0
                
