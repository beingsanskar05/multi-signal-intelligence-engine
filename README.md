#  Multi-Signal Intelligence Engine

A deterministic multi-signal intelligence engine that transforms single-signal analysis into a **multi-signal reasoning system** with temporal and spatial awareness.

---

##  Key Features

*  Multi-signal clustering (location + time)
*  Rule-based anomaly detection (no ML, fully deterministic)
*  Temporal reasoning (RISING / STABLE / FALLING)
*  Spatial awareness (affected regions)
*  Confidence & risk scoring
*  Explainable outputs (human-readable)
*  FastAPI-based deployment

---

##  Architecture

```
Input Signals → Preprocessing → Clustering → Reasoning Engine → Context Analysis → Risk Scoring → Explanation → API Output
```

---

##  API Endpoint

```
POST /analyze-multi
```

### Input:

List of signals:

```json
[
  {
    "signal_type": "temperature",
    "value": 30,
    "timestamp": "2026-01-01",
    "location": "Mumbai Coast"
  }
]
```

### Output:

```json
{
  "anomaly_type": "marine_anomaly",
  "risk_level": "HIGH",
  "temporal_context": "RISING",
  "confidence": "MEDIUM"
}
```

---

##  Test Cases

| Scenario           | Expected |
| ------------------ | -------- |
| Single signal      | LOW      |
| Mixed signals      | MEDIUM   |
| Correlated signals | HIGH     |
| Temporal increase  | RISING   |

---

##  Demo Scenarios

* Case 1: Single signal → LOW
* Case 2: Mixed signals → MEDIUM
* Case 3: Correlated signals → HIGH
* Case 4: Temporal increase → RISING

---

##  Tech Stack

* Python
* Pandas
* FastAPI
* Uvicorn

---

##  Key Concepts

* Deterministic Intelligence Systems
* Rule-Based Reasoning
* Temporal Analysis
* Spatial Clustering
* Explainable AI

---

##  Documentation

Detailed system design and testing available in:

```
REVIEW_PACKET.md
```

---

## Author

**Sanskar Pandey**

---

##  Status

✔ Fully functional
✔ Deterministic
✔ API-ready
✔ Tested

---

##  Highlights

This project demonstrates:

* Real-world system design
* Backend API development
* Explainable intelligence systems
* Production-ready architecture
