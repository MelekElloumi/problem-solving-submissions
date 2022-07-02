import datetime
from dateutil.relativedelta import relativedelta

bdate = datetime.datetime.strptime(input(),'%d.%m.%Y').date()
edate = datetime.datetime.strptime(input(),'%d.%m.%Y').date()
dy = relativedelta(edate, bdate)
dd=edate-bdate
s=''
if dy.years==1:
    s+=str(dy.years)+" year, "
elif dy.years!=0:
    s+=str(dy.years)+" years, "

if dy.months==1:
    s+=str(dy.months)+" month, "
elif dy.months!=0:
    s+=str(dy.months)+" months, "
s+="total "+str(dd.days)+" days"    
print(s)