# -*- coding: utf-8 -*-
"""
Simulations for tuning parameters of the boardgame Donjons-et-Barons
"""

import copy
import math
import random
import statistics

    
print()
print("prepare data: ...")

hexagon_count = 37

hexagon_names = set([ hexagon_index + 1 for hexagon_index in range(hexagon_count)])

hexagon_adjacents = {}

hexagon_adjacents[1] = set(map(int, "2 5 6".split()))
hexagon_adjacents[2] = set(map(int, "1 3 6 7".split()))
hexagon_adjacents[3] = set(map(int, "2 4 7 8".split()))
hexagon_adjacents[4] = set(map(int, "3 8 9".split()))

hexagon_adjacents[5] = set(map(int, "1 6 10 11".split()))
hexagon_adjacents[6] = set(map(int, "1 2 5 7 11 12".split()))
hexagon_adjacents[7] = set(map(int, "2 3 6 8 12 13".split()))
hexagon_adjacents[8] = set(map(int, "3 4 7 9 13 14".split()))
hexagon_adjacents[9] = set(map(int, "4 8 14 15".split()))

hexagon_adjacents[10] = set(map(int, "5 11 16 17".split()))
hexagon_adjacents[11] = set(map(int, "5 6 10 12 17 18".split()))
hexagon_adjacents[12] = set(map(int, "6 7 11 13 18 19".split()))
hexagon_adjacents[13] = set(map(int, "7 8 12 14 19 20".split()))
hexagon_adjacents[14] = set(map(int, "8 9 13 15 20 21".split()))
hexagon_adjacents[15] = set(map(int, "9 14 21 22".split()))

hexagon_adjacents[16] = set(map(int, "10 17 23".split()))
hexagon_adjacents[17] = set(map(int, "10 11 16 18 23 24".split()))
hexagon_adjacents[18] = set(map(int, "11 12 17 19 24 25".split()))
hexagon_adjacents[19] = set(map(int, "12 13 18 20 25 26".split()))
hexagon_adjacents[20] = set(map(int, "13 14 19 21 26 27".split()))
hexagon_adjacents[21] = set(map(int, "14 15 20 22 27 28".split()))
hexagon_adjacents[22] = set(map(int, "15 21 28".split()))

hexagon_adjacents[23] = set(map(int, "16 17 24 29".split()))
hexagon_adjacents[24] = set(map(int, "17 18 23 25 29 30".split()))
hexagon_adjacents[25] = set(map(int, "18 19 24 26 30 31".split()))
hexagon_adjacents[26] = set(map(int, "19 20 25 27 31 32".split()))
hexagon_adjacents[27] = set(map(int, "20 21 26 28 32 33".split()))
hexagon_adjacents[28] = set(map(int, "21 22 27 33".split()))

hexagon_adjacents[29] = set(map(int, "23 24 30 34".split()))
hexagon_adjacents[30] = set(map(int, "24 25 29 31 34 35".split()))
hexagon_adjacents[31] = set(map(int, "25 26 30 32 35 36".split()))
hexagon_adjacents[32] = set(map(int, "26 27 31 33 36 37".split()))
hexagon_adjacents[33] = set(map(int, "27 28 32 37".split()))

hexagon_adjacents[34] = set(map(int, "29 30 35".split()))
hexagon_adjacents[35] = set(map(int, "30 31 34 36".split()))
hexagon_adjacents[36] = set(map(int, "31 32 35 37".split()))
hexagon_adjacents[37] = set(map(int, "32 33 36".split()))

assert set(hexagon_adjacents.keys()) == hexagon_names

for (name1, adjacents1) in hexagon_adjacents.items():
    assert name1 not in adjacents1
    for name2 in adjacents1:
        assert name2 in hexagon_names
        assert name1 in hexagon_adjacents[name2]
        
print()
print(f"hexagon_names = {hexagon_names}")

print()
print(f"hexagon_adjacents = {hexagon_adjacents}")
    
print()
print("prepare data: done")


