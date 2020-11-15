"""Module to merge all csv in data directory to one file
"""

import pandas as pd
import os
import sys
from pathlib import Path, PurePath
sys.path.append("..")

if Path('../data').exists():
    data_directory = PurePath("../data")
    print(data_directory)

if Path('./data').exists():
    data_directory = PurePath("./data")
    print(data_directory)

def merge_csv(result_filename="merged_results"):
    df = None
    for data_file in os.listdir(data_directory):
        if data_file.endswith(".csv"):

            if data_file == result_filename:
                continue # Skips merging previous merges

            if df is None:
                df = pd.read_csv(os.path.join(data_directory, data_file))
            else:
                temp = pd.read_csv(os.path.join(data_directory, data_file))
                df = df.append(temp, ignore_index=True)
        else:
            continue
    print(f"Merged all Dataframes to shape {df.shape}")
    result_filename += ".csv"

    prompt = input(f"Do you want to save the result as {result_filename} Y/[n]: ")
    df.drop_duplicates(subset=df.columns)
    if prompt.lower().__contains__("y"):
        df.to_csv(os.path.join(data_directory, result_filename))
        print(f"csv was saved in {data_directory}")

if __name__ == "__main__":
    merge_csv(result_filename="merged_results")
