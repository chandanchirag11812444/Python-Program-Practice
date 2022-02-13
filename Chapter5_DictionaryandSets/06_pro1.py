#Write a Program to create a dictionary of Hindi words with value as their english translation
#Provide user with an option to look it up!
myDict={
    "BadiSundar":"Beautiful",
    "hero":"actor",
    "bemissal":"outstanding"
}
print("Options are ",myDict.keys())
a=input("Enter the hindi word\n ")
# print("The meaning of your word is ",myDict[a])
# This line will throw an error if following key member is not found .
print("The meaning of your word is ",myDict.get(a))
# this is not throw an error because we are using .get() method


