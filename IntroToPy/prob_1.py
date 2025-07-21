import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("C:/Users/Adriana/CodeSinaia-2025/CodeSinaia-2025/IntroToPy/mountains_db.tsv", sep="\t", names=["Nume", "Altitudine", "Tara", "ISO"])

df["Altitudine"] = pd.to_numeric(df["Altitudine"], errors="coerce")

num_countries = df["ISO"].nunique()
print(f"Numar total de tari: {num_countries}")

missing_altitude = df["Altitudine"].isna().sum()
print(f"Munti fara altitudine: {missing_altitude}")

valid_alts = df["Altitudine"].dropna()
alt_min = valid_alts.min()
alt_max = valid_alts.max()
alt_mean = valid_alts.mean()
alt_median = valid_alts.median()
alt_std = valid_alts.std()

print(f"Altitudine minima: {alt_min} m")
print(f"Altitudine maxima: {alt_max} m")
print(f"Altitudine medie: {alt_mean:.2f} m")
print(f"Mediana altitudinii: {alt_median:.2f} m")
print(f"Deviatie standard: {alt_std:.2f} m")

topN = 10
top_mountains = df.dropna(subset=["Altitudine"]).sort_values(by="Altitudine", ascending=False).head(topN)
print("\n Cei mai inalti munti:")
print(top_mountains[["Nume", "Altitudine", "Tara", "ISO"]])

plt.figure(figsize=(12,6))
sns.countplot(data=df, x="ISO", order=df["ISO"].value_counts().index)
plt.title("Numar de munti pe tara (cod ISO)")
plt.xlabel("Cod ISO")
plt.ylabel("Numar munti")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

max_alt_by_country = df.dropna(subset=["Altitudine"]).groupby("Tara")["Altitudine"].max().sort_values()
plt.figure(figsize=(12,6))
max_alt_by_country.plot(kind="barh")
plt.title("Altitudine maxima pe tara")
plt.xlabel("Altitudine (m)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x=valid_alts)
plt.title("Distributia globala a altitudinilor")
plt.xlabel("Altitudine (m)")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(2, 1, figsize=(14,10), sharex=True)

country_stats = df.dropna(subset=["Altitudine"]).groupby("Tara")["Altitudine"].agg(["min", "median", "max"])
country_stats.plot(ax=ax[0], kind="bar")
ax[0].set_title("Altitudine minima, mediana si maxima pe tara")
ax[0].set_ylabel("Altitudine (m)")
ax[0].legend(loc="upper right")
ax[0].tick_params(axis='x', rotation=45)

sns.boxplot(data=df.dropna(subset=["Altitudine"]), x="Tara", y="Altitudine", ax=ax[1])
ax[1].set_title("Distributia altitudinilor pe tari")
ax[1].set_xlabel("tara")
ax[1].set_ylabel("Altitudine (m)")
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()