def isvalidchess(board_dict):
 board_keys = {'a1':'','a2':'','a3':'','a4':'','a5':'','a6':'','a7':'','a8':'',
                   'b1':'','b2':'','b3':'','b4':'','b5':'','b6':'','b7':'','b8':'',
                   'c1':'','c2':'','c3':'','c4':'','c5':'','c6':'','c7':'','c8':'',
                   'd1':'','d2':'','d3':'','d4':'','d5':'','d6':'','d7':'','d8':'',
                   'e1':'','e2':'','e3':'','e4':'','e5':'','e6':'','e7':'','e8':'',
                   'f1':'','f2':'','f3':'','f4':'','f5':'','f6':'','f7':'','f8':'',
                   'g1':'','g2':'','g3':'','g4':'','g5':'','g6':'','g7':'','g8':'',
                   'h1':'','h2':'','h3':'','h4':'','h5':'','h6':'','h7':'','h8':''}
    
 if 'bking' not in board_dict.values() or 'wking' not in board_dict.values():
  return False
 bking=0
 wking=0
 for king in board_dict.values():
  if king=='bking':
   bking+=1
  if king=='wking':
   wking+=1
 if bking > 1 or wking > 1:
  return False 
 whites=0
 blacks=0
 for item in board_dict.values():
  if item[0]=='w':
   whites+=1
  elif item[0]=='b':
   blacks+=1
 if blacks>=17 or whites>=17:
  return False
 white_pawn = 0
 black_pawn = 0
 for p in board_dict.values():
  if p == 'bpawn':
   black_pawn += 1
  elif p == 'wpawn':
   white_pawn+= 1
 if white_pawn > 8 or black_pawn > 8:
  return False

 for v in board_dict.keys():
  if v not in board_keys.keys():
    return False
 for pieces in board_dict.values():
  if pieces[0] != "b" and pieces[0] != "w":
   return False
 piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
 for names in board_dict.values():
  if names[1:] not in piece_names:
   return False

 return True

n = int(input())
board_dict = dict(input().split() for _ in range(n))
print(board_dict,'This is what you typed')

print(isvalidchess(board_dict))