def compute_distance_occurrences(adjacents):
    
    adjacents_dict = compute_distances(adjacents)
                       
    distances = []
    points = adjacents.keys()
    for x in points:
        for y in points:
            if x > y:
                distances.append(adjacents_dict[(x, y)])
                
    return distances



def compute_distances(adjacents):
    
    # partition = compute_connex_partition(adjacents)
    # assert len(partition) == 1
    
    points = adjacents.keys()

    adjacents_dict = {}
    
    for x in points:
        for y in points:
            adjacents_dict[(x, y)] = None
    
    for x in points:
        adjacents_dict[(x, x)] = 0

    for x in points:
        for y in adjacents[x]:
            adjacents_dict[(x, y)] = 1
            adjacents_dict[(y, x)] = 1
            
    has_new_dxy = True
    while has_new_dxy:
        has_new_dxy = False
        for x in points:
            for y in points:
                if x > y:
                    if adjacents_dict[(x, y)] is None:
                        has_new_dxy = True
                        for z in points:
                            if z != x and z != y and adjacents_dict[(x, z)] is not None and adjacents_dict[(z, y)] is not None:
                                dxy = adjacents_dict[(x, z)] + adjacents_dict[(z, y)]
                                adjacents_dict[(x, y)] = dxy
                                adjacents_dict[(y, x)] = dxy
                                break
            
    has_new_dxy = True
    while has_new_dxy:
        has_new_dxy = False
        for x in points:
            for y in points:
                if x > y:
                    dxy = adjacents_dict[(x, y)]
                    for z in points:
                        if z != x and z != y:
                            new_dxy = adjacents_dict[(x, z)] + adjacents_dict[(z, y)]
                            if new_dxy < dxy:
                                has_new_dxy = True
                                dxy = new_dxy
                    adjacents_dict[(x, y)] = dxy
                    adjacents_dict[(y, x)] = dxy
                        
    return adjacents_dict


def compute_connex_partition(adjacents):
    partition = list()
    
    points = list(adjacents.keys())
    points.sort()
    
    minimal_points = {}
    for x in points:
        minimal_points[x] = min([x] + list(adjacents[x]))
        
    new_min_found = True
    while new_min_found: 
        new_min_found = False
        
        for x in points:
            min_x = minimal_points[x]
            
            new_min_x_found = False
            
            for y in adjacents[x]:
                if minimal_points[y] < min_x:
                    new_min_x_found = True
                    min_x = minimal_points[y]
                    
            if new_min_x_found:
                new_min_found = True
                minimal_points[x] = min_x
                for y in adjacents[x]:
                    minimal_points[y] = min_x               

    class_dict = {x:set() for x in minimal_points.values()}
    for x in points:
        class_dict[minimal_points[x]].add(x)
        
    for class_set in class_dict.values():
        if len(class_set) != 0:
            class_list = list(class_set)
            class_list.sort(key=int)
            partition.append(class_list)
    
    return partition
       

def make_statistics_on_donjon_count(mountain_count=0):
    
    print()
    print("make_statistics_on_donjon_count: ...")

    test_count = 100_000
    
    donjon_count_sample = []
    
    modulo_list = [2, 3, 4]
    donjon_count_modulo_sample = {modulo:[] for modulo in modulo_list}
    
    min_donjon_set = None
    max_donjon_set = None
    ten_donjon_set = None

    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        donjon_set = set()

        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        while len(free_set) != 0:
            name = random.choice(list(free_set))
            donjon_set.add(name)
            free_set.remove(name)
            free_set = free_set - hexagon_adjacents[name]
            
        donjon_count_sample.append(len(donjon_set))
        
        for modulo in modulo_list:
            donjon_count_modulo_sample[modulo].append(len(donjon_set) % modulo)
            
        if min_donjon_set is None:
            min_donjon_set = copy.copy(donjon_set)
            
        if max_donjon_set is None:
            max_donjon_set = copy.copy(donjon_set)
            
        if len(donjon_set) < len(min_donjon_set):
            min_donjon_set = copy.copy(donjon_set)
            
        if len(donjon_set) > len(max_donjon_set):
            max_donjon_set = copy.copy(donjon_set)
        
        if len(donjon_set) == 10 and ten_donjon_set is None:
            ten_donjon_set = copy.copy(donjon_set)
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"    count = {len(donjon_count_sample)}")
    print(f"     mode = {statistics.mode(donjon_count_sample)}")
    print(f"     mean = {statistics.mean(donjon_count_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(donjon_count_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(donjon_count_sample, n=10)}")
    print(f"      min = {min(donjon_count_sample)} ; donjons = {sorted(min_donjon_set)}")
    print(f"      max = {max(donjon_count_sample)} ; donjons = {sorted(max_donjon_set)}")
    print(f"       10 = donjons = {sorted(ten_donjon_set)}")
        
    for modulo in modulo_list:
        print()
        print(f"--- mountain_count: {mountain_count} ; modulo = {modulo} ---")
        for value in range(modulo):
            frequence = donjon_count_modulo_sample[modulo].count(value)/len(donjon_count_modulo_sample[modulo])
            print(f" frequence {value} = {frequence*100:.0f} %")
            
        

    print()
    print("make_statistics_on_donjon_count: done")

           

