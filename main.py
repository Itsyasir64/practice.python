def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text

word = input("Enter a string: ")
print("Reversed string:", reverse_string(word))
