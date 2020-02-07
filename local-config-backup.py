
from cvplibrary import CVPGlobalVariables,GlobalVariableNames,Device
from cvplibrary.auditlogger import alog
import json

ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
serial = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
scriptArgs = CVPGlobalVariables.getValue(GlobalVariableNames.SCRIPT_ARGS)

message = "Running copy running-config to backup-config on device with serial %s" % ( serial )
alog(message)

switch = Device(ip)
result = switch.runCmds(["enable", "copy running-config backup-config"])
resultMessage = result[1]["response"]["messages"]
alog(resultMessage)

outFileName = scriptArgs[ "outfile" ]

with open(outFileName, "w") as outfile:
	json.dump(resultMessage, outfile)
