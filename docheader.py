
import pandas as pd


def getHeader(file):
    f = open(file, 'r')

    df = pd.read_csv(f)
    list_of_column_names = list(df.columns)

    print('List of column names : ',
        list_of_column_names)
    return(list_of_column_names)


if __name__ == '__main__':
    getHeader()
