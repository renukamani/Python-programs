sum = 0
count = 0
while True :
  num = input ('enter a number')
  if num == 'done' :
    break
  try :
    num = float(num)
  except :
    print ('enter a valid number')
    continue
  sum = sum + num
  count = count + 1
  avg = sum / count
print(sum,count,avg)
