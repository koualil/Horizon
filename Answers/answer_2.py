import os
import pandas as pd

def handle_file(file):
    try:
        open_file = open(file)
        line = open_file.readline()
      
        for letter in line:
            if not letter.isalnum():
                break
        index = line.find(letter)
        line = line[index:]
        delimiter = ''
        for i in line:
            if not i.isalnum():
                delimiter += i
            if len(delimiter) >= 2 and i == ' ':
                delimiter = '\t'
                break
            if i.isalnum():
                break



        print("file name is :",os.path.basename(file))
        print(f"the delimiter of the file is : '{delimiter}'")
        df = pd.read_csv(file ,sep=delimiter)
        index = 1
        for col in df.columns:
            print(f"column_{index}: {col}, redshift_dtype:{df[col].dtype}")
            index += 1

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)





if __name__ == "__main__":
    path = "../CSVs/AAME.csv"
    path1 = "../CSVs/file.txt"
    url = 'www.x.com'
    handle_file(path)
   