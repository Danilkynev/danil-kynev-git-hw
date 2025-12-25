characters = [
    "Luke Skywalker",
    "Leia Organa",
    "Darth Vader",
    "Yoda",
    "Obi-Wan Kenobi"
]

with open("result.txt", "w") as f:
    f.write("Star Wars characters:\n")
    for c in characters:
        f.write(f"- {c}\n")

    f.write(f"\nTotal characters: {len(characters)}\n")
