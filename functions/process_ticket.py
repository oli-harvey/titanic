import pandas as pd
def process_ticket(
        df: pd.DataFrame
        ) -> pd.DataFrame:
    processed_df = df.copy()
    processed_df['ticket_letter'] = (
    processed_df['Ticket']
        .replace('(\d)', '', regex=True)
        .str.split(' ')
        .str[0]
        .fillna('z')
        .str[0]
    )

    processed_df['ticket_num'] = (
        processed_df['Ticket']
            .str.extract('(\d+)')
            .fillna(0)
            .astype(int)
    )

    return processed_df