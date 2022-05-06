def in_field(file1,file2):
    with open(file1,'r') as intersection_ids:
        read_ids = intersection_ids.readlines()

    with open(file2,'r') as ips:
        read_ips = ips.readlines()
    true_ips = []
    true_ids = []
    for i in range(len(read_ids)):
        if 'TRUE' in read_ids[i]:
            true_ips.append(read_ips[i])
            true_ids.append(read_ids[i])

    with open('intersections_in_field.txt','w') as write_data:
        write_data.write("These IPs are in the field:\n\n")
        for i in range(len(true_ips)):
            write_data.write(true_ids[i][0:4])
            write_data.write('\n')
            write_data.write(true_ips[i])
            write_data.write('\n')

in_field('scm_list.txt','scm_ips.txt')