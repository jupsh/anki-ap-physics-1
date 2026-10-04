"""All deck diagrams. Each function returns an SVG string; `DIAGRAMS` maps
name -> function. Filenames in Anki are ``ap1_<name>.svg``.

Colour convention: forces red, velocity blue, acceleration green,
displacement/position purple, momentum/torque/angular quantities orange.
"""

import math

from svgkit import (ACC, DISP, FAINT, FILL, FILL2, FLUID, FORCE, INK, MOM, MUTED, VEL,
                    Axes, SVG)

DIAGRAMS = {}


def diagram(fn):
    DIAGRAMS[fn.__name__] = fn
    return fn


def polar(s, x, y, length, deg, color, label=None, lpos=None, **kw):
    """Arrow from (x,y) with math angle `deg` (CCW from +x, y up)."""
    a = math.radians(deg)
    s.arrow(x, y, x + length * math.cos(a), y - length * math.sin(a), color=color,
            label=label, lpos=lpos, **kw)


# =============================================================================
# Unit 1 — Kinematics
# =============================================================================

@diagram
def number_line():
    s = SVG(520, 200, "Distance vs displacement on a number line")
    y = 120
    X = lambda v: 70 + v * 50  # noqa: E731
    s.line(X(-1.4), y, X(7.4), y, INK, 2)
    for v in range(-1, 8):
        s.line(X(v), y - 6, X(v), y + 6, INK, 1.6)
        s.text(X(v), y + 22, f"!{v}", size=14, color=MUTED)
    s.label(X(7.4) + 8, y + 22, "x (m)", anchor="start", size=14)
    s.arrow(X(0), y - 36, X(5), y - 36, VEL, width=2, head=9)
    s.arrow(X(5), y - 62, X(2), y - 62, VEL, width=2, head=9)
    s.line(X(5), y - 36, X(5), y - 62, VEL, 2, dash="3 3")
    s.label(X(2.5), y - 50, "path: 5 m forward", size=13, color=VEL)
    s.label(X(3.5), y - 78, "then 3 m back", size=13, color=VEL)
    s.dot(X(0), y, 6, INK)
    s.dot(X(2), y, 6, DISP)
    s.label(X(0), y - 14, "start", size=12)
    s.arrow(X(0), y + 48, X(2), y + 48, DISP, width=3, head=11)
    s.text(X(2) + 14, y + 49, "!Δx = +2 m", size=15, color=DISP, anchor="start")
    s.text(X(4.6), y + 49, "!distance = 8 m", size=15, color=VEL, anchor="start")
    return s.render()


@diagram
def xt_graph():
    s = SVG(460, 300, "Position-time graph: slope is velocity")
    ax = Axes(s, 60, 250, 340, 200, xr=(0, 4), yr=(0, 16), xlabel="t", ylabel="x")
    f = lambda t: t * t  # noqa: E731
    ax.plot(f, color=DISP)
    # secant from t=1 to t=3.5
    s.line(*ax.P(0.6, 0.6 * 4.5 - 3.5), *ax.P(3.8, 3.8 * 4.5 - 3.5), MUTED, 1.8, dash="6 5")
    s.dot(*ax.P(1, 1), 4, MUTED)
    s.dot(*ax.P(3.5, 12.25), 4, MUTED)
    # tangent at t=2.5: slope 5
    t0 = 2.5
    s.line(*ax.P(1.5, f(t0) + 5 * (1.5 - t0)), *ax.P(3.6, f(t0) + 5 * (3.6 - t0)), VEL, 2.4)
    s.dot(*ax.P(t0, f(t0)), 5, VEL)
    s.label(ax.X(3.5) - 4, ax.Y(15.3), "tangent slope = v", size=14, color=VEL, anchor="end")
    s.label(ax.X(0.15), ax.Y(8.3), "secant slope", size=13, color=MUTED, anchor="start")
    s.label(ax.X(0.15), ax.Y(7.0), "= average v", size=13, color=MUTED, anchor="start")
    return s.render()


@diagram
def vt_graph():
    s = SVG(460, 300, "Velocity-time graph: slope is acceleration, area is displacement")
    ax = Axes(s, 60, 250, 340, 200, xr=(0, 5), yr=(0, 10), xlabel="t", ylabel="v")
    f = lambda t: 2 + 1.4 * t  # noqa: E731
    ax.fill_under(f, 0, 4, color=DISP, opacity=0.18)
    ax.plot(f, 0, 4.7, color=VEL)
    s.line(*ax.P(4, 0), *ax.P(4, f(4)), MUTED, 1.4, dash="4 4")
    s.text(ax.X(2.6), ax.Y(1.3), "!area = Δx", size=16, color=DISP)
    # slope triangle
    s.line(*ax.P(1, f(1)), *ax.P(2.5, f(1)), ACC, 2)
    s.line(*ax.P(2.5, f(1)), *ax.P(2.5, f(2.5)), ACC, 2)
    s.text(ax.X(1.75), ax.Y(f(1)) + 14, "!Δt", size=14, color=ACC)
    s.text(ax.X(2.5) + 20, ax.Y((f(1) + f(2.5)) / 2), "!Δv", size=14, color=ACC)
    s.label(ax.X(0.2), ax.Y(9.3), "slope = Δv/Δt = a", size=15, color=ACC, anchor="start")
    s.text(ax.X(0) - 14, ax.Y(2), "v_0", size=15, color=VEL)
    return s.render()


@diagram
def motion_graphs():
    s = SVG(660, 230, "x-t, v-t, a-t graphs for constant positive acceleration")
    titles = [("x", DISP, lambda t: 0.5 + 0.6 * t + 0.35 * t * t, (0, 6)),
              ("v", VEL, lambda t: 0.6 + 0.7 * t, (0, 3.5)),
              ("a", ACC, lambda t: 1.5, (0, 3))]
    for i, (lab, col, f, yr) in enumerate(titles):
        ox = 40 + i * 215
        ax = Axes(s, ox, 180, 150, 120, xr=(0, 3), yr=yr, xlabel="t", ylabel=lab)
        ax.plot(f, color=col)
    s.label(115, 214, "parabola (slope rising)", size=13)
    s.label(330, 214, "straight line, slope a", size=13)
    s.label(545, 214, "horizontal line", size=13)
    return s.render()


@diagram
def motion_diagram():
    s = SVG(520, 120, "Motion diagram (equal time intervals)")
    y = 55
    xs = [50 + 26 * t * t for t in range(0, 5)]
    s.line(30, y + 22, 500, y + 22, FAINT, 1.4)
    for i, x in enumerate(xs):
        s.dot(x, y, 6, INK)
        s.text(x, y + 38, f"t_{i}", size=13, color=MUTED)
    s.label(270, 108, "positions at equal time intervals", size=12)
    return s.render()


