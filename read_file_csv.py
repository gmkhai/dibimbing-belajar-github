import polars as pl


def read_file_csv(file_path: str):
    """
    function for read file csv
    Args:
        file_path (str): path file read csv
    """

    data_frame = pl.read_csv(file_path, separator=';')
    return data_frame


if __name__ == '__main__':
    print(read_file_csv('username.csv'))
