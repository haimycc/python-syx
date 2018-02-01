import os
import sys
print("main process (%s) start" % os.getpid())
pid=os.fork()
if pid==0:
    print("I'm child process (%s) and my parent process is %s" % (os.getpid(),os.getppid()))
    sys.exit(0)
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    sys.exit(0)
