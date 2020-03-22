text = 'NDA_9999992'
game = 0

for c in text:
	game += ord(c)
game = game << 2
game = ~game
game = game ^ 12648430
game = ~game


print('Game:' + str(game))
if game == 12645638:
	print('game = 12645638')
else:
	print('Game - 12645638 = ' + str(game-12645638))
print('text length:' + str(len(text)))