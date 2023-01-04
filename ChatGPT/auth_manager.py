def load_api_key(filepath):
    # Load API key from file
    with open(filepath, 'r') as f:
        api_key = f.read()
    return api_key

def get_api_key(filepath):
    # Try to load API key from file, if it doesn't exist, ask user to enter it and save it to file
    try:
        api_key = load_api_key(filepath)
    except FileNotFoundError:
        api_key = input("Enter API key: ")
        save_api_key(api_key, filepath)
    return api_key

def save_api_key(api_key, filepath):
    # Save API key to file
    with open(filepath, 'w') as f:
        f.write(api_key)

# CudaText: lexer_file="Python"; tab_size=4; tab_spaces=Yes; newline=LF;
