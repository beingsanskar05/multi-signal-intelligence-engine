import pandas as pd



# Phase 1: Preprocess

def preprocess_signals(df):
    df.columns = df.columns.str.strip().str.lower()
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    required_cols = ['vessel_id', 'lat', 'lon', 'location', 'timestamp', 'signal_type', 'value']
    df = df[required_cols]
    df = df.dropna()
    df = df.sort_values(by='timestamp').reset_index(drop=True)

    # Add extra fields
    df['signal_id'] = df.index.astype(str)
    df['status'] = "ALLOW"
    df['trace_id'] = "T1"
    df['reason'] = "simulated"

    df['confidence_score'] = df['value'] / df['value'].max()

    return df


# Phase 2: Clustering

def create_signal_clusters(df):
    df['time_bucket'] = df['timestamp'].dt.floor('7D')

    grouped = df.groupby(['location', 'time_bucket'])

    clusters = []
    for _, group in grouped:
        clusters.append(group)

    return clusters



# Phase 3: Anomaly Detection

def detect_anomaly(cluster):
    signal_types = set(cluster['signal_type'])

    if 'oil_spill' in signal_types and 'current' in signal_types:
        return 'spread_risk'

    if 'temperature' in signal_types and 'wind' in signal_types:
        return 'environment_anomaly'

    if 'oil_spill' in signal_types and 'temperature' in signal_types:
        return 'marine_anomaly'

    if len(cluster) >= 3 and len(signal_types) == 1:
        return 'habitual_issue'

    return 'normal'



# Phase 4: Trend Detection

def detect_trend(cluster):
    cluster = cluster.sort_values(by='timestamp')
    values = cluster['value'].tolist()

    if len(values) < 2:
        return "STABLE"

    if all(x < y for x, y in zip(values, values[1:])):
        return "RISING"
    elif all(x > y for x, y in zip(values, values[1:])):
        return "FALLING"
    else:
        return "STABLE"


# Phase 5: Spatial Context

def detect_spatial(cluster):
    return cluster['location'].unique().tolist()



# Phase 6: Confidence Layer

def compute_confidence(cluster):
    avg_conf = cluster['confidence_score'].mean()

    if avg_conf >= 0.75:
        return "HIGH"
    elif avg_conf >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"


# Phase 7: Risk Scoring

def compute_risk(cluster, confidence):
    unique_signals = cluster['signal_type'].nunique()

    if unique_signals == 1:
        risk_level = "LOW"
    elif unique_signals >= 3:
        risk_level = "HIGH"
    else:
        risk_level = "MEDIUM"

    risk_score = round(unique_signals * 0.3 + 0.4, 2)

    return risk_level, risk_score

# Phase 8: Explanation Layer

def generate_explanation(cluster, anomaly, trend, spatial, confidence, risk_level):
    signals = ", ".join([s.replace("_", " ") for s in cluster['signal_type'].unique()])
    location = ", ".join(spatial)

    anomaly_text = anomaly.replace("_", " ").title()

    explanation = (
        f"{anomaly_text} detected in {location} "
        f"with {trend.lower()} trend based on {signals} signals, "
        f"confidence is {confidence.lower()} and risk level is {risk_level.lower()}."
    )

    return explanation