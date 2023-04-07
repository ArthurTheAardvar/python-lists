prices = [3.45, 2.72, 9.10, 8.47]

for i in range(len(prices)):
    prices[i] *= 2

print(prices)


print("enter score, -1 to quit")
num = 0
scoreList = []
while num != -1:
    num = int(input("enter score"))
    if num != -1:
        scoreList.append(num)
print("Heres your score")
scoreList.sort()
print(scoreList)
