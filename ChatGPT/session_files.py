
def load_edit_text(filepath):
    with open(filepath, 'r') as f:
        edit_text = f.read()
    return edit_text

def read_edit_text(filepath):
    # Try to load edit from file if it exists
    edit_text = ""
    if filepath:
        print(filepath)
        try:
            edit_text = load_edit_text(filepath)
        except FileNotFoundError:
            pass
    print(edit_text)
    return edit_text

def write_edit_text(filepath, text):
    if filepath:
        with open(filepath, 'w') as f:
            f.write(text)
