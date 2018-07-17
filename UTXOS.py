count=0

class utxos:
    def __init__ (self,m,n):
        self.date=m
        self.btc=n
class rang:
   def __init__(self,a,b,c,d):
    self.A=a
    self.B=b
    self.change=c
    self.check=d
ranges=[]
list = []
list.append(utxos(5,1))
list.append(utxos(6,7))
list.append(utxos(7,6))
list.append(utxos(10,0.6))
list.append(utxos(11,2))
list.append(utxos(12,5))
list.append(utxos(15,3))
list.append(utxos(18,5))
list.append(utxos(23,7.5))
list.append(utxos(28,8))
list.append(utxos(32,8))
list.append(utxos(34,0.1))



def find_ranges (list,x):
    Lenght= len(list)
    for i in range (0, Lenght):
        sum = 0
        ranges.append(rang(i,0,0,1))
        count=i
        
        while sum<x and count<Lenght :
            sum+=list[count].btc
            count+=1
        ranges[i].change= sum-x
        if ranges[i].change < 0:
            ranges[i].check=0
        if ranges[i].check == 1:
            ranges[i].B=count-1
    maxx=1000
    for j in range(0,Lenght):
        if ranges[j].check ==1:
            if maxx > ranges[j].change:
                q=j
                maxx=ranges[j].change
    print (list[ranges[q].A].date)
    print (list[ranges[q].B].date)
find_ranges (list,10)    
