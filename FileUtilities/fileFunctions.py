import shutil
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

