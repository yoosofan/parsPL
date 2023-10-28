# $ python3 interpreter.py test1.psl
# -----------------------------------------------------------------------------
# Ahmad Yoosofan
# The zxbparser use this method.
# The JS/CC (http://jscc.phorward-software.com/jscc/jscc.html) uses this method, too.
# -----------------------------------------------------------------------------
import commonParsPL,executerParsPL,parserParsPL,sys
if __name__ =="__main__":
  executerParsPL.debugMode=False
  if len(sys.argv)>1:   fname=sys.argv[1]
  else: fname='test1.psl'
  src=open(fname,encoding='utf-8').read()#+'\n'
  import os
  try:
    parserParsPL.yacc.parse(src)
    executerParsPL.my_execute()
  except commonParsPL.MyExit1 as myex:
    pass
  except EOFError:pass
