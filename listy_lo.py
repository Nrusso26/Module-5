

food = ["rice", "beans"]
Twowords = food[:]
food.append("broccoli")
food.extend("pizza")
food.extend("bread")


print(Twowords[:])

breakfast = ["eggs", "fruit", "orange juice"]
length = len(breakfast)

middle_index = length

first_half = breakfast[:middle_index]
second_half = breakfast[middle_index:]

print(first_half)
print(second_half)

num = 0
tot = 0.0
while True:
    number = input("Enter a number: ")
    if number == 'stop':
        break
    try :
        num1 = float(number)
    except:
        print('Invailed Input')
        continue
    num = num+1
    tot = tot + num1
print ('Completed! Here are your results: ')
print (tot , num , tot/num)