@diagram
def vector_components():
    s = SVG(400, 300, "Resolving a vector into components")
    ox, oy, L, th = 60, 250, 250, 35
    ex, ey = ox + L * math.cos(math.radians(th)), oy - L * math.sin(math.radians(th))
    s.line(ox - 10, oy, 370, oy, FAINT, 1.4)
    s.line(ox, oy + 10, ox, 30, FAINT, 1.4)
    s.arrow(ox, oy, ex, oy, VEL, width=2.2, dash="7 4")
    s.arrow(ex, oy, ex, ey, VEL, width=2.2, dash="7 4")
    s.arrow(ox, oy, ex, ey, INK, width=3, head=13)
    s.text((ox + ex) / 2 - 16, (oy + ey) / 2 - 16, "A", size=20, weight="bold")
    s.text((ox + ex) / 2, oy + 22, "A_x = A cos θ", size=16, color=VEL)
    s.text(ex + 12, (oy + ey) / 2, "A_y = A sin θ", size=16, color=VEL, anchor="start")
    s.arc(ox, oy, 52, 0, th, label="θ", lr=68)
    return s.render()


@diagram
def projectile():
    s = SVG(560, 370, "Projectile motion: components of velocity")
    ax = Axes(s, 50, 270, 450, 200, xr=(0, 2.2), yr=(0, 1.3), xlabel="x", ylabel="y")
    vx, vy0, g = 1.0, 2.0, 2.0
    ax.plot(lambda x: vy0 * x - 0.5 * g * x * x, 0, 2.0, color=FAINT, width=2.4, dash="6 5")
    k = 38
    for t in (0, 0.5, 1.0, 1.5, 2.0):
        x, y = vx * t, vy0 * t - 0.5 * g * t * t
        px, py = ax.P(x, y)
        vy = vy0 - g * t
        s.dot(px, py, 6, INK)
        s.arrow(px, py, px + vx * k, py, VEL, width=2.2, head=9)
        if abs(vy) > 0.01:
            s.arrow(px, py, px, py - vy * k, VEL, width=2.2, head=9)
    tx, ty = ax.P(1.0, 1.0)
    s.text(tx, ty - 22, "v_y = 0 at the top", size=14, color=VEL)
    s.text(ax.X(0) + 40, ax.Y(0) - 20, "v_x", size=14, color=VEL, anchor="start")
    s.text(ax.X(0) - 12, ax.Y(0) - 60, "v_y", size=14, color=VEL, anchor="end")
    s.arrow(500, 80, 500, 130, ACC, width=2.6, label="a = g", lpos=(0, 16), lsize=15)
    s.label(500, 168, "(everywhere)", size=12, color=ACC)
    s.label(275, 360, "v_x constant · v_y changes by −g each second", size=13)
    return s.render()


@diagram
def relative_motion():
    s = SVG(460, 300, "Boat crossing a river: relative velocity")
    s.rect(30, 40, 400, 220, fill=FLUID, stroke="none", rx=0, opacity=0.55)
    s.line(30, 40, 430, 40, INK, 2)
    s.line(30, 260, 430, 260, INK, 2)
    for y in (70, 150, 230):
        s.arrow(330, y, 400, y, MUTED, width=1.6, head=8)
    s.label(365, 105, "current", size=12)
    ox, oy = 120, 240
    s.arrow(ox, oy, ox, 90, VEL, width=2.6, label="v_{BW}", lpos=(-26, 6))
    s.arrow(ox, 90, ox + 120, 90, MUTED, width=2.6, label="v_{WG}", lpos=(-60, -16))
    s.arrow(ox, oy, ox + 120, 90, INK, width=3, label="v_{BG}", lpos=(-28, 80))
    s.label(230, 280, "v_{BG} = v_{BW} + v_{WG}  (vector sum)", size=14, color=INK)
    s.label(230, 22, "B = boat, W = water, G = ground", size=13)
    return s.render()


# =============================================================================
# Unit 2 — Force and Translational Dynamics
# =============================================================================

@diagram
def fbd_table():
    s = SVG(460, 280, "Free-body diagram: block pushed on a rough floor")
    s.ground(40, 420, 200)
    s.rect(170, 140, 110, 60, fill=FILL)
    cx, cy = 225, 170
    s.dot(cx, cy, 4)
    s.arrow(cx, cy, cx, cy + 90, FORCE, label="F_g", lpos=(22, -8))
    s.arrow(cx, cy, cx, cy - 100, FORCE, label="F_N", lpos=(22, 10))
    s.arrow(cx, cy, cx + 120, cy, FORCE, label="F_{app}", lpos=(10, -18))
    s.arrow(cx, cy, cx - 85, cy, FORCE, label="f_k", lpos=(-6, -18))
    s.arrow(330, 245, 400, 245, VEL, width=2.2, label="v", lpos=(14, 0))
    s.label(80, 245, "friction opposes sliding", size=13, anchor="start")
    return s.render()


INC_TH = 30


def _incline(s, x0=60, y0=270, base=360):
    t = math.tan(math.radians(INC_TH))
    top = y0 - base * t
    s.polygon([(x0, y0), (x0 + base, y0), (x0 + base, top)], fill="#f3f4f6", stroke=INK)
    s.arc(x0, y0, 54, 0, INC_TH, label="θ", lr=72)
    return x0, y0, base, t


@diagram
def fbd_incline():
    s = SVG(470, 300, "Free-body diagram: block on an incline")
    x0, y0, base, t = _incline(s)
    th = math.radians(INC_TH)
    sx, sy = x0 + base * 0.52, y0 - base * 0.52 * t
    nx, ny = -math.sin(th), -math.cos(th)  # outward normal (screen)
    ux, uy = math.cos(th), -math.sin(th)  # up-slope
    cx, cy = sx + 24 * nx, sy + 24 * ny
    s.rbox(cx, cy, 76, 48, INC_TH, fill=FILL)
    s.dot(cx, cy, 4)
    g = 95
    # components (dashed, drawn first)
    s.arrow(cx, cy, cx - ux * g * math.sin(th), cy - uy * g * math.sin(th), FORCE, width=1.8,
            dash="6 4", head=9, label="mg sin θ", lpos=(-34, -6), lsize=14)
    s.arrow(cx, cy, cx - nx * g * math.cos(th), cy - ny * g * math.cos(th), FORCE, width=1.8,
            dash="6 4", head=9, label="mg cos θ", lpos=(40, 4), lsize=14)
    s.arrow(cx, cy, cx, cy + g, FORCE, label="mg", lpos=(-6, 16))
    s.arrow(cx, cy, cx + nx * g * math.cos(th), cy + ny * g * math.cos(th), FORCE,
            label="F_N", lpos=(-10, -12))
    s.arrow(cx, cy, cx + ux * 70, cy + uy * 70, FORCE, label="f", lpos=(10, -8))
    return s.render()


@diagram
def third_law():
    s = SVG(460, 200, "Newton's third law pair")
    s.ground(30, 430, 150)
    s.rect(110, 90, 110, 60, fill=FILL)
    s.rect(220, 100, 90, 50, fill=FILL2)
    s.text(165, 120, "A", size=20, weight="bold")
    s.text(265, 125, "B", size=20, weight="bold")
    s.line(220, 56, 220, 90, MUTED, 1.2, dash="3 3")
    s.arrow(222, 66, 320, 66, FORCE, label="F_{A on B}", lpos=(46, 0), lsize=15)
    s.arrow(218, 66, 120, 66, FORCE, label="F_{B on A}", lpos=(-46, 0), lsize=15)
    s.label(230, 182, "equal magnitude · opposite direction · act on different objects", size=13)
    return s.render()


