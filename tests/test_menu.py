import pytest

from haphilipsjs.data.v6 import MENUITEMS_SETTINGS_STRUCTURE
from haphilipsjs.menu import get_menu_node_strings, walk_menu_nodes
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
        [1],
        [2, 1],
        [3, 2, 1],
        [4, 2, 1],
    ]


def test_walk_menu_nodes_structure():
    paths = list(walk_menu_nodes(MENUITEMS_SETTINGS_STRUCTURE["node"]))

    assert paths[0] == (MENUITEMS_SETTINGS_STRUCTURE["node"],)
    assert all(path[-1] is MENUITEMS_SETTINGS_STRUCTURE["node"] for path in paths)


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
