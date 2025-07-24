print("*** Reading E-Book ***")
print("Text , Highlight : ",end="")
word,key = input().split(",")
i_point = []
count = 0
word = list(word)
for i in range(len(word)):
    if word[i]==key[0]:
        for j in range(len(key)):
            if (word[i]==key[j]):
                i+=1
                count+=1
            else:
                i=i-count
                count = 0
                break
            if count == len(key):
                i_point.append((i-len(key), i))
                count = 0
n=0
for i,j in i_point:
    word.insert(i+n,'[')
    word.insert(j+(n+1),']')
    n+=2
answer=''.join(word)
print(answer)