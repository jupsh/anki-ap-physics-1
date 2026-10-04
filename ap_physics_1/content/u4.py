from cards import B, C, Section, Unit

UNIT = Unit(4, "Linear Momentum", [
    Section("4.1", "Linear Momentum", [
        C(r"Linear momentum: \(\vec p = {{c1::m\vec v}}\)", tags=["formula"]),
        B(r"What is the SI unit of momentum?",
          r"kg·m/s"),
        B(r"Momentum vs. kinetic energy: which is a vector and which is a scalar?",
          r"Momentum is a <b>vector</b>. Kinetic energy is a <b>scalar</b>.",
          extra=r"So momenta in opposite directions can add to zero, but kinetic energies never cancel."),
        C(r"Kinetic energy in terms of momentum: \(K = {{c1::\dfrac{p^2}{2m}}}\)", tags=["formula"]),
        B(r"Which has more momentum: a \(1000\text{ kg}\) car at \(1\text{ m/s}\) or a \(10\text{ kg}\) object at "
          r"\(50\text{ m/s}\)?",
          r"The <b>car</b>: \(1000\text{ kg·m/s}\) vs. \(500\text{ kg·m/s}\).", tags=["problem"],
          extra=r"The small object has far more kinetic energy, though: \(12{,}500\text{ J}\) vs. the car's "
                r"\(500\text{ J}\)."),
        B(r"How do you find the total momentum of a system?",
          r"Add the momenta of its parts <b>as vectors</b>: \(\vec p_{sys} = \sum m_i\vec v_i\).",
          extra=r"Also equal to \(m_{total}\vec v_{cm}\)."),
        C(r"Newton's second law in momentum form: \(\Sigma\vec F = {{c1::\dfrac{\Delta\vec p}{\Delta t}}}\)",
          tags=["formula"]),
    ]),

    Section("4.2", "Change in Momentum and Impulse", [
        C(r"Impulse–momentum theorem: \(\vec F_{avg}\,\Delta t = {{c1::\Delta\vec p}}\)", tags=["formula"],
          extra=r"The left side is the impulse \(\vec J\). Units: N·s = kg·m/s."),
        B(r"On a force–time graph, what does the area under the curve represent?",
          r"The <b>impulse</b>, which equals the change in momentum.",
          bd="impulse_graph",
          extra=r"The average force is the height of a rectangle with the same area over the same \(\Delta t\)."),
        B(r"How does an airbag reduce the force on a passenger in a crash?",
          r"It makes the stopping time \(\Delta t\) <b>longer</b> for the same \(\Delta p\), so the average "
          r"force \(\Delta p/\Delta t\) is <b>smaller</b>."),
        B(r"Two identical balls hit a wall at the same speed. One bounces back and one sticks. Which "
          r"receives the larger impulse?",
          r"The one that <b>bounces</b>. Reversing direction is a larger change in momentum.",
          extra=r"Rebounding at the same speed: \(|\Delta p| = 2mv\). Sticking: \(|\Delta p| = mv\)."),
        B(r"A \(0.5\text{ kg}\) ball hits a wall at \(10\text{ m/s}\) and rebounds at \(10\text{ m/s}\). What is "
          r"the magnitude of its change in momentum?",
          r"\(|\Delta p| = 0.5(10 - (-10)) = 10\text{ kg·m/s}\)", tags=["problem"]),
        B(r"A ball's momentum changes by \(10\text{ kg·m/s}\) during a \(0.01\text{ s}\) collision. What is the "
          r"average force on it?",
          r"\(F_{avg} = \Delta p/\Delta t = 1000\text{ N}\)", tags=["problem"]),
        B(r"Which direction does an impulse point?",
          r"Along the average net force, which is also the direction of \(\Delta\vec p\).",
          extra=r"This is not necessarily the direction of the velocity."),
    ]),

    Section("4.3", "Conservation of Linear Momentum", [
        B(r"When is a system's total momentum conserved?",
          r"When the <b>net external force</b> on the system is zero (or negligible during a brief event "
          r"like a collision)."),
        B(r"Use Newton's third law to explain why momentum is conserved in a collision.",
          r"The objects push on each other with equal and opposite forces for the <b>same time</b>, so "
          r"their impulses are equal and opposite. One object's gain in momentum is the other's loss."),
        B(r"An object at rest explodes into two pieces. How do the momenta of the pieces compare?",
          r"<b>Equal in magnitude and opposite in direction</b>. The total stays zero.",
          extra=r"\(m_1v_1 = m_2v_2\), so the lighter piece moves faster."),
        B(r"A \(60\text{ kg}\) skater at rest on frictionless ice throws a \(2\text{ kg}\) ball forward at "
          r"\(15\text{ m/s}\). What is the skater's velocity afterward?",
          r"\(0 = 2(15) + 60v \Rightarrow v = -0.5\text{ m/s}\) (backward)", tags=["problem"]),
        B(r"A ball falls toward Earth. Taking the system to be <b>just the ball</b>, is its momentum conserved?",
          r"<b>No.</b> Gravity is an external force on that system."),
        B(r"A ball falls toward Earth. Taking the system to be <b>ball + Earth</b>, is momentum conserved?",
          r"<b>Yes.</b> Gravity is now internal: Earth gains momentum equal and opposite to the ball's."),
        B(r"In an isolated system, what happens to the velocity of the center of mass during a collision or explosion?",
          r"It stays <b>constant</b>."),
    ]),

    Section("4.4", "Elastic and Inelastic Collisions", [
        B(r"In which kinds of collisions is momentum conserved (for an isolated system)?",
          r"<b>All of them</b>: elastic, inelastic, and perfectly inelastic."),
        B(r"What distinguishes an <b>elastic</b> collision from an <b>inelastic</b> one?",
          r"In an elastic collision, <b>kinetic energy is conserved</b>. In an inelastic one, some kinetic "
          r"energy is converted to other forms."),
        B(r"What is a <b>perfectly inelastic</b> collision?",
          r"One where the objects <b>stick together</b>. It loses the most kinetic energy that momentum "
          r"conservation allows."),
        C(r"Mass \(m_1\) moving at \(v_1\) hits \(m_2\) at rest and they stick together: "
          r"\(v_f = {{c1::\dfrac{m_1v_1}{m_1 + m_2}}}\)", d="collision_inelastic", tags=["formula"]),
        B(r"In a head-on <b>elastic</b> collision between equal masses, one starts at rest. What happens?",
          r"They <b>swap velocities</b>. The moving one stops and the other moves off at the original velocity.",
          bd="collision_elastic"),
        B(r"Where does the lost kinetic energy go in an inelastic collision?",
          r"Into <b>internal energy</b>: thermal energy, sound, and permanent deformation."),
        B(r"A \(2\text{ kg}\) cart at \(3\text{ m/s}\) hits a \(1\text{ kg}\) cart at rest, and they stick. What "
          r"is their final velocity?",
          r"\(v_f = \dfrac{2(3)}{3} = 2\text{ m/s}\)", tags=["problem"]),
        B(r"A \(2\text{ kg}\) cart at \(3\text{ m/s}\) hits a \(1\text{ kg}\) cart at rest. They stick and move at "
          r"\(2\text{ m/s}\). How much kinetic energy is lost?",
          r"\(K_i = 9\text{ J},\ K_f = \tfrac12(3)(2)^2 = 6\text{ J}\), so \(3\text{ J}\) is lost.", tags=["problem"]),
        B(r"In a 1-D elastic collision, how does the relative speed of approach compare with the relative "
          r"speed of separation?",
          r"They are <b>equal</b>: \(v_1 - v_2 = -(v_1' - v_2')\)."),
        B(r"In a head-on elastic collision, a very heavy object hits a light object at rest. What happens?",
          r"The heavy object barely slows. The light one shoots off at about <b>twice</b> the heavy one's speed."),
        B(r"In a head-on elastic collision, a light object hits a very heavy object at rest. What happens?",
          r"The light object <b>bounces back</b> at nearly its original speed. The heavy one barely moves."),
        B(r"How do you apply momentum conservation to a collision in <b>two dimensions</b>?",
          r"Separately for each axis: total \(p_x\) before = after, and total \(p_y\) before = after."),
    ]),
])
