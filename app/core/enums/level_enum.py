from enum import Enum


class LevelEnum(str, Enum):
    UNDEFINED = 'undefined'
    BASIC = 'basic'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
