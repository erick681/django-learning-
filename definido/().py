# coding: utf-8
from members.models import Table1
x = Table1.objects.all()
x.deathyear = 2004
x.save()
from members.models import Table1
member = Table1(deathyear = 1998)
member.save()
Table1.objects.all().values()
index0 = Table1.objects.all()[0]
index0.deathyear = 2000
index0.save()
index2 = Table.objects.all()[2]
index2 = Table1.objects.all()[2]
index2.firstname = "elon musk"
index2.lastname  = "jobs steve"
index2.save()
Table1.objects.all().values()
for i in Tables.objects.all().values():
    print(i)
    
for i in Table1.objects.all().values():
    print(i)
    
for i in Table1.objects.all().values():
    print(i)
    
get_ipython().run_line_magic('ls', '')
y = Table1.objects.all()
y
x.firstname = "batatinha/new element"
x.lastname = "so pra ver se vai aparecer on django admin"
x.deathyear = 2121
x.save()
y.firstname = "batatinha/new element"
y.lastname = "so pra ver se vai aparecer on django admin"
y.deathyear = 2121
y.save()
