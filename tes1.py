#Magician
api = dType.load()

errorString = [
'Success',
'NotFound',
'Occupied']

result = dType.ConnectDobot(api,"COM3", 115200)
print("Connect status:",errorString[result[0]])

if (result[0] == 0):
    dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    dType.SetPTPCoordinateParams(api,200,200,200,200)
    dType.SetPTPJumpParams(api, 10, 200)
    dType.SetPTPCommonParams(api, 100, 100)

while(True):
    dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
    dType.SetPTPCoordinateParams(api,200,200,200,200)
    dType.SetPTPJumpParams(api, 10, 200)
    dType.SetPTPCommonParams(api, 100, 100)
    dType.dSleep(3000)

    dType.SetPTPCmd(api, 1, 10, 280, 95, 0, 1)
    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)


    dType.SetPTPJointParams(api, 55, 55, 55, 55, 55, 55, 55, 55, 1)
    dType.SetPTPCoordinateParams(api, 55, 55, 55, 55,  1)
    dType.dSleep(3000)

    #motion circle
    dType.SetCircleCmd(api, (15,280,95,0),(10, 270, 95, 0), 3, 1)
    dType.SetPTPJointParams(api, 90, 90, 90, 90, 90, 90, 90, 90, 1)
    dType.SetPTPCoordinateParams(api, 100, 100, 100, 100,  1)

    #Ke costumer
    dType.SetPTPCmdEx(api, 2, 200, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 200, 10, (-10), 0, 1)
    dType.SetWAITCmdEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 2, 300, 10, 0, 0, 1)
    dType.SetWAITCmdEx(api, 0.1, 1)