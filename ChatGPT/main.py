import os
import model_manager
import session_manager
import auth_manager
import chat_loop

def main():
    # Get ChatGPT.data directory from environment variable
    data_dir = os.environ.get("CHAT_GPT_DATA", "ChatGPT.data")

    # Get API key
    api_key_filepath = f"{data_dir}/api_key.txt"
    api_key = auth_manager.get_api_key(api_key_filepath)

    # Get model ID
    model_filepath = f"{data_dir}/model_file.txt"
    model_id = model_manager.get_model(api_key, model_filepath)

    # Get session ID
    #session_filepath = f"{data_dir}/session_id.txt"
    #session_id = session_manager.get_session(model_id, session_filepath)

    # Start chat loop
    #chat_loop.run(model_id, session_id, api_key)
    chat_loop.run(model_id, api_key)

if __name__ == "__main__":
    main()
