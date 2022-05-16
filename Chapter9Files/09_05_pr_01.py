#write a prpgram to read the text from  a given file 'poem.txt' and find out whether the words contains twinkle or not?

f=open('poems.txt')
t=f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()
