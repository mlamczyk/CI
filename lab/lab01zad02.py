import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler



miasta = pd.read_csv('data/miasta.csv')
print(miasta)
print(miasta.values)

miasta.loc['10', :] = [2010, 460, 555, 405]
print(miasta)

plt.plot(miasta['Rok'], miasta['Gdansk'], 'r.-', label='Gdańsk')
plt.xlabel('Lata')
plt.ylabel('Liczba ludności [w tys.]')
plt.title('Ludność w miastach Polski')
plt.legend()
plt.show()

plt.plot(miasta['Rok'], miasta['Gdansk'], 'r.-', label='Gdańsk')
plt.plot(miasta['Rok'], miasta['Poznan'], 'g.-', label='Poznań')
plt.plot(miasta['Rok'], miasta['Szczecin'], 'b.-', label='Szczecin')
plt.xlabel('Lata')
plt.ylabel('Liczba ludności [w tys.]')
plt.title('Ludność w miastach Polski')
plt.legend()
plt.show()


rok =  miasta['Rok']
rok = rok.tolist()
miasta.drop('Rok', axis=1, inplace=True)

std_scaler = StandardScaler()
miasta1 = std_scaler.fit_transform(miasta.to_numpy())
print('Średnia: ', round(np.mean(miasta1), 1))
print('Odchylenie: ', np.std(miasta1))
miasta1 = pd.DataFrame(miasta1, columns=[
    'Gdansk','Poznan','Szczecin'])
miasta1.insert(0, 'Rok', rok)
print(miasta1)

minmax_scaler = MinMaxScaler()
miasta2 = minmax_scaler.fit_transform(miasta.to_numpy())
print('Minimum: ', np.min(miasta2))
print('Maksimum: ', np.max(miasta2))
miasta2 = pd.DataFrame(miasta1, columns=[
    'Gdansk','Poznan','Szczecin'])
miasta2.insert(0, 'Rok', rok)
print(miasta2)
