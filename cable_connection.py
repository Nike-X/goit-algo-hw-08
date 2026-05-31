# In this script, we use heap to connect cables of different lengths
# in pairs, until all cables are connected

import heapq

def connect_cables(cable_set: list):
    # Initialize total cost and connection order
    total_cost = 0
    connection_order = []
    
    # Heapify a copy of the cable list to keep the original list unchanged
    heap_of_cables = cable_set.copy()
    heapq.heapify(heap_of_cables)

    # Loop until we connect all cables in one
    while len(heap_of_cables) > 1:
        # Get the shortest cable from heap
        first_cable = heapq.heappop(heap_of_cables)

        # Get the shortest element from the heap again
        second_cable = heapq.heappop(heap_of_cables)

        # Connect the cables (and calculate length of connected cable)
        connected_cable = first_cable + second_cable

        # Add connection cost to total cost
        total_cost = total_cost + connected_cable

        # Record connected pair to the connection order list
        connection_order.append((first_cable, second_cable, connected_cable))

        # Return connected cable to the heap
        heapq.heappush(heap_of_cables, connected_cable)

    return total_cost, connection_order

# Defines original cable set, calculates connection order and cost, \
# and prints results
def main():
    # Define original cable set
    cable_set = [10, 3, 7, 2, 14, 5, 9, 6]

    # Calculate total length of connected cables (for clarity)
    final_length = sum(cable_set)

    # Calculate connection order and minimum total connection cost
    total_cost, connection_order = connect_cables(cable_set)

    # Print results
    print(f"Original cable set: {cable_set}\n")

    print("Connection order:\n")
    
    for first_cable, second_cable, connected_cable in connection_order:
        print(f"{first_cable} + {second_cable} = {connected_cable}")
    
    print(f"\nFinal cable length: {final_length}")
    
    print(f"\nMinimum total connection cost: {total_cost}")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()