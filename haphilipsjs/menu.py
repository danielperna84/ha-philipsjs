"""Helpers for the menu settings structure."""

from typing import Dict, Iterator, List, Optional, Tuple

from .features import json_feature_supported
from .typing import MenuItemsSettingsCurrentValueValue, MenuItemsSettingsNode, SystemType


def is_menu_supported_on_system(system: Optional[SystemType]) -> bool:
    """Return if a TV provides menu settings, from its system descriptor."""
    return bool(json_feature_supported(system, "menuitems", "Setup_Menu"))


def _get_menu_node_children(node: MenuItemsSettingsNode) -> List[MenuItemsSettingsNode]:
    """Return the child nodes of a menu node."""
    if node["type"] == "PARENT_NODE":
        return node["data"].get("nodes", [])
    return []


def walk_menu_nodes(root: MenuItemsSettingsNode) -> Iterator[Tuple[MenuItemsSettingsNode, ...]]:
    """Yield each menu node below the root with its parents, starting with the node.

    The root node itself is left out, it is the same for all nodes.
    """
    stack: List[Tuple[MenuItemsSettingsNode, ...]] = [
        (child,) for child in reversed(_get_menu_node_children(root))
    ]
    while stack:
        path = stack.pop()
        yield path
        stack.extend((child, *path) for child in reversed(_get_menu_node_children(path[0])))


def get_menu_node_strings(node: MenuItemsSettingsNode) -> Iterator[str]:
    """Yield the ids of all translatable strings of a menu node."""
    if string_id := node.get("string_id"):
        yield string_id

    if node["type"] == "LIST_NODE":
        for enum in node["data"]["enums"]:
            yield enum["string_id"]
    elif node["type"] == "MULTIPLE_SLIDER":
        for slider in node["data"]["sliders"]:
            yield slider["slider_id"]
    elif node["type"] == "PARENT_NODE":
        for child in node["data"].get("nodes", []):
            if string_id := child.get("string_id"):
                yield string_id


def get_menu_node_name(
    node: MenuItemsSettingsNode,
    strings: Dict[str, str],
    value: Optional[MenuItemsSettingsCurrentValueValue],
) -> Optional[str]:
    """Return the translated name of a menu node, from its string id or its current value."""
    if string_id := node.get("string_id"):
        return strings[string_id]
    if value:
        return value.get("string_id")
    return None


def is_menu_node_with_value(
    node: MenuItemsSettingsNode,
    value: Optional[MenuItemsSettingsCurrentValueValue],
) -> bool:
    """Return if a menu node holds a value, rather than just grouping other nodes.

    Parent nodes only hold a value when they select one of their child nodes,
    which shows in their current value.
    """
    if node["type"] != "PARENT_NODE":
        return True
    if not node["data"].get("nodes") or not value or not (data := value.get("data")):
        return False
    return "activenode_id" in data and bool(data["activenode_id"])
