
def load_edit_text(filepath):
    with open(filepath, 'r') as f:
        edit_text = f.read()
    return edit_text

def read_edit_text(filepath):
    # Try to load edit from file if it exists
    edit_text = ""
    if filepath:
        try:
            edit_text = load_edit_text(filepath)
        except FileNotFoundError:
            pass
    return edit_text

def write_edit_text(filepath, text):
    if filepath:
        with open(filepath, 'w') as f:
            f.write(text)

def entry_type(line):
    et = 0
    if not line.startswith('@'):
        return et

    for suffix in (" [Sent]", " [Received]", " [Completion]"):
        et += 1
        if line.endswith(suffix):
            return et

    return 0

def parse_log(filepath):
    text = read_edit_text(filepath)

    primary = []
    output = []

    if not text:
        return ("", primary)

    state = 0
    primary_entry = []
    for line in text.splitlines():
        et = entry_type(line)
        if et == 1:
            state = 1
            output.append(line)
            primary_entry.clear()
            continue
        if et == 2:
            state = 2
            output.append(line)
            if primary_entry:
                sent = '\n'.join(primary_entry).strip()
                if sent:
                    primary.append(sent)
            primary_entry.clear()
            continue
        if et == 3:
            state = 0
            continue

        if state in (1, 2):
            output.append(line)
        if state == 1:
            primary_entry.append(line)

    return ('\n'.join(output), primary)
