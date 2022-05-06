'''
This program takes a data file that contains the scrambled lines of three books, and it sorts them
according to the name of the book, then puts the lines in order. It also returns a summary of each book,
stating the longest and shortest lines of each.
'''
import sys

def main():
    def sort_data(file):
        with open(file,'r') as book_data:
            read_data = book_data.readlines()
        split_data = []
        for line in read_data:
            split_data.append(line.split('|'))

        #organize list alphabetically by book code
        def alpha_key(data):
            return data[2]
        split_data.sort(key=alpha_key)
        #organize list numerically by line number
        def beta_key(data):
            return int(data[1])
        split_data.sort(key=beta_key)

        #store lines from first book to book_one
        book_one = []
        for list in split_data:
            if book_one == []:
                book_one.append(list[2])

        #print(book_one)

        #store lines from book two
        book_two = []
        for list in split_data:
            if list not in book_one and book_two == []:
                book_two.append(list[2])

        #print(book_two[0:10])

        #store lines from book three
        book_three = []
        for list in split_data:
            if list[2] not in book_one and list[2] not in book_two and book_three == []:
                book_three.append(list[2])

        for list in split_data:
            if list[2] in book_one:
                book_one.append(list)
            elif list[2] in book_two:
                book_two.append(list)
            elif list[2] in book_three:
                book_three.append(list)

        #print(book_three)

        #at this point, book_one conatains [AlG, ...every list with ALG in index 2]
        # book_two contains [TTL ... every list with TTL in index 2]
        # and book_three contains [WOO ... every list with WOO in index 2]
        return [book_one,book_two,book_three]

    def write_novel_txt(sorted_books):
        book1 = sorted_books[0]
        book2 = sorted_books[1]
        book3 = sorted_books[2]
        with open('novel_text.txt','w') as finished_novels:
            finished_novels.write(book1[1][2])
            book1.pop(0)
            for line in book1:
                finished_novels.write(line[0] + '\n')
            finished_novels.write("-----\n")
            finished_novels.write(book2[10][2])
            book2.pop(0)
            for line in book2:
                finished_novels.write(line[0] + '\n')
            finished_novels.write('-----\n')
            finished_novels.write(book3[500][2])
            book3.pop(0)
            for line in book3:
                finished_novels.write(line[0] + '\n')


    def sum_data(books):
        book1 = books[0]
        book2 = books[1]
        book3 = books[2]

        book_title_1 = book1.pop(0)
        book_title_2 = book2.pop(0)
        book_title_3 = book3.pop(0)
        #print(book1[0:5])
        
        max_1 = 0
        for line in book1:
            if len(line[0]) > max_1:
                max_1 = len(line[0])
                #print(max_1)
                max_line1 = line
                #print(max_line1)
        max_2 = 0
        for line in book2:
            if len(line[0]) > max_2:
                max_2 = len(line[0])
                #print(max_2)
                max_line2 = line
                #print(max_line2)
        max_3 = 0
        for line in book3:
            if len(line[0]) > max_3:
                max_3 = len(line[0])
                #print(max_2)
                max_line3 = line
                #print(max_line2)
        
        # find minimum line of each book
        min_1 = 1000
        for line in book1:
            if len(line[0]) < min_1:
                min_1 = len(line[0])
                #print(max_1)
                min_line1 = line
                #print(max_line1)
        min_2 = 1000
        for line in book2:
            if len(line[0]) < min_2:
                min_2 = len(line[0])
                #print(max_2)
                min_line2 = line
                #print(max_line2)
        min_3 = 1000
        for line in book3:
            if len(line[0]) < min_3:
                min_3 = len(line[0])
                #print(max_2)
                min_line3 = line
                #print(min_line3)
        
        def avg_len(list):
            temp = []
            for line in list:
                temp.append(len(line[0]))
            avg = sum(temp)/len(temp)
            return avg

        #write summary to text file
        with open("novel_summary.txt", 'w') as sum_file:
            # write data for book one
            sum_file.write(book_title_1[2])
            sum_file.write(f'Longest line ({max_line1[1]}): {max_line1[0]}\n')
            sum_file.write(f'Shortest line ({min_line1[1]}): {min_line1[0]}\n)')
            sum_file.write(f'Average length: {int(avg_len(book1))}\n\n')
            # write data for book two
            sum_file.write(book_title_2[2])
            sum_file.write(f'Longest line ({max_line2[1]}): {max_line2[0]}\n')
            sum_file.write(f'Shortest line ({min_line2[1]}): {min_line2[0]}\n')
            sum_file.write(f'Average length: {int(avg_len(book2))}\n\n')
            # write data for book three
            sum_file.write(book_title_3[2])
            sum_file.write(f'Longest line ({max_line3[1]}): {max_line3[0]}\n')
            sum_file.write(f'Shortest line ({min_line3[1]}): {min_line3[0]}\n')
            sum_file.write(f'Average length: {int(avg_len(book3))}')
            
            
    #function calls
    write_books = sort_data(sys.argv[1])
    write_novel_txt(write_books)
    sum_data(write_books)


if __name__ == '__main__':
    main()
