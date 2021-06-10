import inspect
import math
from datetime import datetime, date
from alt4.proto.definitions_pb2 import Log, Claim
from alt4.settings import get_mode, get_source, get_auth_token
from alt4.grouping import get_group


def get_claim(name, value):
    _type = Claim.Type.STRING
    if isinstance(value, (int, float)):
        _type = Claim.Type.NUMBER
    elif isinstance(value, (datetime, date)):
        if isinstance(value, date):
            value = datetime.combine(value, datetime.min.time())
        _type = Claim.Type.TIMESTAMP
        value = math.floor(value.timestamp() * 1000000000)
    elif isinstance(value, bool):
        _type = Claim.Type.BOOLEAN
    else:
        value = str(value)
    return Claim(type=_type, name=name, value=value)


def write_log(call_depth, as_group, message, claims, level, log_time):
    timestamp = math.floor(log_time.timestamp() * 1000000000)
    frame = inspect.stack()[call_depth]
    alt4claims = []
    if isinstance(claims, dict):
        for key, value in claims.items():
            alt4claims.append(get_claim(key, value))

    msg = Log(source=get_source(), thread=get_group(), message=message, claims=alt4claims,
              function=frame.function, file=frame.filename, line=frame.lineno,
              level=level, timestamp=timestamp, group=as_group)
