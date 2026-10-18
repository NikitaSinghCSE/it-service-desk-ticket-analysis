"""Generate a SYNTHETIC IT helpdesk ticket dataset (no real company data).

Columns are a guess -- rename them to match what your analysis code expects.
Run:  python generate_sample_data.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 2000

priority = rng.choice(["Critical", "High", "Medium", "Low"], N, p=[0.05, 0.20, 0.45, 0.30])
category = rng.choice(["Hardware", "Software", "Network", "Access/Password", "Email"], N,
                      p=[0.15, 0.25, 0.20, 0.30, 0.10])
sla_hours = pd.Series(priority).map({"Critical": 1, "High": 4, "Medium": 8, "Low": 24}).to_numpy()

start = pd.Timestamp("2025-01-01")
created = start + pd.to_timedelta(rng.integers(0, 180 * 24 * 60, N), unit="m")
# resolution time: mostly within SLA, some breaches
resolve_hours = sla_hours * rng.lognormal(mean=-0.2, sigma=0.6, size=N)
resolved = (created + pd.to_timedelta(resolve_hours, unit="h")).round("min")

df = pd.DataFrame({
    "ticket_id": [f"INC{100000 + i}" for i in range(N)],
    "created_at": created,
    "resolved_at": resolved,
    "priority": priority,
    "category": category,
    "status": "Closed",
    "sla_target_hours": sla_hours,
})
df.to_csv("data/sample_tickets.csv", index=False)
print(f"Saved {len(df)} synthetic tickets to data/sample_tickets.csv")
