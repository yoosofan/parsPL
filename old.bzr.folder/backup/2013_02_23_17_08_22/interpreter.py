#!/usr/bin/python3
# -*- coding: utf_8 -*-
# $ python3 interpreter.py test1.psl
# -----------------------------------------------------------------------------
# Ahmad Yoosofan
# The zxbparser use this method.
# The JS/CC (http://jscc.phorward-software.com/jscc/jscc.html) uses this method, too.
# -----------------------------------------------------------------------------
import common,executer,parser,sys
if __name__ =="__main__":
  executer.debugMode=False
  if len(sys.argv)>1:   fname=sys.argv[1]
  else: fname='test1.psl'
  src=open(fname,encoding='utf-8').read()+'\n'
  try:
    parser.yacc.parse(src)
    executer.my_execute()
  except common.MyExit1 as myex:
    pass
  except EOFError:pass
