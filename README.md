# competitive-programming-solutions
# TCS Codificadas 2026 

Este repositorio contiene las soluciones para los problemas de la competencia de programación **TCS Codificadas 2026**. Los algoritmos están implementados en **Python 3**, enfocándose en la eficiencia temporal, el manejo de estructuras de datos avanzadas y la minimización del uso de memoria para cumplir con las restricciones estrictas de la plataforma de evaluación.

---

## 📊 Resumen de Problemas e Implementaciones

| Problema | Nombre | Enfoque / Algoritmo Principal | Complejidad |
| :---: | :--- | :--- | :---: |
| **A** | Ecosistema de Insectos | Indexación Espacial mediante Hash Maps (Diccionarios) | $\mathcal{O}(I)$ |
| **B** | Optimización de Baúles | Max-Heap (`heapq`) con Desempate Lexicográfico | $\mathcal{O}(K \log N)$ |
| **C** | Competición con Compresión | Compresión de Entropía Híbrida (`zlib`) a bajo nivel | $\mathcal{O}(N \times M)$ |
| **D** | Desembocadura | Diseño de Estructura de Árbol Mínima Simétrica | $\mathcal{O}(1)$ |
| **E** | Experimentos Seriales | Continuidad de Rangos Secuencial (Maximización de MEX) | $\mathcal{O}(N)$ |

---

## Detalles de Implementación

## Problema A: Ecosistema de Insectos
**Descripción:** Simulación eficiente de las interacciones y movimientos de una población densa de insectos en un entorno delimitado.

**Estrategia:**Se sustituyó la comparación cuadrática de elementos por un enfoque de Spatial Hashing, agrupando dinámicamente a los insectos en un diccionario por sus coordenadas (x, y). Esto redujo drásticamente el espacio de búsqueda para las interacciones biológicas, permitiendo ejecuciones directas en tiempo lineal.

### Problema B: Optimización de Baúles
* **Descripción:** Encontrar las dimensiones que maximicen la superficie total de un paralelepípedo a partir de tres listas de números, aplicando un criterio estricto de desempate lexicográfico[cite: 3].

* **Estrategia:** Uso de un **Max-Heap (`heapq`)** donde los estados se almacenan con la estructura `(-superficie, -i, -j, -k)`[cite: 3]. Al invertir el signo de los índices, Python prioriza extraer los índices reales más grandes ante superficies idénticas, dejando los menores para el final (cumpliendo la regla de que el menor lexicográfico es considerado "más chico")[cite: 3].

### Problema C: Competición con Compresión de Imágenes
* **Descripción:** Reducir al mínimo una matriz de píxeles hexadecimales en un arreglo de enteros, garantizando una reconstrucción idéntica bit por bit para evitar penalizaciones de cero puntos[cite: 2].

* **Estrategia:** Enfoque **híbrido dinámico**. El algoritmo procesa la entrada linealmente mediante buffers de bytes (`bytearray`) para mitigar picos de RAM. Evalúa el rendimiento de `zlib.compress` en su nivel máximo[cite: 2]; si la imagen es ruido complejo y el archivo se expande, conmuta automáticamente a un "Modo Plano" (marcado con `-1`) que envía los enteros de 32 bits directamente[cite: 2].

### Problema D: Desembocadura
* **Descripción:** Diseñar un árbol con la menor cantidad de nodos posible que confunda el algoritmo de Ancestros Comunes Más Cercanos (LCA) al introducir múltiples raíces válidas.

* **Estrategia:** Diseño de una **estructura mínima simétrica de solo 6 nodos** en forma de línea central ramificada. La simetría matemática del árbol provoca que los registros de confluencia evaluados generen candidatos idénticos para diferentes desembocaduras potenciales, haciendo colapsar el sistema de validación de manera inmediata.

### Problema E: Experimentos Seriales
* **Descripción:** Completar los valores `-1` en un arreglo para maximizar de forma agresiva la suma de los valores MEX de todos los subarreglos posibles.

* **Estrategia:** Estrategia de **continuidad de rangos secuencial**. El algoritmo identifica los números ausentes en el arreglo original. Al ordenarlos de menor a mayor e insertarlos consecutivamente en los espacios libres, se maximiza la densidad combinatoria local y se evita dejar "huecos" que reinicien el contador del MEX a cero, logrando un crecimiento óptimo de la función.

---

## Requisitos y Ejecución

Las soluciones fueron desarrolladas y probadas bajo el intérprete estándar de **Python 3.10+** sin dependencias externas más allá de las librerías nativas del lenguaje.

Para ejecutar cualquiera de las soluciones de forma local utilizando archivos de prueba:

```bash
python nombre_del_problema.py < input.txt   