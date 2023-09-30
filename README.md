# Justificativa

A escolha da estrutura de dados,foi um dicionário para armazenar os elementos únicos de um conjunto.

# Operações
## Insert

Responsável por inserir um elemento no dicionário de forma rápida e sem permitir duplicatas.

|                                      | Complexidade |
|--------------------------------------|--------------|
| **Complexidade De Tempo Caso Médio** |    $O(1)$    |  
| **Complexidade De Espaço**           |    $O(n)$    |

**Complexidade De Tempo Caso Médio** - Normalmente é uma operação de tempo constante O(1), em casos raros, pode haver colisões, mas a probabilidade é baixa.

**Complexidade De Espaço**  - É o número de elementos no conjunto, já que estamos armazenando cada elemento em um dicionário.

## Remove

Responsável por remover um elemento de um dicionário também, desde que o elemento exista no conjunto.

|                                      | Complexidade |
|--------------------------------------|--------------|
| **Complexidade De Tempo Caso Médio** |    $O(1)$    |
| **Complexidade De Espaço**           |    $O(n)$    | 

**Complexidade De Tempo Caso Médio** - Mesma justificativa do INSERT, em raros casos de colisões, pode ser necessário tratar a colisão, o que pode aumentar o tempo de execução.

**Complexidade De Espaço**  - Não afeta a complexidade de espaço, pois apenas remove um elemento existente.

## Contains

Responsavel por verificar se o elemento existe no dicionário eficiante é uma operação apropriada para o conjunto.

|                                      | Complexidade |
|--------------------------------------|--------------|
| **Complexidade De Tempo Caso Médio** |    $O(1)$    |  
| **Complexidade De Espaço**           |    $O(n)$    |

**Complexidade De Tempo Caso Médio**  - A consulta em um dicionário é uma operação de tempo constante (O(1)), em média.

**Complexidade De Espaço**  - Não afeta a complexidade de espaço, pois apenas verifica a existência do elemento.

## União (union), Interseção (intersection) e Diferença (difference)

**Complexidade De Tempo Caso Médio**

Para a UNIÃO e a INTERSEÇÃO, a complexidade de Tempo  é O(n), onde n é o número de elementos no conjunto maior. Para a DIFERENÇA, também é O(n), porque no pior caso, precisa verificar a existência de cada elemento em ambos os conjuntos.

**Complexidade De Espaço** 
As operações não afetam a complexidade de espaço, pois criam um novo conjunto resultante, mantendo os conjuntos originais inalterados.