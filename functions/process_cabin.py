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
            .str[0]
    )
    processed_df['cabin_num'] = (
        processed_df['Cabin']
            .str.extract('(\d+)')
            .fillna(0)
            .astype(int)
    )
    processed_df['num_of_cabins'] = (
        processed_df['Cabin']
            .str.count(' ') 
    )
    return processed_df