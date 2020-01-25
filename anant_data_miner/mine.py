import urllib
import urllib.request
import re
import numpy as np
import csv
import pprint

def write_to_csv(data):
	with open("C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\data.csv", 'a') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(data)


at_no = {}
with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\at_no.csv', mode='r') as infile:
	reader = csv.reader(infile)
	at_no = {rows[0]:rows[1] for rows in reader}

# g_no = {}
# with open('C:\\Users\\Utsav\\Desktop\\Mxene\\anant_data_miner\\g_no.csv', mode='r') as infile:
# 	reader = csv.reader(infile)
# 	g_no = {rows[0]:rows[1] for rows in reader}
	


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(at_no)
# pp.pprint(g_no)


for i in range(1,23870):
	print("\nITERATION NO:" + str(i)+"\n\n")
	try:
		url = "http://anant.mrc.iisc.ac.in/mxenedb/%5Edetails/(" + str(i) + ")"
		req = urllib.request.Request(url)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		val = re.findall(r'<!-- POSCAR FILE(.*?)-->',str(respData))
		bg = re.findall(r'<p>(.*?)</p>',str(respData))
		# print(bg)
		for word in bg:
			if "Band" in word:
				w = word
		# print(val[0])
		w = w.replace("Band Gap = ","").replace("eV", "")
		w = float(w)
		print(w)
		x = val[0].split()
		atoms = x[1].split("-")
		print(atoms)
		x[7] = x[7].replace("\\", "").replace("n", "")
		x[10] = x[10].replace("\\", "").replace("n", "")
		x[13] = x[13].replace("\\", "").replace("n", "")

		# for i in range (5, 14):.replace("\\", "").replace("n", "")
		# 	x[i] = float(x[i])

		print(x[5], end="      ")
		print(x[6], end="      ")
		print(x[7])
		print(x[8], end="      ")
		print(x[9], end="      ")
		print(x[10])
		print(x[11], end="      ")
		print(x[12], end="      ")
		print(x[13])

		i=0
		while("Direct" not in x[i]):
			i = i + 1

		i+=1

		struct = []

		while(x[i] != "\\n"):
			struct.append(x[i])
			i = i+1

		# print(struct)
		print("")
		for i in range(len(struct)):
				struct[i] = struct[i].replace("\\", "").replace("n", "")
				if((i+1)%3==0):
					print(struct[i])
				else:
					print(struct[i], end="      ")
		# print("\n\n\n\n\n\n")
		# print(x)

			#define data_row 

		data = []
		
		for i in range(5,14):
			data.append(float(x[i]))

		for i in range(len(struct)):
			data.append(float(struct[i]))

		many = ['OH','HO','NO','ON','OCl','ClO','CN','NC','PO','OP','OBr','BrO','SCN','SNC','CNS','CSN','NCS','NSC','OCN','ONC','CNO','CON','NOC','NCO']

		if (  (atoms[0] not in many) and (atoms[1] not in many) and (atoms[2] not in many) and (atoms[3] not in many) and (atoms[4] not in many) ):
			print("\n\n\n\n")
			print("*************")
			print(atoms)
			print("*************")
			print("\n\n\n\n")
			data.append(float(at_no[atoms[0]]))
			data.append(float(at_no[atoms[1]]))
			data.append(float(at_no[atoms[2]]))
			data.append(float(at_no[atoms[3]]))
			data.append(float(at_no[atoms[4]]))
			data.append(w)
			if(w>0):
				data.append(1)
			else:
				data.append(0)
			write_to_csv(data)
		print("\n")
		# print("############\n\n")
		# for j in range (len(x)):
		# 	print(str(j) + "  -->>  " + x[j])
		# print("\n\n\n\n\n\n\n\n\n")
	except Exception:
		print("URL not found")