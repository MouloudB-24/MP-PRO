"""---------------------- Nettoyage des données -------------------"""
# Fonction pour détecter les OUTLIERS avec la méthode IQR
def iqr_outlier_detection(df, feature, threshold=1.5):
    q1 = df[feature].quantile(0.25)
    q3 = df[feature].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr

    outliers = df.query(f"{feature} < {lower_bound} | {feature} > {upper_bound}")
    df_cleaned = df.query(f"{feature} >= {lower_bound} | {feature} <= {upper_bound}")

    return outliers, df_cleaned


# Heat map
def get_corr_matrix_and_heatmap(df):

    # Calculate correlation
    corr_matrix = df.corr(numeric_only=True)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Set up the matplotlib figure
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot the correlation matrix
    sns.heatmap(corr_matrix, mask=mask, cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5, square=True, ax=ax)
    return corr_matrix, fig
