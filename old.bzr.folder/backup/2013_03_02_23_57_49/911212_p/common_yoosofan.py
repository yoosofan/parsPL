class MyException(Exception):
  def __init__(self,ms1): self.msg=ms1
  def __str__(self):return self.msg;
class MyExit1(MyException):
  def __init__(self,msg='exit'):
    super().__init__(msg)

class ReturnStmt(Exception):
  def __init__(self,val1=None):
    self.v=val1
class NodeCls:
  def __init__(self,t1='+',l1=0,c1=[],v1=0):
    self.t=t1    #statement type type
    self.l=l1    #line number
    self.c=c1    #code , content, children
    self.v=v1    #value
  def __str__(self):
    stm1="type="+self.t+"\t"+'line number='+str(self.l)+'\n'
    for m1 in self.c:
      stm1 += str(m1)+'\t'
    return stm1+'\n'
class StmtCls:
  def __init__(self,t1='assign',l1=0,c1=[],v1=0):
    self.t=t1    #statement type type
    self.l=l1    #line number
    self.c=c1    #code , content, children
    self.v=v1    #value
  def __str__(self):
    stm1="type="+self.t+"\t"+'line number='+str(self.l)+'\n'
    for m1 in self.c:
      stm1 += str(m1)+'\t'
    return stm1+'\n'
class function_call_list_in_parsing:
  def __init__(self,fname,args):
    self.fcl={} #function call list

def parseError(msg='Parse Error',action='no action'):
  print(msg)
class SymbolTable:
  def __init__(self):# consider array and function name
    self.tb=[]
    self.tb.append({})
    self.lof={} #list of function
  def search(self,name1):
    #for i in range(len(self.tb)-1,-1,-1):
    try:return self.tb[-1][name1]
    except KeyError: 
      try:return self.tb[0][name1]
      except KeyError:pass
    return None
  def insert(self,name1,value1):
    if name1 in self.lof.keys():
      return 'Assigning a value to a function name does not allowed'
    self.tb[-1][name1]=value1;
  def insertFunction(self,name1,args,body,line1):
    if name1 in self.lof.keys():
      return 'The definition of a predefined funtion does not allowed'
    else: self.lof[name1]=[args,body,line1]
  def enterFunction(self):
    self.tb.append({})
  def exitFunction(self):
    self.tb.pop()
  def printSmbolTable(self):
    for m1 in self.tb:
      print(m1)
  def check_fucntion_call_list(self):
    pass
  def check_before_execution(self):
    self.check_fucntion_call_list()
  def searhUserFunction(self,fname):
    if fname in self.lof.keys(): return True
    return False
symt=SymbolTable();
ast=[] # ahmad ast
