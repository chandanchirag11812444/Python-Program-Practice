#A file contains a word donkey multiple times .You need to write a program which replaces this word with ################## by updating the same file.
words=["donkey","kaddu","mote"]
print(words)

with open("sample.txt","r") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#$@##")
    with open("sample.txt","w") as f:
        f.write(content)
print(content)
