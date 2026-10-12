"""Helpers for the menu settings structure."""

from typing import Iterator, List, Tuple

from .typing import MenuItemsSettingsNode


def walk_menu_nodes(root: MenuItemsSettingsNode) -> Iterator[Tuple[MenuItemsSettingsNode, ...]]:
    """Yield each menu node with its parents up to the root, starting with the node."""
    stack: List[Tuple[MenuItemsSettingsNode, ...]] = [(root,)]
    while stack:
        path = stack.pop()
        yield path
        node = path[0]
        if node["type"] == "PARENT_NODE":
            for child in reversed(node["data"].get("nodes", [])):
                stack.append((child, *path))


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
