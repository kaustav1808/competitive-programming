# Dynamic Programming minimum coin sum #  
def minCoins(coins,sum):
    sumArr = [sum+100] * (sum+1)
    sumArr[0] = 0

    for i in range(1,sum+1):
        for v in coins:
            if v<=i and (sumArr[i-v]+1 < sumArr[i]):
                sumArr[i] = sumArr[i-v]+1
    return sumArr[sum]

coins = list(map(int,input().split(" ")))
sum   = int(input())

print(minCoins(coins,sum))
