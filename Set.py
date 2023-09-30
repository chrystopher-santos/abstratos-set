## Dupla: Chrystopher Santos e Rafael Danoski
class Set:
    def __init__(self):
        self.elements = set() # Conjunto para armazenar elementos únicos

    def insert(self, item):
        self.elements.add(item) # Adiciona o item ao conjunto

    def remove(self, item):
        try:
            self.elements.remove(item) # Remove o item do conjunto
        except KeyError:
            raise KeyError("Elemento não encontrado.")

    def contains(self, item):
        return item in self.elements # Verifica se o item está no conjunto

    def union(self, other_set):
        new_set = Set()
        new_set.elements = self.elements.union(other_set.elements) # Retorna conjunto com elementos de ambos os conjuntos
        return new_set

    def intersection(self, other_set):
        new_set = Set()
        new_set.elements = self.elements.intersection(other_set.elements) # Retorna o conjunto com elementos em comum
        return new_set

    def difference(self, other_set):
        new_set = Set()
        new_set.elements = self.elements.difference(other_set.elements) # Retorna o conjunto com elementos que não estão no outro conjunto
        return new_set

    def size(self):
        return len(self.elements) # Retorna o tamanho do conjunto

    def is_empty(self):
        return self.size() == 0 # Verifica se o conjunto está vazio

    def __str__(self):
        return "{" + ", ".join(str(item) for item in self.elements) + "}" # Retorna representação em string do conjunto

# Exemplo de uso:
set1 = Set()
set1.insert(101)
set1.insert(102)
set1.insert(103)

set2 = Set()
set2.insert(102)
set2.insert(103)
set2.insert(104)

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
print("União:", union_set)

intersection_set = set1.intersection(set2)
print("Interseção:", intersection_set)

difference_set = set1.difference(set2)
print("Diferença:", difference_set)