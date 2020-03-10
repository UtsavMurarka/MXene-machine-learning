import csv
import pprint

num_neutrons = {}
num_protons = {}
num_electrons = {}
period = {}
g_no = {}
at_rad = {}
electronegativity = {}
first_ie = {}
density = {}
mp = {}
bp = {}
num_isotopes = {}
num_shells = {}
sp_heat = {}
pp = pprint.PrettyPrinter(indent=4)
l = [num_neutrons, num_protons, num_electrons, period, g_no, at_rad, electronegativity, first_ie, density, mp, bp, num_isotopes, num_shells, sp_heat]

with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	num_neutrons = {rows[1]:rows[2] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	num_protons = {rows[1]:rows[3] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	num_electrons = {rows[1]:rows[4] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	period = {rows[1]:rows[5] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	g_no = {rows[1]:rows[6] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	at_rad = {rows[1]:rows[7] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	electronegativity = {rows[1]:rows[8] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	first_ie = {rows[1]:rows[9] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	density = {rows[1]:rows[10] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	mp = {rows[1]:rows[11] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	bp = {rows[1]:rows[12] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	num_isotopes = {rows[1]:rows[13] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	num_shells = {rows[1]:rows[14] for rows in reader}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\periodicTableData\\g_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	sp_heat = {rows[1]:rows[15] for rows in reader}


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(num_neutrons)
pp.pprint(num_protons)
pp.pprint(num_electrons)
pp.pprint(period)
pp.pprint(g_no)
pp.pprint(at_rad)
pp.pprint(electronegativity)
pp.pprint(first_ie)
pp.pprint(density)
pp.pprint(mp)
pp.pprint(bp)
pp.pprint(num_isotopes)
pp.pprint(num_shells)
pp.pprint(sp_heat)

print("***data read successful***")
row1 = [0] * 100
in_file = open("C:\\Users\\Utsav\\Desktop\\Mxene\\data_exp\\data.csv", "r")
reader = csv.reader(in_file)
out_file = open("C:\\Users\\Utsav\\Desktop\\Mxene\\data_exp\\data_physical.csv", "w")
writer = csv.writer(out_file)
for row in reader:
	# try:
	for i in range(30):
		row1[i] = row[i]
	print(row1[24])
	row1[30] = num_neutrons[str(int(float(row[24])))]
	row1[31] = num_neutrons[str(int(float(row[25])))]
	row1[32] = num_neutrons[str(int(float(row[26])))]
	row1[33] = num_neutrons[str(int(float(row[27])))]
	row1[34] = num_neutrons[str(int(float(row[28])))]

	row1[35] = num_protons[str(int(float(row[24])))]
	row1[36] = num_protons[str(int(float(row[25])))]
	row1[37] = num_protons[str(int(float(row[26])))]
	row1[38] = num_protons[str(int(float(row[27])))]
	row1[39] = num_protons[str(int(float(row[28])))]

	row1[40] = num_electrons[str(int(float(row[24])))]
	row1[41] = num_electrons[str(int(float(row[25])))]
	row1[42] = num_electrons[str(int(float(row[26])))]
	row1[43] = num_electrons[str(int(float(row[27])))]
	row1[44] = num_electrons[str(int(float(row[28])))]

	row1[45] = period[str(int(float(row[24])))]
	row1[46] = period[str(int(float(row[25])))]
	row1[47] = period[str(int(float(row[26])))]
	row1[48] = period[str(int(float(row[27])))]
	row1[49] = period[str(int(float(row[28])))]

	row1[50] = g_no[str(int(float(row[24])))]
	row1[51] = g_no[str(int(float(row[25])))]
	row1[52] = g_no[str(int(float(row[26])))]
	row1[53] = g_no[str(int(float(row[27])))]
	row1[54] = g_no[str(int(float(row[28])))]

	row1[55] = at_rad[str(int(float(row[24])))]
	row1[56] = at_rad[str(int(float(row[25])))]
	row1[57] = at_rad[str(int(float(row[26])))]
	row1[58] = at_rad[str(int(float(row[27])))]
	row1[59] = at_rad[str(int(float(row[28])))]

	row1[60] = electronegativity[str(int(float(row[24])))]
	row1[61] = electronegativity[str(int(float(row[25])))]
	row1[62] = electronegativity[str(int(float(row[26])))]
	row1[63] = electronegativity[str(int(float(row[27])))]
	row1[64] = electronegativity[str(int(float(row[28])))]

	row1[65] = first_ie[str(int(float(row[24])))]
	row1[66] = first_ie[str(int(float(row[25])))]
	row1[67] = first_ie[str(int(float(row[26])))]
	row1[68] = first_ie[str(int(float(row[27])))]
	row1[69] = first_ie[str(int(float(row[28])))]

	row1[70] = density[str(int(float(row[24])))]
	row1[71] = density[str(int(float(row[25])))]
	row1[72] = density[str(int(float(row[26])))]
	row1[73] = density[str(int(float(row[27])))]
	row1[74] = density[str(int(float(row[28])))]

	row1[75] = mp[str(int(float(row[24])))]
	row1[76] = mp[str(int(float(row[25])))]
	row1[77] = mp[str(int(float(row[26])))]
	row1[78] = mp[str(int(float(row[27])))]
	row1[79] = mp[str(int(float(row[28])))]

	row1[80] = bp[str(int(float(row[24])))]
	row1[81] = bp[str(int(float(row[25])))]
	row1[82] = bp[str(int(float(row[26])))]
	row1[83] = bp[str(int(float(row[27])))]
	row1[84] = bp[str(int(float(row[28])))]

	row1[85] = num_isotopes[str(int(float(row[24])))]
	row1[86] = num_isotopes[str(int(float(row[25])))]
	row1[87] = num_isotopes[str(int(float(row[26])))]
	row1[88] = num_isotopes[str(int(float(row[27])))]
	row1[89] = num_isotopes[str(int(float(row[28])))]

	row1[90] = num_shells[str(int(float(row[24])))]
	row1[91] = num_shells[str(int(float(row[25])))]
	row1[92] = num_shells[str(int(float(row[26])))]
	row1[93] = num_shells[str(int(float(row[27])))]
	row1[94] = num_shells[str(int(float(row[28])))]

	row1[95] = sp_heat[str(int(float(row[24])))]
	row1[96] = sp_heat[str(int(float(row[25])))]
	row1[97] = sp_heat[str(int(float(row[26])))]
	row1[98] = sp_heat[str(int(float(row[27])))]
	row1[99] = sp_heat[str(int(float(row[28])))]
	print(row)
	writer.writerow(row1)
	print("Success")

	# except:
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
