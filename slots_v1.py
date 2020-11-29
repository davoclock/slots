from random import randint

winner=0
wins=0
losses=0
loss_streak=0
max_loss_streak=0
i=0
j=10000000 #number of spins

#print("\U0001F4AF :x 100s") #100
#print("\U0001F48E : gem") #gem
#print("\U0001F31F : spark") #spark
#print("\U0001F340 : clover") #clover
#print("\U0001F381 : gift") #gift

slot_items=["diamond","100","gift","clover","spark"]
slot_icons={"diamond": "\U0001F48E", "100" : "\U0001F4AF", "gift" : "\U0001F381", "clover" :"\U0001F340", "spark" : "\U0001F31F"}

def spin_wheel():
    randNumber = randint(0,4)
    return slot_items[randNumber]

def results():
    winner = 0
    if (slot_1 == slot_2 and slot_1 == slot_3 and slot_1 == slot_4 and slot_1 == slot_5):
        #5 slot winner
        if slot_1 == "diamond":
            match="5 x DIAMONDS"
            winner=1
            return winner, match
        elif slot_1 == "clover":
            match="5 x CLOVERS"
            winner=1
            return winner, match
        elif slot_1 == "spark":
            match="5 x SPARKS"
            winner=1
            return winner, match
        elif slot_1 == "100":
            match="5x 100s"
            winner=1
            return winner, match
        elif slot_1 == "gift":
            match="5 x GIFTS"
            winner=1
            return winner, match
    if (slot_1 == slot_2 and slot_1 == slot_3 and slot_1 == slot_4) or (slot_1 == slot_2 and slot_1 == slot_3 and slot_1 == slot_5) or (slot_1 == slot_3 and slot_1 == slot_4 and slot_1 == slot_5):
        #4 slot winner
        if slot_1 == "diamond":
            match="4 x DIAMONDS"
            winner=1
            return winner, match
        elif slot_1 == "clover":
            match="4 x CLOVERS"
            winner=1
            return winner, match
        elif slot_1 == "spark":
            match="4 x SPARKS"
            winner=1
            return winner, match
        elif slot_1 == "100":
            match="4 x 100s"
            winner=1
            return winner, match
        elif slot_1 == "gift":
            match="4 x GIFTS"
            winner=1
            return winner, match
    if (slot_2 == slot_3 and slot_2 == slot_4 and slot_2 == slot_5):
            #4 slot winner
        if slot_2 == "diamond":
            match="4 x DIAMONDS"
            winner=1
            return winner, match
        elif slot_2 == "clover":
            match="4 x CLOVERS"
            winner=1
            return winner, match
        elif slot_2 == "spark":
            match="4 x SPARKS"
            winner=1
            return winner, match
        elif slot_2 == "100":
            match="4 x 100s"
            winner=1
            return winner, match
        elif slot_2 == "gift":
            match="4 x GIFTS"
            winner=1
            return winner, match
    if (slot_1 == slot_2 and slot_1 == slot_3) or (slot_1 == slot_2 and slot_1 == slot_4) or (slot_1 == slot_2 and slot_1 == slot_5) or (slot_1 == slot_3 and slot_1 == slot_4) or (slot_1 == slot_3 and slot_1 == slot_5) or (slot_1 == slot_4 and slot_1 == slot_5):
        #3 slot winner
        if slot_1 == "diamond":
            match="3 x DIAMONDS"
            winner=1
            return winner, match
        if slot_1 == "clover":
            match="3 x CLOVERS"
            winner=1
            return winner, match
        if slot_1 == "spark":
            match="3 x SPARKS"
            winner=1
            return winner, match
        if slot_1 == "100":
            match="3 x 100s"
            winner=1
            return winner, match
        if slot_1 == "gift":
            match="3 x GIFTS"
            winner=1
            return winner, match
    if (slot_2 == slot_3 and slot_2 == slot_4) or (slot_2 == slot_3 and slot_2 == slot_5) or (slot_2 == slot_4 and slot_2 == slot_5):
        #3 slot winner
        if slot_2 == "diamond":
            match="3 x DIAMONDS"
            winner=1
            return winner, match
        if slot_2 == "clover":
            match="3 x CLOVERS"
            winner=1
            return winner, match
        if slot_2 == "spark":
            match="3 x SPARKS"
            winner=1
            return winner, match
        if slot_2 == "100":
            match="3 x 100s"
            winner=1
            return winner, match
        if slot_2 == "gift":
            match="3 x GIFTS"
            winner=1
            return winner, match
    if (slot_3 == slot_4 and slot_3 == slot_5):
        #3 slot winner
        if slot_3 == "diamond":
            match="3 x DIAMONDS"
            winner=1
            return winner, match
        if slot_3 == "clover":
            match="3 x CLOVERS"
            winner=1
            return winner, match
        if slot_3 == "spark":
            match="3 x SPARKS"
            winner=1
            return winner, match
        if slot_3 == "100":
            match="3 x 100s"
            winner=1
            return winner, match
        if slot_3 == "gift":
            match="3 x GIFTS"
            winner=1
            return winner, match
    return 0, "no matches"

while i < j:
    winner=0
    match=None
    slot_1=spin_wheel()
    slot_2=spin_wheel()
    slot_3=spin_wheel()
    slot_4=spin_wheel()
    slot_5=spin_wheel()
    result=results()
    winner=result[0]
    match=result[1]
    if winner == 1:
        #print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5), " -- ", match)
        wins=wins+1
        loss_streak=0
    else:
        #print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5))
        loss_streak = loss_streak + 1
        if loss_streak > max_loss_streak:
            max_loss_streak = loss_streak
    i+=1
print("number of wins: ", wins, " out of ", j , " spins")
print("biggest loss streak: ", max_loss_streak)
