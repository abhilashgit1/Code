'''


a=[1,2,3,4,5,1,2,'abhi','nini']
print(a)
print(type(a))
print(a[3])
print(a[-1])
print(a[0:4:2])

a.append("advik")
print(a)

a.extend([8,9,'trisha'])
print(a)

print(a.count(1))

a.remove(4)
print(a)

a.pop(5)
print(a)

a.index("abhi")
print(a)

for i in [1,2,3,4,'abhi']:
    print(i)



'''