def make_statistics_on_points(mountain_count=0, player_count=2, test_count=100_000, ranking=False):
    
    print()
    print("make_statistics_on_points: ...")
    
    if False:
        # Zipf law with 1.5 exponent
        point_system = {}
        point_system["lande"]       = (1, 20)
        point_system["promomtoire"] = (2, 8)
        point_system["forêt"]       = (3, 4)
        point_system["prairie"]     = (4, 3)
        point_system["mine"]        = (5, 2)

    if False:
        # Fibonacci starting with 2 and 4
        point_system = {}
        point_system["lande"]       = (1, 15)
        point_system["promomtoire"] = (2, 10)
        point_system["forêt"]       = (3, 6)
        point_system["prairie"]     = (4, 4)
        point_system["mine"]        = (5, 2)

    if False:
        # With available material
        point_system = {}
        point_system["lande"]       = (1, 15)
        point_system["promomtoire"] = (2, 10)
        point_system["forêt"]       = (3, 6)
        point_system["prairie"]     = (4, 4)
        point_system["mine"]        = (5, 2)

    if False:
        # Just donjon counting
        point_system = {}
        point_system["donjon"]       = (1, 37)

    if False:
        # Two flavors
        point_system = {}
        point_system["poor"]       = (1, 30)
        point_system["rich"]       = (2, 7)

    if False:
        # Three flavors
        point_system = {}
        point_system["r1"]       = (1, 27)
        point_system["r2"]       = (2, 7)
        point_system["r3"]       = (3, 3)

    if False:
        # Four flavors
        point_system = {}
        point_system["r1"]       = (1, 26)
        point_system["r2"]       = (2, 6)
        point_system["r3"]       = (3, 3)
        point_system["r4"]       = (4, 2)

    if True:
        # Four almost equal flavors
        point_system = {}
        point_system["r1"]       = (1, 9)
        point_system["r2"]       = (2, 9)
        point_system["r3"]       = (3, 9)
        point_system["r4"]       = (4, 10)
    
    total_occurences = 0
    points_list = []
    for (key, (points, occurences)) in point_system.items():
        print(f"{key}: #{occurences} times {points} points")
        total_occurences += occurences
        points_list += [points for _ in range(occurences)]
        
    assert total_occurences == len(hexagon_names)
    assert len(points_list) == len(hexagon_names)
    print()
    print(f"total points = {sum(points_list)}")
    print(f"mean points = {statistics.mean(points_list)}")

    
    points_sample = []
    player_points_sample = {player_index:[] for player_index in range(player_count)}

    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        donjon_set = set()

        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        random.shuffle(points_list)
        points_map = {}
        for (name_index, name) in enumerate(sorted(list(hexagon_names))):
            points_map[name] = points_list[name_index]
        
        player_points = [0 for player_index in range(player_count)]

        points = 0
        player_index = 0
        while len(free_set) != 0:
            name = random.choice(list(free_set))
            donjon_set.add(name)
            free_set.remove(name)
            free_set = free_set - hexagon_adjacents[name]
            
            points += points_map[name]
            player_points[player_index] += points_map[name]
            player_index = (player_index + 1) % player_count
            
        points_sample.append(points)
        if ranking:
            player_points.sort(reverse=True)
            
        for player_index in range(player_count):
            player_points_sample[player_index].append(player_points[player_index])
            

    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print()
    print(f"    count = {len(points_sample)}")
    print(f"     mode = {statistics.mode(points_sample)}")
    print(f"     mean = {statistics.mean(points_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(points_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(points_sample, n=10)}")
    print(f"      min = {min(points_sample)}")
    print(f"      max = {max(points_sample)}")
    print()
    
    
    print()
    print(f"--- points sorted by rank at each test ? : {ranking} ---")
    print()
    for player_index in range(player_count):
        print(f"player {player_index}     count = {len(player_points_sample[player_index])}")
        print(f"player {player_index}      mode = {statistics.mode(player_points_sample[player_index])}")
        print(f"player {player_index}      mean = {statistics.mean(player_points_sample[player_index]):.1f}")
        print(f"player {player_index} quartiles = {statistics.quantiles(player_points_sample[player_index], n=4)}")
        print(f"player {player_index}   deciles = {statistics.quantiles(player_points_sample[player_index], n=10)}")
        print(f"player {player_index}       min = {min(player_points_sample[player_index])}")
        print(f"player {player_index}       max = {max(player_points_sample[player_index])}")
        print()
       

    print()
    print("make_statistics_on_points: done")

           
