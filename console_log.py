with open('console.log','r') as f:
#f = open("console.log", "r")    
    for line in f:
        if "HCL Domino (r) Server (64 Bit)" in line:
            print(line)
        if "OSLoadProgram" in line :
            print(line)
        if "Server shutdown complete" in line :
            print(line)        
        if "Leaked stack" in line :
            print(line)
            
            
