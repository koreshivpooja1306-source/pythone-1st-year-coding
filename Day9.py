# N*N magical square generation
n=int(input("Enter the odd value as a n."))
if ( n % 2!=0):
    square=[[0]*n for _ in range(n)]
    row=0
    col=n//2
    for number in range(1,n*n+1):
        square[row][col]=number
        next_row=(row-1)%n # put row as one cell up
        next_col=(col+1)%n # put col as one cell right
        if square[next_row][next_col]!=0:
            row=(row+1)%n #it move one row downwards also wrap it around edges
        else:
            row=next_row
            col=next_col
    for line in square:
        print(*line)
else:
    print("Enter the odd number.")        