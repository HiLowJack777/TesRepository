def load_names(filename):
    with open(filename, 'r') as file:
        # Strip whitespace and create a set, print for debugging
        names = {name.strip() for name in file.readlines()}
        print("Loaded names:", sorted(names))  # Debug print
        return names

def check_name(name, names_set):
    # Convert input to title case to match format in file
    formatted_name = name.strip().title()
    print(f"Checking for: '{formatted_name}'")  # Debug print
    return "Yes" if formatted_name in names_set else "No"

def main():
    try:
        names = load_names('Names.txt')
        
        while True:
            user_input = input("Enter a name to check (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                break
                
            result = check_name(user_input, names)
            print(f"Is {user_input.title()} in the list? {result}")
            
    except FileNotFoundError:
        print("Error: Names.txt file not found!")

if __name__ == "__main__":
    main() 