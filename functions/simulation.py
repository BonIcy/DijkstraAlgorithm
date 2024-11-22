def simulate_traffic(graph, temp_graph): ## de parametros tiene el grafo original y la copia con la que trabajaremos las simulaciones
    print("\nSimular trancones o accidentes:")
    node1 = int(input("Ingrese el nodo de origen del tramo afectado (1-30): ")) - 1
    node2 = int(input("Ingrese el nodo de destino del tramo afectado (1-30): ")) - 1
    new_seconds = int(input("Ingrese el nuevo valor en segundos del tramo: "))

    # validacion de la existencia del tramo en el grafo
    if 0 <= node1 < len(temp_graph) and 0 <= node2 < len(temp_graph) and temp_graph[node1][node2] > 0: ## se verifican 2 cosas; primero que node1 y node2 estén dentro del rango de índices válidos de la matriz temp_graph (es decir, que existan nodos en el grafo), y tambien que haya un camino entre los nodos
        temp_graph[node1][node2] = new_seconds 
        print(f"El tramo entre {node1 + 1} y {node2 + 1} ha sido modificado temporalmente a {new_seconds}.")
    else:
        print("El tramo especificado no existe en el grafo o es inválido.")

    # mostrar la matriz temporal para verificar los cambios
    print("Estado actual del grafo temporal:")
    for row in temp_graph:
        print(row)


def restore_graph(original_graph, temp_graph):
    # restaurar el grafo temporal a su estado original
    for i in range(len(original_graph)): ## se recorre cada fila y columna del grafo original y se copia al temporal
        for j in range(len(original_graph[i])):
            temp_graph[i][j] = original_graph[i][j]
    print("El grafo ha sido restaurado a su estado original.")

    # imprimir matriz restaurada
    print("Estado del grafo restaurado:")
    for row in temp_graph:
        print(row)
