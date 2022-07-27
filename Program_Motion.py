#Magician
def screensaver():
    #screen saver
    dType.SetPTPCmdEx(api, 0, 235, 185, 29, 0, 1)
    dType.SetPTPCmdEx(api, 0, 230, -185, 29, 0, 1)
    dType.SetPTPCmdEx(api, 0, 185, -155, 35, 0, 1)
    dType.SetPTPCmdEx(api, 0, 225, 105, 35, 0, 1)
    dType.dSleep(1000)

    #cone
    dType.SetPTPCmdEx(api, 1,-10, -260, 60, 0, 1)  

def motion1():
    dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)

def circle():
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)
    #motion circle
    dType.SetCircleCmd(api, (15,280,95,0),(10, 270, 95, 0), 3, 1)

def motion3():
    dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)
    
    #Ke costumer
    dType.SetPTPCmd(api, 1, 210, -175, -40, 0, 1)


def cone_loader():
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 60, 0, 1)
    dType.SetPTPCmd(api, 1, 26.8, -248.6, 30, 0, 1)
    dType.SetPTPCmd(api, 1, 200, 0, 30, 0, 1)

def pre_cone():
    dType.SetPTPCmd(api, 1, 40, 195, 78, 0, 1)  
    dType.SetPTPCmd(api, 1, 17, 262, 93, 0, 1)   

def home():
    dType.SetPTPCmd(api, 1, 200, 0, 30, 0, 1)    

def cost():
    # dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1) 
    dType.SetPTPCmd(api, 1, 131, -243, 59, 0, 1)
    dType.SetPTPCmd(api, 1, 131, -243, 5.9, 0, 1) 

def customer():
    dType.SetPTPCmdEx(api, 2, 200, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 200, 10, (-10), 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 300, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 0.1, 1)

while (True):
    pre_cone()
    circle()
    home()
    dType.dSleep(1000)
    

  