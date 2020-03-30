badgeNames = open('/home/colby/Downloads/Badge/loginNames/badgeNames.txt','r')
names = open('/home/colby/Downloads/Access Log/names.txt','r')
swipeIn = open('/home/colby/Downloads/Badge/loginNames/SwipeIns','w+')

listA = []
listb = []
nope = []
yes = []

for line in names:
	listA.append(line.strip())
for line in badgeNames:
	listb.append(line.strip())

for line in listA:
	if line not in listb:
		yes.append(line)

print(yes)