def make_statistics_on_points_by_moving(mountain_count=0, player_count=2, test_count=100_000, ranking=False):
    
    print()
    print("make_statistics_on_points_by_moving: ...")

    if True:
        # Four almost equal flavors
        point_system = {}
        point_system["r1"]       = (1, 9)
        point_system["r2"]       = (2, 9)
        point_system["r3"]       = (3, 9)
        point_system["r4"]       = (4, 10)
    
    total_occurences = 0
    points_list = []
    for (key, (points, occurences)) in point_system.items():
        print(f"{key}: #{occurences} times {points} points")
        total_occurences += occurences
        points_list += [points for _ in range(occurences)]
        
    assert total_occurences == len(hexagon_names)
    assert len(points_list) == len(hexagon_names)
    print()
    print(f"total points = {sum(points_list)}")
    print(f"mean points = {statistics.mean(points_list)}")

    
    points_sample = []
    donjon_count_sample = []
    round_sample = []
    turn_sample = []
    player_points_sample = {player_index:[] for player_index in range(player_count)}

    debug_index = 0
    debug_count = 3
    
    for test_index in range(test_count):
        
        debug_index += 1
        if debug_index <= debug_count:
            print()
                
        free_set = set(hexagon_names)
        donjon_set = set()

        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        hexagon_for_players = copy.copy(free_set)
         
        adjacents = {}
        for (x, x_set) in hexagon_adjacents.items():
            if x not in mountain_set:
                new_x_set = set()
                for y in x_set:
                    if y not in mountain_set:
                        new_x_set.add(y)
                
                adjacents[x] = new_x_set
                
                    
        partition = compute_connex_partition(adjacents)
        if len(partition) > 1:
            continue
        
        distances = compute_distances(adjacents)
  
        random.shuffle(points_list)
        points_map = {}
        for (name_index, name) in enumerate(sorted(list(hexagon_names))):
            points_map[name] = points_list[name_index]
        
        player_points = [0 for player_index in range(player_count)]
        player_locations = random.sample(list(hexagon_for_players), player_count)

        points = 0
        donjon_count = 0
        player_index = 0
        
        iteration_index = 0
        iteration_count = 100
        
        while len(free_set) != 0 and iteration_index < iteration_count:
            
            iteration_index += 1
            
            fuel = random.choice([1, 2, 3])
            
            src = player_locations[player_index]
            other_player_locations = [player_locations[other_player_index] for other_player_index in range(player_count) if other_player_index != player_index]
            
            target_locations = set()
            target_values = {}
            
            # Find the best possible target
            
            for dst in hexagon_for_players:
                src_dst_distance = distances[(src, dst)]
                if src_dst_distance is not None and src_dst_distance <= fuel:
                    if dst in free_set and dst not in other_player_locations and points_map[dst] != 0:
                        target_locations.add(dst)
                        target_values[dst] = points_map[dst]
                        
            if len(target_locations) != 0:
                max_value = max(target_values.values())
                target_locations = list(target_locations)
                random.shuffle(target_locations)
                for dst in target_locations:
                    if target_values[dst] == max_value:
                        player_locations[player_index] = dst
                        player_points[player_index] += max_value
                        points += max_value
                        donjon_count += 1
                        points_map[dst] = 0
                        donjon_set.add(dst)
                        free_set.remove(dst)
                        free_set = free_set - hexagon_adjacents[dst]
                        if debug_index <= debug_count:
                            print(f"at iteration {iteration_index} with {fuel} fuel, player {player_index} moved from {src} to {dst}" + 
                                  f" and gained {max_value} points ; accumulating {player_points[player_index]} points")
                        break

            # Or get closest to the best possible target
            elif len(target_locations) == 0:
                dst_dst2_distance_min = len(hexagon_names)
                max_value = -1
                for dst in hexagon_for_players:
                    src_dst_distance = distances[(src, dst)]
                    if src_dst_distance is not None and src_dst_distance <= fuel:
                        if dst not in other_player_locations:
                           for dst2 in hexagon_for_players:
                                if dst2 in free_set and points_map[dst2] != 0:
                                    dst_dst2_distance = distances[(dst, dst2)]
                                    if dst_dst2_distance is not None and dst_dst2_distance <= dst_dst2_distance_min:
                                        if dst_dst2_distance < dst_dst2_distance_min:
                                            dst_dst2_distance_min = dst_dst2_distance 
                                            target_locations = set([dst])
                                            max_value = points_map[dst2]
                                            
                                        elif points_map[dst2] > max_value:
                                            target_locations = set([dst])
                                            max_value = points_map[dst2] 
                                            
                                        elif points_map[dst2] == max_value:
                                            target_locations.add(dst)
                                                
                if len(target_locations) != 0:
                    dst = random.choice(list(target_locations))
                    player_locations[player_index] = dst
                    if debug_index <= debug_count:
                        print(f"at iteration {iteration_index} with {fuel} fuel, player {player_index} moved from {src} to {dst} ; chasing for {max_value} points !!!")
                   
            
            player_index = (player_index + 1) % player_count
            
        if debug_index <= debug_count:
            print(f"{points} points gained at test {test_index} after {iteration_index}/{iteration_count} iterations")
        
        points_sample.append(points)
        
        turn_sample.append(iteration_index)
        round_sample.append(math.ceil(iteration_index/player_count))
        
        donjon_count_sample.append(donjon_count)
        
        
        if ranking:
            player_points.sort(reverse=True)
            
        if debug_index <= debug_count:
            print(f"points over players : {player_points}")
            
        for player_index in range(player_count):
            player_points_sample[player_index].append(player_points[player_index])


            

    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print()
    print(f"donjons     count = {len(donjon_count_sample)}")
    print(f"donjons      mode = {statistics.mode(donjon_count_sample)}")
    print(f"donjons      mean = {statistics.mean(donjon_count_sample):.1f}")
    print(f"donjons quartiles = {statistics.quantiles(donjon_count_sample, n=4)}")
    print(f"donjons   deciles = {statistics.quantiles(donjon_count_sample, n=10)}")
    print(f"donjons       min = {min(donjon_count_sample)}")
    print(f"donjons       max = {max(donjon_count_sample)}")
    
    print()
    print(f"points     count = {len(points_sample)}")
    print(f"points      mode = {statistics.mode(points_sample)}")
    print(f"points      mean = {statistics.mean(points_sample):.1f}")
    print(f"points quartiles = {statistics.quantiles(points_sample, n=4)}")
    print(f"points   deciles = {statistics.quantiles(points_sample, n=10)}")
    print(f"points       min = {min(points_sample)}")
    print(f"points       max = {max(points_sample)}")
    print()
    
    print()
    print(f"turns     count = {len(turn_sample)}")
    print(f"turns      mode = {statistics.mode(turn_sample)}")
    print(f"turns      mean = {statistics.mean(turn_sample):.1f}")
    print(f"turns quartiles = {statistics.quantiles(turn_sample, n=4)}")
    print(f"turns   deciles = {statistics.quantiles(turn_sample, n=10)}")
    print(f"turns       min = {min(turn_sample)}")
    print(f"turns       max = {max(turn_sample)}")
    print()
    
    print()
    print(f"rounds     count = {len(round_sample)}")
    print(f"rounds      mode = {statistics.mode(round_sample)}")
    print(f"rounds      mean = {statistics.mean(round_sample):.1f}")
    print(f"rounds quartiles = {statistics.quantiles(round_sample, n=4)}")
    print(f"rounds   deciles = {statistics.quantiles(round_sample, n=10)}")
    print(f"rounds       min = {min(round_sample)}")
    print(f"rounds       max = {max(round_sample)}")
    print()
    
    print()
    print(f"--- points sorted by rank at each test ? : {ranking} ---")
    for player_index in range(player_count):
        print(f"player {player_index}     count = {len(player_points_sample[player_index])}")
        print(f"player {player_index}      mode = {statistics.mode(player_points_sample[player_index])}")
        print(f"player {player_index}      mean = {statistics.mean(player_points_sample[player_index]):.1f}")
        print(f"player {player_index} quartiles = {statistics.quantiles(player_points_sample[player_index], n=4)}")
        print(f"player {player_index}   deciles = {statistics.quantiles(player_points_sample[player_index], n=10)}")
        print(f"player {player_index}       min = {min(player_points_sample[player_index])}")
        print(f"player {player_index}       max = {max(player_points_sample[player_index])}")
        print()
       

    print()
    print("make_statistics_on_points_by_moving: done")

    
