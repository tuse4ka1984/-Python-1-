def bank(X, Y):
    total = X
    for _ in range(Y):
        total = total * 1.10
    return total

X = 1000  
Y = 5     
 
result = bank(X, Y)
print(f'{Y} лет: {result}')