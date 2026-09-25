
import pandas as pd
import matplotlib.pyplot as plt


CSV_PATH = "programming_languages.csv"  
df = pd.read_csv(CSV_PATH)



print("ESTADISTICAS DESCRIPTIVAS (columnas numericas)")

print(df[["difficulty", "popularity", "year_created"]].describe(), end="\n\n")

mas_popular = df.loc[df["popularity"].idxmax()]
menos_popular = df.loc[df["popularity"].idxmin()]
mas_dificil = df.loc[df["difficulty"].idxmax()]
mas_antiguo = df.loc[df["year_created"].idxmin()]
mas_nuevo = df.loc[df["year_created"].idxmax()]


print("DATOS DESTACADOS")
print("=" * 60)
print(f"Lenguaje mas popular:   {mas_popular['language']} ({mas_popular['popularity']}%)")
print(f"Lenguaje menos popular: {menos_popular['language']} ({menos_popular['popularity']}%)")
print(f"Lenguaje mas dificil:   {mas_dificil['language']} (dificultad {mas_dificil['difficulty']})")
print(f"Lenguaje mas antiguo:   {mas_antiguo['language']} ({mas_antiguo['year_created']})")
print(f"Lenguaje mas nuevo:     {mas_nuevo['language']} ({mas_nuevo['year_created']})")


correlacion = df["difficulty"].corr(df["popularity"])
print(f"\nCorrelacion dificultad vs popularidad: {correlacion:.2f}")

print("\nConteo de lenguajes por paradigma:")
print(df["paradigm"].value_counts(), end="\n\n")
print("Conteo de lenguajes por tipado:")
print(df["typing"].value_counts(), end="\n\n")
df_ordenado = df.sort_values("popularity", ascending=False)

plt.figure(figsize=(8, 5))
barras = plt.bar(df_ordenado["language"], df_ordenado["popularity"], color="#4C72B0")
plt.title("Popularidad por lenguaje de programacion")
plt.xlabel("Lenguaje")
plt.ylabel("Popularidad (%)")
plt.ylim(0, max(df["popularity"]) + 10)

for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width() / 2, altura + 1,
              f"{altura}%", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("popularidad_por_lenguaje.png", dpi=150)
print("Grafico guardado: popularidad_por_lenguaje.png")

df_dificultad = df.sort_values("difficulty", ascending=True)

plt.figure(figsize=(8, 5))
barras_h = plt.barh(df_dificultad["language"], df_dificultad["difficulty"], color="#DD8452")

for barra in barras_h:
    ancho = barra.get_width()
    plt.text(ancho + 0.05, barra.get_y() + barra.get_height() / 2,
              f"{ancho}", va="center", fontsize=9)

plt.title("Dificultad por lenguaje de programacion")
plt.xlabel("Dificultad (1 = mas facil, 5 = mas dificil)")
plt.ylabel("Lenguaje")
plt.xlim(0, df["difficulty"].max() + 1)
plt.tight_layout()
plt.savefig("dificultad_por_lenguaje.png", dpi=150)
print("Grafico guardado: dificultad_por_lenguaje.png")

plt.show()
