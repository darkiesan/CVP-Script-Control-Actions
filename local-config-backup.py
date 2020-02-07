
from cvplibrary import CVPGlobalVariables,GlobalVariableNames,Device
from cvplibrary.auditlogger import alog

ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
serial = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
scriptArgs = CVPGlobalVariables.getValue(GlobalVariableNames.SCRIPT_ARGS)

message = "Running copy running-config to backup-config on device with serial %s" % ( serial )
alog(message)

switch = Device(ip)
result = switch.runCmds(["enable", "copy running-config backup-config"])
resultMessage = result[1]["response"]["message"]
alog(resultMessage)
