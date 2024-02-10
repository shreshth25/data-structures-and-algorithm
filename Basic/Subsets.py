s = [1,2,3]
e = [[]]
for i in s:
    e+=[n+[i] for n in e]

print("Subsets are: ", e)