import pandas as pd

def vin_check_digit(full_vin):
    df_pw = pd.read_csv('pw.csv')
    df_lt = pd.read_csv('lt.csv')
    vin = str(full_vin)
    for index, row in df_pw.iterrows():
        df_pw.loc[index, ['vin']] = vin[index]

    df_temp = pd.merge(df_pw, df_lt, on='vin', how='left')

    if len(full_vin) != 17 or (df_temp['trans_number'].isnull() == True).any():
        return False
    else:
        try:
            df_temp['products'] = df_temp['trans_number'] * df_temp['weight']
            vin_sum = df_temp['products'].sum()
            check1 = vin_sum % 11
            if check1 == 10 and vin[8] == 'X':
                return True
            elif check1 == int(vin[8]):
                return True
            else:
                return False
        except Exception:
            return False


df_vin = pd.read_csv('vin.csv')

print(df_vin.loc[:, 'vin'].apply(vin_check_digit))

