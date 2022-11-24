graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : ['1'],
    '4' : ['8'],
    '8' : [],
    '1' : ['2','7']
}

visited = [] # List for visited nodes. Lista de nodos visitados
queue = []     #Initialize a queue  Inicializando la cola

def bfs(visited, graph, node): #function for BFS Funcion para el BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node  Creando ciclo para visitar cada nodo
        m = queue.pop(0) 
        print (m, end = " ") 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling