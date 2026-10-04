"""Card/section data types used by the content modules.

Math uses Anki's MathJax delimiters: \\( inline \\) and \\[ display \\].
Write `<` as `\\lt` in math or `&lt;` in text (fields are HTML).
"""

from dataclasses import dataclass, field


@dataclass
class Basic:
    front: str
    back: str
    fd: str | None = None  # diagram shown on the front
    bd: str | None = None  # diagram shown on the back
    extra: str = ""
    tags: tuple = ()


@dataclass
class Cloze:
    text: str
    d: str | None = None
    extra: str = ""
    tags: tuple = ()


@dataclass
class Section:
    code: str  # e.g. "2.5"
    title: str
    cards: list = field(default_factory=list)


@dataclass
class Unit:
    num: int
    title: str
    sections: list


def B(front, back, fd=None, bd=None, extra="", tags=()):
    return Basic(front, back, fd, bd, extra, tuple(tags))


def C(text, d=None, extra="", tags=()):
    return Cloze(text, d, extra, tuple(tags))
