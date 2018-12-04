"""This program takes a list of locations and attempts to
   reorder their positions to find the most
   efficient route of travel.
"""

import copy
import earth_distance


def read_cities(file_name):
    """
    Takes file_name as a location of a file and converts
    the data into a tuple of four values: State, City, Latitude, Longitude,
    with types string, string, float, float
    """
    road_map = []
    text_index = 1
    for line in open(file_name, 'r'):
        location_data = line.rstrip().split('\t')  # list of the four values for each city
        for value in range(len(location_data)):
            if value > text_index:  # get lat and long which are indexed 2 and 3 in the list
                location_data[value] = float(location_data[value])
        city_tuple = tuple(location_data)
        road_map.append(city_tuple)
    return road_map


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Prints only two digits after the decimal point.
    """
    dec_points = 2
    # specific indexes of tuple values
    state = 0
    name = 1
    lat = 2
    long = 3
    for location in road_map:
        print(location[state], location[name], round(location[lat], dec_points), round(location[long], dec_points))


def compute_total_distance(road_map):
    """
    Takes road_map list and returns the total distance of all locations
    in it when traversed in a loop, e.g the distance between the final
    location and the first location in the list is included.
    """
    lat = 2
    long = 3
    distance = 0.0
    for i in range(len(road_map)):
        city_one = road_map[i]
        city_two = road_map[(i + 1) % len(road_map)]
        distance += earth_distance.distance(city_one[lat], city_one[long], city_two[lat], city_two[long])
    return distance


def swap_adjacent_cities(road_map, index):
    """
    Takes road_map and index of the current city being acted on.
    The indexed city is then swapped with the city following it
    in the circuit and this is returned in a tuple along with the
    new total distance.
    """
    new_road_map = copy.deepcopy(road_map)
    next_index = (index + 1) % len(new_road_map)

    temp_road_map = new_road_map[index]
    new_road_map[index] = new_road_map[next_index]
    new_road_map[next_index] = temp_road_map

    new_total_distance = compute_total_distance(new_road_map)
    return new_road_map, new_total_distance


def swap_cities(road_map, index1, index2):
    """
    Takes road_map and two indexes of cities to be swapped.
    The city at index1 is swapped with the city at index2
    this is returned in a tuple along with the
    new total distance.
    """
    new_road_map = copy.deepcopy(road_map)

    if index1 != index2:
        next1 = (index1 + 1) % len(new_road_map)
        next2 = (index2 + 1) % len(new_road_map)
        temp = new_road_map[next1]
        new_road_map[next1] = new_road_map[next2]
        new_road_map[next2] = temp

    new_total_distance = compute_total_distance(new_road_map)

    return new_road_map, new_total_distance


def find_best_cycle(road_map):
    """
    Takes road_map list and uses a combination of swap_cities
    and swap_adjacent_cities to find a more efficient route
    through the locations. Returns the best route found.
    """
    new_road_map = copy.deepcopy(road_map)
    current_city = 0  # index of city that is being acted on to find a better location
    use_adjacent_swap = True  # switch to alternate between swap city methods
    number_of_swaps = 0  # count to keep check of how many times each swap city method has been used
    optimum_number_swaps = 90  # number of times to perform swap_cities with best found result

    for i in range(10000):
        # next location to check to the fixed current location when using swap_cities
        next_location = ((current_city + i) + 1) % len(new_road_map)

        if use_adjacent_swap:
            temp_road_map = swap_adjacent_cities(new_road_map, i % len(new_road_map))
            # Swap_adjacent is performed for the whole map and then the method is switched to swap_cities
            if number_of_swaps >= len(road_map):
                number_of_swaps = 0
                use_adjacent_swap = False
        else:
            temp_road_map = swap_cities(new_road_map, current_city % len(new_road_map), next_location)
            # if current_city = next_location then every possible switch has been checked for that city
            if current_city == next_location:
                # decrement the current city being checked to perform the loop again
                current_city = (current_city - 1) % len(new_road_map)
                # If optimum swaps have been performed, switch to swap_adjacent method
                if number_of_swaps >= optimum_number_swaps:
                    number_of_swaps = 0
                    use_adjacent_swap = True

        # if the new map is better keep the swap
        if temp_road_map[1] < compute_total_distance(new_road_map):
            new_road_map = copy.deepcopy(temp_road_map[0])
            current_city = next_location  # keep checking that city from its new location
            number_of_swaps = 0  # reset swap count as method is still affective

        number_of_swaps += 1

    return new_road_map


def print_map(road_map):
    """
    Prints out the map in the form
    Current city -> destination (Distance)
    and the total cost of the route in miles
    """
    # indexes of tuples
    state = 0
    name = 1
    lat = 2
    long = 3
    print("")  # extra dividing line of output
    for i in range(len(road_map)):
        city_one = road_map[i]
        city_two = road_map[(i + 1) % len(road_map)]
        print(str(city_one[state]) + ", " + str(city_one[name]), end=' ')
        print("-> " + str(city_two[state]) + ", " + str(city_two[name]), end=' ')
        dist = earth_distance.distance(city_one[lat], city_one[long], city_two[lat], city_two[long])
        print("(Distance: " + str(int(dist)) + ")")
    print("\nTotal cost: " + str(int(compute_total_distance(road_map))))


def main():
    """
    Main method to read in city data, print out the cities and
    positions, try to find the best route and then print out details
    of it.
    """
    road_map = read_cities("city-data.txt")
    print_cities(road_map)
    new_road_map = find_best_cycle(road_map)
    print_map(new_road_map)


if __name__ == "__main__":
    main()
