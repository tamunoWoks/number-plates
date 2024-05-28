def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(text):
    # check if plate is within 2-6 characters
    if len(text) >= 2 and len(text) <= 6:
        # make sure it can accept only alphabets
        if text.isalpha():
            return True
        # check if first two characters are alphabets and if input is alphanumeric
        elif text.isalnum() and text[0:2].isalpha():
            for char in text:
                # check for first digit
                if char.isdigit():
                    # assign first digit to a variable
                    pos = text.index(char)
                    # use variable to ensure that no digit between alphabets and first digit is not a string
                    if text[pos:].isdigit() and char != "0":
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
