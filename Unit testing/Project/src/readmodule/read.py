
def read_count(filename, character):
    """
    Read a txt file and count letter
    """
    # Open file
    with open(filename, "r") as file:
        text = file.read()
    # Count the number occurrences of a character
    number = text.count(character)
    # Store the output in a file
    with open(f"character {character}.txt", 'w') as f:
        f.write(f"{number}")