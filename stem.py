import matplotlib.pyplot as plt
import numpy as np #numerica

# Imposta lo stile del grafico utilizzando uno stile predefinito di matplotlib
plt.style.use('_mpl-gallery')

# Crea i dati per l'asse x: un array che parte da 0.5 e incrementa di 1 per 8 valori (0.5, 1.5, 2.5, ..., 7.5)
x = 0.5 + np.arange(8)
# Crea i dati per l'asse y: una lista di 8 valori che rappresentano le altezze dei "steli"
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# Crea una nuova figura e un nuovo asse (sottografico)
fig, ax = plt.subplots()

# Crea un grafico a stelo, che mostra punti dati come linee verticali che si estendono dalla linea di base all'altezza del valore y
ax.stem(x, y)

# Configura i limiti e le tacche degli assi:
# - xlim: imposta i limiti dell'asse x da 0 a 8
# - xticks: imposta le tacche dell'asse x da 1 a 7
# - ylim: imposta i limiti dell'asse y da 0 a 8
# - yticks: imposta le tacche dell'asse y da 1 a 7
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# Mostra il grafico in una finestra interattiva
plt.show()