def make_statistics_on_partition(mountain_count=0):

    print()
    print("make_statistics_on_partition: ...")
    
    partition_size_sample = []
    partition_multiparts_count = 0

    test_count = 100_000
    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        adjacents = {}
        for (x, x_set) in hexagon_adjacents.items():
            if x not in mountain_set:
                new_x_set = set()
                for y in x_set:
                    if y not in mountain_set:
                        new_x_set.add(y)
                
                adjacents[x] = new_x_set
        
        partition = compute_connex_partition(adjacents)
        partition_size_sample.append(len(partition)) 
        
        if len(partition) > 1:
            partition_multiparts_count += 1
            print()
            print(f"test_index = {test_index}") 
            print(f"mountain_set = {mountain_set}") 
            for (part_index, part) in enumerate(partition):
                print(f"part {part_index} of length {len(part)} = {part}")      
        
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"    partition_multiparts_count = {partition_multiparts_count} ; {partition_multiparts_count/test_count*100:.1f}%")
    print(f"    count = {len(partition_size_sample)}")
    print(f"     mode = {statistics.mode(partition_size_sample)}")
    print(f"     mean = {statistics.mean(partition_size_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(partition_size_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(partition_size_sample, n=10)}")
    print(f"      min = {min(partition_size_sample)}")
    print(f"      max = {max(partition_size_sample)}")
 
    
    print()
    print("make_statistics_on_partition: done")

    
