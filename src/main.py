import os
import sys
import platform

global var
global inner_log
global imports
global av_imports

var = {}
inner_log = ["Welcome to the Inner Log"]
imports = []
av_imports = []

# About
kernel_version = 0.2
kernel_cmds = 0.01
kernel_platform = platform.platform()
kernel_about = f"Builders Intelligence is running threw the Cyclone Kernel via Python\nKernel Version: {kernel_version} Code Platform: {kernel_cmds}\n{kernel_platform}"

def var_add(varname="Variable Required", data="Data Required"):
    var[varname] = data

def var_get(varname):
    try:
        product = var[varname]
    except Exception as e:
        print(f"[BuildersIntelligence] Code 11")
        product = "Uh Oh"
    return product

def runcmd(cmd):
    if cmd["type"]=="#":
        pass
    elif cmd["type"].lower()=="print":
        print(cmd["args"][0])
    elif cmd["type"].lower()=="var":
        if cmd["args"][1]=="=":
            var_add(cmd["args"][0], cmd["args"][2])
    elif cmd["type"].lower()=="os":
        if cmd["args"][0]=="system":
            os.system(cmd["args"][1])
    elif cmd["type"].lower()=="kernel":
        if cmd["args"][0].lower()=="about":
            print(kernel_about)
    else: print(f"[BuildersIntelligence] Command \u001b[4m"+cmd["type"]+"\u001b[0m is not Valid")

def semiparse(file):
    file = (file+" ")
    preproduct = ""
    product = None
    quote = False
    for i in range(len(file)):
        if file[i]==" ":
            if product==None:
                product = {
                    "type": preproduct,
                    "args": []
                }
                preproduct = ""
            elif quote==False:
                product["args"].append(preproduct)
                preproduct = ""
            elif quote==True:
                preproduct = (preproduct+file[i])
        else:
            if file[i]!="\"":
                preproduct = (preproduct+file[i])
            else:
                if quote==False:
                    quote = True
                elif quote==True:
                    quote = False
    return product

def scriptparse(file):
    preproduct = ""
    product = []
    for i in range(len(file)):
        if file[i]=="\n":
            product.append(preproduct)
            preproduct = ""
        else:
            preproduct = (preproduct+file[i])
    product.append(preproduct)
    return product

def runscript(file):
    arrayparsed = scriptparse(file)
    for i in range(len(arrayparsed)):
        runcmd(semiparse(arrayparsed[i]))

while True:
    runscript(open(input("File>>> ")).read())
