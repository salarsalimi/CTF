phoneSteak = [55, 33, 52, 40, 35, 56, 86, 90, 66, 111, 81, 26, 23, 75, 109, 26, 88, 90, 75, 67, 92, 25, 87, 88, 92, 84, 23, 88]

libraryDiscussion = input("Enter the flag: ")
confusedSheep = [ord(herdSlot) for herdSlot in libraryDiscussion]
mintFarm = len(confusedSheep)
trustBreed = len(phoneSteak)

seaTent = 6
callCover = 17
foxEmbox = (248 // trustBreed) % trustBreed ## 8
outfitStrike = 10
brushCopy = (341 // trustBreed) % 17 ## 12
injectPush = (1240 + 28 // trustBreed) % trustBreed  ## 17

makeupRoof = []
tinRoyalty = []
if trustBreed == mintFarm:
    print("1")
    for heartCool in confusedSheep:
        makeupRoof.append(heartCool - 27) ## + 27
    for angelStay in makeupRoof:
        tinRoyalty.append(angelStay ^ 15) ## ^ 15
    
    franchisePath = tinRoyalty[seaTent]  ## 6
    tinRoyalty[seaTent] = tinRoyalty[injectPush] ## 17 - >  6
    tinRoyalty[injectPush] = franchisePath ## 6 -> 17
    eastGhostwriter  = tinRoyalty[outfitStrike]  ## 10

    tinRoyalty[outfitStrike] = tinRoyalty[foxEmbox] ## 8 -> 10
    tinRoyalty[foxEmbox] = eastGhostwriter ## 10 -> 8
    personPioneer = tinRoyalty[callCover] ## 17
    
    tinRoyalty[callCover] = tinRoyalty[brushCopy] ## 12 -> 17
    tinRoyalty[brushCopy] = personPioneer ## 17 -> 12 

    lineMoon = tinRoyalty[0 : len(tinRoyalty) // 2]
    puddingCommission = tinRoyalty[len(tinRoyalty) // 2 : len(tinRoyalty)]
    furRegret = lineMoon + puddingCommission[::-1]
    tinRoyalty = furRegret

    if tinRoyalty == phoneSteak:
        print("Correct!! :)")
    else:
        print("Incorrect flag :(")

else:
    print("Incorrect :(")
