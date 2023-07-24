
import re
import audio as l
import string
# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
					format='%(asctime)s %(message)s',
					filemode='w+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages



class Bank:
    def __init__(self, name:string ,val:int =0 ):
        self.val=val
        self.name=name
      
    def add(self,val):
        self.val+=val
        
        
        
    def minus(self,val):
        self.val-=val
        
        
    def display(self):
        print(self.name,"balance",self.val)

def main(bank):
   
    
    ans= l.listen()
    ans=str(ans)
    k=ans.split(" ")
    flag=0
    if(ans=='-1'):
        flag=1
        logger.error("Error in Microphone")
    else :
        logger.debug(k)
    if (k[0].strip()=="minus"):
        bank.minus(int(k[1]))
        bank.display()
    elif (k[0].strip()=="add"):
        bank.add(int(k[1]))
        bank.display()
    elif( flag == 0 ):
        print("Invalid Format")
        print("Plaeas say \" Add <no> or minus <no> \" ")

if __name__ == '__main__':
    print("Initialize your account")
    val=input("Please enter balance ")
    name=input("Please enter name ")
    bank1 =Bank(name,int(val)) 
    while(1):
         main(bank1)
    