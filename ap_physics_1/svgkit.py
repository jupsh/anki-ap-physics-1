"""Tiny SVG drawing kit for physics diagrams.

Everything is drawn with plain shapes (no <marker>/<defs>) so the files render
identically in Anki desktop, AnkiDroid, AnkiMobile, and cairosvg previews.

Label mini-markup (see `_rich`): ``F_N`` / ``F_{net}`` subscript,
``v^2`` / ``x^{-1}`` superscript. A leading ``!`` makes the label upright
sans-serif instead of italic serif (for words rather than symbols).
"""

import math
import re
from xml.sax.saxutils import escape

INK = "#1f2937"
MUTED = "#6b7280"
FAINT = "#d1d5db"
FORCE = "#dc2626"  # red: forces
VEL = "#2563eb"  # blue: velocity
ACC = "#16a34a"  # green: acceleration
DISP = "#7c3aed"  # purple: displacement / position
MOM = "#ea580c"  # orange: momentum / impulse / torque
FILL = "#dbeafe"  # light blue object fill
FILL2 = "#fde68a"  # light amber object fill
FLUID = "#bfdbfe"
GROUND = "#9ca3af"

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def _rich(s, size):
    """Turn mini-markup into tspans. Returns (inner_svg, is_italic)."""
    italic = True
    if s.startswith("!"):
        italic = False
        s = s[1:]
    out = []
    shift = 0
    small = _f(size * 0.7)
    tokens = re.findall(r"[_^]\{[^}]*\}|[_^].|[^_^]+", s)
    for tok in tokens:
        if tok[0] in "_^" and len(tok) > 1:
            body = tok[2:-1] if tok[1] == "{" else tok[1]
            dy = size * 0.3 if tok[0] == "_" else -size * 0.4
            out.append(
                f'<tspan dy="{_f(dy - shift)}" font-size="{small}" font-style="normal">'
                f"{escape(body)}</tspan>"
            )
            shift = dy
        else:
            if shift:
                out.append(f'<tspan dy="{_f(-shift)}">{escape(tok)}</tspan>')
                shift = 0
            else:
                out.append(escape(tok))
    if shift:  # restore baseline so following text isn't offset
        out.append(f'<tspan dy="{_f(-shift)}">​</tspan>')
    return "".join(out), italic


