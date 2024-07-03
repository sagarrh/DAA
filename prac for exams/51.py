def read_file_character_by_character(filename):
    try:

        with open(filename, 'r') as file:
            content=file.read()
            for char in content:
                print(char, end="")
        print("\nFile reading completed.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


filename = input("Enter the filename: ")
read_file_character_by_character(filename)
