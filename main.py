#!/usr/bin/env python3

import os
import argparse
import pandas as pd


def main(filename):
    CSV_FILE_PATH = '/utils/taxi+_zone_lookup.csv'
    PARQUET_EXTENSION = '.parquet'

    try:
        filenameSplit = os.path.splitext(filename[0])
        fileExtension = filenameSplit[1]
        if fileExtension == PARQUET_EXTENSION:
            taxiDataframe = pd.read_parquet(filename, engine='pyarrow')
            csvFile = os.getcwd() + CSV_FILE_PATH
            zoneDataframe = pd.read_csv(csvFile)
            completeDataframe = pd.merge(taxiDataframe, zoneDataframe, how='right', left_on='DOLocationID',
                                         right_on='LocationID')

            distanceFilteredDataframe = completeDataframe[completeDataframe['trip_distance'] > 0.95]
            groupedDataframe = distanceFilteredDataframe.groupby(['Borough', 'Zone'], dropna=False).size().reset_index(
                name='Trips')
            sortedDataframe = groupedDataframe[['Trips', 'Borough', 'Zone']].sort_values(by=['Trips'],
                                                                                         ascending=False).head(10)
            print(sortedDataframe.to_string(index=False))
        else:
            raise Exception("The file extension is not correct. Please try again using a file with .parquet extension")
    except FileNotFoundError:
        print("The file does not exist. Please try again")
    except Exception as error:
        print(f'An error occurred: <{error}>')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs=1, help='Parquet filename. If it is not in the'
                                                  ' same directory as the executable, '
                                                  'please indicate the full path.')
    argsNamespace = parser.parse_args()
    args = vars(argsNamespace)['filename']
    main(args)
