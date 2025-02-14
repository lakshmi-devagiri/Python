def digits(a):
    count = 0
    while a > 0:
        a //= 10  
        count += 1  
    return count

n = int(input("Enter n value:"))
print("digit:",digits(n))