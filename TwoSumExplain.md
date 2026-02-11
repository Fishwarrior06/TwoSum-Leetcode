# Solucion de Two Sum de Leetcode

## PROBLEMA
Como problema nos dan un array de nuemeros enteros llamado ´´´[nums]´´´ y un numero entero que sera nuestro ´´´[Target]´´´, que combinaods regresan un indice de 2 numeros que sumados den ´´´[Target]´´´

Te tienes que asegurar que cada input tenga exactamente una solucion y no puedes utilizar el mismo elemento 2 veces o mas.
En este caso puedes dar la respuesta en cualquier orden.

**Constrains:**
´´´
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
´´´
**Solo una repsuesta valida existe.**

## OBJETIVO
Puedes crear un algoritmo que lo responda en menos de una complejidad de tiempo de ´´´0(n^2)´´´

## RESPUESTA
En este caso primero se importa **List** desde la libreria **typing** para poder crear los arrays

Definimos la clase **Solucion**. (La clase es solo un modulo al cual llamaremos cada que queremos hacer esta accion)
Definimos los atributos de la clase (En este caso lo que nesecitamos que tenga esta clase o modulo para que funcione)

En este caso los **Atributos** de la clase son:
´´´self´´´, ´´´nums: List[int]´´´, ´´´target: int´´´ y todo esto pasa a ser una **Lista** con numeros enteros (#List[int])

Definimos ´´´Seen{}´´´ como la check por donde pasaran los numeros para verificar cual es.

