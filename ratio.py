number = int(input('Enter a number: '))

thousand = number // 1000
hundred = (number // 100) % 10
ten = (number // 10) % 10
position = number % 10

sum1 = thousand + position
sum2 = hundred - ten

if sum1 == sum2:
    print("YES")
else:
    print("NO")