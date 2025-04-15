import math

class SodaCan:
    #costruttore
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    #self perche è metodo
    def getSurfaceArea(self):
        # Surface Area = 2 * π * r * h + 2 * π * r^2
        lateral_area = 2 * math.pi * self.radius * self.height
        top_bottom_area = 2 * math.pi * self.radius ** 2
        return lateral_area + top_bottom_area

    def getVolume(self):
        # Volume = π * r^2 * h
        return math.pi * self.radius ** 2 * self.height
    
soda = SodaCan(height=10, radius=2)

# Richiamare i metodi e stampare i risultati
surface_area = soda.getSurfaceArea()
volume = soda.getVolume()

# Stampa dei risultati
print(f"Superficie totale della lattina: {surface_area:.2f} cm²")
print(f"Volume della lattina: {volume:.2f} cm³")