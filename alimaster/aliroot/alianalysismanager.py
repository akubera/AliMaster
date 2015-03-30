#
# alimaster/aliroot/alianalysismanager.py
#

from . import (AliRootClass,aliroot_class)

@aliroot_class
class AliAnalysisManager(AliRootClass):
  """
  Manager analysis class. Allows creation of several analysis tasks and data containers
  storing their input/output. Allows connecting/chaining tasks via shared data containers.
  Serializes the current event for all tasks depending only on initial input data.
  """

  members = [
    { 'name': 'name',
      'type': str,
   'default': 'MyManager'
    },
    { 'name': 'title',
      'type': str,
   'default': ''
    },
    { 'name': 'AnalysisType',
      'type': ("kLocalAnalysis","kProofAnalysis","kGridAnalysis","kMixingAnalysis"),
   'default': "kLocalAnalysis"
    },
    { 'name': 'fTasks',
      'type': 'TObjArray*',
    'getter': 'GetTasks',
'visibility': 'protected'
    }
  ]

  def __init__(self, **kargs):
    super().__init__(**kargs)
    print("[AliAnalysisManager]")

  def AddTask(self, task):
    pass

