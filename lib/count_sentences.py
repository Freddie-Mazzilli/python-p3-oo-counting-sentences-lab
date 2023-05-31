
#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value=""):
    self.value = value

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    count = 0
    prev = ""
    punct = [".", "!", "?"]
    for i in self.value:
      if i in punct and not i == prev:
        count += 1
      prev = i
    return count
      
    # sentences = re.split('[.!?]', self.value)
    # non_empty_sentences = [w for w in sentences if not w == ""]
    # return len(non_empty_sentences)

  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)