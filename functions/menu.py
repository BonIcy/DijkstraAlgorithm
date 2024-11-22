from functions.dijkstra import dijkstra
from functions.simulation import simulate_traffic, restore_graph

def main_menu(graph):
    # crear una copia temporal del grafo
    temp_graph = [row[:] for row in graph]

    while True:
        print("\n--- Menú Principal ---")
        print("1. Calcular una ruta")
        print("2. Simular trancones o accidentes")
        print("3. Restaurar el grafo original")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            start_node = int(input("Ingrese el nodo de partida (1-30): ")) - 1
            end_node = int(input("Ingrese el nodo de destino (1-30): ")) - 1
            distance, path = dijkstra(temp_graph, start_node, end_node) # toma de entrada temp_graph para el calculo de la ruta maas corta
            path = [node + 1 for node in path] ## la lista devuelta por el calculo con dijkstra, la recorre y le suma 1 a los nodos para mostrar al usuario

            if distance < float('inf'):
                print(f"La distancia más corta es: {distance} segundos")
                print(f"La ruta más corta es: {path}")
            else:
                print("No hay camino entre los nodos especificados.")

        elif choice == "2":
            simulate_traffic(graph, temp_graph)

        elif choice == "3":
            restore_graph(graph, temp_graph)

        elif choice == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")