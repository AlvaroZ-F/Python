def square(s):
    area = s*s
    perimeter = s*4
    return [area, perimeter]

n = int(input("Introduce the size of the square's side"))

while n > 0:
    print(square(n))
    --n
