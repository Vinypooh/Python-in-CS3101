#part 2
fruit_to_color={'banana':'yellow',
              'blueberry':'blue',
              'cherry':'red',
              'lemon':'yellow',
              'kiwi':'green',
              'strawberry':'red',
              'tomato':'red'}

color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    if not color in color_to_fruit:
        color_to_fruit[color] = []
    color_to_fruit[color].append(fruit)