@diagram
def atwood():
    s = SVG(380, 340, "Atwood machine")
    s.ceiling(130, 250, 20)
    s.line(190, 20, 190, 70, INK, 2)
    s.circle(190, 80, 32, fill="#e5e7eb")
    s.dot(190, 80, 4)
    s.line(158, 80, 158, 220, INK, 2)
    s.line(222, 80, 222, 160, INK, 2)
    s.rect(133, 220, 50, 56, fill=FILL)
    s.rect(202, 160, 40, 40, fill=FILL2)
    s.text(158, 248, "m_1", size=17)
    s.text(222, 180, "m_2", size=16)
    s.arrow(158, 220, 158, 175, FORCE, label="T", lpos=(-14, 4))
    s.arrow(158, 276, 158, 330, FORCE, label="m_1g", lpos=(30, -8))
    s.arrow(222, 160, 222, 118, FORCE, label="T", lpos=(14, 6))
    s.arrow(222, 200, 222, 240, FORCE, label="m_2g", lpos=(28, -6))
    s.arrow(100, 230, 100, 280, ACC, label="a", lpos=(-12, -6))
    s.arrow(285, 200, 285, 150, ACC, label="a", lpos=(12, 6))
    s.label(300, 300, "(m₁ > m₂)", size=13)
    return s.render()


@diagram
def elevator():
    s = SVG(460, 300, "Apparent weight in an accelerating elevator")
    s.rect(40, 30, 170, 240, fill="#f9fafb")
    s.rect(80, 238, 90, 14, fill="#e5e7eb")
    s.label(125, 262, "scale", size=12)
    s.circle(125, 138, 16, fill=FILL2)
    s.rect(105, 156, 40, 82, fill=FILL2, rx=10)
    s.arrow(20, 200, 20, 120, ACC, label="a", lpos=(0, -12))
    cx, cy = 340, 150
    s.label(cx, 30, "FBD of person", size=14, color=INK)
    s.circle(cx, cy, 10, fill=FILL2)
    s.arrow(cx, cy, cx, cy - 105, FORCE, label="F_N", lpos=(22, 10))
    s.arrow(cx, cy, cx, cy + 75, FORCE, label="mg", lpos=(22, -6))
    s.label(cx, 262, "a up → F_N > mg (feel heavier)", size=13)
    s.label(cx, 282, "F_N − mg = ma", size=13, color=INK)
    return s.render()


@diagram
def friction_graph():
    s = SVG(470, 300, "Friction force vs applied force")
    ax = Axes(s, 60, 250, 340, 190, xr=(0, 10), yr=(0, 6), xlabel="F_{app}", ylabel="f")
    ax.plot(lambda x: x, 0, 5, color=FORCE)
    s.line(*ax.P(5, 5), *ax.P(5, 3.8), FORCE, 2.4, dash="4 4")
    ax.plot(lambda x: 3.8, 5, 10, color=FORCE)
    s.dot(*ax.P(5, 5), 5, FORCE)
    s.line(*ax.P(0, 5), *ax.P(5, 5), MUTED, 1.2, dash="3 4")
    s.line(*ax.P(0, 3.8), *ax.P(5, 3.8), MUTED, 1.2, dash="3 4")
    s.text(ax.X(0) - 8, ax.Y(5), "μ_sF_N", size=14, anchor="end")
    s.text(ax.X(0) - 8, ax.Y(3.8), "μ_kF_N", size=14, anchor="end")
    s.label(ax.X(2.4), ax.Y(1.2), "static", size=14, color=FORCE)
    s.label(ax.X(2.4), ax.Y(0.55), "f_s = F_{app}", size=13, color=FORCE)
    s.label(ax.X(7.5), ax.Y(2.7), "kinetic (sliding)", size=14, color=FORCE)
    s.label(ax.X(7.5), ax.Y(2.05), "f_k constant", size=13, color=FORCE)
    s.label(ax.X(5.3), ax.Y(5.6), "starts to slide", size=12, anchor="start")
    return s.render()


@diagram
def spring_force_graph():
    s = SVG(440, 290, "Spring force vs displacement (Hooke's law)")
    ax = Axes(s, 60, 240, 300, 180, xr=(0, 5), yr=(0, 5), xlabel="x", ylabel="|F_s|")
    ax.fill_under(lambda x: x, 0, 4, color=MOM, opacity=0.2)
    ax.plot(lambda x: x, 0, 4.8, color=FORCE)
    s.line(*ax.P(4, 0), *ax.P(4, 4), MUTED, 1.4, dash="4 4")
    s.text(ax.X(4), ax.Y(0) + 18, "x", size=15)
    s.label(ax.X(2.7), ax.Y(0.9), "area = ½kx² = U_s", size=14, color=MOM)
    s.label(ax.X(1.2), ax.Y(3.6), "slope = k", size=15, color=FORCE)
    s.label(220, 280, "magnitude |F_s| = k|x|; force points back toward equilibrium", size=13)
    return s.render()


@diagram
def circular_motion():
    s = SVG(420, 330, "Uniform circular motion")
    cx, cy, r = 200, 170, 115
    s.circle(cx, cy, r, fill="none", stroke=MUTED, width=1.6, dash="6 5")
    s.dot(cx, cy, 4)
    for deg in (40, 205):
        a = math.radians(deg)
        px, py = cx + r * math.cos(a), cy - r * math.sin(a)
        s.circle(px, py, 11, fill=FILL)
        polar(s, px, py, 80, deg + 90, VEL, label="v", lpos=(10, -8))
        polar(s, px, py, 62, deg + 180, ACC, label="a_c", lpos=(4, 16) if deg == 40 else (0, -14))
    s.curved_arrow(cx, cy, 40, 60, 130, color=MUTED, width=1.6)
    s.label(210, 318, "v tangent · a_c and F_{net} point to the center", size=13)
    return s.render()


@diagram
def vertical_circle():
    s = SVG(460, 340, "Vertical loop: forces at top and bottom")
    cx, cy, r = 230, 170, 110
    s.circle(cx, cy, r, fill="none", stroke=INK, width=3)
    s.dot(cx, cy, 3)
    tx, ty = cx, cy - r + 14
    s.circle(tx, ty, 11, fill=FILL)
    s.arrow(tx - 6, ty, tx - 6, ty + 55, FORCE, label="mg", lpos=(-22, -10))
    s.arrow(tx + 6, ty, tx + 6, ty + 45, FORCE, label="F_N", lpos=(24, -12))
    bx, by = cx, cy + r - 14
    s.circle(bx, by, 11, fill=FILL)
    s.arrow(bx + 6, by, bx + 6, by - 95, FORCE, label="F_N", lpos=(24, 18))
    s.arrow(bx - 6, by, bx - 6, by + 45, FORCE, label="mg", lpos=(-24, -12))
    s.label(380, 70, "Top:", size=14, color=INK, anchor="start")
    s.label(380, 90, "mg + F_N", size=13, anchor="start")
    s.label(380, 108, "= mv²/r", size=13, anchor="start")
    s.label(380, 250, "Bottom:", size=14, color=INK, anchor="start")
    s.label(380, 270, "F_N − mg", size=13, anchor="start")
    s.label(380, 288, "= mv²/r", size=13, anchor="start")
    return s.render()


