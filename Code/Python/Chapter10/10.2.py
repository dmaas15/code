name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lst=list()
time=list()
hlst=list()
hours=dict()
handle = open(name)
for line in handle:
    lst=line.split()
    if len(lst) > 1 and lst[0]=="From":
        time.append(lst[5].split(':'))

for h,m,s in time:
    hours[h]=hours.get(h,0)+1

for k,v in hours.items():
    hlst.append(k)
hlst.sort()

for h in hlst:
    print(h, hours[h])
