def transform(df):
    df.columns = df.columns.str.lower()
    df["name"] = df["name"].str.strip()
    return df