@diagram
def center_of_mass():
    s = SVG(440, 190, "Center of mass of two masses")
    y = 90
    s.line(60, y, 380, y, INK, 5)
    s.circle(80, y, 30, fill=FILL)
    s.circle(360, y, 21, fill=FILL2)
    s.text(80, y, "2m", size=17)
    s.text(360, y, "m", size=17)
    xc = (2 * 80 + 360) / 3
    s.polygon([(xc, y + 6), (xc - 14, y + 30), (xc + 14, y + 30)], fill=MOM, stroke=INK, width=1.5)
    s.label(xc, y + 46, "cm", size=14, color=MOM)
    s.dim(80, 150, xc, 150, "!d/3", off=(0, -12))
    s.dim(xc, 150, 360, 150, "!2d/3", off=(0, -12))
    s.label(220, 30, "x_{cm} = (m₁x₁ + m₂x₂)/(m₁ + m₂) — closer to the heavier mass", size=13)
    return s.render()


@diagram
def gravity_two_masses():
    s = SVG(460, 190, "Newton's law of universal gravitation")
    s.circle(90, 90, 44, fill=FILL)
    s.circle(370, 90, 26, fill=FILL2)
    s.text(90, 90, "m_1", size=17)
    s.text(370, 90, "m_2", size=16)
    s.arrow(134, 90, 210, 90, FORCE, label="F_g", lpos=(4, -18))
    s.arrow(344, 90, 268, 90, FORCE, label="F_g", lpos=(-4, -18))
    s.dim(90, 156, 370, 156, "r", off=(0, -12))
    s.label(230, 182, "r measured center to center", size=13)
    return s.render()


# =============================================================================
# Unit 3 — Work, Energy, and Power
# =============================================================================

@diagram
def work_angle():
    s = SVG(460, 260, "Work done by a force at an angle")
    s.ground(30, 430, 180)
    s.rect(140, 120, 100, 60, fill=FILL)
    cx, cy = 240, 140
    th = 35
    L = 140
    ex, ey = cx + L * math.cos(math.radians(th)), cy - L * math.sin(math.radians(th))
    s.arrow(cx, cy, ex, cy, FORCE, width=1.8, dash="6 4", head=9)
    s.text((cx + ex) / 2, cy + 18, "F cos θ", size=14, color=FORCE)
    s.arrow(cx, cy, ex, ey, FORCE, label="F", lpos=(10, -8))
    s.arc(cx, cy, 44, 0, th, label="θ", lr=58)
    s.arrow(140, 225, 340, 225, DISP, width=2.8, label="d", lpos=(14, 0))
    s.label(230, 250, "W = F d cos θ (only the component along d does work)", size=13)
    return s.render()


@diagram
def energy_bar_chart():
    s = SVG(520, 290, "Energy bar charts for a falling ball")
    cols = ["K", "U_g", "U_s"]
    base = 220
    unit = 30

    def chart(x0, vals, title):
        s.label(x0 + 75, 30, title, size=14, color=INK)
        s.line(x0 - 6, base, x0 + 156, base, INK, 1.6)
        for i, (c, v) in enumerate(zip(cols, vals)):
            x = x0 + i * 52
            if v:
                s.rect(x + 6, base - v * unit, 36, v * unit, fill=MOM, stroke=INK, width=1.4, rx=1,
                       opacity=0.75)
            s.text(x + 24, base + 18, c, size=15)

    chart(30, [0, 5, 0], "Initial (at rest, high)")
    s.line(200, 50, 200, 250, FAINT, 1.4)
    s.label(260, 30, "W_{ext}", size=14, color=INK)
    s.text(260, base + 18, "W", size=15)
    s.line(230, base, 290, base, INK, 1.6)
    s.label(260, base - 20, "0", size=13)
    s.line(320, 50, 320, 250, FAINT, 1.4)
    chart(340, [5, 0, 0], "Final (fast, ground)")
    s.label(260, 275, "system = ball + Earth; no external work → total stays 5 blocks", size=13)
    return s.render()


@diagram
def energy_track():
    s = SVG(520, 245, "Frictionless track")
    def f(x):  # screen y of the track (ground at y = 230)
        h = 20 + 130 * math.exp(-((x - 30) / 90) ** 2) + 70 * math.exp(-((x - 400) / 55) ** 2)
        return 230 - h
    pts = [(30 + i * 4.6, f(30 + i * 4.6)) for i in range(101)]
    s.polyline(pts + [(490, 230), (30, 230)], color=INK, width=2, fill="#f3f4f6")
    s.polyline(pts, color=INK, width=3)
    for x, lab in ((40, "A"), (230, "B"), (400, "C")):
        y = f(x)
        s.circle(x, y - 12, 11, fill=FILL)
        s.text(x, y - 38, lab, size=17, weight="bold")
    s.line(10, 230, 510, 230, INK, 2)
    s.dim(500, f(40), 500, f(230), "!", off=(0, 0))
    s.line(40, f(40), 500, f(40), FAINT, 1.2, dash="4 4")
    s.line(230, f(230), 500, f(230), FAINT, 1.2, dash="4 4")
    s.text(486, (f(40) + f(230)) / 2, "h", size=16, anchor="end")
    return s.render()


# =============================================================================
# Unit 4 — Linear Momentum
# =============================================================================

@diagram
def impulse_graph():
    s = SVG(460, 290, "Force-time graph: area is impulse")
    ax = Axes(s, 60, 240, 330, 180, xr=(0, 10), yr=(0, 10), xlabel="t", ylabel="F")
    f = lambda t: 9 * math.sin(math.pi * (t - 2) / 6) ** 2 if 2 <= t <= 8 else 0  # noqa: E731
    ax.fill_under(f, 2, 8, color=MOM, opacity=0.25)
    ax.plot(f, 0, 10, color=FORCE)
    avg = 4.5
    s.rect(ax.X(2), ax.Y(avg), ax.X(8) - ax.X(2), ax.Y(0) - ax.Y(avg), fill="none", stroke=MUTED,
           width=1.6, rx=0)
    s.label(ax.X(5), ax.Y(2.4), "area = J = Δp", size=15, color=MOM)
    s.text(ax.X(8.3), ax.Y(avg), "F_{avg}", size=14, color=MUTED, anchor="start")
    s.dim(ax.X(2), ax.Y(0) + 24, ax.X(8), ax.Y(0) + 24, "!Δt", off=(0, 14))
    return s.render()


def _cart(s, x, y, w, color, label):
    s.rect(x, y - 36, w, 30, fill=color)
    s.circle(x + 14, y - 3, 6, fill="#9ca3af")
    s.circle(x + w - 14, y - 3, 6, fill="#9ca3af")
    s.text(x + w / 2, y - 21, label, size=15)


