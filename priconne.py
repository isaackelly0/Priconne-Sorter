class Princess:
    def __init__(self, name, pic, quest, tower, clan, arena):
        self.name = name
        self.pic = pic
        self.quest = quest
        self.tower = tower
        self.clan = clan
        self.arena = arena
def princessLoop(units): #run a list of units into a list of classes
    princessList = []
    for unit in units:
        princessList.append(Princess(unit[0],unit[1],unit[2],unit[3],unit[4],unit[5]))
    return princessList
def priority(choices, order): #sort from highest priority to lowest based on 'order' param
    prioList = [[],[],[],[],[],[]]
    if order in ["quest", "arena", "tower", "clan"]:
        for choice in choices:
            if order == "quest":
                prioList[choice.quest].append(choice.name)
            elif order == "arena":
                prioList[choice.arena].append(choice.name)
            elif order == "tower":
                prioList[choice.tower].append(choice.name)
            elif order == "clan":
                prioList[choice.clan].append(choice.name)
    return prioList