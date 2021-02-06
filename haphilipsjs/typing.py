from typing import Dict, List, Optional, TypedDict, Union

class ActivitiesChannelType(TypedDict):
    ccid: int
    name: str
    preset: str

class ActivitiesChannelListType(TypedDict):
    id: str
    version: str

class ActivitesTVType(TypedDict):
    channel: ActivitiesChannelType
    channelList: ActivitiesChannelListType

class ChannelsCurrentType(TypedDict):
    id: str

class ComponentType(TypedDict):
    packageName: str
    className: str

class ApplicationIntentType(TypedDict, total=False):
    component: ComponentType
    action: str

class ApplicationType(TypedDict):
    label: str
    intent: ApplicationIntentType
    order: int
    id: str
    type: str

class ApplicationsType(TypedDict):
    version: int
    applications: List[ApplicationType]


class FavoriteType(TypedDict, total=True):
    id: str
    version: Union[int, str]
    parentId: str
    listType: str
    medium: str
    virtual: bool
    modifiable: bool
    name: str

class ChannelType(TypedDict, total=False):
    ccid: int
    preset: str
    name: str

class ChannelListType(TypedDict):
    id: str
    version: int
    listType: str
    medium: str
    active: bool
    virtual: bool
    modifiable: bool
    Channel: List[ChannelType]

class ChannelDbTv(TypedDict):
    channelLists: List[ChannelListType]
    favoriteLists: List[FavoriteType]

class JsonFeaturesType(TypedDict, total=False):
    editfavorites: List[str]
    recordings: List[str]
    ambilight: List[str]
    menuitems: List[str]
    textentry: List[str]
    applications: List[str]
    pointer: List[str]
    inputkey: List[str]
    activities: List[str]
    channels: List[str]
    mappings: List[str]

class SystemFeaturesType(TypedDict, total=False):
    tvtype: str
    content: List[str]
    tvsearch: str
    pairing_type: str
    secured_transport: str
    companion_screen: str
class SystemFeaturingType(TypedDict):
    jsonfeatures: JsonFeaturesType
    systemfeatures: SystemFeaturesType

class SystemType(TypedDict, total=False):
    menulanguage: str
    name: str
    country: str
    serialnumber: str
    serialnumber_encrypted: str
    softwareversion: str
    softwareversion_encrypted: str
    model_encrypted: str
    deviceid_encrypted: str
    nettvversion: str
    epgsource: str
    api_version: Dict
    featuring: SystemFeaturingType
    notifyChange: str
    os_type: str