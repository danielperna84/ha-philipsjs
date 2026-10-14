"""Helpers for the features of a TV."""

from typing import List, Optional, cast, overload

from .typing import SystemType


@overload
def json_feature_supported(system: Optional[SystemType], type: str) -> Optional[List[str]]:
    ...


@overload
def json_feature_supported(system: Optional[SystemType], type: str, value: str) -> Optional[bool]:
    ...


def json_feature_supported(system: Optional[SystemType], type: str, value: Optional[str] = None):
    """Check json features of a system descriptor, without a connection to the TV."""
    if system:
        features = cast(
            List[str],
            system.get("featuring", {}).get("jsonfeatures", {}).get(type, []),
        )
        if value:
            return value in features
        else:
            return features
    else:
        return None
