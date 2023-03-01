def passerRating(passComp, passAtt, totalPY, touchdowns, interceptions):
    cpa = ((passComp/passAtt)*0.3)/20
    ypa = ((totalPY/passAtt)-3)/4
    tpa = (touchdowns/passAtt)*20
    ipa = 2.375-((interceptions/passAtt)*35)
    return ((cpa+ypa+tpa+ipa)/6)*100


passCompletions, passAttempts, totalPassYards, totalTouchdowns,totalInterceptions = int(eval(
    input('Enter num of pass completions, passAttempts, total pass yards, touchdowns, and total interceptions: ')))

print(passerRating(passCompletions, passAttempts, totalPassYards, totalTouchdowns, totalInterceptions))