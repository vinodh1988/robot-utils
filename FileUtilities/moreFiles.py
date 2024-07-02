from datetime import datetime
import csv
def logDictionary(filepath,dict):
    try:
        with open(filepath, 'a') as file:
            for key,value in dict.items():
                file.write(str(datetime.now())+f" INFO - {key} - {value} \n ")
   
    except IOError as e:
        print(f"Error: {e}")
        raise e
    
def read_csv_to_array_of_dictionary(file_path):
    try:
        array=[]
        with open(file_path,mode="r",newline="",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            for row in reader:
                array.append(row)
        return array
    except Exception as e:
        raise e



