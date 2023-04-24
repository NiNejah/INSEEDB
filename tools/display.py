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


def printAction(mess):
   print(color.DARKCYAN+mess+color.END)

def printWarning(mess):
   print(color.RED+mess+color.END)

def tableToString(rows , rowsName):
    page ='\n'
    for r in rowsName : 
        page += f'{r:25} |'
    page = page[:-1] + '\n'
    for i in range (len(rowsName)):
        page += "--------------------------|"
    page = page[:-1] + '\n'
    for d in rows :
        for r in rowsName :
            s = str(d[r])
            page += f'{s:25} |'
        page = page[:-1] + '\n'
    return page

def printCheers(mess):
   print (color.YELLOW+mess+color.END)

def getChoice(befformess, choices):
   ch = color.YELLOW+befformess+'\n'
   for i in range (len(choices)):
      ch += f"{(i+1):3}  -  {choices[i]} \n"
   print (ch+'\n' + color.END)
   while True :
      try :
         userCh = int(input (f"Enter your choice please (1 -> {len(choices)}) : "))
      except Exception as e :
         continue
      if not (userCh > 0 and userCh <= len(choices)):
         printWarning("Invalid choice, possible choices (1 to "+str(len(choices))+')')
      else :
         break
   return userCh