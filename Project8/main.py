'''
Name: Miriam Dixon
The purpose of this program is to verify president Clinton's
claim in 2012 that democratic presidents generated more
jobs in the private sector than republican presidents
(18 million more, according to Clinton).
Through interacting with this program, you should get a good idea
of how different presidential terms affected job amounts.
Make sure presidents.txt and the csv file for private sector jobs
in the correct years are both in the working directory, or enter
the absolute file path.
'''

#C:\Users\10919\Documents\School\Computer Science\presidents.txt
import pandas
from functools import reduce
dem = {}#these first 2 dictionaries will be used to associate presidents with years, then years will be replaced with job totals
rep = {}
both = {}#this dictionary will be used to compare each presidential term to the one before it
dem_p = {}#these two dictionaries will be used to store percent change for each president, depending on the party.
rep_p = {}

def demVrep(file):#creating two dictionaries for dem/rep presidents to compare from the text file
    f = open(file , 'r')
    lines = f.readlines()
    for line in lines:
        lyst = line.strip('\n')
        linelyst = lyst.split(';')
        p_year = linelyst[1].split(',')
        both[linelyst[0]] = p_year
        if "Dem" in linelyst[0]:
            dem[linelyst[0]] = p_year
        else:
            rep[linelyst[0]] = p_year
    f.close()
    

def jobs(year_list):#taking data from the bureau file, returning the total. argument must be a list of years during a president's term
    df = pandas.read_csv('BLS_private.csv', header=5, index_col='Year')
    #change the csv string file name above to your absolute file path if file is not in working directory
    total = 0
    for year in year_list:
        row = int(year)
        total += reduce(lambda x, y: x + y, list(df.loc[row]))
    return total

def pres(d1ct):#replaces the yearly values in original dictionaries with each president's total jobs per term
    for i in d1ct.keys():
        pres_j = jobs(d1ct[i])
        d1ct[i] = pres_j
    return d1ct

def calculate(dyct):#takes a dictionary and calculates the totals of its values
    total_p = 0
    for i in dyct.keys():
        total_p += dyct[i]
    total_p *= 1000
    return total_p

def analysis(dIct):#calculates the percent change in jobs for each president's term
    names = list(dIct.keys())
    for name in names:
        ind = names.index(name)
        if ind > 0:
            inc = 0
            perc = 0
            previous = names[ind - 1]
            inc = dIct[name] - dIct[previous]
            perc = (inc / dIct[previous]) * 100
            if "Dem" in name:
                dem_p[name] = perc
            elif "Rep" in name:
                rep_p[name] = perc
                
def ave(dlct): #find the average percent increase in jobs for both parties
    ave = 0
    count = 0
    for name in dlct:
        ave += dlct[name]
        count +=1
    ave = ave / count
    return ave

def main():
    filename = input("Enter the file path of the presidents.txt: ")
    demVrep(filename)
    choice = input("Type 'summ' to see the explanation of the data vs Clinton's claim in 2012. Type 'all' to see details")
    blue = pres(dem)
    red = pres(rep)
    comp = pres(both)
    analysis(comp)#appends to existing dictionaries with percent increases for each president
    blue_p = ave(dem_p)#give averages for percent increases per party
    red_p = ave(rep_p)
    blue_t = calculate(blue)#returns total jobs under each party
    red_t = calculate(red)

    if choice == 'all':#there are two choices for the user, depending if they want to see the analysis or just the figures
        for name in list(both.keys()):
            if "Kennedy" in name:
                print(name, "N\A")
            elif name in list(dem_p.keys()):
                print(name, "\n Percent Change in Jobs from Previous Term: ", dem_p[name])
            else:
                print(name, "\n Percent Change in Jobs from Previous Term: ", rep_p[name])
        print("Democrats: \n Total Private Sector Jobs: ", blue_t, "\n Average Job Percent Increase: ", blue_p)
        print("Republicans: \n Total Private Sector Jobs: ", red_t, "\n Average Job Percent Increase: ", red_p)

    elif choice == 'summ':
        print("""In 2012, Clinton claimed that Democratic presidents, since 1961, created more jobs
than Republican presidents. Let's look at the data to determine if he was right.""")
        print("Since 1961, these have been the Republican presidents: ")
        for name in list(red.keys()):
            print(name)
        print("Total, during these presidents' terms, there were this many jobs: ", red_t)
        print("And each Republican president increased jobs by an average of ", red_p, "%.")
        print("Since 1961, these have been the Democratic presidents: ")
        for name in list(blue.keys()):
            print(name)
        print("Total, during these presidents' terms, there were this many jobs: ", blue_t)
        print("And each Republican president increased jobs by an average of ", blue_p, "%.")
        print("""While there have been more private sector jobs during Republican presidencies,
you can see that Democratic presidents have increased jobs by significantly more. Clinton was wrong
on the specific figures, but right about Democratic presidents being good for the job force.""")
        
    else:#any input that is not "all" or "summ" will exit the program.
        print("program exited.")

        
    
if __name__ == "__main__":
    main()