class SVG:
    def __init__(self, w, h, title=""):
        self.w, self.h = w, h
        self.title = title
        self.items = []

    # -- primitives ---------------------------------------------------------
    def raw(self, s):
        self.items.append(s)

    def line(self, x1, y1, x2, y2, color=INK, width=2, dash=None, cap="round"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.raw(
            f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}"{d}/>'
        )

    def polyline(self, pts, color=INK, width=2, fill="none", dash=None):
        p = " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.raw(
            f'<polyline points="{p}" fill="{fill}" stroke="{color}" '
            f'stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{d}/>'
        )

    def polygon(self, pts, fill=FILL, stroke=INK, width=2, opacity=1):
        p = " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
        o = f' fill-opacity="{opacity}"' if opacity != 1 else ""
        self.raw(
            f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{width}" stroke-linejoin="round"{o}/>'
        )

    def rect(self, x, y, w, h, fill=FILL, stroke=INK, width=2, rx=3, opacity=1):
        o = f' fill-opacity="{opacity}"' if opacity != 1 else ""
        self.raw(
            f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{o}/>'
        )

    def rbox(self, cx, cy, w, h, angle_deg, fill=FILL, stroke=INK, width=2):
        """Rectangle centred on (cx, cy), rotated by angle (deg, CCW visually)."""
        a = math.radians(angle_deg)
        ux, uy = math.cos(a), -math.sin(a)  # along
        nx, ny = -uy, ux  # perpendicular (screen-down when angle=0)
        pts = []
        for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
            pts.append(
                (cx + sx * w / 2 * ux + sy * h / 2 * nx, cy + sx * w / 2 * uy + sy * h / 2 * ny)
            )
        self.polygon(pts, fill=fill, stroke=stroke, width=width)

    def circle(self, cx, cy, r, fill=FILL, stroke=INK, width=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.raw(
            f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{width}"{d}/>'
        )

    def dot(self, x, y, r=4, color=INK):
        self.circle(x, y, r, fill=color, stroke="none", width=0)

    def path(self, d, color=INK, width=2, fill="none", dash=None, opacity=1):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' fill-opacity="{opacity}"' if opacity != 1 else ""
        self.raw(
            f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da}{o}/>'
        )

    def text(self, x, y, s, size=17, color=INK, anchor="middle", weight="normal", base="middle"):
        inner, italic = _rich(s, size)
        fam = SERIF if italic else SANS
        style = "italic" if italic else "normal"
        self.raw(
            f'<text x="{_f(x)}" y="{_f(y)}" font-family="{fam}" font-size="{size}" '
            f'font-style="{style}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}" dominant-baseline="{base}">{inner}</text>'
        )

    def label(self, x, y, s, size=15, color=MUTED, anchor="middle", weight="normal"):
        """Upright sans label (words, not symbols)."""
        self.text(x, y, "!" + s.lstrip("!"), size=size, color=color, anchor=anchor, weight=weight)

    # -- composite ----------------------------------------------------------
    def arrow(self, x1, y1, x2, y2, color=INK, width=2.6, head=11, label=None,
              lpos=None, lsize=17, dash=None, double=False):
        """Arrow from (x1,y1) to (x2,y2). `lpos` = (dx, dy) offset of label from tip."""
        ang = math.atan2(y2 - y1, x2 - x1)
        hw = head * 0.5
        bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
        self.line(x1, y1, bx, by, color, width, dash=dash, cap="butt")
        self._head(x2, y2, ang, head, hw, color)
        if double:
            bx2, by2 = x1 + head * math.cos(ang), y1 + head * math.sin(ang)
            self.line(bx2, by2, bx, by, color, width, cap="butt")
            self._head(x1, y1, ang + math.pi, head, hw, color)
        if label:
            if lpos is None:
                lpos = (14 * math.cos(ang), 14 * math.sin(ang) + 2)
            self.text(x2 + lpos[0], y2 + lpos[1], label, size=lsize, color=color)

    def _head(self, x, y, ang, head, hw, color):
        p1 = (x, y)
        p2 = (x - head * math.cos(ang) + hw * math.sin(ang), y - head * math.sin(ang) - hw * math.cos(ang))
        p3 = (x - head * math.cos(ang) - hw * math.sin(ang), y - head * math.sin(ang) + hw * math.cos(ang))
        self.polygon([p1, p2, p3], fill=color, stroke=color, width=1)

    def dim(self, x1, y1, x2, y2, label, off=(0, 0), color=MUTED, size=15):
        """Double-headed dimension arrow with label at midpoint + offset."""
        self.arrow(x1, y1, x2, y2, color=color, width=1.4, head=8, double=True)
        self.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, size=size, color=color)

    def spring(self, x1, y1, x2, y2, coils=8, amp=8, color=INK, width=2, lead=10):
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        nx, ny = -uy, ux
        pts = [(x1, y1), (x1 + ux * lead, y1 + uy * lead)]
        body = L - 2 * lead
        n = coils * 2
        for i in range(1, n + 1):
            t = lead + body * (i - 0.5) / n
            s = amp if i % 2 else -amp
            pts.append((x1 + ux * t + nx * s, y1 + uy * t + ny * s))
        pts += [(x2 - ux * lead, y2 - uy * lead), (x2, y2)]
        self.polyline(pts, color=color, width=width)

    def ground(self, x1, x2, y, hatch=True, color=GROUND):
        self.line(x1, y, x2, y, INK, 2)
        if hatch:
            x = x1 + 6
            while x < x2:
                self.line(x, y + 2, x - 8, y + 10, color, 1.4)
                x += 12

    def wall(self, x, y1, y2, side="left"):
        self.line(x, y1, x, y2, INK, 2)
        s = -1 if side == "left" else 1
        y = y1 + 6
        while y < y2:
            self.line(x + 2 * s, y, x + 10 * s, y - 8, GROUND, 1.4)
            y += 12

    def ceiling(self, x1, x2, y):
        self.line(x1, y, x2, y, INK, 2)
        x = x1 + 6
        while x < x2:
            self.line(x, y - 2, x - 8, y - 10, GROUND, 1.4)
            x += 12

    def arc(self, cx, cy, r, a0, a1, color=MUTED, width=1.6, label=None, lr=None, lsize=16, lcolor=None):
        """Arc between math angles a0..a1 (degrees, CCW from +x, y up)."""
        p0 = (cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0)))
        p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
        large = 1 if abs(a1 - a0) > 180 else 0
        sweep = 0 if a1 > a0 else 1
        self.path(f"M{_f(p0[0])},{_f(p0[1])} A{_f(r)},{_f(r)} 0 {large} {sweep} {_f(p1[0])},{_f(p1[1])}",
                  color=color, width=width)
        if label:
            am = math.radians((a0 + a1) / 2)
            rr = lr or r + 14
            self.text(cx + rr * math.cos(am), cy - rr * math.sin(am), label, size=lsize,
                      color=lcolor or INK)

    def curved_arrow(self, cx, cy, r, a0, a1, color=MOM, width=2.4, head=10, label=None, lr=None):
        """Circular arrow from math angle a0 to a1 (deg); arrowhead at a1."""
        self.arc(cx, cy, r, a0, a1, color=color, width=width)
        t = math.radians(a1)
        x, y = cx + r * math.cos(t), cy - r * math.sin(t)
        d = 1 if a1 > a0 else -1  # CCW -> tangent direction
        tang = math.atan2(-math.cos(t) * d, -math.sin(t) * d)
        self._head(x + head * 0.5 * math.cos(tang), y + head * 0.5 * math.sin(tang), tang, head, head * 0.5, color)
        if label:
            am = math.radians((a0 + a1) / 2)
            rr = lr or r + 16
            self.text(cx + rr * math.cos(am), cy - rr * math.sin(am), label, color=color)

    def render(self):
        body = "\n  ".join(self.items)
        t = f"<title>{escape(self.title)}</title>" if self.title else ""
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}">{t}\n'
            f'  <rect width="100%" height="100%" fill="#ffffff"/>\n  {body}\n</svg>\n'
        )


