def square(s):
    area = s*s
    perimeter = s*4
    return "Square's Area is: "+str(area)+" and its perimeter is: "+str(perimeter)

n = int(input("Introduce the size of the square's side"))

for i in range(1,n+1):
    print(square(i))
