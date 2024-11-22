import heapq ##heapq implementa una cola de prioridad (min-heap), para obtener de manera eficiente el nodo con la menor distancia ACUMULADA durante la ejecución del algoritmo de Dijkstra

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n ##va guardando las distancias mas cortas, se inicia con infinito porque se desconoce la distania de los demas nodos
    distances[start] = 0 ## se inicia en 0 porque es la inicial
    priority_queue = [(0, start)] ## almaenamiento de los nodos que deben ser visitados, inicia con el nodo de inicio
    previous_nodes = [-1] * n ## mantiene el nodo anterior para ir reconstruyendo el camino, se inicia con -1 porque aun no hay nodos previos asignados
    
    ## cuando haya nodos almacenados en la lista priority_queue
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) ##la función heapq.heappop extrae el nodo con la menor distancia acumulada que haya en priority_queque, eliminando ese elemento y devolviendolo

        if current_node == end:
            break

        for neighbor, seconds in enumerate(graph[current_node]): ## para cada vecino del nodo actual (current_node), se obtiene el valor de la arista de la matriz de adyacencia (en nuestro caso los segundos), graph[current_node] obtiene la lista de vecinos o conecciones que tiene el nodo actual
            if seconds > 0:
                distance = current_distance + seconds
                if distance < distances[neighbor]: ## si esta nueva distancia es menor que la distancia previamente conocida para el vecino (distances[neighbor]), se actualizan los valores
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node ## se asigna el nodo actual como el nodo previo del vecino
                    heapq.heappush(priority_queue, (distance, neighbor)) ## se pushea el vecino con con su nueva distancia a la cola de prioridad
## reconstruccion del camino siguiendo los nodos previos almacenados (previous_nodes)
    path = []
    current = end
    while current != -1: ## el -1 es un marcador especial que se utiliza para indicar que has llegado a un nodo que no tenga nada previo
        path.append(current)
        current = previous_nodes[current] 
    path.reverse()

    return distances[end], path