import os 
funcs = os.listdir('functions')
for func in funcs:
    if func.startswith('__') or func == 'import_all_functions.py':
        continue
    func = func.replace('.py','')
    exec(f'from functions.{func} import *')

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    processed_df = df.copy()
    processed_df = impute_cond_mean(
        df=processed_df,
        col_with_na='Age',
        cond_cols=['Pclass', 'Sex']
    )
    processed_df = process_cabin(processed_df)
    remove_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'num_of_cabins']
    dummy_cols = ['Sex', 'Embarked', 'cabin_num', 'cabin_letter']
    processed_df = processed_df.drop(columns=remove_cols)
    processed_df = pd.get_dummies(processed_df, columns=dummy_cols)
    return processed_df