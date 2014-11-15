# AliMaster

AliMaster intends to be a utility for managing files and jobs on CERN's grid through
AliMonitor. It currently uses the commands provided by the AliEn software package. Perhaps
one day there will be python bindings to the services, but until then, AliEn (and AliROOT,
for that matter) should be installed before AliMaster (to do so, follow the guide 
[here](https://dberzano.github.io/alice/install-aliroot)).

This project uses python 3.4 with the [Tkinter](https://wiki.python.org/moin/TkInter) 
graphical toolkit.


## Installation
Right now the easiest way to install would be to use pip and this git repository. You can 
trust that the master branch will always work, while the dev branch _should_ work. To 
install the most recent stable version, use the command:

```bash
sudo pip install git+ssh://git@github.com/akubera/AliMaster.git
```

and cross your fingers. This will install a python script 'alimaster' which can be run from
the command line, and the alimaster python package, (which the alimaster script uses) which 
can be imported by any python script to send AliEn commands.

Good luck, and if you have any any issues or feature-requests, please create an issue on
[github](https://github.com/akubera/AliMaster/issues).
