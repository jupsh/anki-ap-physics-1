from cards import B, C, Section, Unit

UNIT = Unit(3, "Work, Energy, and Power", [
    Section("3.1", "Translational Kinetic Energy", [
        C(r"Translational kinetic energy: \(K = {{c1::\tfrac12 mv^2}}\)", tags=["formula"]),
        B(r"Is kinetic energy a scalar or a vector?",
          r"A <b>scalar</b>."),
        B(r"Can kinetic energy be negative?",
          r"<b>No.</b> Mass is positive and \(v^2\) can't be negative."),
        B(r"What is the SI unit of energy?",
          r"The joule: \(1\text{ J} = 1\text{ kg·m}^2/\text{s}^2 = 1\text{ N·m}\)"),
        B(r"If an object's speed <b>doubles</b>, what happens to its kinetic energy?",
          r"It becomes <b>4×</b> as large (\(K \propto v^2\)).",
          extra=r"This is why braking distance grows with the square of speed."),
        B(r"Does an object's kinetic energy depend on its direction of motion?",
          r"<b>No.</b> It depends only on speed, through \(v^2\)."),
        B(r"Does an object's kinetic energy depend on the reference frame?",
          r"<b>Yes</b>, because speed depends on the frame."),
        B(r"What is the kinetic energy of a \(2\text{ kg}\) object moving at \(3\text{ m/s}\)?",
          r"\(K = \tfrac12(2)(3)^2 = 9\text{ J}\)", tags=["problem"]),
    ]),

    Section("3.2", "Work", [
        C(r"Work done by a constant force: \(W = {{c1::Fd\cos\theta}}\), where \(\theta\) is the angle "
          r"between \(\vec F\) and the displacement", d="work_angle", tags=["formula"],
          extra=r"Equivalently, \(W = F_\parallel d\): only the force component along the displacement does work."),
        C(r"The work done by a force is positive when \(\theta\) {{c1::\(\lt 90^\circ\)}}, negative when "
          r"\(\theta\) {{c2::\(> 90^\circ\)}}, and zero when \(\theta\) {{c3::\(= 90^\circ\)}}."),
        B(r"An object slides along a level floor. How much work does the <b>normal force</b> do on it?",
          r"<b>Zero.</b> The normal force is perpendicular to the displacement."),
        B(r"How much work does the centripetal force do on an object in <b>uniform circular motion</b>?",
          r"<b>Zero.</b> The force is always perpendicular to the velocity.",
          extra=r"That's why the speed stays constant."),
        B(r"You carry a box horizontally at constant velocity. How much work does your upward force do on it?",
          r"<b>Zero.</b> Your force is vertical and the displacement is horizontal."),
        C(r"Work–energy theorem: \(W_{net} = {{c1::\Delta K}}\)", tags=["formula"]),
        B(r"How do you find the work done by a varying force from a graph?",
          r"Find the <b>area under the graph</b> of force (component along the motion) vs. position."),
        B(r"How much work does kinetic friction do on an object that slides a distance \(d\)?",
          r"\(W_f = -f_kd\)"),
        B(r"How much work does gravity do on an object that rises by \(\Delta y\)?",
          r"\(W_g = -mg\,\Delta y\)",
          extra=r"It's negative going up and positive coming down. Only the change in height matters, "
                r"not the path."),
        B(r"A \(10\text{ N}\) force at \(60^\circ\) above horizontal pulls a box \(5\text{ m}\) along the floor. "
          r"How much work does it do?",
          r"\(W = (10)(5)\cos60^\circ = 25\text{ J}\)", tags=["problem"]),
        B(r"How much work does it take to stretch a spring from equilibrium to a stretch of \(x\)?",
          r"\(W = \tfrac12kx^2\), the area of the triangle under \(F = kx\).",
          extra=r"The spring itself does \(-\tfrac12kx^2\) of work during the stretch."),
    ]),

    Section("3.3", "Potential Energy", [
        B(r"What is <b>potential energy</b>?",
          r"Energy stored in the <b>configuration</b> (arrangement) of objects that interact through "
          r"conservative forces."),
        B(r"Does potential energy belong to a single object or to a system?",
          r"To a <b>system</b> of interacting objects.",
          extra=r"The ball–Earth system has gravitational PE. It isn't correct to say the ball alone has it."),
        C(r"Change in gravitational PE near Earth's surface: \(\Delta U_g = {{c1::mg\,\Delta y}}\)",
          tags=["formula"]),
        C(r"Elastic potential energy of a spring: \(U_s = {{c1::\tfrac12kx^2}}\)", tags=["formula"],
          extra=r"\(x\) is measured from the natural length. Stretching and compressing both store energy."),
        C(r"Gravitational PE of two masses (any separation): \(U_G = {{c1::-\dfrac{Gm_1m_2}{r}}}\)",
          tags=["formula"]),
        B(r"Why is \(U_G = -Gm_1m_2/r\) negative?",
          r"Zero is set at \(r = \infty\). You would have to add energy to separate the masses to infinity, "
          r"so a bound pair has <b>less</b> than zero energy."),
        B(r"Does it matter where you choose \(U = 0\)?",
          r"<b>No.</b> Only <b>changes</b> in potential energy are physically meaningful."),
        B(r"What makes a force <b>conservative</b>?",
          r"The work it does is <b>path-independent</b> (zero around any closed loop). That's what allows "
          r"it to have a potential energy."),
        B(r"Name the two conservative forces in AP Physics 1.",
          r"<b>Gravity</b> and the <b>spring force</b>."),
        B(r"Is kinetic friction a conservative force?",
          r"<b>No.</b> The work it does depends on the path length."),
        C(r"Work done by a conservative force: \(W_{cons} = {{c1::-\Delta U}}\)", tags=["formula"]),
    ]),

    Section("3.4", "Conservation of Energy", [
        B(r"How can the total energy of a system change?",
          r"Only through energy transfers across its boundary, such as work by external forces: "
          r"\(\Delta E_{sys} = W_{ext}\).",
          extra=r"If no external work is done, the total energy stays constant."),
        C(r"If only conservative forces do work, mechanical energy is conserved: "
          r"\(K_i + U_i = {{c1::K_f + U_f}}\)", tags=["formula"]),
        B(r"A ball is dropped from rest (system: ball + Earth). How do the energy bar charts compare just "
          r"after release and just before landing?",
          r"All \(U_g\) at the start, all \(K\) at the end. The <b>total</b> stays the same, because no "
          r"external work is done.",
          bd="energy_bar_chart"),
        B(r"A ball is released from rest at A on this frictionless track. Where is it moving fastest?",
          r"At <b>B</b>, the lowest point, where the most \(U_g\) has turned into \(K\).",
          fd="energy_track"),
        B(r"A ball is released from rest at A on this frictionless track. Does it make it over the hill at C?",
          r"<b>Yes.</b> C is lower than A, so the ball still has some \(K\) there.",
          fd="energy_track",
          extra=r"Without friction, the ball can reach any point lower than its release height, but never "
                r"higher."),
        B(r"An object falls from rest through a height \(h\) with no friction or air resistance. How fast is "
          r"it going?",
          r"\[v = \sqrt{2gh}\]",
          extra=r"From \(mgh = \tfrac12mv^2\)."),
        B(r"Two objects of different mass slide from rest down frictionless ramps of different shapes but "
          r"the same height. Which one is faster at the bottom?",
          r"<b>Neither</b>. Both arrive at \(\sqrt{2gh}\). Mass and path don't matter."),
        B(r"When kinetic friction acts, what happens to the mechanical energy that is lost?",
          r"It becomes <b>thermal (internal) energy</b> of the surfaces."),
        C(r"Thermal energy produced when an object slides distance \(d\) against kinetic friction: "
          r"\(\Delta E_{th} = {{c1::f_kd}}\)", tags=["formula"]),
        B(r"A spring (constant \(k\)) is compressed by \(x\) and launches a block of mass \(m\) on a "
          r"frictionless surface. What is the launch speed?",
          r"\(\tfrac12kx^2 = \tfrac12mv^2 \Rightarrow v = x\sqrt{k/m}\)"),
        B(r"How does your choice of system change the way you account for gravity in an energy problem?",
          r"<b>Earth in the system:</b> gravity is internal, so track \(U_g\).<br>"
          r"<b>Earth outside the system:</b> gravity does external work, and there is no \(U_g\).",
          extra=r"Both give the same answer. Don't count gravity twice."),
        B(r"A \(2\text{ kg}\) ball is dropped from \(5\text{ m}\). How fast is it moving just before landing? "
          r"\((g = 10\text{ m/s}^2)\)",
          r"\(v = \sqrt{2(10)(5)} = 10\text{ m/s}\)", tags=["problem"]),
    ]),

    Section("3.5", "Power", [
        C(r"Average power: \(P = {{c1::\dfrac{\Delta E}{\Delta t}}}\)", tags=["formula"]),
        B(r"What is the SI unit of power?",
          r"The watt: \(1\text{ W} = 1\text{ J/s}\)"),
        C(r"Instantaneous power delivered by a force: \(P = {{c1::Fv\cos\theta}}\)", tags=["formula"],
          extra=r"Equivalently \(P = F_\parallel v\)."),
        B(r"Two people of equal mass climb the same stairs, one twice as fast. Who does more work?",
          r"<b>Neither</b>. Both do \(mg\,\Delta h\)."),
        B(r"Two people of equal mass climb the same stairs, one twice as fast. How do their average powers compare?",
          r"The faster climber delivers <b>twice</b> the power."),
        B(r"A \(60\text{ kg}\) person climbs \(5\text{ m}\) of stairs in \(10\text{ s}\). What is their average "
          r"power? \((g = 10\text{ m/s}^2)\)",
          r"\(P = \dfrac{mgh}{t} = 300\text{ W}\)", tags=["problem"]),
        B(r"A car moves at a constant \(20\text{ m/s}\) against \(500\text{ N}\) of drag. What power must the "
          r"engine deliver?",
          r"\(P = Fv = 10{,}000\text{ W} = 10\text{ kW}\)", tags=["problem"]),
        B(r"Is the kilowatt-hour (kWh) a unit of power or of energy?",
          r"<b>Energy</b>: \(1\text{ kWh} = 3.6\times10^6\text{ J}\)."),
    ]),
])
