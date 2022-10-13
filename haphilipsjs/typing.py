from typing import Dict, List, Literal, NamedTuple, Optional, Type, TypedDict, Union


class ActivitiesChannelType(TypedDict, total=False):
    ccid: int
    name: str
    preset: str
    onid: str
    tsid: str
    sid: str
    serviceType: str
    type: str
    logoVersion: str


class ActivitiesChannelListType(TypedDict, total=False):
    id: str
    version: str


class ActivitesTVType(TypedDict, total=False):
    channel: ActivitiesChannelType
    channelList: ActivitiesChannelListType


class ChannelsCurrentType(TypedDict):
    id: str


class ComponentType(TypedDict):
    packageName: str
    className: str


class ApplicationIntentType(TypedDict, total=False):
    extras: Dict
    component: ComponentType
    action: str


class ApplicationType(TypedDict, total=False):
    label: str
    intent: ApplicationIntentType
    order: int
    id: str
    type: str


class ApplicationsType(TypedDict):
    version: int
    applications: List[ApplicationType]


class FavoriteChannelType(TypedDict):
    ccid: int
    preset: str


class FavoriteListType(TypedDict, total=False):
    id: str
    version: Union[int, str]
    parentId: str
    listType: str
    medium: str
    virtual: bool
    modifiable: bool
    name: str
    channels: List[FavoriteChannelType]


class ChannelType(TypedDict, total=False):
    ccid: int
    preset: str
    name: str


class ChannelListType(TypedDict, total=False):
    id: str
    version: Union[int, str]
    listType: str
    medium: str
    active: bool
    virtual: bool
    modifiable: bool
    Channel: List[ChannelType]


ChannelsType = Dict[str, ChannelType]


class ChannelDbTv(TypedDict, total=False):
    channelLists: List[ChannelListType]
    favoriteLists: List[FavoriteListType]


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
    companion_screen: Union[str, bool]

    # stored here on saphi
    os_type: str


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
    model: str
    model_encrypted: str
    deviceid_encrypted: str
    nettvversion: str
    epgsource: str
    api_version: Dict
    featuring: SystemFeaturingType
    notifyChange: str

    # here on android systems
    os_type: str


class SourceType(TypedDict, total=False):
    name: str


SourcesType = Dict[str, SourceType]


class SourceCurrentType(TypedDict):
    id: str


class ContextType(TypedDict, total=False):
    data: str
    level1: str
    level2: str
    level3: str

    # in some older context these exists
    activity: str
    menu: str
    Recording: str


AmbilightPixelType = Dict[Literal["r", "g", "b"], int]

AmbilightSideType = Dict[str, AmbilightPixelType]

AmbilightLayerType = Dict[Literal["left", "top", "right", "bottom"], AmbilightSideType]

AmbilightLayersType = Dict[str, AmbilightLayerType]


class AmbilightSupportedStyleType(TypedDict, total=False):
    styleName: str
    algorithms: List[str]
    maxTuning: int
    maxSpeed: int

    # Extension to get the non expert modes too
    menuSettings: List[str]


class AmbilightSupportedStylesType(TypedDict):
    supportedStyles: List[AmbilightSupportedStyleType]


class AmbilightColorType(TypedDict):
    hue: int
    saturation: int
    brightness: int


class AmbilightAudioSettingsType(TypedDict):
    color: AmbilightColorType
    colorDelta: AmbilightColorType
    tuning: int
    algorithm: str


class AmbilightColorSettingsType(TypedDict):
    color: AmbilightColorType
    colorDelta: AmbilightColorType
    speed: int
    algorithm: str


class AmbilightCurrentConfiguration(TypedDict, total=False):
    styleName: str
    isExpert: bool
    menuSetting: str
    stringValue: str

    audioSettings: AmbilightAudioSettingsType
    colorSettings: AmbilightColorSettingsType

class MenuItemsSettingsNodeDataSliderData(TypedDict):
    min: int
    max: int
    step_size: int

