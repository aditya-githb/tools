import pyzipper

def crack_zip(zip_filename, dictionary_file):
    try:
        with pyzipper.AESZipFile(zip_filename) as zip_file, open(dictionary_file, "r", encoding="utf-8") as f:
            for password in f:
                try:
                    zip_file.extractall(pwd=password.strip().encode("utf-8"))
                    print(f"[+] Password Found: {password.strip()}")
                    return password.strip()
                except (RuntimeError, pyzipper.BadZipFile):
                    continue
        print("[-] Password Not Found")
    except FileNotFoundError:
        print("[-] File not found.")

# User inputs
crack_zip(input("Enter ZIP file: ").strip(), input("Enter dictionary file: ").strip())