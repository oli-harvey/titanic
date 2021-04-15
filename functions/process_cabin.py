import pandas as pd

def process_cabin(
    df: pd.DataFrame
) -> pd.DataFrame:
    processed_df = df.copy()
    processed_df['cabin_letter'] = (
        processed_df['Cabin']
            .replace('(\d)', '', regex=True)
            .str.split(' ')
            .str[0]
            .fillna('z')
    )
    processed_df['cabin_num'] = (
        processed_df['Cabin']
            .replace('[A-Z]', '', regex=True)
            .str.split(' ')
            .str[0]
            .fillna(0)
    )
    processed_df['num_of_cabins'] = (
        processed_df['Cabin']
            .str.count(' ')
            .fillna(0)
    ) + 1
    return processed_df