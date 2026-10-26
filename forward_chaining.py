# Forward Chaining

facts = ["raining"]

rules = [
    ("raining", "road is wet"),
    ("road is wet", "driving is slow")
]

print("Forward Chaining")

for condition, conclusion in rules:
    if condition in facts:
        facts.append(conclusion)
        print(condition, "->", conclusion)

print("Final Facts:")
for fact in facts:
    print(fact)