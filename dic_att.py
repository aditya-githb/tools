def dictionary_attack(password, dictionary_file):
    try:
        with open(dictionary_file, "r", encoding="utf-8") as f:
            for word in f:
                if password == word.strip():
                    print(f"[+] Password Found: {password}")
                    return password
        print("[-] Password Not Found in Dictionary")
    except FileNotFoundError:
        print(f"[-] Error: File '{dictionary_file}' not found.")
    return None

# User inputs
dictionary_file = input("Enter the dictionary file name (e.g., dictionary.txt): ").strip()
password = input("Enter the password to check: ").strip()

# Run the attack
dictionary_attack(password, dictionary_file)
