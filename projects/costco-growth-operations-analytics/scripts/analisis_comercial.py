"""Análisis reproducible con datos publicados por Costco.
Desde la raíz de este proyecto: python scripts/analisis_comercial.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "ventas_mensuales_fy2026.csv")
assert len(df) == 12
assert int(df["semanas"].sum()) == 52
assert df.isna().sum().sum() == 0
assert df["ventas_netas_millones_usd"].gt(0).all()

df["ventas_promedio_semanal"] = df["ventas_netas_millones_usd"] / df["semanas"]
top = df.loc[df["ventas_promedio_semanal"].idxmax()]
print("Mayor promedio semanal:", top["mes"], top["anio"],
      round(top["ventas_promedio_semanal"], 2), "millones USD/semana")
print("Suma periodos comerciales FY2026:", int(df["ventas_netas_millones_usd"].sum()))
print("Total exacto Form 10-K FY2026: 297247 millones USD")
print("Diferencia por redondeo: ",
      int(df["ventas_netas_millones_usd"].sum()) - 297247, "millones USD")
print("Máximo crecimiento mensual:", df.loc[df["crecimiento_ventas_pct"].idxmax(),
                                             ["mes", "crecimiento_ventas_pct"]].to_dict())
