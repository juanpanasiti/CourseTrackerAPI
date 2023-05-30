from enum import Enum


class StatusEnum(str, Enum):
    TO_CHECK = 'to_check'
    TO_DOWNLOAD = 'to_download'
    TO_REDOWNLOAD = 'to_redownload'
    DOWNLOADED_OK = 'downloaded_ok'
    TO_IGNORE = 'to_ignore'
