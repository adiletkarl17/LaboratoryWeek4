col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

sum1 = col1-col2
sum2 = row1-row2

if sum1 <= 1 and sum2 <= 1:
    print("YES")
else:
    print("NO")