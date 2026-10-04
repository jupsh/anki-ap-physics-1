"""Build the AP Physics 1 Anki deck.

    uv run python ap_physics_1/build.py            # -> dist/AP_Physics_1.apkg
    uv run python ap_physics_1/build.py --html X   # also write an HTML preview of every card
"""

import argparse
import hashlib
import importlib
import re
import sys
from pathlib import Path

import genanki

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from cards import Basic, Cloze  # noqa: E402
from diagrams import DIAGRAMS  # noqa: E402

ROOT = HERE.parent
BUILD = ROOT / "build" / "ap_physics_1"
DIST = ROOT / "dist"
DECK_ROOT = "AP Physics 1"
UNIT_MODULES = [f"content.u{i}" for i in range(1, 9)]

BASIC_MODEL_ID = 1729384756
CLOZE_MODEL_ID = 1729384757

CSS = r"""
.card {
  font-family: -apple-system, "Segoe UI", Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 19px; line-height: 1.55; color: #1f2937; background: #fafaf9;
  text-align: left; margin: 0; padding: 0;
}
.wrap { max-width: 700px; margin: 0 auto; padding: 20px 16px 28px; --accent: #2563eb; }
.u1 { --accent: #2563eb; } .u2 { --accent: #dc2626; } .u3 { --accent: #b45309; }
.u4 { --accent: #ea580c; } .u5 { --accent: #7c3aed; } .u6 { --accent: #db2777; }
.u7 { --accent: #0d9488; } .u8 { --accent: #0369a1; }
.crumb {
  font-size: 12px; font-weight: 600; letter-spacing: .05em; text-transform: uppercase;
  color: var(--accent); border-left: 4px solid var(--accent); padding: 2px 0 2px 10px;
  margin-bottom: 18px; display: flex; flex-wrap: wrap; gap: 4px 8px;
}
.crumb .sec { color: #6b7280; }
.q { font-size: 1.08em; font-weight: 500; }
.a { margin-top: 4px; }
hr#answer { border: none; border-top: 1px solid #e5e7eb; margin: 20px 0 16px; }
.diagram { margin: 16px 0 6px; text-align: center; }
.diagram img {
  max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #e5e7eb;
  background: #fff;
}
.extra {
  margin-top: 18px; padding: 10px 14px; border-radius: 10px; font-size: .86em;
  background: #f3f4f6; color: #4b5563; border-left: 3px solid var(--accent);
}
.cloze { color: var(--accent); font-weight: 700; }
.cloze-inactive { color: inherit; }
ul, ol { margin: 6px 0; padding-left: 1.3em; }
li { margin: 2px 0; }
table.t { border-collapse: collapse; margin: 8px 0; font-size: .92em; }
table.t td, table.t th { border: 1px solid #e5e7eb; padding: 4px 10px; text-align: left; }
table.t th { background: #f3f4f6; font-weight: 600; }
b, strong { font-weight: 650; }
.key { color: var(--accent); font-weight: 650; }

/* night mode (desktop: .nightMode, AnkiDroid: .night_mode) */
.card.nightMode, .card.night_mode { background: #1c1c1e; color: #e5e7eb; }
.nightMode .u1, .night_mode .u1 { --accent: #60a5fa; } .nightMode .u2, .night_mode .u2 { --accent: #f87171; }
.nightMode .u3, .night_mode .u3 { --accent: #fbbf24; } .nightMode .u4, .night_mode .u4 { --accent: #fb923c; }
.nightMode .u5, .night_mode .u5 { --accent: #a78bfa; } .nightMode .u6, .night_mode .u6 { --accent: #f472b6; }
.nightMode .u7, .night_mode .u7 { --accent: #2dd4bf; } .nightMode .u8, .night_mode .u8 { --accent: #38bdf8; }
.nightMode .crumb .sec, .night_mode .crumb .sec { color: #9ca3af; }
.nightMode hr#answer, .night_mode hr#answer { border-top-color: #3f3f46; }
.nightMode .extra, .night_mode .extra { background: #27272a; color: #d4d4d8; }
.nightMode .diagram img, .night_mode .diagram img {
  filter: invert(.9) hue-rotate(180deg); border-color: #3f3f46;
}
.nightMode table.t td, .nightMode table.t th, .night_mode table.t td, .night_mode table.t th { border-color: #3f3f46; }
.nightMode table.t th, .night_mode table.t th { background: #27272a; }
"""

CRUMB = '<div class="crumb"><span>{{Unit}}</span><span class="sec">{{Section}}</span></div>'

