from enum import Enum


class RoleEnum(str, Enum):
    ADMIN = 'admin'
    PRIVILEGED = 'privileged'
    COMMON = 'common'
    UNCONFIRMED = 'unconfirmed'
