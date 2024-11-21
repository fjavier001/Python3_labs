


def get_numbers():

    numbers = []
    for x in range(0, 10):
        numbers.append(x)

    return numbers

def generate_numbers():
    for x in range(0,10):
        yield x

for z in generate_numbers():
    print(z)

gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break