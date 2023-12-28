#Named Argument or Named Parameter:

def compInfo(compName,empCount):
    print(compName,":",empCount)

compInfo("Microsoft",70000)
compInfo("Amazon",50000)
compInfo("Apple",30000)
compInfo(10000,"Google")

compInfo(empCount = 10000, compName = "Google")
