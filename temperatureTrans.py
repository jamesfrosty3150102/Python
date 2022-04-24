import sys

def tempK(temp):
    temp_k = float(temp)+273.13
    return str(temp_k)

if __name__=="__main__":
    print("main")
    temp = sys.argv[1]
    #print("absolute temperature:",tempK(temp))
    print(tempK(temp))    
    #print(temp)
#temp = input("please enter a number")
#temp = sys.argv[0]
#print("absolute temperature:",tempK(temp))