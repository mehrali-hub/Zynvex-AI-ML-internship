import traceback
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
try:
    import seaborn as sns
except ModuleNotFoundError:
    import subprocess, sys
    print('seaborn not found; installing...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'seaborn'])
    import seaborn as sns

try:
    df = pd.read_csv('WineQT.csv')
    print('Loaded CSV, shape:', df.shape)
    print('Columns:', list(df.columns))
    print('\nInfo:')
    print(df.dtypes)

    # create quality_cat
    if pd.api.types.is_integer_dtype(df['quality']):
        df['quality_cat'] = df['quality'].astype('category')
    else:
        df['quality_cat'] = df['quality']
    print('\nCreated quality_cat')

    # check keys used in notebook
    keys = ['quality','alcohol','residual sugar','pH','volatile acidity']
    for k in keys:
        if k not in df.columns:
            raise KeyError(f"Missing column: {k}")
    print('\nAll expected columns present')

    # compute corr
    corr = df.corr()
    print('\nCorr computed')
    print(corr['quality'].sort_values(ascending=False).head())

    print('\nValidation succeeded')
except Exception as e:
    print('Validation failed:', e)
    traceback.print_exc()
