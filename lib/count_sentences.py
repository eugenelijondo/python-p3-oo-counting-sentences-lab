#!/usr/bin/env python3

class MyString:
  def __init__(self, value):
        self.value = value

  def is_sentence(self):
        if isinstance(self.value, str):
            return self.value.endswith('.')
        else:
            print("The value must be a string.")
            return False

  def is_question(self):
        if isinstance(self.value, str):
            return self.value.endswith('?')
        else:
            print("The value must be a string.")
            return False

  def is_exclamation(self):
        if isinstance(self.value, str):
            return self.value.endswith('!')
        else:
            print("The value must be a string.")
            return False

  def count_sentences(self):
        if isinstance(self.value, str):
            return self.value.count('.') + self.value.count('?') + self.value.count('!')
        else:
            print("The value must be a string.")
            return 0
  pass
