import common
debugMode=False;

class ExprError(common.MyException):
  def __init__(self,msg='divisionByZero'):super().__init__(msg)
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
  def print(self):
    for m1 in self.tb:
      print(m1)

symt=SymbolTable();

def exper(exp):
  a=1; tm1=exp.t;
  if tm1 == 'id': 
    a=symt.search(exp.v);
  elif  tm1 =='literal' : a=exp.v;
  elif  tm1 =='number' : a=exp.v;
  elif  tm1 == '+': a=exper(exp.c[0])+exper(exp.c[1])
  elif  tm1 == '-': a=exper(exp.c[0])-exper(exp.c[1])
  elif  tm1 == '*': a=exper(exp.c[0])*exper(exp.c[1])
  elif  tm1 == '/': 
    d=exper(exp.c[1]) 
    if d!=0: a=exper(exp.c[0])/d
    else:
      print('divide by zero ')
      raise ExprError('divisionByZero')
  elif  tm1 == '<' : a=exper(exp.c[0])< exper(exp.c[1])
  elif  tm1 == '<=': a=exper(exp.c[0])<=exper(exp.c[1])
  elif  tm1 == '>' : a=exper(exp.c[0])> exper(exp.c[1])
  elif  tm1 == '>=': a=exper(exp.c[0])>=exper(exp.c[1])
  elif  tm1 == '==': a=exper(exp.c[0])==exper(exp.c[1])
  elif  tm1 == '!=': a=exper(exp.c[0])!=exper(exp.c[1])
  else: print("type Error "+str(tm1)); raise ExpError('UnknownExper');
  return a
def my_execute(cmsarg=common.ast):
  i=0
  for st in cmsarg:
    tm1=st.t
    if debugMode != False: print('>> '+str(st))
    if    tm1=='exit'     : raise common.MyExit1()
    elif  tm1=='assign'   :
      a=exper(st.c[1])
      symt.insert(st.c[0].v,a)
    elif  tm1=='print': print(symt.search(st.c[0].v))
    elif tm1 == 'if':
      a=exper(st.c[0])
      if a == True: my_execute(st.c[1])
    elif tm1 == 'ifelse':
      a=exper(st.c[0])
      if a == True: my_execute(st.c[1])
      else: my_execute(st.c[2])
    elif tm1 == 'while':
      while exper(st.c[0])==True: my_execute(st.c[1])
    elif  tm1=='input':pass
