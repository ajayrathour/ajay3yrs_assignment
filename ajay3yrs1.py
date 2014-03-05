import csv
import random

print "Enter no. of companies",
comp_nos = raw_input()
total_comp =  int(comp_nos)

ofile  = open('company.csv', "ab",0)
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
i = 1
comp_list1 = ['year','month']

while i <= total_comp:
    com_name = 'comp_'+str(i)
    i += 1
    comp_list1.append(com_name)
    
writer.writerow(comp_list1)

month_list = ['jan','feb','mar','apl','may','jun','jul','aug','sep','oct','nov','dec']

for year in range(1990,2014,1):
    data_list = []
    year_list = []
    year_list.append(year)
    for mon in month_list:
        mon_list = []
        mon_list.append(mon)
        index = 1
        price_list = []
        while  index <= total_comp:
            share_price = str(random.randrange(10,100,1))
            price_list.append(share_price)
            index += 1
        data_list.append(year_list[-1])
        data_list.append(mon_list[-1])
        for item in price_list:
            data_list.append(item)
        try:
            writer.writerow(data_list)
            print "row written"
        except:
            print "No Row written"
        data_list = []
ofile.close()




            



