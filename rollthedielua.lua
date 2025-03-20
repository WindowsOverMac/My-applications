math.randomseed(os.time())
print("Roll the die?")
local userinput = io.read()

if userinput == "yes" or userinput == "Yes" or userinput == "ye" or userinput =="Ye" or userinput == "Y" or userinput == "y" or userinput =="Sure" or userinput == "sure" then
  local die_roll = math.random(1, 20)
  print(die_roll)
else
  print("Not rolled.")
  end
