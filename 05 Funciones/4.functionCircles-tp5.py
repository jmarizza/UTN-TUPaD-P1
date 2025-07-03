import math

def circle_area(radius):
    area = (math.pi * (radius ** 2))
    return area


def circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter



if __name__ == "__main__":
    radius = float(input("Ingrese el radio del circulo para calcular area y perimetro: "))

    print(f"Area del circulo = {round(circle_area(radius),2)}\nPerimetro del circulo = {round(circle_perimeter(radius),2)}")
