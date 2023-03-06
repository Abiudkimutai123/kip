data = {'color': 'red',
        'fruit': 'apple',
        'pet': 'dog',
        'car': 'van'}





num = 1
while num <= 4:
    print(data)
    num = num + 4
for key in data:
    value = data[key]
    print(key + ':' + str(value))