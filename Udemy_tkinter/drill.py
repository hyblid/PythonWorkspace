from pythonds.basic import Stack

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      print(f"coin:{coin}")
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

coin_list = [1,5,10,25]
used_coin = dict.fromkeys(coin_list, 0)

def rec_change(change, coin):
    if len(coin_list) > 0:
       coin = coin_list[-1]
    else: 
        return
 
    if change // coin >=1:
        change -= coin
        used_coin[coin] += 1
    else: coin_list.pop()
    return str(rec_change(change, coin))
        
rec_change(63, coin_list)
print(used_coin)
    
