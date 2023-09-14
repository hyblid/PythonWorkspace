import os
    
def how_many_different_numbers(*args):
    print(len(set(args)))


#return {} is set
def different_ips():
    return {one_line.split()[0]
            for one_line in open("apach_err_log.txt")}

def error_code():
    err = {}
    for one_line in open("apach_err_log.txt"):
        if one_line.split()[5] == "200":
            err[one_line.split()[0]]= "OK"
        else:
            err[one_line.split()[0]]= "ERROR" 
    return err     

def file_exetention():
    return { lst [-3:] for lst in os.listdir() }

print(file_exetention())
    