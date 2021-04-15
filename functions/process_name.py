import pandas as pd
def process_name(
        df: pd.DataFrame
        ) -> pd.DataFrame:
    processed_df = df.copy()
    processed_df['surname'] = processed_df['Name'].str.extract(r'(\w+),')
    processed_df['title'] = processed_df['Name'].str.extract(r', (\w+).')
    return processed_df