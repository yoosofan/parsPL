import commonParsPL
debugMode=False;
def ahmadPrint(args):
  retVal=None
  if args == None or len(args) == 0: print()
  elif len(args) == 1: print(str(args[0]));retVal=args[0]
  else:
    retVal='' 
    for m1 in args: retVal+=str(m1);
    print(retVal)
  return retVal;
def ahmadInput(args):
  retVal=None;stm=''
  if args != None and len(args) != 0:
    for m1 in args: stm+=str(m1)
    print(stm)
  retVal=input()
  try:
    retVal=float(retVal)
  except ValueError: pass
  return retVal;
def ahmadExit(args):
  print('Exit statement ')
  raise commonParsPL.MyExit1('exit')
listOfStandardFunctions={
 "بنویس" : ahmadPrint,
 "بخوان" : ahmadInput,
 "پایان" : ahmadExit,
}
stackOfCurrentLines=[]
stackOfFunctionNames=['body']
def executeUserFunction(fname,args1):
  try:[args,body,line1]=commonParsPL.symt.lof[fname]; 
  except KeyError:executionError('Function has not been defined');return 1;
  if len(args) != len(args1):
    executionError('Different number of arguments',fname); return 1;
  commonParsPL.symt.enterFunction()
  for i in range(len(args)):
    msg=commonParsPL.symt.insert(args[i],args1[i])
    if msg: executionError('assign error',msg, st); return 1;
  try: retVal=my_execute(body)
  except commonParsPL.ReturnStmt as rs:retVal=rs.v
  finally : commonParsPL.symt.exitFunction()
  return retVal
def callFunction(fname,args=[]):
  ag=[]; retVal=None
  for m1 in args: ag.append(exper(m1));
  if commonParsPL.symt.searhUserFunction(fname) == True:
    stackOfFunctionNames.append(fname)
    retVal=executeUserFunction(fname,ag)
    stackOfFunctionNames.pop()
  else:
    try:
      retVal=listOfStandardFunctions[fname](ag)
    except KeyError:
      raise MyException('Function did not find: '+fname)
  return retVal
def valueOfArray(aname,indexList):
  return commonParsPL.symt.search(aname+'.'+'.'.join([str(exper(d)) for d in indexList]))
def exper(exp):
  a=1; tm1=exp.t;
  if tm1 == 'id': 
    a=commonParsPL.symt.search(exp.v);
  elif  tm1 =='array'   : a=valueOfArray(exp.v,exp.c[0]);
  elif  tm1 =='literal' : a=exp.v;
  elif  tm1 =='number'  : a=exp.v;
  elif  tm1 =='fcal'    : a=callFunction(exp.v,exp.c[0]);
  elif  tm1 == '+': a=exper(exp.c[0])+exper(exp.c[1])
  elif  tm1 == '-': a=exper(exp.c[0])-exper(exp.c[1])
  elif  tm1 == '*': a=exper(exp.c[0])*exper(exp.c[1])
  elif  tm1 == 'uminus': a=-1*exper(exp.c[0])
  elif  tm1 == '/': 
    d=exper(exp.c[1]) 
    if d!=0: a=exper(exp.c[0])/d
    else:    executionError('divide by zero')
  elif  tm1 == '<' : a=exper(exp.c[0])< exper(exp.c[1])
  elif  tm1 == '<=': a=exper(exp.c[0])<=exper(exp.c[1])
  elif  tm1 == '>' : a=exper(exp.c[0])> exper(exp.c[1])
  elif  tm1 == '>=': a=exper(exp.c[0])>=exper(exp.c[1])
  elif  tm1 == '==': a=exper(exp.c[0])==exper(exp.c[1])
  elif  tm1 == '!=': a=exper(exp.c[0])!=exper(exp.c[1])
  else: executionError('UnknownExper',tm1);
  return a
def my_execute(cmsarg=commonParsPL.ast):
  i=0
  for st in cmsarg:
    tm1=st.t; stackOfCurrentLines.append(st.l)
    if debugMode != False: print('>> '+str(st))
    if  tm1=='assign'   :
      a=exper(st.c[1])
      name1=st.c[0].v
      if st.c[0].t=='array':
        indexList = st.c[0].c[0]
        name1+='.'+'.'.join([str(exper(d)) for d in indexList])
      msg=commonParsPL.symt.insert(name1,a)
      if msg: executionError('assign error',msg, st)
    elif  tm1=='return': a=exper(st.c[0]); raise commonParsPL.ReturnStmt(a);
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
