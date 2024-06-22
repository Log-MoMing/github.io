from pathlib import Path
from pprint import pprint
from typing import Any
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation, Section, Link
from mkdocs.structure.pages import Page
from material.plugins.blog.structure import Post, View
from natsort import natsorted

def process_items(items):
    """处理导航项列表
    """
    if len(items) >= 1:
        item = items[0]
        if isinstance(item, View):
            if item.url and "blog/" == item.url:
                return items

    sortable_items = []

    for item in items:
        if isinstance(item, Section):
            item.children = process_items(item.children)
        sortable_items.append(item)

    return natsorted(sortable_items, key=lambda x: x.title)


def on_nav(
    nav: Navigation, *, config: MkDocsConfig, files: Files, **kwargs: Any
) -> Navigation:
    for item in nav.items:
        if isinstance(item, Section):
            item.children = process_items(item.children)
    return nav