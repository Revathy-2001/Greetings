


st = input()
ecnt = st[1:len(st)-1]
if(ecnt == len(ecnt) * 'e'):
  e_length = len(ecnt)
  if(e_length == 1):
    print(st[0]+(ecnt+ecnt)+st[-1])
  else:
    print(st[0]+(ecnt*2)+st[-1])