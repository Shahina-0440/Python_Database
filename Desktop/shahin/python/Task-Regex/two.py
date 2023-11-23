import re
import csv

fp=open("data.txt","r")
data=fp.read()

mobile_num=re.compile(r'\b\d{10}\b')
email_address=re.compile(r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-zA-Z]{2,}\b')
md=mobile_num.findall(data)
ed=email_address.findall(data)

fs=open("details.csv","w",newline="")
writer_obj=csv.writer(fs)
writer_obj.writerow(["Mobile Numbers"])
for m in (md):
    writer_obj.writerow([m])
writer_obj.writerow(["Email Adresses"])
for e in (ed):
    writer_obj.writerow([e])