@diagram
def collision_inelastic():
    s = SVG(500, 260, "Perfectly inelastic collision")
    s.label(20, 22, "Before", size=14, color=INK, anchor="start")
    s.ground(20, 480, 100, hatch=False)
    _cart(s, 70, 100, 80, FILL, "m_1")
    _cart(s, 300, 100, 80, FILL2, "m_2")
    s.arrow(110, 44, 190, 44, VEL, label="v_1", lpos=(16, 0))
    s.label(340, 44, "at rest", size=13)
    s.label(20, 142, "After (stick together)", size=14, color=INK, anchor="start")
    s.ground(20, 480, 220, hatch=False)
    _cart(s, 200, 220, 80, FILL, "m_1")
    _cart(s, 280, 220, 80, FILL2, "m_2")
    s.arrow(280, 164, 330, 164, VEL, label="v_f", lpos=(16, 0))
    s.label(250, 248, "m₁v₁ = (m₁ + m₂) v_f · momentum conserved, KE is not", size=13)
    return s.render()


@diagram
def collision_elastic():
    s = SVG(500, 260, "Elastic collision of equal masses")
    s.label(20, 22, "Before", size=14, color=INK, anchor="start")
    s.ground(20, 480, 100, hatch=False)
    _cart(s, 80, 100, 80, FILL, "m")
    _cart(s, 300, 100, 80, FILL2, "m")
    s.arrow(120, 44, 200, 44, VEL, label="v", lpos=(14, 0))
    s.label(340, 44, "at rest", size=13)
    s.label(20, 142, "After", size=14, color=INK, anchor="start")
    s.ground(20, 480, 220, hatch=False)
    _cart(s, 200, 220, 80, FILL, "m")
    _cart(s, 360, 220, 80, FILL2, "m")
    s.label(240, 164, "at rest", size=13)
    s.arrow(400, 164, 480, 164, VEL, label="v", lpos=(0, -16))
    s.label(250, 248, "equal masses, elastic: velocities swap · p and KE both conserved", size=13)
    return s.render()


# =============================================================================
# Unit 5 — Torque and Rotational Dynamics
# =============================================================================

@diagram
def rot_kinematics():
    s = SVG(400, 345, "Angular position and arc length")
    cx, cy, r = 190, 190, 115
    s.circle(cx, cy, r, fill="#f3f4f6")
    s.dot(cx, cy, 4)
    th = 55
    s.line(cx, cy, cx + r + 30, cy, MUTED, 1.4, dash="5 4")
    px, py = cx + r * math.cos(math.radians(th)), cy - r * math.sin(math.radians(th))
    s.line(cx, cy, px, py, INK, 2)
    s.text((cx + px) / 2 - 12, (cy + py) / 2 + 2, "r", size=17)
    s.dot(px, py, 6, DISP)
    s.arc(cx, cy, r, 0, th, color=DISP, width=4.5)
    s.text(cx + (r + 18) * math.cos(math.radians(27)), cy - (r + 18) * math.sin(math.radians(27)),
           "s", size=18, color=DISP)
    s.arc(cx, cy, 36, 0, th, label="θ", lr=50)
    s.curved_arrow(cx, cy, r + 32, 70, 125, color=MOM, label="ω", lr=r + 50)
    s.label(200, 335, "s = rθ (θ in radians)", size=14, color=INK)
    return s.render()


@diagram
def linear_vs_rotational():
    s = SVG(420, 300, "Tangential speed grows with radius")
    cx, cy, r = 170, 150, 110
    s.circle(cx, cy, r, fill="#f3f4f6")
    s.dot(cx, cy, 4)
    for rr, lab in ((r / 2, "v₁"), (r, "v₂ = 2v₁")):
        s.line(cx, cy, cx, cy - rr, MUTED, 1.4, dash="4 4")
        s.dot(cx, cy - rr, 5, INK)
        s.arrow(cx, cy - rr, cx + rr * 0.95, cy - rr, VEL, label="!" + lab, lpos=(10, -14), lsize=14)
    s.text(cx - 12, cy - r / 4, "r", size=15)
    s.text(cx - 12, cy - 3 * r / 4, "r", size=15)
    s.curved_arrow(cx, cy, 70, -40, -140, color=MOM, label="ω", lr=88)
    s.label(355, 160, "v = rω", size=16, color=INK)
    s.label(355, 185, "a_t = rα", size=16, color=INK)
    s.label(355, 210, "a_c = rω²", size=16, color=INK)
    s.label(210, 285, "same ω everywhere on a rigid body, but v depends on r", size=13)
    return s.render()


@diagram
def torque_lever_arm():
    s = SVG(460, 360, "Torque: lever arm and angle")
    hx, hy = 60, 170
    s.rect(hx, hy - 7, 290, 14, fill="#e5e7eb", stroke=INK, width=1.6, rx=2)
    s.circle(hx, hy, 9, fill="#ffffff", stroke=INK)
    s.dot(hx, hy, 3)
    s.label(hx, hy - 24, "pivot", size=12)
    px, py = 340, hy
    th = 60
    u = (math.cos(math.radians(th)), -math.sin(math.radians(th)))
    proj = (hx - px) * u[0] + (hy - py) * u[1]
    fx, fy = px + proj * u[0], py + proj * u[1]
    s.line(px + 60 * u[0], py + 60 * u[1], fx - 25 * u[0], fy - 25 * u[1], MUTED, 1.4, dash="6 5")
    s.label(fx + 30, fy + 8, "line of action", size=12, anchor="start")
    s.arrow(hx, hy + 2, px, py + 2, DISP, width=2, head=9)
    s.text((hx + px) / 2, hy + 22, "r", size=17, color=DISP)
    s.dim(hx, hy, fx, fy, "r_⊥ = r sin θ", off=(-58, 12))
    s.line(fx, fy, fx + 10 * u[0], fy + 10 * u[1], INK, 1.2)
    s.arrow(px, py, px + 110 * u[0], py + 110 * u[1], FORCE, label="F", lpos=(12, -6))
    s.arc(px, py, 34, 0, th, label="θ", lr=48)
    s.label(320, 30, "τ = r F sin θ = r⊥ F", size=16, color=INK)
    return s.render()


@diagram
def rot_inertia_shapes():
    s = SVG(660, 230, "Rotational inertia of common shapes")
    y = 85
    # hoop
    s.circle(70, y, 46, fill="none", stroke=INK, width=5)
    s.dot(70, y, 4)
    s.label(70, 160, "hoop / ring", size=13)
    s.text(70, 186, "MR^2", size=16)
    # disk
    s.circle(195, y, 46, fill=FILL)
    s.dot(195, y, 4)
    s.label(195, 160, "solid disk / cylinder", size=13)
    s.text(195, 186, "!½MR²", size=16)
    # sphere
    s.circle(320, y, 46, fill=FILL2)
    s.path(f"M274,{y} A46,14 0 0 0 366,{y}", color=MUTED, width=1.2)
    s.dot(320, y, 4)
    s.label(320, 160, "solid sphere", size=13)
    s.text(320, 186, "!⅖MR²", size=16)
    # rod centre
    s.rect(390, y - 5, 110, 10, fill="#e5e7eb", stroke=INK, width=1.6, rx=2)
    s.line(445, y - 32, 445, y + 32, MUTED, 1.6, dash="4 3")
    s.label(445, 160, "rod, center axis", size=13)
    s.text(445, 186, "!¹⁄₁₂ ML²", size=16)
    # rod end
    s.rect(530, y - 5, 110, 10, fill="#e5e7eb", stroke=INK, width=1.6, rx=2)
    s.line(530, y - 32, 530, y + 32, MUTED, 1.6, dash="4 3")
    s.label(585, 160, "rod, end axis", size=13)
    s.text(585, 186, "!⅓ ML²", size=16)
    s.label(330, 220, "more mass farther from the axis → larger I", size=13)
    return s.render()