def make_statistics_on_distances(mountain_count=0, test_count=100_000):

    print()
    print("make_statistics_on_distances: ...")
    
    distance_mean_sample = []
    distance_std_sample = []
    distance_q25_sample = []
    distance_q50_sample = []
    distance_q75_sample = []
    distance_q90_sample = []
    distance_max_sample = []

    
    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        adjacents = {}
        for (x, x_set) in hexagon_adjacents.items():
            if x not in mountain_set:
                new_x_set = set()
                for y in x_set:
                    if y not in mountain_set:
                        new_x_set.add(y)
                
                adjacents[x] = new_x_set
                
                    
        partition = compute_connex_partition(adjacents)
        if len(partition) > 1:
            continue
        
        distances = compute_distance_occurrences(adjacents)

        distance_max_sample.append(max(distances))     
        distance_mean_sample.append(statistics.mean(distances))       
        distance_std_sample.append(statistics.stdev(distances))      
        distance_q25_sample.append(statistics.quantiles(distances, n=4)[0])       
        distance_q50_sample.append(statistics.quantiles(distances, n=4)[1])       
        distance_q75_sample.append(statistics.quantiles(distances, n=4)[-1])       
        distance_q90_sample.append(statistics.quantiles(distances, n=10)[-1])       
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"         count  = {len(distance_mean_sample)}")
    print(f"   mean of max  = {statistics.mean(distance_max_sample):.1f}")
    print(f"   mean of mean = {statistics.mean(distance_mean_sample):.1f}")
    print(f"   mean of std  = {statistics.mean(distance_std_sample):.1f}")
    print(f"   mean of q25  = {statistics.mean(distance_q25_sample):.1f}")
    print(f"   mean of q50  = {statistics.mean(distance_q50_sample):.1f}")
    print(f"   mean of q75  = {statistics.mean(distance_q75_sample):.1f}")
    print(f"   mean of q90  = {statistics.mean(distance_q90_sample):.1f}")
 
    print()
    print("make_statistics_on_distances: done")
    
        
    
