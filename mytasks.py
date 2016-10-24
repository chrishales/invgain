#
# User defined tasks setup.
# Generated from buildmytask.
#

if sys.path[1] != '/home/echidna/software/invgain/v1.3':
  sys.path.insert(1, '/home/echidna/software/invgain/v1.3')
from odict import odict
if not globals().has_key('mytasks') :
  mytasks = odict()

mytasks['invgain'] = 'Invert gain solutions, overwriting caltable.'

if not globals().has_key('task_location') :
  task_location = odict()

task_location['invgain'] = '/home/echidna/software/invgain/v1.3'
import inspect
myglobals = sys._getframe(len(inspect.stack())-1).f_globals
tasksum = myglobals['tasksum'] 
for key in mytasks.keys() :
  tasksum[key] = mytasks[key]

from invgain_cli import  invgain_cli as invgain
