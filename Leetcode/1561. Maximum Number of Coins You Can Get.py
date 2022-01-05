def maxCoins(piles):

    myCoins = 0
    piles = sorted(piles)
    
    for i in range(len(piles)//3):
        mine = piles[-2]
        myCoins += mine
        piles.pop()
        piles.pop()
        
    return myCoins
