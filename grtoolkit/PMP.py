# PV = Planned value
# EV = Earned value
# AC = Actual Cost
# BAC = Budget at completion
# EAC = Estimate at completion
# ETC = Estimate to complete
# VAC = Variance at completion

#Cost Variance
def CostVariance(EV,AC):
    return EV-AC
def ScheduleVariance(EV,PV):
    return 
def CostPerformanceIndex(EV,AC):
    return EV/AC
def SchedulePerformanceIndex(EV,PV):
    return EV/PV

#use *args
# def EstimateAtCompletion(**kwargs):
def EstimateAtCompletion1(AC, BottomUpEAC):
    # Method1, used if original estimate is fundamentally flawed
    return AC + BottomUpEAC
def EstimateAtCompletion2(BAC,CPI=None, EV=None, AC=None):
    # Method2, no variances from BAC or expected continued rate of spending
    # if EV and AC:
    #     return BAC/CPI
    # else:
    #     return BAC/CPI(EV,AC)
    if EV: print(EV)

#     return BAC/CPI(EV,AC)
#     return BAC/CPI
#     # Method3, used when current variances are though to be atypical of future trends
#     return AC + (BAC-EV)
#     # Method4, used when current variances are thought to be typical of future trends and project schedule constraints will influence the completion of the remaining effort
#     return AC + ((BAC - EV)/
#                 (CPI * SPI))
    # KeyCheck(kwargs,"boo")
    # if ('boo' in kwargs) and ('sugar' in kwargs):
    # if KeyCheck(kwargs,"boo"):
    #     print("scared you")
    # else:
    #     print("hoo")

def ToCompletePerformanceIndex(BAC, EV, AC):
    return (BAC-EV)/(BAC-AC) #divides the value of work remaining by the money remaining to do it
def EstimateToComplete(EAC, AC):
    return EAC - AC #or reestimate
def VarianceAtCompletion(BAC,EAC):
    return BAC - EAC


# KeyCheck = lambda kwargs,*args: args in kwargs
def KeyCheck(kwargs,*args):
    for key in kwargs:
        if not(key in args):
            return False
    return True



#Multiple names for functions
CV = CostVariance
SV = ScheduleVariance
CPI = CostPerformanceIndex
SPI = SchedulePerformanceIndex
EAC1 = EstimateAtCompletion1
EAC2 = EstimateAtCompletion2
TCPI = ToCompletePerformanceIndex
ETC = EstimateToComplete
VAC = VarianceAtCompletion

print(EAC2(26000,EV=65000,AC=75000))