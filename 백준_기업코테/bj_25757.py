n, g = input().strip().split()

game = {"Y" : 2, "F": 3, "O" : 4}

person = []
for _ in range(int(n)):
    person.append(input().strip())

plist = list(set(person))

min_person = game[g] - 1
print(len(plist) // min_person)