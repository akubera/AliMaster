#
# alimaster/aliroot/__init__.py
#
"""
A wrapper around select aliroot classes. Maybe this will be generated
automatically by a script from the real aliroot classes, but for now
it'll be hand written classes.
"""

def aliroot_class(cls):
  cls.classname = cls.__name__
  print ("[aliroot_class]", cls, cls.classname)
  return cls

class AliRootClass():

  def __init__(self, **kargs):
    print ("[AliRootClass]")
    print (" Custom Constructor {}({})".format( __class__.__name__, ','.join(['%s = %s' % s for s in kargs.items()])))
    member_names = [v['name'] for v in self.members]
    print (" Memebers: ", member_names)
    for member in self.members:
      # print(member)
      # print ("  ",member['name'])
      setattr(self, member['name'], member['default'] if 'default' in member else None)
    for key,val in kargs.items():
      if key not in member_names: print("Unknown member set {}".format(key))
      else:
        # print ("Setting {}::{} = {}".format(__class__, key,val))
        setattr(self, key,val)

  @classmethod
  def build_from_json(cls, json):
    required_fields = {'classname'}
    if isinstance(json, str):
      from json import loads
      json = loads(json)
    has_all_fields = required_fields.issubset(json.keys())
    if not has_all_fields:
      raise "JSON missing required field(s) : {}" %  (required_fields-json.keys())
  
  def save_to_json(self):
    obj = {'classname': self.classname}
    # for
    return obj

  def write_to_json_string(self):
    from json import dumps
    return dumps(self.save_to_json())
    

from .alianalysismanager import AliAnalysisManager