@diagram
def seesaw():
    s = SVG(480, 250, "Rotational equilibrium on a seesaw")
    y = 130
    s.polygon([(240, y + 6), (218, y + 50), (262, y + 50)], fill="#e5e7eb")
    s.ground(170, 310, y + 50, hatch=True)
    s.rect(40, y - 6, 400, 12, fill="#fef3c7", stroke=INK, width=1.6, rx=2)
    s.rect(122, y - 62, 56, 56, fill=FILL)
    s.text(150, y - 34, "m_1", size=17)
    s.rect(380, y - 42, 40, 36, fill=FILL2)
    s.text(400, y - 24, "m_2", size=15)
    s.arrow(150, y, 150, y + 80, FORCE, label="m_1g", lpos=(-30, -10))
    s.arrow(400, y, 400, y + 50, FORCE, label="m_2g", lpos=(30, -10))
    s.arrow(240, y, 240, y - 72, FORCE, label="F_N", lpos=(22, 14))
    s.dim(150, y - 95, 240, y - 95, "d_1", off=(0, -12))
    s.dim(240, y - 95, 400, y - 95, "d_2", off=(0, -12))
    s.label(240, 236, "Στ = 0:  m₁g d₁ = m₂g d₂", size=14, color=INK)
    return s.render()


@diagram
def massive_pulley():
    s = SVG(420, 360, "Hanging mass on a pulley with rotational inertia")
    cx, cy, R = 170, 100, 60
    s.ceiling(110, 230, 20)
    s.line(cx, 20, cx, cy, INK, 2)
    s.circle(cx, cy, R, fill="#e5e7eb")
    s.dot(cx, cy, 5)
    s.text(cx - 22, cy + 6, "M, R", size=15)
    s.line(cx + R, cy, cx + R, 255, INK, 2)
    s.rect(cx + R - 24, 255, 48, 48, fill=FILL)
    s.text(cx + R, 279, "m", size=17)
    s.arrow(cx + R, cy + 6, cx + R, cy + 56, FORCE, label="T", lpos=(16, -6))
    s.arrow(cx + R, 255, cx + R, 207, FORCE, label="T", lpos=(14, 8))
    s.arrow(cx + R, 303, cx + R, 351, FORCE, label="mg", lpos=(24, -10))
    s.curved_arrow(cx, cy, R + 18, 215, 145, color=MOM, label="α", lr=R + 34)
    s.arrow(320, 240, 320, 290, ACC, label="a", lpos=(14, 0))
    s.label(330, 180, "TR = Iα", size=14, color=INK, anchor="start")
    s.label(330, 200, "mg − T = ma", size=14, color=INK, anchor="start")
    s.label(330, 220, "a = Rα", size=14, color=INK, anchor="start")
    return s.render()


@diagram
def parallel_axis():
    s = SVG(460, 210, "Parallel-axis theorem")
    y = 90
    s.rect(80, y - 7, 300, 14, fill="#e5e7eb", stroke=INK, width=1.6, rx=2)
    for x, col, lab in ((230, MUTED, "axis through cm"), (80, MOM, "new axis")):
        s.circle(x, y, 10, fill="#ffffff", stroke=col, width=2)
        s.dot(x, y, 3, col)
        s.label(x, y - 28, lab, size=13, color=col)
    s.dim(80, y + 36, 230, y + 36, "d", off=(0, 14))
    s.label(230, 180, "I = I_{cm} + Md²   (rod: ¹⁄₁₂ML² + M(L/2)² = ⅓ML²)", size=14, color=INK)
    return s.render()


# =============================================================================
# Unit 6 — Energy and Momentum of Rotating Systems
# =============================================================================

@diagram
def rolling():
    s = SVG(440, 300, "Rolling without slipping")
    cx, cy, R = 190, 150, 90
    s.ground(30, 410, cy + R)
    s.circle(cx, cy, R, fill="#f3f4f6")
    s.dot(cx, cy, 5)
    s.arrow(cx, cy, cx + 70, cy, VEL, label="v_{cm}", lpos=(8, -16))
    s.arrow(cx, cy - R, cx + 140, cy - R, VEL, label="2v_{cm}", lpos=(10, -16))
    s.dot(cx, cy + R, 6, FORCE)
    s.line(cx + 6, cy + R - 4, cx + 62, cy + R - 22, FORCE, 1.2)
    s.label(cx + 66, cy + R - 24, "contact point: v = 0", size=13, color=FORCE, anchor="start")
    s.curved_arrow(cx, cy, 40, 160, 40, color=MOM, label="ω", lr=56)
    s.label(220, 290, "v_{cm} = Rω  ·  K = ½Mv² + ½Iω²", size=14, color=INK)
    return s.render()


@diagram
def angular_momentum_particle():
    s = SVG(460, 260, "Angular momentum of a point particle")
    ox, oy = 90, 200
    s.dot(ox, oy, 6, INK)
    s.text(ox - 16, oy + 4, "O", size=16)
    y = 80
    s.line(40, y, 440, y, FAINT, 1.4, dash="6 5")
    px = 300
    s.line(ox, oy, px, y, DISP, 2)
    s.text((ox + px) / 2 + 12, (oy + y) / 2 + 12, "r", size=17, color=DISP)
    s.circle(px, y, 12, fill=FILL)
    s.arrow(px, y, px + 100, y, VEL, label="v", lpos=(14, 0))
    s.dim(ox, oy, ox, y, "r_⊥", off=(-22, 0))
    s.label(260, 240, "L = m v r⊥ = m v r sin θ (constant if no net torque)", size=14, color=INK)
    return s.render()


@diagram
def spinning_skater():
    s = SVG(520, 270, "Conservation of angular momentum: skater pulls arms in")
    for cx, reach, w, lab in ((130, 85, 70, "arms out: large I, small ω"),
                              (390, 34, 150, "arms in: small I, large ω")):
        s.circle(cx, 140, 22, fill=FILL2)
        s.line(cx - reach, 140, cx + reach, 140, INK, 4)
        s.circle(cx - reach, 140, 9, fill=FILL)
        s.circle(cx + reach, 140, 9, fill=FILL)
        if reach > 50:
            s.curved_arrow(cx, 140, reach + 22, 65, 115, color=MOM, label="ω", lr=reach + 40)
        else:
            s.curved_arrow(cx, 140, reach + 22, 10, 240, color=MOM, label="ω", lr=reach + 40)
        s.label(cx, 236, lab, size=13)
    s.arrow(240, 140, 290, 140, MUTED, width=2)
    s.label(260, 260, "top view · L = Iω stays constant", size=14, color=INK)
    return s.render()


