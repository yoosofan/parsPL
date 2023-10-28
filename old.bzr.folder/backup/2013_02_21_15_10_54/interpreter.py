#!/usr/bin/python3
# -*- coding: utf_8 -*-
# Use only python 3
# $ python3 interpreter.py test1.psl
# -----------------------------------------------------------------------------
# calc.py
# Ahmad Yoosofan
# A simple calculator with variables -- all in one file.
# The creation of nodes in a tree is the best way for creating an interpreter for ParsPL.
# The zxbparser use this method.
# The JS/CC (http://jscc.phorward-software.com/jscc/jscc.html) uses this method, too.
#
# -----------------------------------------------------------------------------
import common,executer,parser,sys
if __name__ =="__main__":
  executer.debugMode=False
  if len(sys.argv)>1:
    src=open(sys.argv[1]).readlines()
    try:
      for line1 in src:
        parser.yacc.parse(line1)
      common.ast.append(common.StmtCls('exit',0))
      executer.my_execute()
    except common.MyExit1 as myex:
      print('برنامه به پایان رسید. ')
    except EOFError:pass
