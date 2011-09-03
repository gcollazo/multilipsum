#!/usr/bin/env python
# encoding: utf-8
"""
mlipsum.py

Created by Giovanni Collazo on 2011-09-03.
"""

import string
import random

class MultiLipsum:
  def __init__(self, filename):
    self.filename = filename
    self.text = self.load(filename)
    self.words = self.clean(self.text)
  
  def load(self, filename):
    f = open('text/%s.txt' % filename)
    return f.read()

  def clean(self, text):
    """
    Remove punctuation, make lowercase,
    remove line breaks and return as a
    list of distinct words
    """
    exclude = set(string.punctuation)
    self.text = ''.join(ch for ch in self.text if ch not in exclude)
    self.text = self.text.lower()
    self.text = self.text.replace('\n', '')
    return self.distinct(self.to_list(self.text))

  def distinct(self, words):
    """
    Returns a list of distinct words
    from a list of words
    """
    distinct = set()
    for w in words:
      if w not in distinct:
        distinct.add(w)
    return list(distinct)

  def to_list(self, text):
    """
    Splits a string by space and returs a list
    """
    return text.split(' ')
  
  def shuffle(self):
    random.shuffle(self.words)
    return self.words
  
  def get_words(self, number):
    """
    Return 'number' of words
    """
    self.shuffle()
    return " ".join(self.words[:number]).capitalize()
    
  def get_sentences(self, number):
    """
    Return 'number' of 4 to 6 word sentences
    """
    length = random.randint(4,6)
    sentences = ""
    for x in range(number):
      sentences += "%s. " % self.get_words(length)
    return sentences

  def get_paragraphs(self, number):
    """
    Return 'number' of paragraphs with a
    5 to 7 sentences
    """
    length = random.randint(5,7)
    paragraphs = ""
    for x in range(number):
      paragraphs += "%s\n\n" % self.get_sentences(length)
    return paragraphs
      
      
def main():
  ml = MultiLipsum('lipsum')
  
  # Words
  print ml.get_words(3)
  
  print
  
  # Sentences
  print ml.get_sentences(3)
  
  print
  
  # Paragraphs
  print ml.get_paragraphs(3)

if __name__ == '__main__':
  main()