BASIC_FRONT = (
    '<div class="wrap u{{UnitNum}}">' + CRUMB +
    '<div class="q">{{Front}}</div>'
    '{{#FrontDiagram}}<div class="diagram">{{FrontDiagram}}</div>{{/FrontDiagram}}'
    '</div>'
)
BASIC_BACK = (
    '<div class="wrap u{{UnitNum}}">' + CRUMB +
    '<div class="q">{{Front}}</div>'
    '{{#FrontDiagram}}<div class="diagram">{{FrontDiagram}}</div>{{/FrontDiagram}}'
    '<hr id="answer"><div class="a">{{Back}}</div>'
    '{{#BackDiagram}}<div class="diagram">{{BackDiagram}}</div>{{/BackDiagram}}'
    '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
    '</div>'
)
CLOZE_FRONT = (
    '<div class="wrap u{{UnitNum}}">' + CRUMB +
    '<div class="q">{{cloze:Text}}</div>'
    '</div>'
)
CLOZE_BACK = (
    '<div class="wrap u{{UnitNum}}">' + CRUMB +
    '<div class="q">{{cloze:Text}}</div>'
    '{{#Diagram}}<div class="diagram">{{Diagram}}</div>{{/Diagram}}'
    '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
    '</div>'
)

BASIC_MODEL = genanki.Model(
    BASIC_MODEL_ID, "AP Physics 1 · Basic",
    fields=[{"name": n} for n in
            ("Front", "Back", "FrontDiagram", "BackDiagram", "Extra", "Unit", "Section", "UnitNum")],
    templates=[{"name": "Card 1", "qfmt": BASIC_FRONT, "afmt": BASIC_BACK}],
    css=CSS,
)
CLOZE_MODEL = genanki.Model(
    CLOZE_MODEL_ID, "AP Physics 1 · Cloze",
    fields=[{"name": n} for n in ("Text", "Extra", "Diagram", "Unit", "Section", "UnitNum")],
    templates=[{"name": "Cloze", "qfmt": CLOZE_FRONT, "afmt": CLOZE_BACK}],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)

DECK_DESCRIPTION = (
    "AP Physics 1, following the College Board course framework used by Khan Academy's "
    "AP Physics 1 course (8 units). Subdecks per unit and topic. Diagram colour key: "
    "<b style='color:#dc2626'>forces</b>, <b style='color:#2563eb'>velocity</b>, "
    "<b style='color:#16a34a'>acceleration</b>, <b style='color:#7c3aed'>displacement</b>, "
    "<b style='color:#ea580c'>momentum / rotation</b>."
)


# --------------------------------------------------------------------------- helpers

CLOZE_OPEN = re.compile(r"\{\{c\d+::")


def fix_cloze_math(text):
    """Make LaTeX braces inside a cloze safe for Anki's cloze parser.

    Anki ends a cloze at the first `}}`. Inside each cloze we track LaTeX brace
    depth: the terminator is the `}}` reached at depth 0. Every other `}}`
    (inside or outside clozes) is spaced to `} }`, and a cloze body ending in
    `}` gets a trailing space so it can't merge with the terminator.
    """
    def space(seg):
        while "}}" in seg:
            seg = seg.replace("}}", "} }")
        return seg

    out, pos = [], 0
    for m in CLOZE_OPEN.finditer(text):
        if m.start() < pos:
            raise SystemExit(f"nested cloze not supported: {text[:80]}")
        out.append(space(text[pos:m.start()]) + m.group(0))
        i, depth = m.end(), 0
        while True:
            if i >= len(text):
                raise SystemExit(f"unterminated cloze: {text[:80]}")
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                if depth == 0:
                    if text[i:i + 2] != "}}":
                        raise SystemExit(f"unbalanced braces in cloze: {text[:80]}")
                    break
                depth -= 1
            i += 1
        body = space(text[m.end():i])
        if body.endswith("}"):
            body += " "
        out.append(body + "}}")
        pos = i + 2
    out.append(space(text[pos:]))
    return "".join(out)


def img(name):
    if name is None:
        return ""
    if name not in DIAGRAMS:
        raise SystemExit(f"unknown diagram: {name}")
    return f'<img src="ap1_{name}.svg">'


def deck_id(name):
    return 1_500_000_000 + int(hashlib.sha1(name.encode()).hexdigest()[:7], 16)


def slug(s):
    return re.sub(r"[^A-Za-z0-9.]+", "_", s).strip("_")


def validate(where, *fields):
    for f in fields:
        if not f:
            continue
        if re.search(r"<(?![a-zA-Z/!])", f):
            raise SystemExit(f"{where}: raw '<' (use \\lt or &lt;): {f[:80]}")
        if '\\"' in f:
            raise SystemExit(f"{where}: stray backslash-quote: {f[:80]}")
        if f.count(r"\(") != f.count(r"\)") or f.count(r"\[") != f.count(r"\]"):
            raise SystemExit(f"{where}: unbalanced math delimiters: {f[:80]}")


# --------------------------------------------------------------------------- build

def load_units():
    return [importlib.import_module(m).UNIT for m in UNIT_MODULES]


