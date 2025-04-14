"""---------------------- Nettoyage des données -------------------"""
# Fonction pour détecter les OUTLIERS avec la méthode IQR
def iqr_outlier_detection(df, feature, threshold=1.5):
    q1 = df[feature].quantile(0.25)
    q3 = df[feature].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr

    return df.query(f"{feature} < {lower_bound} | {feature} > {upper_bound}")
