from datetime import datetime
def logDictionary(filepath,dict):
    try:
        with open(filepath, 'a') as file:
            for key,value in dict.items():
                file.write(str(datetime.now())+f" INFO - {key} - {value} \n ")
   
    except IOError as e:
        print(f"Error: {e}")
        raise e
    


