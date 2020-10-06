import pandas as pd
import sqlite3

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    stock_codes = pd.read_csv('data.csv', index_col=False, dtype={'종목코드': str, '기업명': str, '업종코드': str,
                                                                  '업종': str})
    del stock_codes['번호']
    del stock_codes['상장주식수(주)']
    del stock_codes['자본금(원)']
    del stock_codes['액면가(원)']
    del stock_codes['통화구분']
    del stock_codes['대표전화']
    del stock_codes['주소']
    del stock_codes['총카운트']

    stock_codes.rename(columns={'종목코드': 'code',
                                '기업명': 'company',
                                '업종코드': 'business_code',
                                '업종': 'category'}, inplace=True)
    conn = sqlite3.connect('../db.sqlite3')
    stock_codes.to_sql('stock_codes', conn)
    # print('Insert stock codes into sqlite3')
