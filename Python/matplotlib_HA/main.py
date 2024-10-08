import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Quadratzahlen
x = np.arange(10)
y1 = x**2

# Kubikzahlen
y2 = x**3

# Plotten der Daten
plt.plot(x, y1, label='Quadratzahlen', color='blue')
plt.plot(x, y2, label='Kubikzahlen', color='red', linestyle='dashed')

# Beschriftungen und Legende
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Vergleich von Quadrat- und Kubikzahlen')
plt.legend()

# Diagramm speichern
plt.savefig('vergleich_funktionen.png', dpi=300, bbox_inches='tight')

# Erstelle ein Pandas DataFrame
df = pd.DataFrame({'Zahl': x, 'Quadrat': y1, 'Kubik': y2})

# Speichere das DataFrame als CSV-Datei
df.to_csv('zahlen.csv', index=False)