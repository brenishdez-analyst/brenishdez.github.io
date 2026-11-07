"""Simulación HIPOTÉTICA de colas: no son datos reales de Costco.
Ejecutar: python scripts/simulacion.py
"""
import numpy as np
import pandas as pd

RATES = [25, 30, 35, 50, 55, 52, 40, 30]
POLICIES = {
    "3 cajas fijas": [(0, float("inf"))] * 3,
    "5 cajas fijas": [(0, float("inf"))] * 5,
    "3 + 2 en horas pico": [(0, float("inf"))] * 3 + [(180, 360)] * 2,
}
SEED, REPS, COST_PER_HOUR = 2026, 300, 150

def sample_day(rng, factor=1):
    pieces = []
    for hour, rate in enumerate(RATES):
        n = rng.poisson(rate * factor)
        pieces.append(hour * 60 + rng.uniform(0, 60, n))
    arrivals = np.sort(np.concatenate(pieces))
    services = rng.triangular(2.5, 3.5, 6, len(arrivals))
    return arrivals, services

def simulate(arrivals, services, shifts):
    available = np.array([start for start, end in shifts], dtype=float)
    waits = []
    for arrival, duration in zip(arrivals, services):
        starts = [max(arrival, available[i], start)
                  if max(arrival, available[i], start) < end else np.inf
                  for i, (start, end) in enumerate(shifts)]
        i = int(np.argmin(starts))
        start = starts[i]
        if not np.isfinite(start):
            raise RuntimeError("No hay caja disponible")
        available[i] = start + duration
        waits.append(start - arrival)
    waits = np.array(waits)
    paid = sum(480 if np.isinf(end) else end-start for start, end in shifts)
    overtime = sum(max(0, available[i] - (480 if np.isinf(end) else end))
                   for i, (_, end) in enumerate(shifts))
    return {
        "clientes": len(arrivals),
        "espera_media_min": waits.mean(),
        "p90_espera_min": np.quantile(waits, .9),
        "espera_hasta_10min_pct": (waits <= 10).mean() * 100,
        "costo_diario_mxn": (paid+overtime) / 60 * COST_PER_HOUR,
    }

def run():
    rng = np.random.default_rng(SEED)
    results = []
    for factor in [1.0, 1.1, 1.2]:
        for repeat in range(REPS):
            arrivals, services = sample_day(rng, factor)
            for name, policy in POLICIES.items():
                results.append({"factor": factor, "repeticion": repeat+1,
                                "politica": name,
                                **simulate(arrivals, services, policy)})
    df = pd.DataFrame(results)
    metrics = ["clientes", "espera_media_min", "p90_espera_min",
               "espera_hasta_10min_pct", "costo_diario_mxn"]
    summary = df.groupby(["factor", "politica"])[metrics].mean().round(3)
    print(summary.to_string())
    df.to_csv("simulacion_detalle.csv", index=False)
    summary.to_csv("simulacion_resumen.csv")
    return summary

if __name__ == "__main__":
    run()
