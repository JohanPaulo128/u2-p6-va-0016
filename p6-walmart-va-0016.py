import matplotlib.pyplot as plt
import numpy as np
# Johan Paulo Aros NC 0016

cant_productos=[100,150,200,300,500]
precio = [4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

## Personalizar grafica
plt.plot(cant_productos,precio,color="green",marker="o", linestyle='dashed',linewidth=2, markersize=12)
plt.title("Ventas de walmart NC 0016")
plt.xlabel("cant product")
plt.ylabel("precios")
plt.show()