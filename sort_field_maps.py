def sort_field_maps():
    with open('map_data.csv','r') as maps:
        mapMap = maps.readlines()
        print(mapMap)
        mapLists = []
        for line in mapMap:
            if 'FALSE' in line[4]:
                mapLists.append(line)
    
    with open('field_maps_config.csv','w') as fieldMaps:
        for i in mapLists:
            fieldMaps.write(i)
    print(mapLists)

sort_field_maps()
