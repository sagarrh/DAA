class Reverse:
    def reversedword(self, input_string):
        words = input_string.split()
        reversed_words = words[::-1]  # Reverse the order of words
        reversed_string = ' '.join(reversed_words)
        return reversed_string

# Create an object of the Reverse class
revse = Reverse()

# Input string
input_string = "hello my name is sagar"

# Call the reversedword() method to reverse the input string word by word
reversed_string = revse.reversedword(input_string)

# Print the reversed string
print(reversed_string)
