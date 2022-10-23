price = int(input())

high, low = price, price
    
while True:
    high += 1
    low -= 1
    
    if str(high)[-2:] == "99":
        price = high; break
    if str(low)[-2:] == "99":
        price = low; break

print(price)