if False:
    make_statistics_on_donjon_count(mountain_count=0)
    make_statistics_on_donjon_count(mountain_count=1)
    make_statistics_on_donjon_count(mountain_count=2)
    make_statistics_on_donjon_count(mountain_count=3)
    make_statistics_on_donjon_count(mountain_count=4)
    make_statistics_on_donjon_count(mountain_count=5)
    make_statistics_on_donjon_count(mountain_count=6)
    make_statistics_on_donjon_count(mountain_count=7)
    make_statistics_on_donjon_count(mountain_count=8)
    make_statistics_on_donjon_count(mountain_count=9)
    make_statistics_on_donjon_count(mountain_count=10)

if False:
    make_statistics_on_points(mountain_count=0)
    make_statistics_on_points(mountain_count=1)
    make_statistics_on_points(mountain_count=2)
    make_statistics_on_points(mountain_count=3)
    make_statistics_on_points(mountain_count=4)
    make_statistics_on_points(mountain_count=5)
    make_statistics_on_points(mountain_count=6)
    make_statistics_on_points(mountain_count=7)
    make_statistics_on_points(mountain_count=8)
    make_statistics_on_points(mountain_count=9)
    make_statistics_on_points(mountain_count=10)

if False:
    make_statistics_on_points(mountain_count=0, player_count=2)
    make_statistics_on_points(mountain_count=0, player_count=3)
    make_statistics_on_points(mountain_count=0, player_count=4)

if False:
    make_statistics_on_points(mountain_count=4, player_count=2, test_count=100_000, ranking=True)
    make_statistics_on_points(mountain_count=4, player_count=3, test_count=100_000, ranking=True)
    make_statistics_on_points(mountain_count=4, player_count=4, test_count=100_000, ranking=True)
    
if False:
    partition = compute_connex_partition(hexagon_adjacents)
    for (part_index, part) in enumerate(partition):
        print(f"part {part_index} of length {len(part)} = {part}")
     
if False:
    make_statistics_on_partition(mountain_count=4)
     
if False:
    make_statistics_on_distances(mountain_count=0, test_count=1)
    make_statistics_on_distances(mountain_count=4)
 
if True:
    make_statistics_on_points_by_moving(mountain_count=4, player_count=2, test_count=1_000, ranking=True)
    make_statistics_on_points_by_moving(mountain_count=4, player_count=3, test_count=1_000, ranking=True)
    make_statistics_on_points_by_moving(mountain_count=4, player_count=4, test_count=1_000, ranking=True)
        
print()
_ = input("main: done ; press enter to terminate")
