#!/usr/bin/env python

#-*-coding:utf-8-*-

import aiml
import sys
import os
  
  
def get_module_dir(name):
  path = getattr(sys.modules[name], '__file__', None)
  if not path:
    raise AttributeError('module %s has not attribute __file__' % name)
  return os.path.dirname(os.path.abspath(path))
  

def aliceRespond(mesege):
	return alice.respond(mesege)


if __name__ == "main":
	alice_path = get_module_dir('aiml') + '\\botdata\\alice'
	os.chdir(alice_path)
	alice = aiml.Kernel()
	alice.learn("startup.xml")
	alice.respond('LOAD ALICE')
	
	while True:
		print(alice.respond(input(">mesege  ")))


if __name__ == "alice":
	alice_path = get_module_dir('aiml') + '\\botdata\\alice'
	os.chdir(alice_path)
	alice = aiml.Kernel()
	alice.learn("startup.xml")
	alice.respond('LOAD ALICE')

