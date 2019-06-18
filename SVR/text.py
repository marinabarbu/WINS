time_list = [line.rstrip('\n') for line in open('time_file.txt')]

data_list = [line.rstrip('\n') for line in open('data_file.txt')]

type_list = [line.rstrip('\n') for line in open('type_file.txt')]

print(len(time_list))
print(len(data_list))
print(len(type_list))

