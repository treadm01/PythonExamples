from cities import *

def testCompute_total_distance():
    test_road_map = []
    a_tuple = ("State A", "City A", 0.0, 0.0)
    b_tuple = ("State B", "City B", 10.0, 10.0)
    expected = (earth_distance.distance(0.0, 0.0, 10.0, 10.0)
     + earth_distance.distance(10.0, 10.0, 0.0, 0.0))
    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)
    assert (expected == compute_total_distance(test_road_map))

    test_road_map.clear()
    x_tuple = ("State A", "City A", 0.0, 0.0)
    y_tuple = ("State B", "City B", 0.0, 0.0)
    expected = 0.0
    test_road_map.append(x_tuple)
    test_road_map.append(y_tuple)
    assert (expected == compute_total_distance(test_road_map))

    test_road_map.clear()
    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)
    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)
    expected = earth_distance.distance(a_tuple[2], a_tuple[3], b_tuple[2], b_tuple[3])
    expected += earth_distance.distance(b_tuple[2], b_tuple[3], a_tuple[2], a_tuple[3])
    expected += earth_distance.distance(a_tuple[2], a_tuple[3], b_tuple[2], b_tuple[3])
    expected += earth_distance.distance(b_tuple[2], b_tuple[3], a_tuple[2], a_tuple[3])
    assert (expected == compute_total_distance(test_road_map))

    test_road_map.clear()

    a_tuple = ("State A", "City A", 3.0, 1.0)
    b_tuple = ("State B", "City B", 1.0, 1.0)
    x_tuple = ("State X", "City X", 4.0, 3.0)
    y_tuple = ("State Y", "City Y", 9.0, 4.5)

    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)
    test_road_map.append(x_tuple)
    test_road_map.append(y_tuple)

    expected = earth_distance.distance(a_tuple[2], a_tuple[3], b_tuple[2], b_tuple[3])
    expected += earth_distance.distance(b_tuple[2], b_tuple[3], x_tuple[2], x_tuple[3])
    expected += earth_distance.distance(x_tuple[2], x_tuple[3], y_tuple[2], y_tuple[3])
    expected += earth_distance.distance(y_tuple[2], y_tuple[3], a_tuple[2], a_tuple[3])

    assert (expected == compute_total_distance(test_road_map))

    test_road_map.clear()

    a_tuple = ("State A", "City A", 32.361538, 86.279118)
    b_tuple = ("State B", "City B", 58.301935, 134.41974)

    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)

    #expected values from calculator
    expected = 2854 * 2

    epsilon = expected * 0.01

    assert abs(expected - compute_total_distance(test_road_map)) < epsilon

    test_road_map.clear()

    a_tuple = ("State A", "City A", 32.361538, 86.279118)
    b_tuple = ("State B", "City B", 58.301935, 134.41974)
    x_tuple = ("State X", "City X", 33.448457, -112.073844)
    y_tuple = ("State Y", "City Y", 34.736009, -92.331122)

    test_road_map.append(a_tuple)
    test_road_map.append(b_tuple)
    test_road_map.append(x_tuple)
    test_road_map.append(y_tuple)

    # expected values from calculator
    expected = 2854
    expected += 5036
    expected += 1135
    expected += 7798.2085

    epsilon = expected * 0.001

    assert abs(expected - compute_total_distance(test_road_map)) < epsilon


