import random
import string

CHARACTER_TYPES = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]


def main():
    num_chars = int(input("How many characters would you like to generate? "))
    while num_chars < 12:
        print("\nYou need at least 12 characters in your password.")
        num_chars = int(input("How many characters would you like to generate? "))

    chars_per_group = num_chars // len(CHARACTER_TYPES)
    character_list = []
    for chr_type in CHARACTER_TYPES:
        for _ in range(chars_per_group):
            character_list.append(random.choice(chr_type))
    while len(character_list) < num_chars:
        character_list.append(chr(random.randint(33, 126)))

    random.shuffle(character_list)
    password = ''.join(character_list)

    print(f'\nPassword: {password}')


if __name__ == '__main__':
    main()
