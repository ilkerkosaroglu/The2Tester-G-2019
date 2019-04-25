# -*- coding: utf-8 -*-
from __future__ import print_function
import mpmath
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication,implicit_application
transformations = (standard_transformations + (implicit_multiplication,  implicit_application))
from colorama import *
import time
import subprocess
import sys
import os

init() #colorama
x=Symbol("x") #sympy

flagplatform=0
if os.name=="nt":
    flagplatform=1
else:import readline

#EPS=1e-1
try:
    pv=2
    type(raw_input)
except:
    pv=3

def res():
    return Style.RESET_ALL
if len(sys.argv)<=1:
    print("Need to specify executable!")
    sys.exit()
try:
    with open(sys.argv[1],"r") as f:
        pass
except:
    print("There is no file named \""+sys.argv[1]+"\"")
    sys.exit()

def parse(st):
    st=st.replace("sinh"," sh")
    st=st.replace("cosh"," ch")
    st=st.replace("sin"," sin(x)")
    st=st.replace("cos"," cos(x)")
    st=st.replace("tan"," tan(x)")
    st=st.replace("sh"," sinh(x)")
    st=st.replace("ch"," cosh(x)")
    st=st.replace("ln"," ln(x)")
    st=st.replace("X"," x")
    st=st.replace("ˆ"," **")
    st=st.replace("^"," **")
    return st.strip()
def reverseParse(st):
    st=st.replace("sin(x)","sin")
    st=st.replace("cos(x)","cos")
    st=st.replace("tan(x)","tan")
    st=st.replace("sinh(x)","sh")
    st=st.replace("cosh(x)","ch")
    st=st.replace("ln(x)","ln")
    st=st.replace("x","X")
    st=st.replace("**","^")
    return st.strip()
def halfparse(st):
    st=st.replace("ˆ","^")
    return st.strip()
"""
def check(orgst,st2):
    ANS=[]
    L=[]
    i=0
    while i<2:
        ANS.append(eval(orgst.replace("x",str(i))))
        L.append(eval(st2.replace("x",str(i))))
        i+=0.001
    for k in range(10):
        k=float(k)
        ANS.append(eval(orgst.replace("x",str(k))))
        L.append(eval(st2.replace("x",str(k))))
    BL=[]
    for i,x in enumerate(ANS):
        try:
            if x - L[i] < EPS:
                BL.append(1) #YES
            else:
                # print x,L[i]
                BL.append(0) #NO
        except:
            if x == L[i]:
                BL.append(1) #YES
            else:
                BL.append(0) #NO
    sum=0
    for i in BL:
        sum+=i
    # print BL
    # print ANS
    # print L
    print 1.0*sum/len(BL)
    return sum>=(98/100.0)*len(BL)
"""
def checksimple(st,st2):
    return (simplify(eval(st)-eval(st2))==0)
def simple(st,st2):
    return (simplify(eval(st)-eval(st2)))

def y(st):
    return Fore.YELLOW+Style.BRIGHT+st+res()
def g(st):
    return Fore.GREEN+Style.BRIGHT+st+res()
def r(st):
    return Fore.RED+Style.BRIGHT+st+res()
def box(st):
    print ( "-"*4+"-"*len(st),"\n|",st,"|\n"+"-"*len(st)+"-"*4 )

##MAIN
count=1
corcount=0
wrocount=0

print("a tester by")
time.sleep(0.2)
print(Style.BRIGHT + g("#ilkerkosaroglu") + res())
time.sleep(1.2)
print(".")
print("\ngood luck!")
print()
time.sleep(1)
print(Style.BRIGHT+"!Press Ctrl+C to finish.!"+res())
print("type in any equation (you can enter python compatible operations, i.e. x**3):")
try:
    while True:
        if pv==2:
            inp=raw_input("eq #{}:\n".format(count))
        else:
            inp=input("eq #{}:\n".format(count))
        if not inp:continue
        if inp=="A" or inp=="a":
            inp="(X^2-1)*tan - ln^2 /X"
        inp=reverseParse(inp)
        # time.sleep(0.5)
        print("\n"*3)
        print(Style.BRIGHT+'\033[4m'+"TESTCASE #{}: ".format(count)+res())
        time.sleep(0.5)
        count+=1
        originalEq=inp.strip()
        derEq=str(parse_expr(parse(originalEq),transformations=transformations,evaluate=False).diff())
        originalEq=halfparse(originalEq)
        derEq=derEq.replace(" ","")
        derEq=derEq.replace("log","ln")

        print(y("Original equation:"))
        box(reverseParse(originalEq))
        pprint(parse_expr(parse(originalEq),transformations=transformations,evaluate=False),use_unicode=False)
        print("---"*5,"\n")
        time.sleep(1)

        print(y("Derivative:"))
        box(reverseParse(derEq))
        pprint(eval(derEq),use_unicode=False)
        print("---"*5,"\n")
        time.sleep(1)


        process = subprocess.Popen([("" if flagplatform else "./") + sys.argv[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.stdin.write(reverseParse(originalEq).encode('utf-8'))
        fromuser = process.communicate()[0].strip().decode('utf-8')
        process.stdin.close()
        # fromuser=eval(originalEq).diff()

        print(y("Your calculation:"))
        temp=str(fromuser).replace("log","ln")
        box(temp)
        temp=parse(temp)
        temp2=parse_expr(temp,transformations=transformations,evaluate=False)
        pprint(temp2,use_unicode=False)
        time.sleep(1)

        print("\033[1;37;40m *** "+res())
        time.sleep(0.1)
        print(y("..."))
        time.sleep(0.4)

        result=checksimple(str(temp2),derEq)

        if result:
            print(g("-------\nCorrect\n-------\n"))
            corcount+=1
        else:
            print(r("-----\nWrong\n-----\n"))
            print(y("Difference:"),end="")
            pprint(simple(derEq,temp2),use_unicode=False)
            wrocount+=1
        time.sleep(0.5)
except EOFError:
    try:
        print ("\t")
    except KeyboardInterrupt:
        try:
            print ("\t")
        except:
            pass
except KeyboardInterrupt:
    try:
        print ("\t")
    except:
        pass
print()
if corcount>=wrocount:
    print(g("{} correct out of: {}").format(corcount,count-1))
else:
    print(r("{} correct out of: {}").format(corcount,count-1))
print(y("---"))
