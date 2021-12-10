import random, time
maxH = int(input("Maximum bar size? (I'd advice between 10 & 30)"))
randomList = [i for i in range(1,maxH+1)]
random.shuffle(randomList)
itter_count = 0
check_count = 0
change_count = 0
notSorted = True
def render(listToRender):
    frames = [
        ['# ' if v > maxH-y else '  ' for v in listToRender] for y in range(0, maxH+1)
    ]
    fullframe = ""
    fullframe+=("\n"*20)
    fullframe+='\n'+(f"+{'-'*(((len(listToRender)+2)*2)-1)}+")
    for frame in frames:
        renderedLayer = ''
        for item in frame:
            renderedLayer+=item
        fullframe+='\n'+(f"|  {renderedLayer} |")
    fullframe+='\n'+(f"+{'-'*(((len(listToRender)+2)*2)-1)}+")
    print(fullframe)
    time.sleep(0.1)

while notSorted:
    itter_count +=1
    for index, number in enumerate(list(randomList)):
        check_count +=1
        if index == len(randomList)-1:
            pass
        else:
            if randomList[index] > randomList[index+1]:
                change_count += 1
                higherValue = int(randomList[index])
                lowerValue = int(randomList[index+1])
                randomList[index+1] = higherValue
                randomList[index] = lowerValue
    lastNumber = 0
    notSorted = False
    for number in randomList:
        if number < lastNumber:
            notSorted = True
        lastNumber = number
    render(randomList)
print(f"{itter_count=}, {check_count=}, {change_count=}")