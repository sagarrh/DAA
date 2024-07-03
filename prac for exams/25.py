def display_elements_with_numbers(string):
    if len(string) > 15:
        return "String length exceeds 15 characters"
    
    for index, char in enumerate(string, 1):
        print(f"Element {index}: {char}")

# Accept input string
input_string = input("Enter a string up to 15 characters: ")

# Display elements with their element numbers
display_elements_with_numbers(input_string)
