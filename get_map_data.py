def get_map_data():
    with open('map_data.csv','r') as maps:
        mapMap = maps.readlines()
        splitMap = []
        for line in mapMap:
            splitMap.append(line.split(','))
        workMaps = []
        for line in splitMap:
            if 'TRUE' in line[3] and 'FALSE' in line[4]:
                workMaps.append(line)

    with open('field_maps_config.csv','w') as configMaps:
        for i in workMaps:
            configMaps.write(str(i))
            configMaps.write('\n')

get_map_data()