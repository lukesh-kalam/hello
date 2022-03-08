# Author  :- K.Lukesh Kumar
# Date  :- 13-Jan-2022
# Purpose :- Basic usage to check the error from the csv file  

import os,sys
import datetime

now = datetime.datetime.now()
sort_array=[]
check_error=[]
error_count_array=[]
head=0
count=0
error_count=int(0)


class csv_error_check() :
    def __init__(self) :
        pass
    # Consuming the input arguments and fetch file exists or not
    def input_arguments(self) :
        count=0
        arguments_error_list=[]
        argvs=sys.argv[1]
        search_file=sys.argv[2]
        new_path=sys.argv[3]
        os.chdir(new_path)
        for i in range(len(argvs)) :
            if argvs[i] == "," :
                count=count+1
        print(count)
        line=argvs.split(',')
        for j in range(count+1) :
            print(line[j])
            separator=str(',')+line[j]+str(',')
            arguments_error_list.append(separator)
        print(arguments_error_list)
        print(len(arguments_error_list))
        files=os.path.isfile(search_file)
        if files==True :
            print(" files exist with name :- " ,search_file,"exists here ")
            obj.view_error(arguments_error_list)
        else :
            print("file not found here please check the spelling and try again")
    # print the error arguents passed from command line 
    def view_error(self,arguments_error_list) :
        self.arguments_error_list=arguments_error_list
        for i in range(len(arguments_error_list)) :
            print(arguments_error_list[i])
        obj.error_count(arguments_error_list)
    # count the error argumants passed 
    def error_count(self,arguments_error_list) :
        self.arguments_error_list=arguments_error_list
        search_file=sys.argv[2]
        error_count=0
        error_count_array=[]
        for i in range(len(arguments_error_list)) :
            with open(search_file,'r') as lines :
                for line in lines :
                    if arguments_error_list[i] in line :
                        error_count=error_count+1
            print("Count of errors with message  ",arguments_error_list[i],"are",error_count)
            error_count_array.append(error_count)
        obj.print_error(error_count,error_count_array,arguments_error_list)
    # Adding all the error messaged lines into the list
    def print_error(self,error_count,error_count_array,arguments_error_list) :
        self.error_count=error_count
        self.arguments_error_list=arguments_error_list
        self.error_count_array=error_count_array
        search_file=sys.argv[2]
        head=0
        check_error=[]
        
        for i in range(len(arguments_error_list)) :
            with open (search_file, "r") as ifile : 
                for line in ifile :
                    if head==0 :
                        line=line.replace(','," ")
                        print("Printing results for :- ",arguments_error_list[i])
                        print(line)
                        head_line=line
                        head=head+1
                    if arguments_error_list[i] in  line :
                        error_count +=error_count
                        line=line.replace(','," ")
                        sort_array.append(line)
                        if line not in check_error :
                            check_error.append(line)
                            line=line.replace(','," ")
                            print(line)
            head=0
        obj.writing_new_file(error_count_array,check_error,arguments_error_list,head_line)
    # Create new file with time stamp and write all the error lines into that
    def writing_new_file(self,error_count_array,check_error,arguments_error_list,head_line) :
        self.error_count_array=error_count_array
        self.head_line=head_line
        self.check_error=check_error
        self.arguments_error_list=arguments_error_list
        print(error_count_array)
        time1=now.strftime("%Y_%m_%d_%H_%M_%S")
        a="error_csv"
        b=str(time1)
        c=".txt"
        new_file=str(a)+b+str(c)
        print(" Creating file with the name :- ",new_file)
        f=open(new_file,"w")
        for i in range(len(error_count_array)) :
            print(error_count_array[i])
        #print(head_array)
        f.write(head_line)
        for i in range(len(check_error)) :
            f.write(check_error[i])
        for i in range(len(error_count_array)):
            f.write("Count of errors with message ")
            f.write(arguments_error_list[i])
            f.write("are")
            f.write(str(error_count_array[i]))
            f.write("\n")
        f.close()

obj=csv_error_check()
obj.input_arguments()
