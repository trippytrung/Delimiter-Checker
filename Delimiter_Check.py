from inspect import stack
import sys
from fileinput import filename
from Stack import Stack
from typing import Deque # for sys.argv, the command-line arguments


def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

  file=open(filename, "r")
  myString=file.read()
  stack=Stack()
  for char in myString:
    if char in ['(', '[', '{']:
      stack.push(char)
    elif char == ')':
      if len(stack) == 0 or stack.pop() != '(':
        return False
    elif char == ']':
      if len(stack) == 0 or stack.pop() != '[':
        return False
    elif char == '}':
      if len(stack) == 0 or stack.pop() != '{':
        return False
  return True

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')