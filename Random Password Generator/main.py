import random
import string
import argparse
import pyperclip

def generate_password(length, exclude_ambiguous):
    characters = string.ascii_letters + string.digits + string.punctuation
    if exclude_ambiguous:
        # Exclude ambiguous characters ('1', 'l', '0', 'o', etc.)
        characters = ''.join([char for char in characters if char not in 'l1o0'])
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('--length', type=int, default=12, help='Length of the password (default: 12)')
    parser.add_argument('--exclude-ambiguous', action='store_true', help='Exclude ambiguous characters')
    args = parser.parse_args()

    password = generate_password(args.length, args.exclude_ambiguous)
    print('Generated Password:', repr(password))

    try:
        pyperclip.copy(password)
        print('Password copied to clipboard.')
    except pyperclip.PyperclipException:
        print('Warning: Clipboard functionality not available.')

if __name__ == '__main__':
    main()
