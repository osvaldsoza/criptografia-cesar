import sys
import hashlib

ALPHABET = 'abcdefghijklmnopqrstuvwxz'
NUMBER_DECIMAL_PLACES = 12


def encrypt_decrypt(message, operator):
    new_message = ''
    for character in message:
        if character in ALPHABET:
            character_index = ALPHABET.index(character)
            new_message += ALPHABET[(character_index + (operator * NUMBER_DECIMAL_PLACES)) % len(ALPHABET)]
        else:
            new_message += character
    return new_message


def encrypt(message):
    return encrypt_decrypt(message, 1)


def decrypt(message):
    return encrypt_decrypt(message, -1)


def get_hashcode(message):
    return hashlib.sha1(message.encode(encoding='utf-8', errors="strict")).hexdigest()


def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
        print(encrypt(message))
    elif command == 'decrypt':
        print(decrypt(message))
        print(get_hashcode(message))
    else:
        print(command + '-> command not found')


if __name__ == '__main__':
    main()
