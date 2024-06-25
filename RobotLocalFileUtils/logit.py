def write_text_to_log_file(filepath:str, text: str):
    try:
        with open(file, 'a') as file:
            file.write(text + '\n')
   
    except IOError as e:
        print(f"Error: {e}")
        raise e