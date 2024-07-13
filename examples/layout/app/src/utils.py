import pandas as pd


def convert_to_df(data: list[dict[str, str]]) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df
