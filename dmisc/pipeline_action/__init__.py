from sys import stderr
import subprocess

# running in shell
def runProcess(command, samplename):
    stderr.write('[%s] Running %s\n' %(samplename, command))
    result = subprocess.call('time ' + command, shell=True)
    stderr.write('[%s] Finished %s\n' %(samplename, command))
    return 0