class MenuItemsSettingsNodeDataSlider(TypedDict):
    slider_id: str
    slider_data: MenuItemsSettingsNodeDataSliderData

class MenuItemsSettingsNodeDataEnumRequired(TypedDict):
    enum_id: int
    string_id: str

class MenuItemsSettingsNodeDataEnum(MenuItemsSettingsNodeDataEnumRequired, total=False):
    icon: Optional[str]

class MenuItemsSettingsNodeData(TypedDict, total=False):
    nodes: List["MenuItemsSettingsNode"]              # PARENT_NODE
    enums: List[MenuItemsSettingsNodeDataEnum]        # LIST_NODE
    slider_data: MenuItemsSettingsNodeDataSliderData  # SLIDER_NODE
    sliders: List[MenuItemsSettingsNodeDataSlider]    # MULTIPLE_SLIDERS
    colors: List[int]                                 # WALL_COLOR_NODE

class MenuItemsSettingsNodeRequired(TypedDict):
    node_id: int
    type: str
    data: MenuItemsSettingsNodeData

class MenuItemsSettingsNode(MenuItemsSettingsNodeRequired, total=False):
    string_id: str
    icon: Optional[str]
    context: str

class MenuItemsSettingsEntry(NamedTuple):
    node: MenuItemsSettingsNode
    parent: Optional[int]

class MenuItemsSettingsStructure(TypedDict, total=False):
    node: MenuItemsSettingsNode

class MenuItemsSettingsValueInt(TypedDict):
    value: int

class MenuItemsSettingsValueBool(TypedDict):
    value: bool

class MenuItemsSettingsValueEnumEntry(TypedDict):
    enum_id: int
    controllable: bool
    available: bool
    string_id: str

class MenuItemsSettingsValueEnumRequired(TypedDict):
    select_item: Optional[int]

class MenuItemsSettingsValueEnum(MenuItemsSettingsValueEnumRequired, total=False):
    enum_values: List[MenuItemsSettingsValueEnumEntry]

class MenuItemsSettingsValueNode(TypedDict):
    activenode_id: int

class MenuItemsSettingsValueSlider(TypedDict):
    slider_id: int
    value: int

class MenuItemsSettingsValueSliders(TypedDict):
    values: List[MenuItemsSettingsValueSlider]

MenuItemsSettingsValueData = Union[
    MenuItemsSettingsValueInt,
    MenuItemsSettingsValueBool,
    MenuItemsSettingsValueEnum,
    MenuItemsSettingsValueNode,
    MenuItemsSettingsValueSliders
]

class MenuItemsSettingsCurrentValueValue(TypedDict):
    Nodeid: int
    Controllable: bool
    Available: bool
    string_id: str
    data: MenuItemsSettingsValueData

class MenuItemsSettingsCurrentValue(TypedDict):
    value: MenuItemsSettingsCurrentValueValue

class MenuItemsSettingsCurrent(TypedDict):
    values: List[MenuItemsSettingsCurrentValue]
    version: int

class MenuItemsSettingsCurrentPostNode(TypedDict):
    nodeid: int

class MenuItemsSettingsCurrentPost(TypedDict):
    nodes: List[MenuItemsSettingsCurrentPostNode]

class MenuItemsSettingsUpdateValueValue(TypedDict):
    Nodeid: int
    data: MenuItemsSettingsValueData

class MenuItemsSettingsUpdateValue(TypedDict):
    value: MenuItemsSettingsUpdateValueValue

class MenuItemsSettingsUpdate(TypedDict):
    values: List[MenuItemsSettingsUpdateValue]

class StringsTranslation(TypedDict):
    string_id: str
    string_translation: Optional[str]

class Strings(TypedDict):
    translations: List[StringsTranslation]

class StringId(TypedDict):
    string_id: str

class StringLocale(TypedDict):
    language: str
    country: str
    variant: str

class StringsRequest(TypedDict):
    strings: List[StringId]
    locale: StringLocale
