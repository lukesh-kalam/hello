# Author :- K.Lukesh Kumar
#Purpose :- Collecting leak stack from the console file
#Date :- 11-Nov-2021

import os,sys

class leak_search() :
    def __init__(self) :
        pass 
    def input_argumnets (self) :
        server_name=sys.argv[1]
        search_file=sys.argv[2]
        #platform=sys.argv[3]
        print(server_name)
        print(search_file)
    #    print(platform)
        print("Current working directory: {0}".format(os.getcwd()))
        with open("working_leak.properties","r") as lines:
            for line in lines :
                if server_name in line :
                    a=line.split('=')
                    b=a[1]
                    c=b.rstrip("\n")
                    os.chdir(c)
                if "search_domino_version" in line :
                    hello = line.split("=")
                    version=str(hello[1])
                    version1=version.rstrip("\n")
                if "search_osload_program" in line :
                    hi=line.split('=')
                    osload=str(hi[1])
                    osload1=osload.rstrip("\n")
                if "search_server_shutdown" in line :
                    hey=line.split('=')
                    shutdown=str(hey[1])
                    shutdown1=shutdown.rstrip("\n")
        files=os.path.isfile(search_file)
        if files==True :
            print("Console files exist with name :- " ,search_file,"exists here ")
            obj.search_leaks(search_file,shutdown1,osload1,version1)
        else :
            print("Console file not found here please check the spelling and try again")
    def search_leaks(self,search_file,shutdown1,osload1,version1) :
        self.search_file=search_file
        self.shutdown1=shutdown1
        self.osload1=osload1
        self.version1=version1
        server_shutdown=1                
        with open (search_file, "r") as ifile : 
            for line in ifile :
                # checking Domino Version
                if version1 in line:
                    print(line)
                # checking for OSLOADProgram
                if osload1 in line :
                    print(line)
                # checking for server shutdown
                if shutdown1 in line :
                    print(line)
                    server_shutdown=server_shutdown+1                    
        # Checking total number of lines in the file
        file = open(search_file,"r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1
        if server_shutdown!= 1 :
            f = open(search_file,'r')
            leak_line=0
            line_num = 0
            search_phrase = "Server shutdown complete"
            for line in f.readlines():
                line_num += 1
                if line.find(search_phrase) >= 0:
            #        print(line_num)
                    break 
            leak_line=line_num-1
            file = open(search_file,'r')
            all_lines = file.readlines()
            # Here I am printing the leaks by taking server shutdown as reference string as refrence
            for i in range (leak_line,Counter) :
                print(all_lines[i])
        else  :
            print("Server shut keyword is not found I think server still up and running")

obj=leak_search()
obj.input_argumnets()
