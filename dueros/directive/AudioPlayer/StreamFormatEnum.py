# encoding: utf8

from enum import Enum, unique


@unique
class StreamFormatEnum(Enum):
    STREAM_FORMAT_MP3 = 'AUDIO_MP3'
    STREAM_FORMAT_M3U8 = 'AUDIO_M3U8'
    STREAM_FORMAT_M4A = 'AUDIO_M4A'

    @staticmethod
    def inEnum(streamFormat):
        return streamFormat in StreamFormatEnum.__members__.values()

    pass

