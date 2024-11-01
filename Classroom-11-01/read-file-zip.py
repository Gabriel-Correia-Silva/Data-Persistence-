import zipfile

zip_file_path = "./file-zip.zip"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    
    file_name = zip_ref.namelist()[0]
        
    with zip_ref.open(file_name) as file:
            
            for line in file:
                print(line.decode('utf-8').strip())