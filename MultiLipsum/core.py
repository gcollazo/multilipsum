#!/usr/bin/env python
# encoding: utf-8
"""
mlipsum.py

Created by Giovanni Collazo on 2011-09-03.
"""

import random
import json
import os

class MultiLipsum:
  
  def __init__(self, filename=None):
    self.project_path = os.sep.join(os.path.realpath(os.path.dirname(__file__)).split('/')[:-1])
    lipsum = self.load('lipsum')
    if filename is not None:
      self.words = lipsum + self.load(filename)
    else:
      self.words = lipsum
  
  def load(self, filename):
    f = open('%s/text/%s.json' % (self.project_path, filename))
    return json.loads(f.read())
    
  def shuffle(self):
    random.shuffle(self.words)
    return self.words
  
  def get_words(self, number):
    """
    Return 'number' of words
    """
    self.shuffle()
    return " ".join(self.words[:number]).rstrip()
    
  def get_sentences(self, number):
    """
    Return 'number' of 4 to 6 word sentences
    """
    length = random.randint(4,6)
    sentences = ""
    for x in range(number):
      sentences += "%s. " % self.get_words(length).capitalize()
    return sentences.rstrip()

  def get_paragraphs(self, number):
    """
    Return 'number' of paragraphs with a
    5 to 7 sentences
    """
    length = random.randint(5,7)
    paragraphs = ""
    for x in range(number):
      paragraphs += "%s\n\n" % self.get_sentences(length)
    return paragraphs.rstrip()
      
      
def main():
  ml = MultiLipsum()
  print ml.get_paragraphs(1)

if __name__ == '__main__':
  main()






