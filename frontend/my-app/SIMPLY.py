def read_binary_file(file_path):
    try:
        # Open the binary file in read mode
        with open(file_path, 'rb') as file:
            # Read the content of the file
            content = file.read()
            
            # Convert binary data to a string
            text = content.decode('utf-8', errors='ignore')  # Use 'ignore' to skip invalid characters
            
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def search_for_flag(text):
    # Search for the term 'FLAG' or 'flag'
    if text:
        if 'FLAG' in text:
            print("Found 'FLAG'!")
        else:
            print("'FLAG' not found.")

        if 'flag' in text:
            print("Found 'flag'!")
        else:
            print("'flag' not found.")
    else:
        print("No text to search in.")

if __name__ == "__main__":
    # Specify the path to your binary file
    file_path = 'D:\projects\CodeFusion\UNKNOWN'  # Change this to your binary file path
    
    # Read the binary file
    text = read_binary_file(file_path)
    
    # Search for the FLAG in the converted text
    search_for_flag(text)
