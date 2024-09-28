col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if col1 <= 8 and col2 <= 8 and row1 <= 8 and row2 <= 8 and col1 == col2 or row1 == row2:
    print("YES")
else:
    print("NO")