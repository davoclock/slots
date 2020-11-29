from random import randint

winner=0
wins=0
losses=0
loss_streak=0
max_loss_streak=0
i=0
j=100 #number of spins

#print("\U0001F4AF : 100s") #100
#print("\U0001F48E : gem") #gem
#print("\U0001F31F : spark") #spark
#print("\U0001F340 : clover") #clover
#print("\U0001F381 : gift") #gift

slot_items=["diamond","100","gift","clover","spark"]
slot_icons={"diamond": "\U0001F48E", "100" : "\U0001F4AF", "gift" : "\U0001F381", "clover" :"\U0001F340", "spark" : "\U0001F31F"}

def spin_wheel():
    randNumber = randint(0,4)
    return slot_items[randNumber]

def results(slots):
    winner = 0
    matching = dict()
    for elem in slots:
        if elem in matching:
            matching[elem] += 1
        else:
            matching[elem] = 1    
    matching = { key:value for key, value in matching.items() if value > 1}
    return matching

while i < j:
    winner=0
    match=None
    message=None
    slot_result=[]
    slot_1=spin_wheel()
    slot_2=spin_wheel()
    slot_3=spin_wheel()
    slot_4=spin_wheel()
    slot_5=spin_wheel()
    slot_result = [slot_1,slot_2,slot_3,slot_4,slot_5]
    result=results(slot_result)
    for slot, number in result.items():
        if number > 4:
            if slot == "diamond":
                message="5 x DIAMONDS"
            if slot == "spark":
                message="5 x SPARKS"
            if slot == "100":
                message="5 x 100s"
            if slot == "clover":
                message="5 x CLOVERS"
            if slot == "gift":
                message="5 x GIFTS"
            wins=wins+1
            loss_streak=0
            print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5), " -- ", message)
        elif number > 3:
            if slot == "diamond":
                message="4 x DIAMONDS"
            if slot == "spark":
                message="4 x SPARKS"
            if slot == "100":
                message="4 x 100s"
            if slot == "clover":
                message="4 x CLOVERS"
            if slot == "gift":
                message="4 x GIFTS"
            wins=wins+1
            loss_streak=0
            print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5), " -- ", message)
        elif number > 2:
            if slot == "diamond":
                message="3 x DIAMONDS"
            if slot == "spark":
                message="3 x SPARKS"
            if slot == "100":
                message="3 x 100s"
            if slot == "clover":
                message="3 x CLOVERS"
            if slot == "gift":
                message="3 x GIFTS"
            wins=wins+1
            loss_streak=0
            print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5), " -- ", message)
        else:
            print(slot_icons.get(slot_1),slot_icons.get(slot_2),slot_icons.get(slot_3),slot_icons.get(slot_4),slot_icons.get(slot_5))
            loss_streak = loss_streak + 1
            if loss_streak > max_loss_streak:
                max_loss_streak = loss_streak
    i+=1
print("number of wins: ", wins, " out of ", j , " spins")
print("biggest loss streak: ", max_loss_streak)