def build(html_out=None):
    units = load_units()
    decks, used, seen = [], set(), set()
    root = genanki.Deck(deck_id(DECK_ROOT), DECK_ROOT, description=DECK_DESCRIPTION)
    decks.append(root)
    due = 0
    preview = []
    counts = {}
    for u in units:
        unit_label = f"Unit {u.num} · {u.title}"
        unit_deck_name = f"{DECK_ROOT}::{unit_label}"
        decks.append(genanki.Deck(deck_id(unit_deck_name), unit_deck_name))
        for sec in u.sections:
            sec_label = f"{sec.code} {sec.title}"
            name = f"{unit_deck_name}::{sec_label}"
            deck = genanki.Deck(deck_id(name), name)
            decks.append(deck)
            base_tags = [f"AP_Physics_1::U{u.num}_{slug(u.title)}::{slug(sec_label)}"]
            for card in sec.cards:
                due += 1
                where = f"{sec.code} card {sec.cards.index(card) + 1}"
                if isinstance(card, Basic):
                    validate(where, card.front, card.back, card.extra)
                    key = ("B", sec.code, card.front)
                    fields = [card.front, card.back, img(card.fd), img(card.bd), card.extra,
                              unit_label, sec_label, str(u.num)]
                    model = BASIC_MODEL
                    used.update(d for d in (card.fd, card.bd) if d)
                elif isinstance(card, Cloze):
                    validate(where, card.text, card.extra)
                    if not re.search(r"\{\{c\d+::", card.text):
                        raise SystemExit(f"{where}: cloze without deletions")
                    text = fix_cloze_math(card.text)
                    # every remaining `}}` must be a cloze terminator
                    if text.count("}}") != len(CLOZE_OPEN.findall(text)):
                        raise SystemExit(f"{where}: ambiguous '}}}}' in cloze text: {text[:80]}")
                    key = ("C", sec.code, card.text)
                    fields = [text, card.extra, img(card.d), unit_label, sec_label, str(u.num)]
                    model = CLOZE_MODEL
                    if card.d:
                        used.add(card.d)
                else:
                    raise SystemExit(f"{where}: unknown card type")
                if key in seen:
                    raise SystemExit(f"{where}: duplicate card")
                seen.add(key)
                tags = base_tags + [t.replace(" ", "_") for t in card.tags]
                if any(fields[i] for i in ((2, 3) if model is BASIC_MODEL else (2,))):
                    tags.append("diagram")
                note = genanki.Note(model=model, fields=fields, tags=tags,
                                    guid=genanki.guid_for("ap1", *key), due=due)
                deck.add_note(note)
                counts[u.num] = counts.get(u.num, 0) + 1
                preview.append((model is CLOZE_MODEL, fields, u.num))

    BUILD.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)
    media = []
    for name in sorted(used):
        p = BUILD / f"ap1_{name}.svg"
        p.write_text(DIAGRAMS[name]())
        media.append(str(p))
    out = DIST / "AP_Physics_1.apkg"
    genanki.Package(decks, media_files=media).write_to_file(out)

    unused = sorted(set(DIAGRAMS) - used)
    total = sum(counts.values())
    print(f"wrote {out}  ({total} notes, {len(media)} diagrams)")
    for n, c in counts.items():
        print(f"  unit {n}: {c}")
    if unused:
        print("unused diagrams:", ", ".join(unused))
    if html_out:
        write_preview(Path(html_out), preview, media)


def write_preview(path, preview, media):
    """Static HTML rendering of every card (front + back) for proofreading."""
    import shutil
    path.parent.mkdir(parents=True, exist_ok=True)
    for m in media:
        shutil.copy(m, path.parent)
    rows = []
    for is_cloze, f, unum in preview:
        if is_cloze:
            text, extra, diag, unit, sec, _ = f
            front = re.sub(r"\{\{c(\d+)::(.*?)(::(.*?))?\}\}", r'<span class="cloze">[...]</span>', text)
            back = re.sub(r"\{\{c(\d+)::(.*?)(::(.*?))?\}\}", r'<span class="cloze">\2</span>', text)
            body = (f'<div class="q">{front}</div><hr id="answer"><div class="q">{back}</div>'
                    + (f'<div class="diagram">{diag}</div>' if diag else "")
                    + (f'<div class="extra">{extra}</div>' if extra else ""))
        else:
            fr, bk, fd, bd, extra, unit, sec, _ = f
            body = (f'<div class="q">{fr}</div>' + (f'<div class="diagram">{fd}</div>' if fd else "")
                    + f'<hr id="answer"><div class="a">{bk}</div>'
                    + (f'<div class="diagram">{bd}</div>' if bd else "")
                    + (f'<div class="extra">{extra}</div>' if extra else ""))
        rows.append(f'<div class="wrap u{unum}" style="border-bottom:6px solid #ddd">'
                    f'<div class="crumb"><span>{unit}</span><span class="sec">{sec}</span></div>{body}</div>')
    path.write_text(
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}};</script>"
        "<script src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js'></script>"
        f"<style>{CSS}</style></head><body class='card'>" + "".join(rows) + "</body></html>"
    )
    print(f"preview: {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", help="write an HTML preview to this path")
    build(ap.parse_args().html)
