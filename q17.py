total_amount=0
n=int(input())
for i in range(0,n) :
    transaction_log=input()
    amount=int(input())
    if(transaction_log==("d" or"D")):
        total_amount += amount
    if(transaction_log==("w"or "W")):
        total_amount -= amount
print(total_amount)

