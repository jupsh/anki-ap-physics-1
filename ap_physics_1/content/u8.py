from cards import B, C, Section, Unit

UNIT = Unit(8, "Fluids", [
    Section("8.1", "Internal Structure and Density", [
        C(r"Density: \(\rho = {{c1::\dfrac{m}{V}}}\)", tags=["formula"]),
        B(r"What is the density of water, in SI units?",
          r"\(\rho \approx 1000\text{ kg/m}^3\)"),
        B(r"What is a <b>fluid</b>?",
          r"A substance that can <b>flow</b> and takes the shape of its container: liquids and gases."),
        B(r"What are the assumptions of an <b>ideal fluid</b>?",
          r"<b>Incompressible</b> (constant density), <b>non-viscous</b> (no internal friction), and "
          r"<b>steady, laminar</b> flow."),
        B(r"A uniform block is cut in half. What happens to the density of each half?",
          r"<b>Nothing.</b> The mass and the volume both halve."),
        B(r"An object has a mass of \(2\text{ kg}\) and a volume of \(0.001\text{ m}^3\). What is its density?",
          r"\(\rho = 2/0.001 = 2000\text{ kg/m}^3\)", tags=["problem"]),
        B(r"Does an object with density \(2000\text{ kg/m}^3\) float or sink in water?",
          r"It <b>sinks</b>: it's denser than water (\(1000\text{ kg/m}^3\))."),
    ]),

    Section("8.2", "Pressure", [
        C(r"Pressure: \(P = {{c1::\dfrac{F_\perp}{A}}}\)", tags=["formula"]),
        B(r"What is the SI unit of pressure?",
          r"The pascal: \(1\text{ Pa} = 1\text{ N/m}^2\)"),
        C(r"Absolute pressure at depth \(h\) in a fluid: \(P = {{c1::P_0 + \rho gh}}\)", d="pressure_depth",
          tags=["formula"]),
        B(r"What is <b>gauge pressure</b>?",
          r"Pressure above atmospheric: \(P_{gauge} = P - P_{atm}\).",
          extra=r"At depth \(h\) in an open container: \(P_{gauge} = \rho gh\)."),
        B(r"Does the pressure at a given depth depend on the shape of the container?",
          r"<b>No.</b> Only on depth, fluid density, and the pressure at the surface.",
          bd="pressure_depth"),
        B(r"Two points are at the same depth in the same connected, still fluid. How do their pressures compare?",
          r"They are <b>equal</b>."),
        B(r"Which direction does fluid pressure push on a surface?",
          r"<b>Perpendicular</b> to the surface."),
        B(r"Roughly what is atmospheric pressure at sea level?",
          r"\(1.0\times10^5\text{ Pa}\) (1 atm)"),
        B(r"What is the gauge pressure \(10\text{ m}\) under water? \((g = 10\text{ m/s}^2)\)",
          r"\(\rho gh = 1000(10)(10) = 1\times10^5\text{ Pa}\), about 1 atm", tags=["problem"]),
        B(r"What is the absolute pressure \(10\text{ m}\) under water?",
          r"About \(2\times10^5\text{ Pa}\) (2 atm): 1 atm of air plus 1 atm of water.", tags=["problem"]),
        B(r"State <b>Pascal's principle</b>.",
          r"A pressure change applied to an enclosed fluid is passed on <b>undiminished</b> to every part "
          r"of the fluid."),
        C(r"Hydraulic lift: \(\dfrac{F_1}{A_1} = {{c1::\dfrac{F_2}{A_2}}}\)", tags=["formula"],
          extra=r"A small force on a small piston gives a large force on a large piston."),
    ]),

    Section("8.3", "Fluids and Newton's Laws", [
        C(r"Archimedes' principle: \(F_b = {{c1::\rho_{fluid}V_{disp}g}}\)", tags=["formula"],
          extra=r"The buoyant force equals the <b>weight of the fluid displaced</b>."),
        B(r"What causes the buoyant force?",
          r"Pressure increases with depth, so the fluid pushes up on the bottom of an object harder than it "
          r"pushes down on the top.",
          bd="buoyancy"),
        B(r"What is the condition for an object to float?",
          r"\(\rho_{obj} \lt \rho_{fluid}\)",
          extra=r"When it floats, \(F_b = mg\)."),
        C(r"Fraction of a floating object below the surface: \(\dfrac{V_{sub}}{V} = {{c1::\dfrac{\rho_{obj}}{\rho_{fluid}}}}\)",
          d="floating", tags=["formula"]),
        B(r"Ice (\(\rho = 920\text{ kg/m}^3\)) floats in water. What fraction of it is under the surface?",
          r"\(920/1000 = 92\%\)", tags=["problem"]),
        C(r"Apparent weight of an object fully submerged in a fluid: \(W_{app} = {{c1::mg - F_b}}\)",
          tags=["formula"],
          extra=r"This is what a scale reads if the object hangs from it underwater."),
        B(r"Does the buoyant force on a <b>fully submerged</b> object change as it goes deeper (incompressible fluid)?",
          r"<b>No.</b> The difference in pressure between top and bottom stays the same, and so does \(V_{disp}\)."),
        B(r"A \(0.002\text{ m}^3\) rock is fully submerged in water. What is the buoyant force on it? "
          r"\((g = 10\text{ m/s}^2)\)",
          r"\(F_b = 1000(0.002)(10) = 20\text{ N}\)", tags=["problem"]),
    ]),

    Section("8.4", "Fluids and Conservation Laws", [
        C(r"Continuity equation: \(A_1v_1 = {{c1::A_2v_2}}\)", d="continuity", tags=["formula"],
          extra=r"The volume flow rate \(Av\) (m³/s) is the same everywhere along the pipe."),
        B(r"What conservation law does the continuity equation express?",
          r"<b>Conservation of mass</b>. For an incompressible fluid, the volume in per second equals the "
          r"volume out per second."),
        B(r"Why does water speed up when you partly cover the end of a hose?",
          r"The area gets smaller, and \(Av\) must stay constant, so \(v\) increases."),
        C(r"Bernoulli's equation: \(P_1 + {{c1::\tfrac12\rho v_1^2}} + {{c2::\rho gy_1}} = "
          r"P_2 + \tfrac12\rho v_2^2 + \rho gy_2\)", d="bernoulli", tags=["formula"]),
        B(r"What conservation law does Bernoulli's equation express?",
          r"<b>Conservation of energy</b> for a flowing fluid, per unit volume."),
        B(r"In a <b>horizontal</b> pipe, is the pressure lower in a wide section or a narrow section?",
          r"The <b>narrow</b> section. The fluid moves faster there, so its pressure is lower."),
        C(r"Torricelli's theorem: fluid flows out of a hole a depth \(h\) below the surface at speed "
          r"\(v = {{c1::\sqrt{2gh}}}\)", d="torricelli", tags=["formula"],
          extra=r"That's the same speed as an object dropped from height \(h\)."),
        B(r"Water flows at \(2\text{ m/s}\) in a pipe that narrows to half its cross-sectional area. What is "
          r"the new speed?",
          r"\(v_2 = v_1\dfrac{A_1}{A_2} = 4\text{ m/s}\)", tags=["problem"]),
        B(r"In a horizontal pipe, water speeds up from \(2\text{ m/s}\) to \(4\text{ m/s}\). By how much does "
          r"the pressure drop?",
          r"\(\Delta P = \tfrac12\rho(v_2^2 - v_1^2) = \tfrac12(1000)(16 - 4) = 6000\text{ Pa}\)", tags=["problem"]),
    ]),
])
