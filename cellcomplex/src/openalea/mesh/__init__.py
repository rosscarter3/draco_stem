
# Redirect path
import os

cdir = os.path.dirname(__file__)
pdir = os.path.join(cdir, "../cellcomplex/property_topomesh")
pdir = os.path.abspath(pdir)

__path__ = [pdir] + __path__[:]

from openalea.my_mesh.__init__ import *
