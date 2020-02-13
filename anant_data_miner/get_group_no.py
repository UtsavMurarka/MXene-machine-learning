import csv
import pprint

g_no = {}


# def write_to_csv(data):
# 	with open("C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\data.csv", 'w') as csv_file:
# 		writer = csv.writer(csv_file, delimiter=',')
# 		writer.writerow(data)


with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	g_no = {rows[1]:rows[2] for rows in reader}


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(g_no)


in_file = open("C:\\Users\\Utsav\\Desktop\\Mxene\\finalData\\data.csv", "r")
reader = csv.reader(in_file)
out_file = open("C:\\Users\\Utsav\\Desktop\\Mxene\\finalData\\data_new.csv", "w")
writer = csv.writer(out_file)
for row in reader:
	try:
	    row[30] = g_no[str(int(float(row[24])))]
	    row[31] = g_no[str(int(float(row[25])))]
	    row[32] = g_no[str(int(float(row[26])))]
	    row[33] = g_no[str(int(float(row[27])))]
	    row[34] = g_no[str(int(float(row[28])))]
	    writer.writerow(row)
	    print("Success")
	except:
	   	print("Error")
in_file.close()    
out_file.close()



# with open('C:\\Users\\Utsav\\Desktop\\Mxene\\finalData\\data.csv', mode='r') as infile:
# 	reader = csv.reader(infile)
# 	for rows in reader:
# 		v1 = rows[24]
# 		v2 = rows[25]
# 		v3 = rows[26]
# 		v4 = rows[27]
# 		v5 = rows[28]
# 		try:
# 			print(int(float(v1)))
# 		except Exception:
# 			pass



# import csv
# in_file = open("d:/in.csv", "rb")
# reader = csv.reader(in_file)
# out_file = open("d:/out.csv", "wb")
# writer = csv.writer(out_file)
# for row in reader:
#     row[3] = 4
#     writer.writerow(row)
# in_file.close()    
# out_file.close()
