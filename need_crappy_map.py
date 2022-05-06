def main(): 
    def need_crappy_map():
        with open('map_need_made.txt','r') as maps:
            map_boolean = maps.readlines()
        with open('intersection_list.txt','r') as mops:
            map_ids = mops.readlines()

        maps_needed = []
        for i in range(len(map_ids)):
            if map_boolean[i]:
                maps_needed.append(map_ids[i])
        
        return maps_needed

    def map_made():
        pass

if __name__ == '__main__':
    main()
