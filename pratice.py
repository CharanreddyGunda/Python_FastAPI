def fabi(num):
    a = 0 
    b = 1
    c = 0
    for i in range(2,num+1):
        c = a+b
        a = b
        b = c
    return c

print(fabi(6))

# 0 1 1 2 3 5