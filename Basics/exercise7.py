phonebook = {
        "John" : 938477566,
        "Jack" : 938377624,
        "Jill" : 947662781
}

phonebook["Jack"] = 938273443
phonebook.pop("Jill")

if "Jack" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
