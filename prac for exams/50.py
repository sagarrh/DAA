def read_file_word_by_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            for word in words:
                print(word)
        print("File reading completed.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
        
filename = input("Enter the filename: ")
read_file_word_by_word(filename)
