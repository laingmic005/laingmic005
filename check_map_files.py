from os.path import exists
def check_map_files():
    print("These folders contain unwanted parent maps: ")
    i = 6016
    while i < 7000:
        if exists(f"Maps for Panosonic Phase 2\{i}\ISD_{i}_parent_r1.geojson"):
            print(i)
        i+=1
        
check_map_files()
    