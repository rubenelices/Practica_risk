import time
import numpy as np
from itertools import permutations
from typing import List, Dict, Tuple

class TableroRisk:
    def __init__(self, tropas: Dict[str, Dict], territorios: Dict[str, Tuple[int, str]], puntos_totales: int):
        self.tropas = tropas
        self.territorios = territorios  # Diccionario de {nombre: (defensa, tipo)}
        self.puntos_totales = puntos_totales
        self.combinaciones = []
        self.permutaciones = []
        self.modificadores_terreno = {
            'montañoso': {'Infantería': 0.8, 'Caballería': 1, 'Artillería': 1},
            'pantanoso': {'Infantería': 1.2, 'Caballería': 0.8, 'Artillería': 1.2},
            'llanura': {'Infantería': 1, 'Caballería': 1.2, 'Artillería': 0.8}
        }

    def generar_combinaciones(self) -> List[Dict[str, int]]:
        max_infanteria = self.puntos_totales // self.tropas['Infantería']['costo']
        max_caballeria = self.puntos_totales // self.tropas['Caballería']['costo']
        max_artilleria = self.puntos_totales // self.tropas['Artillería']['costo']

        for inf in range(1, max_infanteria + 1):
            for cab in range(1, max_caballeria + 1):
                for art in range(1, max_artilleria + 1):
                    costo_total = (inf * self.tropas['Infantería']['costo'] +
                                   cab * self.tropas['Caballería']['costo'] +
                                   art * self.tropas['Artillería']['costo'])

                    if costo_total <= self.puntos_totales:
                        combinacion = {
                            'Infantería': inf,
                            'Caballería': cab,
                            'Artillería': art,
                            'Costo Total': costo_total,
                            'Fuerza Total': (inf * self.tropas['Infantería']['fuerza'] +
                                             cab * self.tropas['Caballería']['fuerza'] +
                                             art * self.tropas['Artillería']['fuerza']),
                        }
                        self.combinaciones.append(combinacion)

        return self.combinaciones

    def generar_permutaciones(self) -> List[Tuple[str, ...]]:
        territorios_ordenados = sorted(self.territorios.items(), key=lambda x: x[1][0])
        self.permutaciones = list(permutations([territorio[0] for territorio in territorios_ordenados]))
        return self.permutaciones

    def atacar(self, combinacion: Dict[str, int], permutacion: Tuple[str, ...]) -> Dict[str, int]:
        fuerza_restante = combinacion['Fuerza Total']
        territorios_conquistados = 0

        for territorio in permutacion:
            defensa, tipo_terreno = self.territorios[territorio]

            fuerza_ataque = (
                combinacion['Infantería'] * self.tropas['Infantería']['fuerza'] * 
                    self.modificadores_terreno[tipo_terreno]['Infantería'] +
                combinacion['Caballería'] * self.tropas['Caballería']['fuerza'] * 
                    self.modificadores_terreno[tipo_terreno]['Caballería'] +
                combinacion['Artillería'] * self.tropas['Artillería']['fuerza'] * 
                    self.modificadores_terreno[tipo_terreno]['Artillería']
            )

            if fuerza_ataque >= defensa and fuerza_restante >= defensa:
                territorios_conquistados += 1
                fuerza_restante -= defensa
            else:
                break

        return {
            'Territorios Conquistados': territorios_conquistados,
            'Tropas Restantes': fuerza_restante
        }

    def simular_todas_permutaciones(self):
        mejores_resultados = []

        for combinacion in self.combinaciones:
            for permutacion in self.permutaciones:
                resultado = self.atacar(combinacion, permutacion)
                mejores_resultados.append({
                    'Combinacion': combinacion,
                    'Permutacion': permutacion,
                    'Resultado': resultado
                })
                print(f"Combinación: Inf: {combinacion['Infantería']}, Cab: {combinacion['Caballería']}, Art: {combinacion['Artillería']} | "
                      f"Permutación: {' -> '.join(permutacion)} | "
                      f"Territorios Conquistados: {resultado['Territorios Conquistados']} | Tropas Restantes: {resultado['Tropas Restantes']}")
                time.sleep(0.1)

        return mejores_resultados

    def obtener_mejor_combinacion(self, resultados):
        mejor_resultado = max(resultados, key=lambda x: (x['Resultado']['Territorios Conquistados'], x['Resultado']['Tropas Restantes']))
        return mejor_resultado

def obtener_datos_usuario():
    print("\nElija una opción:")
    print("1. Usar datos predeterminados")
    print("2. Ingresar datos manualmente")
    opcion = int(input("Seleccione una opción (1 o 2): "))

    if opcion == 1:
        puntos_totales = 20
        tropas = {
            'Infantería': {'fuerza': 3, 'costo': 1},
            'Caballería': {'fuerza': 5, 'costo': 3},
            'Artillería': {'fuerza': 8, 'costo': 5}
        }
        territorios = {
            'Territorio 1': (10, 'montañoso'),
            'Territorio 2': (15, 'pantanoso'),
            'Territorio 3': (12, 'llanura')
        }
    elif opcion == 2:
        puntos_totales = int(input("Ingrese el número total de puntos disponibles: "))
        tropas = {
            'Infantería': {},
            'Caballería': {},
            'Artillería': {}
        }
        for tipo in tropas.keys():
            fuerza = int(input(f"Ingrese la fuerza de {tipo}: "))
            costo = int(input(f"Ingrese el costo de {tipo}: "))
            tropas[tipo] = {'fuerza': fuerza, 'costo': costo}

        num_territorios = int(input("Ingrese el número de territorios enemigos: "))
        territorios = {}
        for i in range(num_territorios):
            nombre = f"Territorio {i+1}"
            defensa = int(input(f"Ingrese la defensa del {nombre}: "))
            tipo = input(f"Ingrese el tipo del {nombre} (montañoso, pantanoso, llanura): ")
            territorios[nombre] = (defensa, tipo)
    else:
        print("Opción no válida. Intente de nuevo.")
        return obtener_datos_usuario()

    return tropas, territorios, puntos_totales

def main():
    tropas, territorios, puntos_totales = obtener_datos_usuario()

    tablero = TableroRisk(tropas, territorios, puntos_totales)

    tablero.generar_combinaciones()

    tablero.generar_permutaciones()

    resultados = tablero.simular_todas_permutaciones()

    mejor_resultado = tablero.obtener_mejor_combinacion(resultados)
    print("\n==========================================")
    print("MEJOR COMBINACIÓN ENCONTRADA:")
    print("==========================================")
    combinacion = mejor_resultado['Combinacion']
    permutacion = mejor_resultado['Permutacion']
    detalles = mejor_resultado['Resultado']

    print(f"Infantería: {combinacion['Infantería']}, Caballería: {combinacion['Caballería']}, Artillería: {combinacion['Artillería']} | "
          f"Permutación: {' -> '.join(permutacion)} | "
          f"Territorios Conquistados: {detalles['Territorios Conquistados']} | Tropas Restantes: {detalles['Tropas Restantes']}")

if __name__ == "__main__":
    main()
