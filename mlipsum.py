#!/usr/bin/env python
# encoding: utf-8
"""
mlipsum.py

Created by Giovanni Collazo on 2011-09-03.
"""

import string
from random import shuffle


def main():
  f = open('lipsum.txt')
  words = f.read()
  f.close()
  words = clean(words)
  # print words
  shuffle(words)
  print ' '.join(words[:10])
  
def clean(text):
  """
  Remove punctuation, make lowercase,
  remove line breaks and return as a
  list of distinct words
  """
  exclude = set(string.punctuation)
  text = ''.join(ch for ch in text if ch not in exclude)
  text = text.lower()
  text = text.replace('\n', '')
  return distinct(to_list(text))

def distinct(words):
  """
  Returns a list of distinct words
  from a list of words
  """
  distinct = set()
  for w in words:
    if w not in distinct:
      distinct.add(w)
  return list(distinct)
  
def to_list(text):
  """
  Splits a string by space and returs a list
  """
  return text.split(' ')

if __name__ == '__main__':
  main()
