import numpy

def sales_management(names, records):
    record_dict = dict() # dictionary for record
    for i in range(len(names)):
        record_dict[names[i]] = numpy.mean(records[i]) #calcuate the mean of scores

    ranking = [ (v,k) for k,v in record_dict.items() ] #rearange the data to 2D list (mean, name)
    ranking = sorted(ranking, reverse=True) #sort
    
    # reject bonus if the score is lower than 5
    for bn in [ranking[0][1], ranking[1][1]]: #check the 2 highest ranking 
        if record_dict[bn] < 5:
            continue
        print(f"보너스 대상자 {bn}")
    print()
    
    # reject consulting if the score is higher than 3
    for cn in [ranking[4][1], ranking[5][1]]: #check the 2 lowest ranking 
        if record_dict[cn] > 3:
            continue
        print(f"면담 대상자 {cn} ")

#read data from file
member_names=[]
member_records=[]
with open('data.csv', 'r') as f:
    for line in f:
        member_names.append(line.strip('\n').split(',')[0]) #sort name
        member_records.append(list(map(int,line.strip('\n').split(',')[1:]))) #sort records as tpye of list

sales_management(member_names,member_records)