class Axes:
    """Plot area mapping data coords to SVG coords."""

    def __init__(self, svg, ox, oy, w, h, xr=(0, 1), yr=(0, 1), xlabel="t", ylabel="x",
                 xlabel_pos="end", arrows=True, color=INK):
        self.s, self.ox, self.oy, self.w, self.h = svg, ox, oy, w, h
        self.xr, self.yr = xr, yr
        # zero lines
        x0 = self.X(0) if xr[0] <= 0 <= xr[1] else ox
        y0 = self.Y(0) if yr[0] <= 0 <= yr[1] else oy
        if arrows:
            svg.arrow(ox, y0, ox + w + 12, y0, color=color, width=1.8, head=9)
            svg.arrow(x0, oy, x0, oy - h - 12, color=color, width=1.8, head=9)
        if xlabel:
            svg.text(ox + w + 18, y0, xlabel, size=17, anchor="start")
        if ylabel:
            svg.text(x0, oy - h - 26, ylabel, size=17)

    def X(self, x):
        return self.ox + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * self.w

    def Y(self, y):
        return self.oy - (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * self.h

    def P(self, x, y):
        return self.X(x), self.Y(y)

    def plot(self, f, x0=None, x1=None, n=120, color=VEL, width=2.6, dash=None):
        x0 = self.xr[0] if x0 is None else x0
        x1 = self.xr[1] if x1 is None else x1
        pts = [self.P(x0 + (x1 - x0) * i / n, f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]
        self.s.polyline(pts, color=color, width=width, dash=dash)
        return pts

    def fill_under(self, f, x0, x1, color=VEL, opacity=0.18, n=80, base=0):
        pts = [self.P(x0, base)]
        pts += [self.P(x0 + (x1 - x0) * i / n, f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]
        pts.append(self.P(x1, base))
        self.s.polygon(pts, fill=color, stroke="none", width=0, opacity=opacity)
