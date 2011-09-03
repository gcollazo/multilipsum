#!/usr/bin/env python
# encoding: utf-8
"""
mlipsum.py

Created by Giovanni Collazo on 2011-09-03.
"""

import string


def main():
  f = open('lipsum.txt')
  words = f.read()
  f.close()
  print clean(words)
  
def clean(text):
  exclude = set(string.punctuation)
  text = ''.join(ch for ch in text if ch not in exclude)
  text = text.lower()
  text = text.replace('\n', '')
  return list(distinct(to_list(text)))

def distinct(words):
  distinct = set()
  for w in words:
    if w not in distinct:
      distinct.add(w)
  return distinct
  
def to_list(text):
  return text.split(' ')

if __name__ == '__main__':
  main()
