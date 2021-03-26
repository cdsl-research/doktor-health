import json
from enum import Enum
from collections import namedtuple


class HealthStatus(Enum):
    GREEN = 100
    YELLOW = 200
    RED = 300

class Health(namedtuple):
    status : HealthStatus
    description : str