def testSwap_adjacent_cities():
    test_road_map_A = []
    test_road_map_B = []
    a_tuple = ("State A", "City A", 42.2352, -71.0275)
    b_tuple = ("State B", "City B", 42.7335, -84.5467)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_B.append(b_tuple)
    test_road_map_B.append(a_tuple)
    expected = (test_road_map_B, compute_total_distance(test_road_map_B))
    assert (expected == swap_adjacent_cities(test_road_map_A, 0))
    
    
    test_road_map_A.clear()
    test_road_map_B.clear()
    x_tuple = ("State X", "City X", 38.197274, -84.86311)
    y_tuple = ("State Y", "City Y", 38.572954, -92.189283)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_A.append(x_tuple)
    test_road_map_A.append(y_tuple)
    test_road_map_B.append(a_tuple)
    test_road_map_B.append(x_tuple)
    test_road_map_B.append(b_tuple)
    test_road_map_B.append(y_tuple)
    expected = (test_road_map_B, compute_total_distance(test_road_map_B))
    assert (expected == swap_adjacent_cities(test_road_map_A, 1))
    
    
    test_road_map_A.clear()
    test_road_map_B.clear()
    a_tuple = ("State A", "City A", 0, 0)
    b_tuple = ("State B", "City B", 1, 1)
    x_tuple = ("State X", "City X", 1, -1)
    y_tuple = ("State Y", "City Y", 8, 0)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_A.append(x_tuple)
    test_road_map_A.append(y_tuple)
    expected = compute_total_distance(test_road_map_A)
    assert (expected > swap_adjacent_cities(test_road_map_A, 2)[1])
    
    assert (swap_adjacent_cities(test_road_map_A, 3)[0][0] == y_tuple)
    assert (swap_adjacent_cities(test_road_map_A, 3)[0][3] == a_tuple)
    
def testSwap_cities():
    test_road_map_A = []
    test_road_map_B = []
    a_tuple = ("State A", "City A", 42.2352, -71.0275)
    b_tuple = ("State B", "City B", 42.7335, -84.5467)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_B.append(b_tuple)
    test_road_map_B.append(a_tuple)
    expected = (test_road_map_B, compute_total_distance(test_road_map_B))
    assert (expected == swap_cities(test_road_map_A, 0, 1))
    assert (expected == swap_cities(test_road_map_A, 1, 0))
    assert (expected == swap_cities(test_road_map_B, 1, 1))
    
def testFind_best_cycle():
    test_road_map_A = []
    a_tuple = ("State A", "City A", 0, 0)
    b_tuple = ("State B", "City B", 1, 1)
    x_tuple = ("State X", "City X", 1, -1)
    y_tuple = ("State Y", "City Y", 8, 0)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_A.append(x_tuple)
    test_road_map_A.append(y_tuple)
    expected = compute_total_distance(test_road_map_A)
    answer = find_best_cycle(test_road_map_A)
    assert (expected > compute_total_distance(answer))

    test_road_map_A.clear()
    a_tuple = ("State A", "City A", 0, 0)
    b_tuple = ("State B", "City B", 0, 0)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    expected = compute_total_distance(test_road_map_A)
    answer = find_best_cycle(test_road_map_A)
    assert (expected == compute_total_distance(answer))

    test_road_map_A.clear()
    a_tuple = ("State A", "City A", 42.2352, -71.0275)
    b_tuple = ("State B", "City B", 42.7335, -84.5467)
    x_tuple = ("State X", "City X", 38.197274, -84.86311)
    y_tuple = ("State Y", "City Y", 38.572954, -92.189283)

    test_road_map_A.append(a_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_A.append(x_tuple)
    test_road_map_A.append(y_tuple)
    expected = compute_total_distance(test_road_map_A)
    answer = find_best_cycle(test_road_map_A)
    assert (expected > compute_total_distance(answer))

    test_road_map_A.clear()
    test_road_map_A.append(a_tuple)
    expected = compute_total_distance(test_road_map_A)
    answer = find_best_cycle(test_road_map_A)
    assert (expected == compute_total_distance(answer))
    # 1.414214, 2.828427, 2.236068, 2.236068, 2

    test_road_map_A.clear()
    a_tuple = ("State A", "City A", 0.0, 0.0)
    b_tuple = ("State B", "City B", -1.0, 1.0)
    x_tuple = ("State X", "City X", 1.0, 3.0)
    y_tuple = ("State Y", "City Y", 3.0, 2.0)
    z_tuple = ("State Z", "City Z", 2.0, 0.0)
    test_road_map_A.append(a_tuple)
    test_road_map_A.append(y_tuple)
    test_road_map_A.append(b_tuple)
    test_road_map_A.append(z_tuple)
    test_road_map_A.append(x_tuple)

    test_road_map_B = []
    test_road_map_B.append(a_tuple)
    test_road_map_B.append(z_tuple)
    test_road_map_B.append(y_tuple)
    test_road_map_B.append(x_tuple)
    test_road_map_B.append(b_tuple)

    expected = compute_total_distance(test_road_map_B)
    answer = find_best_cycle(test_road_map_A)

    assert(expected == compute_total_distance(answer))