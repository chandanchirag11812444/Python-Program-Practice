# myDict = {
#     "Potential": "Power",
#     "Chandan": "A coder",
#     "marks": "[5,10,20,15]",
#     # we can even create nested dictionary
#     "onotherDic": {'chandan': 'Player'}
# }
# print(myDict['Pot,ential'])
# print(myDict['Chandan'])
# print(myDict['marks'])
# print(myDict['onotherDic'])
# print(myDict['onotherDic']['chandan'])  # like this we can do

# myDictionary = {
#     "Apple": "Seyb Sir",
#     "Banana": "kela Sir",
# }
# print(myDictionary['Apple'])
# print(myDictionary['Banana'])
# # dictionary methods
# # printthe keys of tkeys will give the first left side value
# print(list(myDict.keys()))#WILL GIVE THE LEFT SIDE VALUES  
# print(list(myDict.values()))#WILL GIVE RIGHT SIDE VALUES 

# print(list(myDict.items()))
# # print the key ,values of all contents ofthe dictionary

Mydic={
    "chandan":"coder",
    "Rajesh":"hardworker",
    "apple":"sayb",
    "listoff":"[1,5,4,7,7,5,5]",
    "powerful":{'manisha':'darpokni'}
}
print(Mydic['chandan'])
print(Mydic['Rajesh'])
print(Mydic['apple'])
print(Mydic['listoff'])
print(Mydic['powerful']['manisha'])

#dictionary methods
print(list(Mydic.keys()))
print(list(Mydic.values()))
print(list(Mydic.items()))