@diagram
def orbits():
    s = SVG(640, 300, "Circular and elliptical orbits")
    cx, cy, r = 150, 150, 100
    s.circle(cx, cy, r, fill="none", stroke=MUTED, width=1.6, dash="6 5")
    s.circle(cx, cy, 26, fill=FILL)
    s.text(cx, cy, "M", size=16)
    sx, sy = cx + r * math.cos(math.radians(40)), cy - r * math.sin(math.radians(40))
    s.circle(sx, sy, 8, fill=FILL2)
    polar(s, sx, sy, 70, 130, VEL, label="v", lpos=(-6, -12))
    polar(s, sx, sy, 50, 220, FORCE, label="F_g", lpos=(14, 10))
    s.label(cx, 280, "circular: F_g = mv²/r", size=13, color=INK)
    # ellipse
    ex, ey, a, b = 460, 150, 150, 95
    c = math.sqrt(a * a - b * b)
    s.raw(f'<ellipse cx="{ex}" cy="{ey}" rx="{a}" ry="{b}" fill="none" stroke="{MUTED}" '
          f'stroke-width="1.6" stroke-dasharray="6 5"/>')
    fx = ex - c
    s.circle(fx, ey, 18, fill="#fde047")
    s.circle(ex - a, ey, 8, fill=FILL2)
    s.circle(ex + a, ey, 8, fill=FILL2)
    s.arrow(ex - a, ey, ex - a, ey - 90, VEL, label="v_{fast}", lpos=(4, -14), lsize=15)
    s.arrow(ex + a, ey, ex + a, ey + 34, VEL, label="v_{slow}", lpos=(0, 16), lsize=15)
    s.dim(ex - a, ey + 24, fx, ey + 24, "!r_p", off=(0, 14), size=13)
    s.dim(fx, ey - 28, ex + a, ey - 28, "!r_a", off=(0, -12), size=13)
    s.label(ex, 280, "elliptical: L conserved → fastest when closest", size=13, color=INK)
    return s.render()


# =============================================================================
# Unit 7 — Oscillations
# =============================================================================

@diagram
def shm_spring():
    s = SVG(540, 330, "Mass-spring oscillator at -A, 0, +A")
    X = lambda v: 260 + v * 120  # noqa: E731
    wall = 40
    rows = [(-1, "x = −A", "v = 0", "a, F max →"), (0, "x = 0", "v max", "a = F = 0"),
            (1, "x = +A", "v = 0", "← a, F max")]
    for i, (pos, _, vt, at) in enumerate(rows):
        y = 70 + i * 90
        s.wall(wall, y - 30, y + 30, side="left")
        s.ground(wall, 500, y + 22, hatch=False)
        bx = X(pos)
        s.spring(wall, y, bx - 25, y, coils=9, amp=9)
        s.rect(bx - 25, y - 22, 50, 44, fill=FILL)
        s.text(bx, y, "m", size=16)
        if pos == -1:
            s.arrow(bx + 28, y - 30, bx + 90, y - 30, ACC, width=2.4, label="a", lpos=(12, 0))
        elif pos == 1:
            s.arrow(bx - 28, y - 30, bx - 90, y - 30, ACC, width=2.4, label="a", lpos=(-12, 0))
        else:
            s.arrow(bx - 20, y - 32, bx + 50, y - 32, VEL, width=2.4, label="v_{max}",
                    lpos=(24, 0), lsize=15)
        s.label(510, y - 6, vt, size=13, anchor="end")
        s.label(510, y + 10, at, size=12, anchor="end")
    for pos, lab in ((-1, "−A"), (0, "0"), (1, "+A")):
        s.line(X(pos), 30, X(pos), 300, FAINT, 1.2, dash="4 4")
        s.text(X(pos), 316, "!" + lab, size=14, color=MUTED)
    return s.render()


@diagram
def shm_graphs():
    s = SVG(460, 440, "Position, velocity, acceleration vs time in SHM")
    data = [("x", DISP, math.cos), ("v", VEL, lambda t: -math.sin(t)),
            ("a", ACC, lambda t: -math.cos(t))]
    for i, (lab, col, f) in enumerate(data):
        oy = 95 + i * 135
        ax = Axes(s, 60, oy, 340, 50, xr=(0, 4 * math.pi), yr=(0, 1), xlabel="t", ylabel=None)
        s.arrow(60, oy + 55, 60, oy - 60, INK, width=1.8, head=9)
        s.text(44, oy - 52, lab, size=17)
        ax.yr = (-1.15, 1.15)
        ax.oy = oy + 50
        ax.h = 100
        ax.plot(f, color=col)
    for k in range(1, 5):
        x = 60 + 340 * k / 4
        s.line(x, 40, x, 420, FAINT, 1, dash="3 4")
    s.label(60 + 340 / 2, 432, "T", size=13)
    s.label(230, 16, "x = A cos ωt    v = −Aω sin ωt    a = −Aω² cos ωt", size=13, color=INK)
    return s.render()


@diagram
def pendulum():
    s = SVG(470, 330, "Simple pendulum forces")
    px, py, L, th = 150, 40, 170, 25
    s.ceiling(100, 200, py)
    s.line(px, py, px, py + L + 20, FAINT, 1.4, dash="5 5")
    sn, cs = math.sin(math.radians(th)), math.cos(math.radians(th))
    bx, by = px + L * sn, py + L * cs
    s.line(px, py, bx, by, INK, 2)
    s.text(px + 0.3 * (bx - px) + 16, py + 0.3 * (by - py) - 2, "L", size=17)
    s.arc(px, py, 56, -90, -90 + th, label="θ", lr=72)
    g = 100
    # components first (dashed), then the real forces on top
    s.arrow(bx, by, bx - cs * g * sn, by + sn * g * sn, FORCE, width=1.8, dash="6 4", head=9,
            label="mg sin θ", lpos=(-44, 6), lsize=14)
    s.arrow(bx, by, bx + sn * g * cs, by + cs * g * cs, FORCE, width=1.8, dash="6 4", head=9,
            label="mg cos θ", lpos=(46, 0), lsize=14)
    s.arrow(bx, by, bx, by + g, FORCE, label="mg", lpos=(0, 16))
    s.arrow(bx, by, bx - sn * 80, by - cs * 80, FORCE, label="F_T", lpos=(20, 12))
    s.circle(bx, by, 14, fill=FILL)
    s.label(360, 60, "restoring force:", size=13, color=INK)
    s.label(360, 80, "mg sin θ (toward equilibrium)", size=13, color=INK)
    s.label(360, 112, "small θ:", size=13, color=INK)
    s.label(360, 132, "period T = 2π√(L/g)", size=13, color=INK)
    return s.render()


@diagram
def shm_energy():
    s = SVG(460, 290, "Energy vs position in simple harmonic motion")
    ax = Axes(s, 230, 240, 180, 180, xr=(-1.2, 1.2), yr=(0, 1.2), xlabel="x", ylabel="E")
    ax.ox, ax.w = 50, 360
    ax.plot(lambda x: x * x, -1, 1, color=DISP)
    ax.plot(lambda x: 1 - x * x, -1, 1, color=VEL)
    ax.plot(lambda x: 1, -1.05, 1.05, color=INK, width=2, dash="7 4")
    for v, lab in ((-1, "−A"), (1, "+A")):
        s.line(ax.X(v), ax.Y(0), ax.X(v), ax.Y(1), FAINT, 1.2, dash="4 4")
        s.text(ax.X(v), ax.Y(0) + 18, "!" + lab, size=14, color=MUTED)
    s.label(ax.X(0.8) + 20, ax.Y(0.55), "U = ½kx²", size=14, color=DISP, anchor="start")
    s.label(ax.X(0) + 28, ax.Y(0.88), "K", size=15, color=VEL, anchor="start")
    s.label(ax.X(1.05) + 6, ax.Y(1) - 12, "E = ½kA²", size=14, color=INK, anchor="start")
    return s.render()


