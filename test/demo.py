"""
Author:kingsley
Version:0.0.1
Requirements:股票数据行情
"""
import pandas as pd
import tushare as ts

if __name__ == '__main__':
    df = ts.get_k_data("300104")
    df.index = pd.to_datetime(df.date)
    df.drop('date', inplace=True, axis=1)
    days = [5, 15, 50]
    for ma in days:
        column_name = "MA{}".format(ma)
        df[column_name] = pd.Series.rolling(df.close, ma)

    # 计算浮动比例
    df["pchange"] = df.close.pct_change()
    # 计算浮动点数
    df["change"] = df.close.diff()

    df[["close", "MA5", "MA15", "MA50"]].plot(figsiz=(10, 18))