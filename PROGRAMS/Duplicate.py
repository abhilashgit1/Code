elements=[10,20,10,30,10,40,20]
unique=[]
count=0
for i in range(len(elements)):
    for j in range(len(elements)):
        if (elements[i] == elements[j]):
            count=count+1
        if(count>1):
            if elements [i] not in unique:
                unique.append(elements[i])
                count=0
print(unique)
