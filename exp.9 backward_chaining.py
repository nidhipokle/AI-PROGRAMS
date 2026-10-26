# Backward Chaining

facts = ["raining"]

rules = [
    ("raining", "road is wet"),
    ("road is wet", "driving is slow")
]

goal = "driving is slow"

print("Backward Chaining")
print("Goal:", goal)

for condition, conclusion in reversed(rules):
    if conclusion == goal:
        print("To prove", goal, "we need:", condition)

        if condition == "road is wet":
            for condition2, conclusion2 in rules:
                if conclusion2 == condition:
                    print("To prove", condition, "we need:", condition2)

                    if condition2 in facts:
                        print("Fact found:", condition2)
                        print("Goal is proved.")