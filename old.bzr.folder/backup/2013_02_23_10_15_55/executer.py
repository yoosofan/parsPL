import common
debugMode=False;

def ahmadPrint(args):
  retVal=None
  if args == None or len(args) == 0: print()
  elif len(args) == 1: print(args[0]);retVal=args[0]
  else:
    retVal='' 
    for m1 in args: retVal+=str(m1);
    print(retVal)
  return retVal;
def ahmadInput(args):
  retVal=None;
  if args != None and len(args) != 0:
    for m1 in args: print(str(m1))
  retVal=input()
  return retVal;
def ahmadExit(args):
  print('Exit statement ')
  raise common.MyExit1('exit')
listOfStandardFunctions={
 "بنویس" : ahmadPrint,
 "بخوان" : ahmadInput,
 "پایان" : ahmadExit,
}
stackOfCurrentLines=[]
stackOfFunctionNames=['body']
class ExprError(common.MyException):
  def __init__(self,msg='divisionByZero'):super().__init__(msg)
def executeUserFunction(fname,args1):
  try:[args,body,line1]=common.symt.lof[fname]; 
  except KeyError:executionError('Function has not been defined');return 1;
  if len(args) != len(args1):
    executionError('Different number of arguments',fname); return 1;
  common.symt.enterFunction()
  for i in range(len(args)):
    msg=common.symt.insert(args[i],args1[i])
    if msg: executionError('assign error',msg, st); return 1;
  try: retVal=my_execute(body)
  except common.ReturnStmt as rs:retVal=rs.v
  finally : common.symt.exitFunction()
  return retVal
def callFunction(fname,args=[]):
  ag=[]; retVal=None
  for m1 in args: ag.append(exper(m1));
  if common.symt.searhUserFunction(fname) == True:
    stackOfFunctionNames.append(fname)
    retVal=executeUserFunction(fname,ag)
    stackOfFunctionNames.pop()
  else:
    try:
      retVal=listOfStandardFunctions[fname](ag)
    except KeyError:
      raise MyException('Function did not find: '+fname)
  return retVal
def exper(exp):
  a=1; tm1=exp.t;
  if tm1 == 'id': 
    a=common.symt.search(exp.v);
  elif  tm1 =='literal' : a=exp.v;
  elif  tm1 =='number'  : a=exp.v;
  elif  tm1 =='fcal'    : a=callFunction(exp.v,exp.c[0]);
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
    tm1=st.t; stackOfCurrentLines.append(st.l)
    if debugMode != False: print('>> '+str(st))
    if  tm1=='assign'   :
      a=exper(st.c[1])
      msg=common.symt.insert(st.c[0].v,a)
      if msg: executionError('assign error',msg, st)
    elif  tm1=='return': a=exper(st.c[0]); raise common.ReturnStmt(a);
    elif tm1 == 'if':
      a=exper(st.c[0])
      if a == True: my_execute(st.c[1])
    elif tm1 == 'ifelse':
      a=exper(st.c[0])
      if a == True: my_execute(st.c[1])
      else: my_execute(st.c[2])
    elif tm1 == 'while':
      while exper(st.c[0])==True: my_execute(st.c[1])
    elif  tm1 =='exprs'   : a=exper(st.c[0]);
    else: executionError('Undefined Instruction','',st)
    stackOfCurrentLines.pop()
def executionError(type1,msg='', st=None):
  print(type1+' >> ', stackOfCurrentLines[-1])
  if msg !='':print(msg)
