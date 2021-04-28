import hash_table
import numpy as np
import csv
import time
import sys

# The first value of the hash_table function is size, which defines the length of m
# The method specifies which hash function will be used to get a hash value for selecting a slot.
# The different methods are: DivisionMethod, MultiplicationMethod and UniversalMethod.
# The collisionType variable is which technique to use for handling collisions.
# The different options are: Chaining and OpenAddressing.
# The probeType variable defines the probe type, when using open addressing.
# The different operations are: Linear, Quadratic, and DoubleHashing.
hash_table = hash_table.HashTable(20000, 
                              method = "MultiplicationMethod", 
                              collisionType = "Chaining", 
                              probeType = "Linear")

# The two datasets are Video_Games.csv and disney-voice-actors.csv
# To change the dataset, then in line 18 define the dataset by writing one of the two datasets mentioned the line above.
with open('datasets/Video_Games.csv', mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    startime = time.time()
    for row in csv_reader:
        if row is not None:
            if line_count == 0:
                line_count += 1
            # The key is set to provide a random key value between 0 and 3500 for each Name element.
            # The value variable when using the Video_games.csv files should be set to Name.
            # The value variable when using the disney-voice-actors.csv files should be set to voice-actor.
            hash_table.Insert(key = np.random.randint(0, 3500), value = row["Name"])
            line_count += 1
    #hash_table.print()
    m = hash_table.size
    n = line_count
    alpha = n/m
    
    print("\n")
    print("Experimental results:")
    print("-"*50)
    print("Time:", time.time()-startime, "sec")
    print("-"*50)
    print("U:" ,line_count, "elements")
    print("-"*50)
    print("Space requirements:", (sys.getsizeof(hash_table.table))/(1024*1024), "MB")
    print("-"*50)
