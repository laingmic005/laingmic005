def main():
    '''
    Was Clinton right?
    By Micah Laing
    CS 1400, Professor: Chris Brewer
    '''
    # This will provide an introduction to the conclusion.md file that states the claims made by Clinton.
    # I have left this outside of its own function within main, because the data here should stay unaffected
    # by the rest of my code.
    with open('conclusions.md', 'w') as conclude:
        conclude.write('# President Clinton\'s claims:')
        conclude.write('\nNumber of years Republicans held White House: **28**\nNumber of years Democrats held White House: **24**\nNumber of private jobs produced during Republican years: **24 million**\nNumber of private jobs produced during Democrat years: **42 million**')
    
    def verify_parties():
        '''
        This function will verify if Clinton's statements about how many years
        each party held office. The outcome will be written to conclusion.md
        '''
        with open('us_presidents.csv', 'r') as parties:
            list_parties = parties.readlines()
            for line in list_parties:
                line.split(',')
            republicans = 0
            democrats = 0
            for line in list_parties:
                if 'REPUBLICAN' in line:
                    republicans += 1
                elif 'DEMOCRAT' in line:
                    democrats += 1
        with open('conclusions.md','a') as conclude:
            conclude.write(f'\n\n# Actual Data:\nNumber of years Republicans held White House: **{republicans}**\nNumber of years Democrats held White House: **{democrats}**')
    verify_parties()

    def verify_jobs():
        '''
        This function will verify the statistics for how many private-sector jobs existed for each year.
        '''
        with open('BLS_private.csv', 'r') as private_jobs:
            jobs = private_jobs.readlines()
            split_jobs = []
            for line in jobs:
                split_jobs.append(line.split(','))
        with open('us_presidents.csv', 'r') as parties:
            list_parties = parties.readlines()
            split_parties = []
            for line in list_parties:
                split_parties.append(line.split(','))
            split_parties.pop(0)
        
        year_party = []
        for line in split_parties:
            year_party.append(line[1])
        repub_jobs = []
        demo_jobs = []
        party_jobs = []
        for line in split_jobs[6:]:
            party_jobs.append(line[1:])

        for i in range(len(party_jobs)):
            if year_party[i] == 'REPUBLICAN\n':
                repub_jobs.append(party_jobs[i])
            elif year_party[i] == 'DEMOCRAT\n':
                demo_jobs.append(party_jobs[i])

        repub_total = 0
        demo_total = 0
        for list in repub_jobs:
            for num in list:
                repub_total += int(num)
        for list in demo_jobs:
            for num in list:
                if num != '' and num != '\n':
                    demo_total += int(num)

        with open('conclusions.md','a') as conclude:
            conclude.write(f'\nActual number of private jobs held during Republican years: **{repub_total*1000}**\nActual number of private jobs held during Democrat years: **{demo_total*1000}**')

    def write_conclusion():
        '''
        Write the conclusion drawn from the information gathered
        '''
        with open('conclusions.md', 'a') as conclude:
            conclude.write('\n\n# Conclusion:\nPresident Clinton was right about the number of years each party held the White House (thank goodness he got that right),\nbut he was laughably wrong about the number of private jobs during each party\'s presidencies.\nClinton claimed that **24 million** jobs were produced during Republican years, but there were actually **28.5 million** -- a difference of **4.5 million**.\nClinton claimed that **42 million** jobs were produced during Democrat years, but there were only **23 million** -- a dfference of **-19 million**.')

    verify_jobs()
    write_conclusion()



if __name__ == '__main__':
    main()
