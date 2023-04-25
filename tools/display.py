
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m' # acction 
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m' # welcome 
   RED = '\033[91m' # error 
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def printAction(mess:str):
   print(color.DARKCYAN+mess+color.END)

def printWarning(mess):
   print(color.RED+mess+color.END)

def printCheers(mess):
   print (color.YELLOW+mess+color.END)

# This function takes a list of dictionaries and a list of strings as input, 
# representing the rows of a table and the names of the columns, respectively. 
# It converts the table to a string representation and returns it.
def tableToString(rows , rowsName):
    page ='\n'
    for r in rowsName : 
        page += f'{r:25} |'
    page = page[:-1] + '\n'
    for i in range (len(rowsName)):
        page += "--------------------------+"
    page = page[:-1] + '\n'
    for d in rows :
        for r in rowsName :
            s = str(d[r])
            page += f'{s:25} |'
        page = page[:-1] + '\n'
    return page

# This function takes a message and a list of strings as input, 
# representing the prompt message and the available choices, respectively. 
# It prints the message and the choices in yellow color, then prompts the user to enter their choice. 
# It returns the user's choice as an integer.
def getChoice(title, choices):
   ch = color.YELLOW+title+'\n'
   for i in range (len(choices)):
      ch += f"{(i+1):3}  -  {choices[i]} \n"
   print (ch+'\n' + color.END)
   while True :
      try :
         userCh = int(input (f"Enter your choice please (1 -> {len(choices)}) : "))
      except Exception as e :
         printWarning("Invalid choice, possible choices (1 to "+str(len(choices))+')')
         continue
      if not (userCh > 0 and userCh <= len(choices)):
         printWarning("Invalid choice, possible choices (1 to "+str(len(choices))+')')
      else :
         break
   return userCh

def getPeriodFromCategory(category:str):
   words = category.split()
   return (words[2], words[4])