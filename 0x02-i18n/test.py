import pandas as pd

# Supposons que vous avez une base de données sous forme de DataFrame
data = {
    'Groupe_ABO': ['A', 'B', 'AB', 'O', 'A', 'B', 'O', 'A', 'AB', 'B'],
    'Rhesus': ['+', '-', '+', '-', '+', '+', '-', '+', '+', '-']
}
df = pd.DataFrame(data)

# Compter les fréquences phénotypiques pour ABO
freq_abo = df['Groupe_ABO'].value_counts(normalize=True)

# Calcul des fréquences alléliques pour ABO
p = freq_abo['A'] + 0.5 * freq_abo['AB']
q = freq_abo['B'] + 0.5 * freq_abo['AB']
r = freq_abo['O']

# Afficher les fréquences alléliques
print(f"Fréquences alléliques pour ABO : A={p:.2f}, B={q:.2f}, O={r:.2f}")

# Calcul des fréquences génotypiques pour ABO
freq_genotypiques_abo = {
    'AA': p**2,
    'AO': 2*p*r,
    'BB': q**2,
    'BO': 2*q*r,
    'AB': 2*p*q,
    'OO': r**2
}

# Afficher les fréquences génotypiques
print("Fréquences génotypiques pour ABO :")
for genotype, freq in freq_genotypiques_abo.items():
    print(f"{genotype}: {freq:.2f}")

# Compter les fréquences phénotypiques pour Rhésus
freq_rhesus = df['Rhesus'].value_counts(normalize=True)

# Calcul des fréquences alléliques pour Rhésus
d = (freq_rhesus.get('-', 0)) ** 0.5
D = 1 - d

# Afficher les fréquences alléliques pour Rhésus
print(f"Fréquences alléliques pour Rhésus : D={D:.2f}, d={d:.2f}")

# Calcul des fréquences génotypiques pour Rhésus
freq_genotypiques_rhesus = {
    'Rh+/Rh+': D**2,
    'Rh+/Rh-': 2*D*d,
    'Rh-/Rh-': d**2
}

# Afficher les fréquences génotypiques pour Rhésus
print("Fréquences génotypiques pour Rhésus :")
for genotype, freq in freq_genotypiques_rhesus.items():
    print(f"{genotype}: {freq:.2f}")
