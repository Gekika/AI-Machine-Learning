# here I write small code snippets to reduce redundant work 

# to view value counts of my categorical columns

exclude = ['id']

for cols in df_train.select_dtypes(include='object').columns:
    if cols not in exclude:
        print(df_train[cols].value_counts())
        print('\n')