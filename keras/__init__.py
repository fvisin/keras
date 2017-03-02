from __future__ import absolute_import
from . import backend
from . import datasets
from . import engine
from . import layers
from . import preprocessing
from . import utils
from . import wrappers
from . import callbacks
from . import constraints
from . import initializations
from . import metrics
from . import models
from . import objectives
from . import optimizers
from . import regularizers

from subprocess import check_output

__version__ = check_output('git rev-parse HEAD',
                           shell=True).strip().decode('ascii')
