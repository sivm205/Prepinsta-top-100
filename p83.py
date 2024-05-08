#find the ascii vvalue of a character

def find_ascii(character:chr):
    return ord(character)

if __name__ == "__main__":
    character = input("Enter a character\n")
    print(find_ascii(character))
    