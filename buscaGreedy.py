import heapq

grafo = {
    'A': ['B'],
    'B': ['C', 'D', 'E'],
    'C': ['E', 'F', 'G'],
    'D': ['H', 'I'],
    'E': ['I', 'J', 'M'],
    'F': ['K', 'M'],
    'G': ['L', 'M'],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': []
}

h = {
    'A': 1, 'B': 6, 'C': 3, 'D': 7, 'E': 4,
    'F': 5, 'G': 8, 'H': 3, 'I': 2, 'J': 0,
    'K': 3, 'L': 2, 'M': 1
}


def buscaGulosa(inicio, objetivo):
    fronteira = []
    heapq.heappush(fronteira, (h[inicio], inicio)) 

    explorados = set() 
    caminho = {inicio: None}

    while fronteira:
        _, noAtual = heapq.heappop(fronteira)

        if noAtual == objetivo:
            percorrido = [] 

            while noAtual is not None:
                percorrido.append(noAtual) 
                noAtual = caminho[noAtual]
            return percorrido[::-1]
      
        explorados.add(noAtual) 
    
        for sucessor in grafo[noAtual]: 
            if sucessor not in explorados:
                heapq.heappush(fronteira, (h[sucessor], sucessor))
                caminho[sucessor] = noAtual 
            
    return None

   
percorrido = buscaGulosa('A', 'H')
print(percorrido)