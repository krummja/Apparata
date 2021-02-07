from __future__ import annotations

from apparata.graph import Graph


class Production:
    """Representation of a Production."""

    def __init__(self, *, pattern: Graph, replacement: Graph) -> None:
        """Constructor."""
        self.pattern = pattern
        self.replacement = replacement


class Transformation:
    """Representation of a transformation rule."""

    def __init__(self, *, pattern: Graph, replacement: Graph) -> None:
        """Constructor."""
        self.pattern = pattern
        self.replacement = replacement
