
# 14/15 is a strong buy
# 13 is a buy
# 12 is on the bubble
# 11 and below is no buy
def calculateNumber(pe, peg, profit, short, analystScore, symbol):
    totalScore = 0
    count = 0
    
    #calculate pe
    if pe is not None:
        if 15 <= pe <= 25:
            totalScore += 3
        elif (10 <= pe < 15) or (25 < pe <= 35):
            totalScore += 2
        else:
            totalScore += 1
        count += 1

           
    #calculate peg
    if peg is not None:
        if peg > 0 and peg <= 1:
            totalScore += 3
        elif peg > 1 and peg <= 3:
            totalScore += 2
        else:
            totalScore += 1
        count += 1
            
    #calculate profit
    if profit is not None:
        if profit >= 25:
            totalScore += 3
        elif profit >= 15 and profit < 25:
            totalScore += 2
        else:
            totalScore += 1
        count += 1
        
    #calculate short
    if short is not None:
        if short < 5:
            totalScore += 3
        elif short >= 5 and short < 15:
            totalScore += 2
        else:
            totalScore += 1
        count += 1
            
    #calculate average analyst score
    if analystScore is not None:
        if analystScore >= 4:
            totalScore += 3
        elif analystScore >= 3:
            totalScore += 2
        else:
            totalScore += 1
        count += 1
        
    # print(symbol, ":", totalScore)
    
    if count == 5:
        if totalScore >= 14:
            return "Strong Buy"
        elif totalScore == 13:
            return "Buy"
        elif totalScore == 12:
            return "Maybe"
        else:
            return "No Buy"
    elif count == 4:
        if totalScore >= 11:
            return "Strong Buy"
        elif totalScore == 10:
            return "Buy"
        elif totalScore == 9:
            return "Maybe"
        else:
            return "No Buy"
    elif count == 3:
        if totalScore == 9:
            return "Strong Buy"
        elif totalScore == 8:
            return "Buy"
        else:
            return "No Buy"
    else:
        return "No Buy"