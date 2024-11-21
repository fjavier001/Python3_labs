import decimal

def frange(start, stop, step=0.25):
    curr = float(start)
    while curr < stop:
        yield curr
        curr += step

def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = start
        curr = 0.0
    else:
        curr = float(start)

    while curr < stop:
        yield curr
        curr += step


def frange(start, stop=None, step=0.25):
    step = decimal.Decimal(str(step))

    if stop is None:
        stop = decimal.Decimal(str(start))
        curr = decimal.Decimal(0)
    else:
        stop = decimal.Decimal(str(stop))
        curr = decimal.Decimal(str(start))

    if step != 0:
        while curr < stop:
            yield float(curr)
            curr += step

print(list(frange(1.1,3)))
print(list(frange(1, 3,0.33)))
print(list(frange(1, 3,1)))
print(list(frange(3, 1)))
print(list(frange(1, 3,0)))
print(list(frange(-1, -5,0.1)))

for num in frange(3.142,12):
    print(f"{num:05.2f}")

print(frange(1,2))
