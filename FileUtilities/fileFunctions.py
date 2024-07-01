import shutil
import os 
def moveFile(source,destination):
    try:
        shutil.move(source,destination)
    except FileExistsError as f:
        raise f
    except PermissionError as f:
        raise f
    except Exception as f:
        raise f
    
def copyFile(source,destination):
    try:
        shutil.copy(source,destination)
    except FileExistsError as f:
        raise f
    except PermissionError as f:
        raise f
    except Exception as f:
        raise f

def  numberOfFiles(path):
    try:
        if os.path.exists(path):
            files=[f for  f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
            return len(files)
    except Exception as e:
        raise e
    
def getFileSize(file_path):
    try:
        if os.path.isfile(file_path):
            return os.path.getsize(file_path)/1024
        else:
            raise Exception
    except Exception as e:
        raise Exception



