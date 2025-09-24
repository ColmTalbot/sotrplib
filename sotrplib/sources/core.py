"""
Core searches for known sources in a map (forced photometry) and
unknown sources in a map (blind search)
"""

from abc import ABC, abstractmethod

from pixell import enmap

from sotrplib.maps.core import ProcessableMap
from sotrplib.sources.sources import (
    MeasuredSource,
    RegisteredSource,
)


class ForcedPhotometryProvider(ABC):
    # thumbnail now attribute of MeasuredSource
    @abstractmethod
    def force_source(
        self,
        input_map: ProcessableMap,
        source: RegisteredSource,
    ) -> MeasuredSource:
        raise NotImplementedError

    def force(
        self,
        input_map: ProcessableMap,
        sources: list[RegisteredSource],
    ) -> list[MeasuredSource]:
        return [self.force_source(input_map, source) for source in sources]


class BlindSearchProvider(ABC):
    @abstractmethod
    def search(
        self,
        input_map: ProcessableMap,
    ) -> tuple[list[MeasuredSource], list[enmap.ndmap]]:
        return [], []
