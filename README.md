# 🚀 Simulador Interactivo de Campos Vectoriales – Cálculo 2

Este proyecto es un videojuego interactivo desarrollado con **Python y Pygame** que simula el movimiento de una nave espacial bajo la influencia de **campos vectoriales**. Fue desarrollado como trabajo final para la materia **Cálculo 2**.

---

## 🎯 Objetivo del Proyecto

Demostrar de forma visual e interactiva cómo los campos vectoriales afectan el movimiento de un cuerpo en el espacio bidimensional, usando el ejemplo de una nave que debe esquivar asteroides mientras es atraída o girada por un campo vectorial.

---

## 🕹️ Funcionalidad

- Control total de la nave con teclado:
  - `↑` Acelera en la dirección actual.
  - `←` y `→` Giran la nave.
- Cambiar el campo vectorial aplicado:
  - `ESPACIO`: Campo **circular**.
  - `TAB`: Campo **radial** (hacia el centro).
- Colisión con asteroides:
  - Genera una explosión visual con partículas.
  - Reinicia la nave después de 2 segundos.
- Visualización del campo vectorial con flechas en pantalla.

---

## 🔬 Relación con Cálculo 2

Este juego es una representación práctica de conceptos fundamentales de cálculo vectorial, como:

- **Campos vectoriales bidimensionales**.
- Aplicación de fuerzas mediante funciones vectoriales:  
  - Campo circular:  **F(x, y) = (y, -x)**
  - Campo radial: **F(x, y) = (x - cx, y - cy)**
- Movimiento influenciado por fuerzas simuladas usando la fórmula `F = ma`.

---

## 📁 Estructura del Proyecto
