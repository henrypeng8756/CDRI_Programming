# TODOcardSum = 0for cards in range(5):    cardNum = input()    if cardNum == 'A':        cardSum += 1    elif cardNum == 'J':        cardSum += 11    elif cardNum == 'Q':        cardSum += 12    elif cardNum == 'K':        cardSum += 13    else:        cardSum += int(cardNum)print(cardSum)