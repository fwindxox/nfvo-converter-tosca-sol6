
from .ToscaModel import ToscaModel
from .ToscaElement import ToscaElement
from .VNF import VNF
# Import this so it's accessed like VDU.VDU
# Import these so they are accessed via VDU.Compute
from .vdu_model.VDU import VDU
from .vdu_model.Storage import Storage
from .vdu_model.Compute import Compute
from .vdu_model.ConnectionPoint import ConnectionPoint

