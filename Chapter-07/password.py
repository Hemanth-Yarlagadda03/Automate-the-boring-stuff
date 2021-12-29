password = input("Enter your password --> ")
_num =  upper_alpha =lower_alpha =0
pass_char = False
if len(password)>=8:
  for i in password:
    if(i.isdigit()):
      _num = _num +1
    if(i.isupper()):
      upper_alpha = upper_alpha+1
    elif(i.islower()):
      lower_alpha = lower_alpha+1
    elif(ord(i) <=96 and ord(i)>=91) or (ord(i) <=48 and ord(i)>=33) or (ord(i)>=123 and ord(i)<=127):
      pass_char = True
 
if(_num>=1 and upper_alpha>=1 and lower_alpha>=1 and pass_char == True):
  print("Strong Password")
else:
  print("Weak Password")