import itertools

def generate_dictionary(words, numbers, special_chars, output_file):
    with open(output_file, "w") as f:
        for word in words:
            f.write(word + "\n")  # Add base word
            for num in numbers:
                f.write(word + num + "\n")  # Append number
            for char in special_chars:
                f.write(word + char + "\n")  # Append special character
            for num, char in itertools.product(numbers, special_chars):
                f.write(word + num + char + "\n")  # Append both

    print(f"Dictionary saved to {output_file}")

# Example Usage
words = ["password", "admin", "letmein", "welcome"]
numbers = ["123", "2024", "007"]
special_chars = ["!", "@", "#"]

generate_dictionary(words, numbers, special_chars, "dictionary.txt")