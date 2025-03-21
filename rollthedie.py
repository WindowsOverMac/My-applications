import random
print("Roll the dice?")

userinput = input()

if  userinput in ["Yes","Yeah","Yup","Si","Sure","yes","yeah","si","sure","ye","Ye","y","Y"]:
  random_int = random.randint(1, 50)
  print(random_int)
else:
  print("Not rolled. Either denied or invalid syntax.")
  
  

  
  




























