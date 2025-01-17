from stegano import lsb
import os
import random
import re

def get_file_input():
    while True:
        filename = input("Enter the path of the image file (png, jpg, jpeg, bmp, gif, etc.): ")
        if os.path.isfile(filename) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            return filename
        else:
            print("Please enter a valid image file path with extension (.png, .jpg, .jpeg, .bmp, .gif).")

def get_message_input():
    message = input("Enter the message you want to embed in the image: ")
    return message

def get_password_input():
    password = input("Enter a password (or press Enter to skip): ")
    if not password:
        password = "no_password_given"
    return password

def get_action_input():
    while True:
        action = input("Would you like to [e]mbed a message or [x]tract a message? (e/x): ").lower()
        if action in ['e', 'x']:
            return action
        else:
            print("Invalid input. Please choose either 'e' to embed or 'x' to extract.")

def embed_message():
    image_path = get_file_input()
    message = get_message_input()
    password = get_password_input()

    embed = password + " " + message

    secret = lsb.hide(image_path, embed)

    random_filename = "secret" + str(random.randint(0, 100)) + os.path.splitext(image_path)[1]
    secret.save(random_filename)
    print(f"File saved as {random_filename}")

def extract_message():
    image_path = get_file_input()
    password = get_password_input()

    message = lsb.reveal(image_path)

    if message and re.search(r'\b' + re.escape(password) + r'\b', message):
        message = message.replace(password, "")
        print(f"The secret message is: {message}")
    else:
        print("[-] Could not reveal the message with the provided password.")

def main():
    while True:
        action = get_action_input()
        
        if action == 'e':
            embed_message()
        elif action == 'x':
            extract_message()

        # continue_action = input("\nDo you want to perform another action? (y/n): ").lower()
        # if continue_action != 'y':
        #     print("Exiting program.")
        #     break

if __name__ == "__main__":
    main()
