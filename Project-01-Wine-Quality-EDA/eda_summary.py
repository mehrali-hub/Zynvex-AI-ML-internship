import pandas as pd

df = pd.read_csv('WineQT.csv')
print('Shape:', df.shape)
print('\nMissing values per column:\n', df.isnull().sum())
print('\nData types:\n', df.dtypes)

print('\nQuality value counts:\n', df['quality'].value_counts().sort_index())
print('\nQuality percentages:\n', (df['quality'].value_counts(normalize=True).sort_index()*100).round(2))

# Mean alcohol by quality
alcohol_means = df.groupby('quality')['alcohol'].mean().sort_index()
print('\nMean alcohol by quality:\n', alcohol_means.round(3))

# Top correlations with quality
corr = df.corr()
quality_corr = corr['quality'].drop('quality').sort_values(ascending=False)
print('\nTop correlations with quality (descending):\n', quality_corr.round(4))

# Show strongest negative correlations
print('\nStrongest negative correlations with quality:\n', quality_corr[quality_corr<0].sort_values())

# Compare means for high vs low quality
high_q = df[df['quality']>=7]
low_q = df[df['quality']<=4]
print('\nSamples: high quality (>=7):', len(high_q), 'low quality (<=4):', len(low_q))
if len(high_q)>0 and len(low_q)>0:
    compare = pd.DataFrame({
        'high_mean': high_q.mean(),
        'low_mean': low_q.mean(),
        'diff': (high_q.mean()-low_q.mean())
    })
    cols_of_interest = ['alcohol','volatile acidity','residual sugar','pH','sulphates','citric acid']
    print('\nMean differences (high - low) for key features:\n', compare.loc[cols_of_interest].round(3))

print('\nDone')
