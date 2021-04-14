#3-4

nation = ['Roman', 'Egypt', 'Greek', 'Chinese', 'Islamic', 'Mayan', 'Persian', 'Mongol']
golden_age = ['27BC-1453AD', '3150BC-30BC', '800BC-600AD', '221BC-1912AD', '750AD-1257AD', '2000BC-1540AD', '550BC-651AD','1206AD-1368AD']

zipped = zip(nation, golden_age)

print(list(zipped))

_dict = dict(zipped)
print(_dict)

# _dict.get('Roman')
# _dict['Roman']