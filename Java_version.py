# Author :- K.Lukesh Kumar
#Purpose :- Checking the Java Version of the server
#Date :- 21-Oct-2021

import sys,os

class java_check:
    def __init__(self) :
        pass
    def input_arguments(self) :
        server=str(sys.argv[1])
        platform=str(sys.argv[2])
        print(server)
        if(platform=="windows") :
             obj.windows(platform)
        elif(platform=="linux") :
            obj.linux(platform)
        else  :
            obj.aix(platform)
    def windows (self,platform) :
        print("------------------------------------------------------------------------------------")
        os.system('java -version')
    def linux (self,platform)  :
        os.chdir('/local/notesdata')
        print("---------------------------------------------------------------------------------")
        print("java version ")
        os.system('/opt/hcl/domino/notes/latest/linux/java -version')
        print("-------------------------------------------------------------------------------------")
    def aix (self,platform) :
        os.chdir('/local/notesdata')
        print("-----------------------------------------------------------------------------------------")
        print("java version")
        os.system('/opt/hcl/domino/notes/latest/ibmpow/java -version')


obj=java_check()
obj.input_arguments()

