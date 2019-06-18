time_list = [line.rstrip('\n') for line in open('time_file.txt')]
data_list = [line.rstrip('\n') for line in open('data_file.txt')]
type_list = [line.rstrip('\n') for line in open('type_file.txt')]

#print(len(time_list))
#print(len(data_list))
#print(len(type_list))
HUM_time = []
HUM_data = []
PM1_time = []
PM1_data = []
PM10_time = []
PM10_data = []
PM2_5_time = []
PM2_5_data = []
PRES_time = []
PRES_data = []
TC_time = []
TC_data = []
for i in range(len(type_list)):
    if type_list[i] == "HUM":
        HUM_time.append(time_list[i])
        HUM_data.append(data_list[i])
    elif type_list[i] == "PM1":
        PM1_time.append(time_list[i])
        PM1_data.append(data_list[i])
    elif type_list[i] == "PM10":
        PM10_time.append(time_list[i])
        PM10_data.append(data_list[i])
    elif type_list[i] == "PM2_5":
        PM2_5_time.append(time_list[i])
        PM2_5_data.append(data_list[i])
    elif type_list[i] == "PRES":
        PRES_time.append(time_list[i])
        PRES_data.append(data_list[i])
    elif type_list[i] == "TC":
        TC_time.append(time_list[i])
        TC_data.append(data_list[i])

#print(len(TC_data))
#print(len(TC_time))

for i in range(len(HUM_data)):
    print(HUM_time[i][9:14])
    '''if HUM_time[i][1]
    print(HUM_time[i] + " " + HUM_data[i])'''