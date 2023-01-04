import os
import model_manager
import auth_manager
import chat_ui

def main():
    # Get ChatGPT.data directory from environment variable
    data_dir = os.environ.get("CHAT_GPT_DATA", "ChatGPT.data")

    # Get API key
    api_key_filepath = f"{data_dir}/api_key.txt"
    api_key = auth_manager.get_api_key(api_key_filepath)

    # Get model ID
    model_filepath = f"{data_dir}/model_file.txt"
    model_id = model_manager.get_model(api_key, model_filepath)

    # Lauch GUI
    chat_ui.main(data_dir, api_key, model_id)

if __name__ == "__main__":
    main()

# CudaText: lexer_file="Python"; tab_size=4; tab_spaces=Yes; newline=LF;
