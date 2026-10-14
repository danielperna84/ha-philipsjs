import pytest

from haphilipsjs.data.v6 import MENUITEMS_SETTINGS_STRUCTURE
from haphilipsjs.menu import (
    get_menu_node_name,
    get_menu_node_strings,
    is_menu_node_with_value,
    is_menu_supported_on_system,
    walk_menu_nodes,
)
from haphilipsjs.typing import MenuItemsSettingsNode, MenuItemsSettingsNodeType

SLIDER: MenuItemsSettingsNode = {
    "node_id": 3,
    "type": "MULTIPLE_SLIDER",
    "string_id": "SLIDERS",
    "data": {
        "sliders": [
            {"slider_id": "RED", "slider_data": {"min": 0, "max": 10, "step_size": 1}},
            {"slider_id": "GREEN", "slider_data": {"min": 0, "max": 10, "step_size": 1}},
        ]
    },
}
LIST: MenuItemsSettingsNode = {
    "node_id": 4,
    "type": "LIST_NODE",
    "string_id": "LIST",
    "data": {"enums": [{"enum_id": 0, "string_id": "OFF"}, {"enum_id": 1, "string_id": "ON"}]},
}
MENU: MenuItemsSettingsNode = {
    "node_id": 2,
    "type": "PARENT_NODE",
    "data": {"nodes": [SLIDER, LIST]},
}
ROOT: MenuItemsSettingsNode = {
    "node_id": 1,
    "type": "PARENT_NODE",
    "string_id": "ROOT",
    "data": {"nodes": [MENU]},
}


def test_walk_menu_nodes():
    assert [[node["node_id"] for node in path] for path in walk_menu_nodes(ROOT)] == [
        [2],
        [3, 2],
        [4, 2],
    ]


def test_walk_menu_nodes_structure():
    root = MENUITEMS_SETTINGS_STRUCTURE["node"]
    paths = list(walk_menu_nodes(root))

    assert paths[0] == (root["data"]["nodes"][0],)
    assert all(
        any(path[-1] is child for child in root["data"]["nodes"]) for path in paths
    )


@pytest.mark.parametrize(
    ("node", "strings"),
    [
        (ROOT, ["ROOT"]),
        # Children without string id are skipped
        (MENU, ["SLIDERS", "LIST"]),
        (SLIDER, ["SLIDERS", "RED", "GREEN"]),
        (LIST, ["LIST", "OFF", "ON"]),
    ],
)
def test_get_menu_node_strings(node, strings):
    assert list(get_menu_node_strings(node)) == strings


def test_menu_node_type():
    assert LIST["type"] == MenuItemsSettingsNodeType.LIST_NODE


@pytest.mark.parametrize(
    ("node", "value", "name"),
    [
        (LIST, None, "List"),
        # The string id of the node wins over the current value
        (LIST, {"string_id": "Other"}, "List"),
        (MENU, {"string_id": "Menu"}, "Menu"),
        (MENU, {}, None),
        (MENU, None, None),
    ],
)
def test_get_menu_node_name(node, value, name):
    assert get_menu_node_name(node, {"LIST": "List"}, value) == name


@pytest.mark.parametrize(
    ("node", "value", "result"),
    [
        (LIST, None, True),
        (MENU, {"data": {"activenode_id": 3}}, True),
        (MENU, {"data": {}}, False),
        (MENU, {}, False),
        (MENU, None, False),
        # Parent nodes without children have nothing to choose from
        ({"node_id": 5, "type": "PARENT_NODE", "data": {}}, {"data": {"activenode_id": 3}}, False),
    ],
)
def test_is_menu_node_with_value(node, value, result):
    assert is_menu_node_with_value(node, value) is result


@pytest.mark.parametrize(
    ("system", "result"),
    [
        ({"featuring": {"jsonfeatures": {"menuitems": ["Setup_Menu"]}}}, True),
        ({"featuring": {"jsonfeatures": {"menuitems": []}}}, False),
        ({}, False),
        (None, False),
    ],
)
def test_is_menu_supported_on_system(system, result):
    assert is_menu_supported_on_system(system) is result
