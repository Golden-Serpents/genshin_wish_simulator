import random

number_of_wishes = 0
wish = []
desired = [0, 1]
guarantee = False

for i in range(0,854):  ##creating the list of values with some duplicates to create weighted probability
    wish.append(i)
    
for i in range(16):
    wish.append(2000)

for i in range(130):
    wish.append(1000)

for i in range(0, 100):       ##looping for a set number of wishes
    
    result = random.choice(wish)        ##chosing result of the wish
    
    if number_of_wishes % 90 == 0 and number_of_wishes > 0:     ##creating an approximation of the pitty system, only approximating as i don't want to
        result = 2000

    elif number_of_wishes % 10 == 0 and number_of_wishes > 0:   ##try to go from 0.6% through to 100% at 90 wishes and just use 1.6% as average with a guarantee every 90th
        result = 1000
        
    else:           ##finishing the selection statement
        result = result
        
    if guarantee == False:      ##proceedure when a 4/5 star that is not part of the set of featured characters hasn't been rolled yet
        
        featured = random.choice(desired) ##chosing whether the character is desired if it is 4/5 star if it is rolled, it may significantly reduce computing time if it is only done when the result is rolled however i would have to rewrite code and i'm lazy with plenty of time
        
        if result == 1000 and featured == 1:        ##a 4* being rolled that is in the set of featured characters
            number_of_wishes += 1

        elif result == 1000 and featured == 0:      ##a 4* being rolled that is not in the set of featured characters granting a guarantee that the next 4/5 star rolled is in the set of featured characters
            guarantee = True
            number_of_wishes += 1

        elif result == 2000 and featured == 1:      ##a 5* being rolled in the set of featured characters
            number_of_wishes += 1

            with open("number_of_wishes_experimental.txt", mode = "a", encoding = "UTF-8") as file: ##appending the number of wishes taken to roll the desired 5 star to the file
                file.write(str(number_of_wishes) + "\n")

            number_of_wishes = 0        ##resetting number of wishes so that it doesn't become a cumulative total of wishes
            
        elif result == 2000 and featured == 0:  ##a 5* being rolled that is not in the set of featured characters creating a guarantee that the next 4/5 star is a desired character
            guarantee = True
            number_of_wishes += 1
            
        else:           ##generic result that does not contain 4/5* but still uses a wish
            number_of_wishes += 1

    else:       ##guarantee can only be True or False so simply using else should be ok as there is no way i can envision that guarantee is not either
        
        if result == 1000:      ##result is a 4* and is guaranteed to be featured. this means that it resets the guarantee
            number_of_wishes += 1
            guarantee = False
            
        elif result == 2000:            ##result is a 5* and is guaranteed to be the desired character
            number_of_wishes += 1
            guarantee = False

            with open("number_of_wishes_experimental.txt", mode = "a", encoding = "UTF-8") as file:     ##writing to the file
                file.write(str(number_of_wishes) + "\n")

            number_of_wishes = 0        ##resetting wish count

        else:               ##wish is not desired and 1 is added to wish count
            number_of_wishes += 1
                
