import pandas as pd 
import os

def CheckHeader(path):
    header = ["Date","Low","Open","Volume","High","Close","Adjusted Close"]
    try:
        df = pd.read_csv(path)
    except:
        print(f"cannot open file {path}")
        exit(1)

    if list(df.columns) != header:
        df = df[header]
    return df
    
def Combine_files(files):
    dfs =[]
    for file in files:
        dfs.append(CheckHeader(file))
    df_combined = pd.concat(dfs)
    df_combined.to_csv('fileCombined.csv', index=False, sep='\t')
    print("Files combined successfully.")







if __name__ == "__main__":
    
    path = "../CSVs"
    try:
        folder = os.listdir(path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)
    files_input = [path+"/"+file for file in folder if file.split('.')[1] == 'csv']
    Combine_files(files_input)




