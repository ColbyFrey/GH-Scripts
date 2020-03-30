dayBadge = open('/home/colby/Downloads/Badge/Badge 4th.txt','r')
badgeNames = open('/home/colby/Downloads/Badge/loginNames/SwipeIns','w+')


for line in dayBadge:
	if 'Swipe In' in line:
		badgeNames.write(line)