from engine import *
from fastapi import FastAPI
from typing import List
import pandas as pd

app = FastAPI()

@app.post("/analyze-multi")
def analyze_multi(signals: List[dict]):

    df = pd.DataFrame(signals)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # clean pipeline
    df = preprocess_signals(df)
    clusters = create_signal_clusters(df)

    final_results = []

    for cluster in clusters:
        anomaly = detect_anomaly(cluster)
        trend = detect_trend(cluster)
        spatial = detect_spatial(cluster)
        confidence = compute_confidence(cluster)
        risk_level, risk_score = compute_risk(cluster, confidence)

        explanation = generate_explanation(
            cluster, anomaly, trend, spatial, confidence, risk_level
        )

        final_results.append({
            "situation_summary": f"{anomaly.replace('_',' ').title()} detected",
            "anomaly_type": anomaly,
            "anomaly_count": len(cluster),
            "risk_level": risk_level,
            "risk_score": float(risk_score),  
            "temporal_context": trend,
            "spatial_context": spatial,
            "confidence": confidence,
            "key_indicators": list(cluster['signal_type'].unique()),
            "contributing_signals": cluster['signal_type'].tolist(),
            "explanation": explanation
        })

    return final_results