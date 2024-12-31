## JUEGO RISK EDA II

## Descripción del Proyecto
Este programa simula un sistema de ataque optimizado para un tablero inspirado en el juego Risk. Utiliza combinaciones de tropas, permutaciones de orden de ataque, y modificadores de terreno para calcular las mejores estrategias de ataque y determinar la configuración más eficiente para conquistar territorios enemigos.

---

## Funcionalidades Principales
1. **Cálculo de combinaciones de tropas:**
   - Genera todas las posibles configuraciones de tropas dentro de un límite de puntos disponibles.
   
2. **Simulación de ataques:**
   - Simula ataques utilizando cada combinación de tropas y todas las permutaciones de orden de ataque para los territorios enemigos.
   - Evalúa el número de territorios conquistados y las tropas restantes después del ataque.

3. **Modificadores de terreno:**
   - Cada territorio tiene un tipo de terreno (montañoso, pantanoso, llanura).
   - Los modificadores ajustan la fuerza de ataque de las tropas según el tipo de terreno.

4. **Optimización:**
   - Calcula la combinación más eficiente basándose en el número de territorios conquistados y las tropas restantes.

5. **Configuración de entrada:**
   - Permite elegir entre datos predeterminados y entrada manual de datos para personalizar la simulación.

6. **Salida gradual:**
   - Imprime en consola los resultados de cada simulación de manera escalonada, con pausas breves entre cada salida.

---

## Cambios Incorporados (Bonus)
1. **Aumentar Complejidad:**
   - **Orden de ataque optimizado:** Las permutaciones de ataque ahora se generan priorizando los territorios con menor defensa.

2. **Estrategias Avanzadas:**
   - **Tipos de terreno:** Cada territorio tiene un tipo de terreno que modifica la efectividad de las tropas.
     - Infantería, caballería y artillería tienen diferentes niveles de efectividad dependiendo del terreno.

3. **Optimización Adicional:**
   - Mejora la evaluación de combinaciones para detener los ataques cuando las tropas restantes son insuficientes.

---

## Ejemplo de Salida
### Entrada Predeterminada:
- Puntos disponibles: 20
- Tropas:
  - Infantería: Fuerza = 1, Costo = 1
  - Caballería: Fuerza = 3, Costo = 3
  - Artillería: Fuerza = 5, Costo = 5
- Territorios:
  - Territorio 1: Defensa = 10, Tipo = Montañoso
  - Territorio 2: Defensa = 15, Tipo = Pantanoso
  - Territorio 3: Defensa = 12, Tipo = Llanura

### Salida:
```
Combinación: Inf: 4, Cab: 1, Art: 1 | Permutación: Territorio 1 -> Territorio 3 -> Territorio 2 | Territorios Conquistados: 2 | Tropas Restantes: 5
...(Todas las combinaciones)
==========================================
MEJOR COMBINACIÓN ENCONTRADA:
==========================================
Infantería: 5, Caballería: 1, Artillería: 0 | Permutación: Territorio 1 -> Territorio 3 -> Territorio 2 | Territorios Conquistados: 3 | Tropas Restantes: 3
```

---

## Requisitos
1. **Python 3.7+**
2. Librerías necesarias:
   - `numpy`
   - `itertools` (incluido en Python estándar)
   - `time` (incluido en Python estándar)

Instalar dependencias adicionales:
```bash
pip install numpy
```

---

## Cómo Ejecutar el Programa
1. Clonar este repositorio o descargar el archivo principal del código.
2. Asegurarse de tener los requisitos instalados.
3. Seguir las instrucciones en consola para seleccionar los datos predeterminados o ingresar datos personalizados.

---

## Notas
- El programa detiene automáticamente los ataques cuando las tropas restantes son insuficientes para continuar.
- Todas las combinaciones y permutaciones se imprimen de forma escalonada para mejorar la legibilidad.
- El calculo de los puntos de fuerza se hace considerando los terrenos.


