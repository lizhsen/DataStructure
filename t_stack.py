# -*- coding:utf-8 -*-

from pythonds.basic.stack import Stack

s = Stack()
print s.isEmpty()
s.push(8)
print s.isEmpty()
print s.size()
s.push(9)
print s.size()
print s.peek()