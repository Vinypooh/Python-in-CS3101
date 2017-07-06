#Home 2
##############################################

#Part1
#List Comprehensions
#####################

#create the datasets using zip() method:
name = ['Bob', 'Mary', 'John', 'Carl', 'Meg']
hour = [40, 10, 0, 19, 60]
wage = [18.25, 20.00, 100.90, 17.21, 22.10]

employees = zip(name, hour, wage)

lst = [(name, hour * wage) for (name, hour, wage) in employees if hour != 0] 
print(lst)


#Part2
#Dictionaries
##########################
fruit_to_color = { 
                    'banana' : 'yellow',
                    'blueberry' : 'blue',
                    'cherry' : 'red',
                    'lemon' : 'yellow',
                    'kiwi' : 'green',
                    'strawberry' : 'red',
                    'tomato' : 'red'
                    }
color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    if color_to_fruit.get(color):
        color_to_fruit[color].append(fruit)
    else:
        color_to_fruit[color] = [fruit]

    #or using in test:
    #if color in color_to_fruit.keys():
    #    color_to_fruit[color].append(fruit)
    #else:
    #    color_to_fruit[color] = [fruit]
print(color_to_fruit)

