#!/usr/bin/python
import sys
def resetdata():
    return [3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,64,225,1101,15,56,225,1,14,153,224,101,-147,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,2,162,188,224,101,-2014,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1001,18,81,224,1001,224,-137,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,16,16,224,101,-256,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,101,48,217,224,1001,224,-125,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1002,158,22,224,1001,224,-1540,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,83,31,225,1101,56,70,225,1101,13,38,225,102,36,192,224,1001,224,-3312,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1102,75,53,225,1101,14,92,225,1101,7,66,224,101,-73,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,77,60,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,614,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]
    return [3,3,1105,-1,9,1101,0,0,12,4,12,99,1] # ex6, jump immediate
    return [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9] # ex5, 1st Jump test
    return [3,3,1107,-1,8,3,4,3,99] # ex4
    return [3,3,1108,-1,8,3,4,3,99] # ex3
    return [3,9,7,9,10,9,4,9,99,-1,8] # ex2
    return [3,9,8,9,10,9,4,9,99,-1,8] # ex1
    return [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
def getinput():
    if len(sys.argv) > 1:
        return int(sys.argv[1])
    return 5 # CHANGE INPUT HERE, or pass it to the program
def processa(mydata):
    lenmydata = len(mydata)
    # keeping this here speeds up the big loop tons
    #print(mydata)
    mydata[mydata[1]] = getinput()
    i = 2
    while (i < lenmydata and mydata[i] != 99 ):
        #print(mydata)
        oc = mydata[i]%10
        if mydata[i] > 100 and int(mydata[i]/100)%10 == 1:
            p1 = 1 # immediate
        else:
            p1 = 0 # positional
        if mydata[i] > 1000:
            p2 = 1
        else:
            p2 = 0
        if (4 == oc):
            if p1:
                dout = mydata[i+1]
            else:
                dout = mydata[mydata[i+1]]
            print("diag output, 0 good: {}".format(dout))
            i += 2
#        elif (3 == oc):
#            mydata[mydata[i+1]] = 8 # input value
#            i += 2
        else:
            a = mydata[i+1]
            b = mydata[i+2]
            p = mydata[i+3] # always positional
            #print ("setof4 ocfull:{},a:{},b:{},p:{},|,p1:{},p2:{}".format(mydata[i],a,b,p,p1,p2))
            # 000oo
            if p1:
                av = a
            else:
                av = mydata[a]
            if p2:
                bv = b
            else:
                bv = mydata[b]
            #print ("av,bv={},{}".format(av,bv))
            if (1 == oc):
                mydata[p] = av + bv
                i += 4
            elif (2 == oc):
                mydata[p] = av * bv
                i += 4
            elif (5 == oc):
                # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
                # Otherwise, it does nothing.
                if 0 != av:
                    i = bv
                else:
                    i += 3
            elif (6 == oc):
                #    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
                # Otherwise, it does nothing.
                if 0 == av:
                    i = bv
                else:
                    i += 3
            elif (7 == oc):
                #    Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
                # Otherwise, it stores 0.
                if av < bv:
                    mydata[p] = 1
                    i += 4
                else:
                    mydata[p] = 0
                    i += 4
            elif (8 == oc):
                #    Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
                # Otherwise, it stores 0.
                if av == bv:
                    mydata[p] = 1
                    i += 4
                else:
                    mydata[p] = 0
                    i += 4
            else:
                i += 1 
if __name__ == "__main__":
    mydata = resetdata()
    processa(mydata)
    # 7988899 is to low
