def crack_text_file(text_filename, dictionary_file):
    try:
        with open(text_filename, 'r', encoding="utf-8") as text_file:
            target_password = text_file.read().strip()

        with open(dictionary_file, 'r', encoding="utf-8") as f:
            if target_password in map(str.strip, f):
                print(f"[+] Password Found: {target_password}")
                return target_password
        print("[-] Password Not Found")
    except FileNotFoundError:
        print("[-] File not found.")

# User inputs
crack_text_file(input("Enter text file: ").strip(), input("Enter dictionary file: ").strip())
