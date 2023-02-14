int_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = []
for x in int_lst:
    new_lst.append(x **2)

print(new_lst)

print(list(map(lambda x: x ** 2, int_lst)))

cars = [
    {
        'make': 'Mercedes',
        'model': 'S500',
        'color': 'Black'
    },
    {
        'make': 'BMW',
        'model': 'M5',
        'color': 'red'
    },
    {
        'make': 'Audi',
        'model': 'A7',
        'color': 'white'
    }
]

def return_dictionary(car):
    make, model, color = car['make'], car['model'], car['color']
    return {
        color: {
            'make': make,
            'model': model
        }
    }

new = map(return_dictionary, cars)
for color in new:
    print(color)