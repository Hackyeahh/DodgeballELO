import csv
from itertools import combinations
import random

K = 32

names = [
	"Austin",
	"Nathan",
	"Won",
	"Hyeongu",
	"Annie",
	"Chaewoo",
	"Henry",
	"Caleb",
	"Katelyn",
	"Mary",
	"Joyce",
	"Joel",
	"Gilles",
	"Anna",
	"Jennifer",
	"Lorraine",
	"Tomas",
	"Hugo",
	"Tina",
	"Abby",
	"Patrick",
	"Steven",
	"Brian",
	"Jeremiah",
	"Josh",
]

class Person:
	def __init__(self, name, elo=1000, matches=0):
		self.name = name
		self.elo = elo
		self.matches = matches

	def win(self, loser):
		self.matches += 1

		expected_performance = 1 / (1 + 10 ** ((loser.elo - self.elo) / 400))
		elo_gain = K*(1-expected_performance)
		self.elo += elo_gain

		loser.lose(elo_gain)

	def tie(self, opponent):
		self.matches += 1

		expected_performance = 1 / (1 + 10 ** ((opponent.elo - self.elo) / 400))
		elo_gain = K * (0.5 - expected_performance)
		self.elo += elo_gain

		opponent.lose(elo_gain)

	def lose(self, elo_change):
		self.matches += 1

		self.elo -= elo_change

	def __repr__(self):
		return self.name



def Rank(alice: Person, bob: Person):
	choice = -1
	while True:
		try:
			choice = int(input( f"{alice}(1) vs. {bob}(2) or tied?(3)"))
		except:
			pass

		if choice == 1:
			alice.win(bob)
			break
		elif choice == 2:
			bob.win(alice)
			break
		elif choice == 3:
			alice.tie(bob)
			break
		else:
			print("retry typing")


def saveElo():
	global headers

	with open('data.csv', 'w', newline='') as data:
		writer = csv.DictWriter(data, fieldnames=headers)
		writer.writeheader()

		for person in people:
			writer.writerow({'name': person.name, 'elo': person.elo})


people = []
for name in names:
	# load csv, if player not in csv
	people.append(Person(name))


headers = ['name', 'elo']
saveElo()


cases = list(combinations(people, 2))
random.shuffle(cases)
for i,(a,b) in enumerate(cases):
	Rank(a,b)

	saveElo()

	if i % 20 == 0:
		print(f"{i} out of {len(cases)}")


for person in people:
	print(person, person.elo)

