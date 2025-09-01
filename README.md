# Coffee Machine System

Un sistema completo de gestión de máquina de café desarrollado en Python que simula el funcionamiento de
una cafetería automatizada con múltiples tipos de bebidas, gestión de inventario y análisis de ventas.

## Descripción del Proyecto

Este proyecto implementa un sistema de máquina de café que permite:

- Preparar diferentes tipos de café: Espresso, Latte y Cappuccino en tres tamaños (pequeño, mediano, grande)
- Gestión de inventario: Control automático de ingredientes (granos, agua, leche, hielo, vasos)
- Sistema de pagos: Soporte para pagos con tarjeta y efectivo
- Panel administrativo: Análisis de ventas, reportes financieros y reabastecimiento
- Alertas automáticas: Notificaciones cuando los ingredientes están bajos
- Opción de donación: Integración de donaciones para refugio de perros

## Características Principales

### Tipos de Café Disponibles

|     Bebida    |          Tamaños         |   Precios  |
|---------------|--------------------------|------------|
| **Espresso**  | Pequeño, Mediano, Grande | $4, $5, $6 |
| **Latte**     | Pequeño, Mediano, Grande | $6, $7, $8 |
| **Cappuccino**| Pequeño, Mediano, Grande | $6, $7, $8 |

### Capacidades del Sistema

- **Granos de café**: 200g máximo
- **Agua**: 2500ml máximo
- **Leche**: 1000ml máximo
- **Hielo**: 500ml máximo
- **Vasos**: 10 unidades por tamaño
- **Límite por orden**: Máximo 3 cafés por transacción

## Instalación

### Requisitos Previos

- Python 3.6 o superior
- Sistema operativo: Windows, macOS o Linux

1. Clonar el repositorio
git clone https://github.com/D-Lemus/coffee-machine-system.git
cd coffee-machine-system

2. Verificar la instalación de Python
python --version

3. Ejecutar el programa
python main.py


## Estructura del Proyecto

```
coffee-machine-system/
├── coffeeMachine.py    # Clase principal de la máquina de café
├── coffeeShop.py       # Clase de la tienda de café (interfaz de usuario)
├── main.py            # Archivo principal para ejecutar el programa
├── README.md          # Documentación del proyecto

```

## Uso del Sistema

### Para Clientes


1. **Seleccionar bebida**
   - Escoge el número correspondiente al café deseado (1-9)
   - Indica la cantidad (máximo 3 unidades)
   - Para Latte y Cappuccino, elige temperatura (caliente/frío)

3. **Realizar pago**
   - Revisa el total de tu orden
   - Opcionalmente dona $1 al refugio de perros
   - Selecciona método de pago (tarjeta o efectivo)

### Para Administradores

**Contraseña de administrador**: 'HOFOY'

1. **Acceder al menú administrativo**
   - Selecciona la opción 10 en el menú principal
   - Ingresa la contraseña de administrador

2. **Funciones disponibles**:
   - **Analytics**: Ver reportes de reabastecimiento
   - **Finance**: Análisis de ventas y métodos de pago
   - **Show Storage**: Estado actual del inventario
   - **Fill Machine**: Reabastecer todos los ingredientes



##  Contribuir al Proyecto

Este proyecto no acepta contribuciones externas.
Este es un proyecto personal/académico y por el momento no estamos aceptando pull requests,
forks con modificaciones, ni contribuciones de código de terceros.

### ¿Qué puedes hacer?

- Usar el código para aprender y referencia
- Hacer preguntas sobre el funcionamiento


### Versión Actual (1.0)

## Autores

- **Diego Lemus** - [@D-Lemus](https://github.com/D-Lemus)
- **Karen Santana** - [@karenelizabg](https://github.com/karenelizabg)

---

⭐ **¡Si este proyecto te fue útil, considera darle una estrella en GitHub!** ⭐
