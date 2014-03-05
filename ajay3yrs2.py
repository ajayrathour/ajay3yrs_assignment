import csv

def return_max():
    ofile1  = open('company.csv', "rb",0)
    ofile2  = open('company_max.csv', "ab",0)
    writer = csv.writer(ofile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['year','month','company_name', 'max_price'])
    
    reader = csv.reader(ofile1)
    reader_list =  list(reader)
    read_list = []
    max_pos_list = []
    max_val_list = []
    pos = 0
    col_cnt = 0
    while col_cnt < len(reader_list[0][2:]):
        read_list = []
        for row in reader_list[1:]:
            read_list.append(row[2:][col_cnt])
            pos += 1
        col_cnt += 1    
        max_value =  max(read_list)
        pos_max =  read_list.index(str(max_value))
        max_pos_list.append(pos_max)
        max_val_list.append(max_value)
        
    final_list = []
    i=2
    list_unit = []
    for val in max_pos_list:
        list_for_csv = []
        final_list = reader_list[val+1]
        list_for_csv.append(final_list[0])
        list_for_csv.append(final_list[1])
        list_for_csv.append(reader_list[0][i])
        list_for_csv.append(final_list[i])
        i += 1
        try:
            writer.writerow(list_for_csv)
        except:
            pass
        list_unit.append(list_for_csv)
    print list_unit
    return list_unit

if __name__ == "__main__":
    return_max()
    