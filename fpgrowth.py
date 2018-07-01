items=[['E','A','D','B'],['D','A','C','E','B'],['C','A','B','E'],['B','A','D'],['D'],['D','B'],['A','D','E'],['B','C']]
s=[]
for i in items:
    for j in i:
        s.append(j)
counts = {}
for i in s:
    if i in counts:
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1
result = sorted(counts.items(), key=lambda t: (-t[1],t[0]))
new_dict = {}
for k, v in result:
    new_dict[k] = v
print(new_dict)
oitems=[]

for j in items:
    ci = []
    for i in new_dict:
        for k in j:
          if i==k:
              ci.append(i)
    oitems.append(ci)
print(oitems)

nl=[]
fitems=[]
for p in new_dict:
    nl.append(p)
    #fitems.append(p)

for j in oitems:
    fi = []
    z=0
    i=0
    for k in j:
        if nl[i]==k and z==0:
            fitems.append(k)
            i = i + 1
        else:
            z=1
            for q in fitems:
                if isinstance(q,list) and len(q)==1 and q[0]==k:
                    fitems.remove(q)
                    fi.append(k)
            fi.append(k)
            i = i + 1
    if fi:
       fitems.append(fi)
#print(fitems)

temp=[]
tv=[]
for p in fitems:
    if isinstance(p,list):
        temp.append(p)
    else:
        tv.append(p)
#print(temp)
#print(tv)

scounts = {}
for i in tv:
    if i in scounts:
        scounts[i] = scounts[i] + 1
    else:
        scounts[i] = 1
sresult = sorted(scounts.items(), key=lambda t: (-t[1],t[0]))
print(scounts)
for item in temp:
    wcounts = {}
    for i in item:
        if i in wcounts:
            wcounts[i] = wcounts[i] + 1
        else:
            wcounts[i] = 1
    sresult = sorted(wcounts.items(), key=lambda t: (-t[1], t[0]))
    print(wcounts)