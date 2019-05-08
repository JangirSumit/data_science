import base64

def_key = "12345678"

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def check_alpha(ref_id):
    contains_upper = False
    for string in ref_id:
        if string.isalpha():
            contains_upper = True
            break
    return contains_upper


def check_digit(ref_id):
    contains_digit = False
    for string in ref_id:
        if string.isnumeric():
            contains_digit = True
            break
    return contains_digit


def check_special_characters(ref_id):
    contains_special_chars = False
    special_chars = "$#@"
    for string in ref_id:
        if string in special_chars:
            contains_special_chars = True
            break
    return contains_special_chars


def validate_length(ref_id):
    length = len(ref_id)
    return length == 12


def validate_reference_id(ref_id):
    return (check_alpha(ref_id) and check_digit(ref_id)  and validate_length(ref_id)) or check_special_characters(ref_id)

while True:

        print("\n")
        print("select any of below option")
        print("1. Get Encrypted reference id")
        print("2. Decrypt the existing reference id")
        print("3. Exit")

        user_input = input(">>> ")

        if user_input == "1":
            print("Please enter 12 digit reference id which should only contains numbers, alphabetes or [$#@] special characters")
            ref_number = input(">>> ")  

            if not validate_reference_id(ref_number):
                print("Refernce ID is not valid.\n")
                continue

            print(encode(def_key, ref_number))
            continue
        elif user_input == "2":
            print("Enter existing reference id")
            decode_ref = input(">>> ")

            print("Reference id after decoding : " + decode(def_key,decode_ref))
            continue
        elif user_input == "3":
            break
        else:
            print("You selected wrong option.")
            continue