'''
Library of Congress. Revision Two. By Micah Laing, for CS1400
'''
import sys
def main():
    '''
    This program organizes a large file containing three mixed up novels
    '''
    def sort_data(file):
        '''sort the data from the text file'''
        with open(file,'r',encoding = 'utf-8') as book_data:
            read_data = book_data.readlines()
            split_data = []
            for line in read_data:
                split_data.append(line.split('|'))
        #organize list alphabetically by book code
        def alpha_key(data):
            '''make key to sort lines alphabetically'''
            return data[2]
        split_data.sort(key=alpha_key)
        #organize list numerically by line number
        def beta_key(data):
            '''make key to sort lines numerically'''
            return int(data[1])
        split_data.sort(key=beta_key)
        #organize into books
        book_one = []
        book_two = []
        book_three = []

        for line in split_data:
            if book_one == []:
                book_one.append(line)
            elif book_two == [] and line[2] not in book_one[0]:
                book_two.append(line)
            elif book_three == [] and line[2] not in book_two[0] and line[2] not in book_one[0]:
                book_three.append(line)
            elif line[2] in book_one[0]:
                book_one.append(line)
            elif line[2] in book_two[0]:
                book_two.append(line)
            elif line[2] in book_three[0]:
                book_three.append(line)

        #print(book_one[0:10])
        #print(book_two[0:10])
        #print(book_three[0:10])
        return [book_one,book_two,book_three]

    def write_text(book_list):
        '''create the novel_text.txt file'''
        book1 = book_list[0]
        book2 = book_list[1]
        book3 = book_list[2]

        with open('novel_text.txt', 'w') as book_txt:
            book_txt.write(book1[0][2])
            for line in book1:
                book_txt.write(line[0])
                book_txt.write('\n')
            book_txt.write('-----\n')

            book_txt.write(book2[0][2])
            for line in book2:
                book_txt.write(line[0])
                book_txt.write('\n')
            book_txt.write('-----\n')

            book_txt.write(book3[0][2])
            for line in book3:
                book_txt.write(line[0])
                book_txt.write('\n')

    def sum_data(book_data):
        '''write novel_sumary.txt'''
        sum_one = book_data[0]
        sum_two = book_data[1]
        sum_three = book_data[2]

        def maxl(data):
            '''find max values'''
            max_val = 0
            for line in data:
                if len(line[0]) > max_val:
                    max_val = len(line[0])
                    max_line = line
                elif len(line[0]) == max_val:
                    if int(line[1]) > int(max_line[1]):
                        max_val = len(line[0])
                        max_line = line
            return max_line
        max_one = maxl(sum_one)
        max_two = maxl(sum_two)
        max_three = maxl(sum_three)

        def minl(data):
            '''find min values'''
            min_val = 1000
            for line in data:
                if len(line[0]) < min_val:
                    min_val = len(line[0])
                    min_line = line
            return min_line
        min_one = minl(sum_one)
        min_two = minl(sum_two)
        min_three = minl(sum_three)
        #print(min_one)
        #print(min_two)
        #print(min_three)
        avg_one = []
        avg_two = []
        avg_three = []
        for line in sum_one:
            avg_one.append(len(line[0]))
        for line in sum_two:
            avg_two.append(len(line[0]))
        for line in sum_three:
            avg_three.append(len(line[0]))
        #calculate averages
        average1 = round(sum(avg_one)/len(avg_one))
        average2 = round(sum(avg_two)/len(avg_two))
        average3 = round(sum(avg_three)/len(avg_three))

        with open('novel_summary.txt', 'w') as nov_sum:
            #book one data
            nov_sum.write(sum_one[0][2])
            nov_sum.write(f"Longest line ({max_one[1]}): {max_one[0]}\n")
            nov_sum.write(f"Shortest line ({min_one[1]}): {min_one[0]}\n")
            nov_sum.write(f"Average length: {average1}\n\n")
            # book two data
            nov_sum.write(sum_two[0][2])
            nov_sum.write(f"Longest line ({max_two[1]}): {max_two[0]}\n")
            nov_sum.write(f"Shortest line ({min_two[1]}): {min_two[0]}\n")
            nov_sum.write(f"Average length: {average2}\n\n")
            #book three data
            nov_sum.write(sum_three[0][2])
            nov_sum.write(f'Longest line ({max_three[1]}): {max_three[0]}\n')
            nov_sum.write(f'Shortest line ({min_three[1]}): {min_three[0]}\n')
            nov_sum.write(f'Average length: {average3}\n\n')

    #function calls
    write_text(sort_data("book_data.txt"))
    sum_data(sort_data("book_data.txt"))

if __name__ == '__main__':
    main()
