from collections import Counter
Number_shoes=int(input())

shoe_size=(input().split())
customer_number=int(input())
shoe_size_price=[]
for _ in range(customer_number):
    ssp=(input().split())
    shoe_size_price.append(ssp)
    
total=0

for shoe in shoe_size_price:
        available=0
        available=shoe_size.count(shoe[0])
        if available != 0:
                total+=int(shoe[1])
                shoe_size.remove(shoe[0])
                
        else:
            pass
print(total)       