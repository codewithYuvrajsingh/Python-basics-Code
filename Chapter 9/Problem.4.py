word = "donkey"
with open("donkey.txt", "r") as file:
    content = file.read()
contentnew = content.replace("donkey", "######") 
with open("donkey.txt", "w") as file:
      file.write(contentnew)   
    