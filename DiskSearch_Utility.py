import re
from hurry.filesize import size
import os
import time
class ccollection:
    def collection(self,starting):
        a=os.scandir(starting)
        for i in a:    
            try:
                if (i.is_file()):
                    print (i)
                    z=os.stat(i)
                    fullpath=(str(i.path)+"\\("+"file size:"+str(size(z.st_size))+")("+"time of creation:"+str(time.ctime(z.st_ctime)) +")("+("time of modification:")+str(time.ctime(z.st_mtime))+")")
                    f=open ("paths.txt","a")
                    f.write(fullpath+"\n")                                                                                                  
                    f.close
                else:
                    self.collection(   i.path)
            except   PermissionError:
                 print("permission error")
            except UnicodeEncodeError:
                print("unicode error")

class Chardisk_search:
    def __init__(self, name):
        self.__name = name

    def search(self):
        f = open("C:\\Users\\M\\Desktop\\paths.txt", "r")
        self.__path = 0
        for i in f.readlines():
            self.__a = i.find(self.__name)
            if self.__a < 0:
                pass
            else:
                self.__path = i
        if self.__path == 0:
            return "file is not here"

    def collecting_data(self):
        self.__w = re.findall("\(.*?\)", self.__path)
        self.dir = self.__path[:(self.__path.find("("))]
        for i in range(len(self.__w)):
            if i == 0:
                self.size = self.__w[i]
            if i == 1:
                self.ctime = self.__w[i]
            if i == 2:
                self.mtime = self.__w[i]

    def display(self):
        print("Name:"+self.__name)
        print(self.size)
        print(self.ctime)
        print(self.mtime)
        print("Directory"+self.dir)

def  procedure():
 Condition = True
 while Condition:
        n = str(input("Enter file name:"))
        obj = Chardisk_search(n)
        x = obj.search()
        if x == "file is not here":
            print("give filename is not exist")
            if (str(input("End program?"))) == "y":
                Condition = False
            else:
                pass
        else:
            obj.collecting_data()
            obj.display()
            if (str(input("End program?"))) == "y":
                Condition = False


path="C:\\Users\\M\\Desktop\\paths.txt"
isExists=os.path.exists(path)
if isExists:
    procedure()
else:
    ob1=ccollection()
    ob1.collection(r"C:\\")
    procedure()