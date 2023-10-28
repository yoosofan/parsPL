class MyException(Exception):
  def __init__(self,ms1): self.msg=ms1
  def __str__(self):return self.msg;
class MyExit1(MyException):
  def __init__(self,msg='exit'):
    super().__init__(msg)

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
ast=[] # ahmad ast
