def sqrt(x):
    x0 = x / 2
    x2 = 0
    
    while True:
        x1 = (x0 + x / x0) / 2
        x0 = (x1 + x / x1) / 2

        if x0 == x2:
            return x0
        x2 = x0
        
print(sqrt(250))