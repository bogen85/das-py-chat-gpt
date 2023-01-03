from datetime import datetime

def log_response(response, filepath):
    # Append response to file
    with open(filepath, 'a') as f:
        f.write(response + "\n")


def timestamp():
    # Getting current datetime and converting
    # it to string
    dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')
