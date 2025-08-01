import os

def generatetables(n):
    table = ""
    for i in range(1, 11):
        table += f"{i} X {n} = {i * n}\n"
    # Ensure the 'tables' directory exists
    os.makedirs("tables", exist_ok=True)
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generatetables(i)