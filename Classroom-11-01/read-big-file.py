import pandas as pd

file_path = 'large_file.csv'

df = pd.read_csv(file_path)


chunk_size = 100000  
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    print(chunk.head(1))
