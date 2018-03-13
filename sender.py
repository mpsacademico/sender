import os, time, requests

serialnumber = "78"
key = "454545"

file = "/home2/marcos/data/ptu.txt"

modtime = 0
linesnum = 0

while 1:
	curtime = os.path.getmtime(file)
	if curtime != modtime:
		print("mudou -- modtime: %f -- curtime: %f"%(modtime, curtime))
		print("iniciando envio...")
		f = open(file, "r")
		lines = f.readlines()
		#print(lines[linesnum:])		
		for l in lines[linesnum:]:
			url = 'http://localhost:8000/mongo/?serialnumber='+serialnumber+'&key='+key+'&data='+l
			r = requests.get(url)
			print(r)
			print(url)
		print("envio concluido -- linesnum: %d"%linesnum)
		linesnum = len(lines)
		modtime = curtime
	else:
		print("nao mudou -- modtime: %f -- curtime: %f"%(modtime, curtime))
	time.sleep(60)