
class Token:
  def __init__(self,t1='assign',l1=0,p1=0,c=[],v1=0):
    self.t=t1 #token type
    self.l=l1    #line number
    self.p=p1    #position
    self.c=v1   #code , content, children
    self.v=v1    #value
  def __str__(self):
    return "type="+self.t+"\t\t"+'line number='+str(self.l)+'\t\t position='+str(self.p)+'\n'
    

mar=[]
mar.append(Token('ID'))
mar.append(Token('NUM'))
for m1 in mar : print(str(m1))
k=0
#for j in range(9,-1,-1):print(j)

class SymbolTable:
  def __init__(self):# consider array and function name
    self.tb=[]
    self.tb.append({})
  def search(self,name1):
    #for i in range(len(self.tb)-1,-1,-1):
    try:return self.tb[len(self.tb)-1][name1]
    except KeyError: 
      try:return self.tb[0][name1]
      except KeyError:pass
    return None
    
  def insert(self,name1,value1):
    self.tb[len(self.tb)-1][name1]=value1;
  def enterFunction(self):
    self.tb.append({})
  def exitFunction(self):
    self.tb.pop()
a1=SymbolTable();
a1.insert('ali',12)
a1.insert('reza',34)
print(a1.search('ali'))
print(a1.search('reza'))
print(a1.search('reza4'))
a1.enterFunction()
a1.insert('kazem',4567)
a1.insert('reza4',4567)
print(a1.search('kazem'))
print(a1.search('reza'))
print(a1.search('reza4'))
print(a1.search('reza45'))
a1.exitFunction()
print(a1.search('ali'))
print(a1.search('reza'))
print(a1.search('kazem'))
print(a1.search('reza4'))
