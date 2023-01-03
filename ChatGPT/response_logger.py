def log_response(response, filepath):
    # Append response to file
    with open(filepath, 'a') as f:
        f.write(response + "\n")