# =============================================================================
# Unit 8 — Fluids
# =============================================================================

@diagram
def pressure_depth():
    s = SVG(440, 290, "Pressure increases with depth")
    s.rect(60, 70, 280, 190, fill=FLUID, stroke="none", rx=0)
    s.polyline([(60, 40), (60, 260), (340, 260), (340, 40)], color=INK, width=3)
    s.line(60, 70, 340, 70, VEL, 1.6)
    for x in (110, 200, 290):
        s.arrow(x, 30, x, 66, MUTED, width=1.6, head=8)
    s.text(370, 40, "P_0", size=16, color=MUTED)
    s.dot(130, 190, 6, INK)
    s.dot(280, 190, 6, INK)
    s.text(130, 210, "A", size=15, weight="bold")
    s.text(280, 210, "B", size=15, weight="bold")
    s.dim(200, 72, 200, 188, "h", off=(14, 0))
    s.line(130, 190, 280, 190, MUTED, 1.2, dash="4 4")
    s.label(220, 282, "P = P₀ + ρgh  ·  same depth → same pressure (P_A = P_B)", size=13, color=INK)
    return s.render()


@diagram
def buoyancy():
    s = SVG(440, 300, "Buoyant force on a submerged object")
    s.rect(40, 50, 260, 220, fill=FLUID, stroke="none", rx=0)
    s.polyline([(40, 30), (40, 270), (300, 270), (300, 30)], color=INK, width=3)
    s.line(40, 50, 300, 50, VEL, 1.6)
    s.rect(120, 120, 90, 70, fill=FILL2)
    for x in (140, 165, 190):
        s.arrow(x, 98, x, 118, MUTED, width=1.6, head=7)
        s.arrow(x, 222, x, 192, MUTED, width=1.6, head=8)
    s.label(112, 106, "smaller P", size=12, anchor="end")
    s.label(112, 214, "larger P", size=12, anchor="end")
    s.arrow(165, 155, 165, 70, FORCE, width=2.8, label="F_b", lpos=(-22, 6))
    s.arrow(150, 155, 150, 245, FORCE, width=2.8, label="mg", lpos=(-22, -6))
    s.label(370, 140, "F_b = ρ_{fluid} V_{disp} g", size=14, color=INK)
    s.label(370, 162, "= weight of fluid", size=13)
    s.label(370, 180, "displaced", size=13)
    return s.render()


@diagram
def floating():
    s = SVG(420, 275, "Floating object: buoyant force equals weight")
    s.rect(40, 110, 300, 130, fill=FLUID, stroke="none", rx=0)
    s.polyline([(40, 50), (40, 240), (340, 240), (340, 50)], color=INK, width=3)
    s.line(40, 110, 340, 110, VEL, 1.6)
    s.rect(140, 60, 100, 100, fill="#fde68a")
    s.rect(140, 110, 100, 50, fill=VEL, stroke="none", rx=0, opacity=0.18)
    s.arrow(200, 110, 200, 30, FORCE, label="F_b", lpos=(22, 10))
    s.arrow(180, 110, 180, 190, FORCE, label="mg", lpos=(-24, -8))
    s.dim(260, 110, 260, 160, "!V_{sub}", off=(32, 0), size=13)
    s.label(210, 262, "F_b = mg  →  V_{sub} / V = ρ_{obj} / ρ_{fluid}", size=13, color=INK)
    return s.render()


@diagram
def continuity():
    s = SVG(500, 210, "Continuity equation in a narrowing pipe")
    top = [(20, 50), (190, 50), (290, 85), (480, 85)]
    bot = [(20, 160), (190, 160), (290, 125), (480, 125)]
    s.polygon(top + bot[::-1], fill=FLUID, stroke="none", width=0)
    s.polyline(top, INK, 3)
    s.polyline(bot, INK, 3)
    s.raw(f'<ellipse cx="90" cy="105" rx="14" ry="55" fill="none" stroke="{DISP}" stroke-width="2"/>')
    s.raw(f'<ellipse cx="400" cy="105" rx="7" ry="20" fill="none" stroke="{DISP}" stroke-width="2"/>')
    s.text(90, 34, "A_1", size=16, color=DISP)
    s.text(400, 68, "A_2", size=16, color=DISP)
    s.arrow(110, 105, 165, 105, VEL, label="v_1", lpos=(16, 0))
    s.arrow(320, 105, 440, 105, VEL, label="v_2", lpos=(18, 0))
    s.label(250, 196, "A₁v₁ = A₂v₂  ·  narrower → faster", size=14, color=INK)
    return s.render()


@diagram
def bernoulli():
    s = SVG(520, 280, "Bernoulli's equation along a pipe")
    top = [(20, 150), (170, 150), (290, 55), (500, 55)]
    bot = [(20, 225), (170, 225), (300, 100), (500, 100)]
    s.polygon(top + bot[::-1], fill=FLUID, stroke="none", width=0)
    s.polyline(top, INK, 3)
    s.polyline(bot, INK, 3)
    s.arrow(60, 188, 115, 188, VEL, label="v_1", lpos=(16, 0))
    s.arrow(380, 78, 470, 78, VEL, label="v_2", lpos=(0, -16))
    s.text(85, 130, "P_1", size=16)
    s.text(420, 36, "P_2", size=16)
    s.line(10, 262, 510, 262, MUTED, 1.4, dash="6 4")
    s.label(490, 252, "y = 0", size=12, anchor="end")
    s.dim(40, 262, 40, 188, "y_1", off=(16, 20), size=14)
    s.dim(340, 262, 340, 78, "y_2", off=(18, 0), size=14)
    s.label(250, 20, "P + ½ρv² + ρgy = constant along a streamline", size=14, color=INK)
    return s.render()


@diagram
def torricelli():
    s = SVG(460, 300, "Torricelli's theorem: flow from a hole")
    s.rect(50, 60, 160, 180, fill=FLUID, stroke="none", rx=0)
    s.polyline([(50, 30), (50, 240), (210, 240), (210, 30)], color=INK, width=3)
    s.line(50, 60, 210, 60, VEL, 1.6)
    hy = 210
    s.rect(206, hy - 6, 8, 12, fill="#ffffff", stroke="none", rx=0)
    pts = [(214 + t * 160, hy + 0.0045 * (t * 160) ** 2) for t in [i / 30 for i in range(31)]]
    pts = [(x, y) for x, y in pts if y <= 285]
    s.polyline(pts, VEL, 5)
    s.arrow(214, hy, 290, hy, VEL, label="v", lpos=(14, -12))
    s.dim(130, 62, 130, hy, "h", off=(14, 0))
    s.line(60, hy, 206, hy, MUTED, 1.2, dash="4 4")
    s.label(330, 120, "v = √(2gh)", size=16, color=INK)
    s.label(330, 144, "same as free fall from h", size=13)
    s.ground(30, 440, 290, hatch=False)
    return s.render()
