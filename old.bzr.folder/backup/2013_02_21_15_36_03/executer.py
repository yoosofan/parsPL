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

symt=SymbolTable();

def exper(exp):
  a=1; tm1=type(exp)
  if tm1 != list: 
    if tm1 == str: a=symt.search(exp);
    elif tm1 == float or tm1==int: a=exp;
    else: print("type Error "+str(tm1)); raise ExpError('UnknownExper');
  elif  exp[0] == '+': a=exper(exp[1])+exper(exp[2])
  elif  exp[0] == '-': a=exper(exp[1])-exper(exp[2])
  elif  exp[0] == '*': a=exper(exp[1])*exper(exp[2])
  elif  exp[0] == '/': 
    d=expr(exp[1]) 
    if d!=0: a=exper(exp[1])/exper(exp[1])
    else:
      print('divide by zero ')
      raise ExprError('divisionByZero')
  return a
def my_execute():
  i=0
  for st in common.ast:
    if debugMode != False: print('>> '+str(st))
    if    st.t=='exit'     : raise common.MyExit1()
    elif  st.t=='assign'   :
      a=exper(st.c[1])
      symt.insert(st.c[0],a)
    elif  st.t=='print': print(symt.search(st.c[0]))
    elif  st.t=='input':pass
