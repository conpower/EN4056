# Bloom's Taxonomy Interactive Ranking Shell

# Example learning outcomes
learning_outcomes = {
    "1.1": "describe a systematic process for solving problems and making decisions",
    "1.2": "explain how the power of computing enables different solutions to difficult problems",
    "1.3": "solve problems by breaking them into smaller steps using a systematic approach",
    "2.7": "write programs to solve problems using a programming language",
    "3.8": "create a model to test different scenarios"
}

# Bloom's levels dictionary
bloom_levels = {
    1: "Remember",
    2: "Understand",
    3: "Apply",
    4: "Analyse",
    5: "Evaluate",
    6: "Create"
}

# Dictionary to store student rankings
ranked_outcomes = {}

print("Welcome! Let's rank these learning outcomes by Bloom's Taxonomy levels.\n")

print("Bloom's Levels (with examples):")
print("1 - Remember (list, recall)")
print("2 - Understand (explain, describe)")
print("3 - Apply (use, implement)")
print("4 - Analyse (compare, break down)")
print("5 - Evaluate (judge, critique)")
print("6 - Create (design, develop)")

print("\nFor each learning outcome, type a number (1-6) that matches its Bloom's level.\n")

# Interactive loop for ranking


# Show results
print("\nYour Bloom's rankings:")
for code, level in ranked_outcomes.items():
    print(f"{code}: {learning_outcomes[code]} --> {bloom_levels[level]}")
