import re
def regex_strip(a, chars = None):
 if chars != None:
  strip_left = re.compile(r'^[' + re.escape(chars) + r']*')
  strip_right = re.compile(r'[' + re.escape(chars) + r']*$')
  a = re.sub(strip_left, "", a)   
  a = re.sub(strip_right, "", a)
 else:
  strip_left = re.compile(r'^\a*')
  strip_right = re.compile(r'\a*$')
  a = re.sub(strip_left, "", a)
  a = re.sub(strip_right, "", a)
    
 return a
a=input()
regex_strip(a)




