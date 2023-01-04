import time

def log_response(response, filepath):
    # Append response to file
    with open(filepath, 'a') as f:
        f.write(response + "\n")


def timestamp():
    # Getting current datetime and converting
    # it to string
    dt = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S %Z', dt)

def get_timestamp(which):
    return f'@{timestamp()} [{which}]'

# CudaText: lexer_file="Python"; tab_size=4; tab_spaces=Yes; newline=LF;
