a = int(input("Give a number = "))
b = int(input("Give a number = "))
c = int(input("Give a number = "))
if a + b >= c:
  if a + c >= b:
    if b + c >= a:
      print("It forms a triangle")
else:
  print("It does not form a traingle")
