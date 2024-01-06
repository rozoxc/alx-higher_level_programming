for i in range(6, 29):
    filename = f"{i}-answer.txt"
    with open(filename, "w") as file:
        file.write(f"This is file {filename}")
