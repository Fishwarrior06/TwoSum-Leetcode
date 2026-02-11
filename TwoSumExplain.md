x# Solucion de Two Sum de Leetcode

## PROBLEMA
Como problema nos dan un array de nuemeros enteros llamado ```[nums]``` y un numero entero que sera nuestro ```[Target]```, que combinaods regresan un indice de 2 numeros que sumados den ```[Target]```

Te tienes que asegurar que cada input tenga exactamente una solucion y no puedes utilizar el mismo elemento 2 veces o mas.
En este caso puedes dar la respuesta en cualquier orden.

**Constrains:**

- **2 <= nums.length <= 10^4**
- **-10^9 <= nums[i] <= 10^9**
- **-10^9 <= target <= 10^9**

**Solo una repsuesta valida existe.**

## OBJETIVO
Puedes crear un algoritmo que lo responda en menos de una complejidad de tiempo de ```0(n^2)```

## RESPUESTA
En este caso primero se importa **List** desde la libreria **typing** para poder crear los arrays

Definimos la clase **Solucion**. (La clase es solo un modulo al cual llamaremos cada que queremos hacer esta accion)
Definimos los atributos de la clase (En este caso lo que nesecitamos que tenga esta clase o modulo para que funcione)

En este caso los **Atributos** de la clase son:
```self```, ```nums: List[int]```, ```target: int``` y todo esto pasa a ser una **Lista** con numeros enteros ```(#List[int])```

Definimos ```Seen{}``` como la check por donde pasaran los numeros para verificar cual ya pasaron.

Por cada ```index(i)``` **enumera** numeros dentro de ```nums```.

Definimos ```complement``` como la funcion que nos permitira restar el ```target``` menos (-) ```num```.

Si hay ```complement```. (osea un ```target``` - ```num```)
Entonces regresa si ya fue visto el complemento y su index (i)

Si ya vio el numero (```seen[num]```) te regresara el index (i) en el que se encuentran los numeros ya sumados que juntos dan a la respuesta del problema

En este caso se utilizan los **numeros** [3, 2, 4] y como **target** 6

Imprimimos la clase con su metodo y atributos que en este caso serian:
```print(Solution().twoSum(nums, target))```

En este caso agarra el primer numero y hace 6 - 3 y da como resultados 3 y lo guarda en ```seen``` junto con su ```index(i)```, luego hace 6 - 2 y da como resultado 4 y hace lo mismo, luego por ultimo hace 6 - 4 y da como resultado 2 y hace lo mismo.

Entonces guarda los resultados de la siguiente manera ```{3:0, 2:1, 4:2}```

Aqui ya damos con que 2 si esta en ```seen``` en la 3ra iteracion.
Entonces tenemos que
```
nums[1] = 2
nums[2] = 4
2 + 4 = 6
```

## Conclusion:
En este caso la solucion es O(n) ya que es un hashmap que recuerda que fue lo que ya vio y es mejor para saltos directos, inputs grandes y lo mejor es que es escala. Es decir que tiene acceso directo en tiempo constante.

A diferencia de el otro script que viene en el repositorio que hace brute force y es de complejidad de O(n^2) la cual dura mas tiempo