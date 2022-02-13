


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
updateDic={
    "Lovish":"very Cool Boy",
    "shubham":"friend",
    "divya":"friend",
     "chandan":"he is coder"
     
}
Mydic.update(updateDic)#Updates the dictionary with key value pairs from update keys
print(Mydic)
print(Mydic.get("harry2"))#if if the key is not present this is not throw an error instead it will throw and non value where [] will throw an error if it is not present in dictionary key
print(Mydic["harry2"]) 