from cards import B, C, Section, Unit

UNIT = Unit(6, "Energy and Momentum of Rotating Systems", [
    Section("6.1", "Rotational Kinetic Energy", [
        C(r"Rotational kinetic energy: \(K_{rot} = {{c1::\tfrac12I\omega^2}}\)", tags=["formula"]),
        B(r"Can an object whose center of mass is at rest have kinetic energy?",
          r"<b>Yes</b>, if it is spinning: \(K = \tfrac12I\omega^2\)."),
        C(r"Total kinetic energy of an object that translates and rotates: "
          r"\(K = {{c1::\tfrac12Mv_{cm}^2}} + {{c2::\tfrac12I_{cm}\omega^2}}\)", tags=["formula"]),
        B(r"A disk with \(I = 2\text{ kg·m}^2\) spins at \(3\text{ rad/s}\). What is its rotational kinetic energy?",
          r"\(K = \tfrac12(2)(3)^2 = 9\text{ J}\)", tags=["problem"]),
        B(r"Where does the formula \(\tfrac12I\omega^2\) come from?",
          r"It's \(\tfrac12mv^2\) summed over every particle, using \(v = r\omega\): "
          r"\(\sum\tfrac12m(r\omega)^2 = \tfrac12\left(\sum mr^2\right)\omega^2\)."),
    ]),

    Section("6.2", "Torque and Work", [
        C(r"Work done by a constant torque: \(W = {{c1::\tau\,\Delta\theta}}\)", tags=["formula"],
          extra=r"\(\Delta\theta\) must be in radians."),
        C(r"Rotational work–energy theorem: \(W_{net} = {{c1::\Delta\left(\tfrac12I\omega^2\right)}}\)",
          tags=["formula"]),
        B(r"How do you find work from a graph of torque vs. angular position?",
          r"Find the <b>area under the \(\tau\)–\(\theta\) graph</b>."),
        B(r"A motor applies a constant \(5\text{ N·m}\) torque through \(10\text{ rad}\). How much work does it do?",
          r"\(W = 5(10) = 50\text{ J}\)", tags=["problem"]),
        C(r"Power delivered by a torque: \(P = {{c1::\tau\omega}}\)", tags=["formula"],
          extra=r"This is the rotational version of \(P = Fv\)."),
    ]),

    Section("6.3", "Angular Momentum and Angular Impulse", [
        C(r"Angular momentum of a rigid body: \(L = {{c1::I\omega}}\)", tags=["formula"]),
        B(r"What is the SI unit of angular momentum?",
          r"kg·m²/s"),
        C(r"Angular momentum of a point particle about a point: \(L = {{c1::mvr\sin\theta}}\)",
          d="angular_momentum_particle", tags=["formula"],
          extra=r"Equivalently \(L = mvr_\perp\), where \(r_\perp\) is the perpendicular distance from the "
                r"point to the particle's line of motion."),
        B(r"Does a particle moving in a straight line have angular momentum?",
          r"<b>Yes</b>, about any point that isn't on its line of motion.",
          bd="angular_momentum_particle",
          extra=r"If the particle moves at constant velocity, its angular momentum stays constant."),
        C(r"Angular impulse: \(\tau\,\Delta t = {{c1::\Delta L}}\)", tags=["formula"],
          extra=r"This is the rotational version of \(F\Delta t = \Delta p\)."),
        B(r"On a graph of torque vs. time, what does the area under the curve represent?",
          r"The <b>change in angular momentum</b> (angular impulse)."),
        B(r"A wheel starts at rest. A \(2\text{ N·m}\) torque acts on it for \(3\text{ s}\). What is its "
          r"angular momentum afterward?",
          r"\(L = \tau\Delta t = 6\text{ kg·m}^2/\text{s}\)", tags=["problem"]),
        B(r"A wheel with \(I = 0.5\text{ kg·m}^2\) has \(L = 6\text{ kg·m}^2/\text{s}\). What is its angular velocity?",
          r"\(\omega = L/I = 12\text{ rad/s}\)", tags=["problem"]),
    ]),

    Section("6.4", "Conservation of Angular Momentum", [
        B(r"When is a system's angular momentum conserved?",
          r"When the <b>net external torque</b> on the system is zero."),
        B(r"A spinning skater pulls their arms in. What happens to the angular velocity?",
          r"It <b>increases</b>: \(I\) drops while \(L = I\omega\) stays constant.", bd="spinning_skater"),
        B(r"A spinning skater pulls their arms in. What happens to the rotational kinetic energy?",
          r"It <b>increases</b>. The extra energy comes from the work the skater's muscles do pulling the "
          r"arms inward.",
          extra=r"\(K = L^2/2I\), and \(L\) is constant while \(I\) decreases."),
        B(r"A skater spinning at \(2\text{ rad/s}\) with \(I = 4\text{ kg·m}^2\) pulls in to \(I = 1\text{ kg·m}^2\). "
          r"What is the new angular velocity?",
          r"\(4(2) = 1\cdot\omega \Rightarrow \omega = 8\text{ rad/s}\)", tags=["problem"]),
        B(r"A lump of clay drops straight down onto a spinning turntable and sticks. What happens to the "
          r"turntable's angular velocity?",
          r"It <b>decreases</b>: \(I_1\omega_1 = (I_1 + mr^2)\omega_2\)."),
        B(r"A lump of clay drops onto a spinning turntable and sticks. Is kinetic energy conserved?",
          r"<b>No.</b> This is an inelastic collision, so some kinetic energy is lost."),
        B(r"Why does a diver tuck to do somersaults?",
          r"Tucking lowers \(I\). Angular momentum is conserved in the air, so \(\omega\) increases."),
        B(r"A ball hits a rod pinned at one end and sticks to it. Is the system's <b>linear</b> momentum conserved?",
          r"<b>No.</b> The pivot exerts an external force during the collision."),
        B(r"A ball hits a rod pinned at one end and sticks to it. Is angular momentum about the pivot conserved?",
          r"<b>Yes.</b> The pivot's force acts at the axis, so it exerts no torque about it."),
    ]),

    Section("6.5", "Rolling", [
        C(r"Rolling without slipping: \(v_{cm} = {{c1::R\omega}}\)", tags=["formula"]),
        B(r"For a wheel rolling without slipping, how fast is the point <b>touching the ground</b> moving?",
          r"<b>Zero</b>: it is momentarily at rest.", bd="rolling"),
        B(r"For a wheel rolling without slipping, how fast is the <b>top</b> of the wheel moving?",
          r"\(2v_{cm}\)", bd="rolling"),
        B(r"A hoop, a solid disk, and a solid sphere roll from rest down the same incline without slipping. "
          r"In what order do they reach the bottom?",
          r"<b>Sphere, then disk, then hoop.</b>",
          extra=r"The smaller \(I/MR^2\), the less energy goes into rotation, so the faster the object "
                r"translates. Mass and radius don't matter."),
        B(r"An object rolls from rest down a height \(h\) without slipping. What is its speed at the bottom?",
          r"\[v = \sqrt{\frac{2gh}{1 + I/MR^2}}\]",
          extra=r"From \(Mgh = \tfrac12Mv^2 + \tfrac12I\omega^2\) with \(\omega = v/R\)."),
        B(r"Does static friction do work on an object rolling without slipping?",
          r"<b>No.</b> The contact point doesn't move.",
          extra=r"Static friction does supply the torque that makes the object spin."),
        B(r"A block slides down a frictionless incline. A ball rolls without slipping down an identical "
          r"incline. Which reaches the bottom first?",
          r"The <b>block</b>. All of its energy goes into translation, while the ball puts some into rotation."),
        B(r"What fraction of a rolling solid sphere's kinetic energy is rotational? \((I = \tfrac25MR^2)\)",
          r"\(\dfrac{\tfrac15Mv^2}{\tfrac12Mv^2 + \tfrac15Mv^2} = \dfrac27\)", tags=["problem"]),
        B(r"When a ball rolls <b>with</b> slipping (e.g. a skidding bowling ball), what kind of friction acts, "
          r"and what does it do to mechanical energy?",
          r"<b>Kinetic</b> friction. It turns mechanical energy into thermal energy until the ball rolls "
          r"without slipping."),
    ]),

    Section("6.6", "Motion of Orbiting Satellites", [
        B(r"What is the speed of a satellite in a circular orbit of radius \(r\) around a mass \(M\)?",
          r"\[v = \sqrt{\frac{GM}{r}}\]",
          bd="orbits",
          extra=r"From \(\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}\)."),
        B(r"Does a satellite's circular orbital speed depend on the satellite's mass?",
          r"<b>No</b>. The mass cancels."),
        C(r"Kepler's third law (circular orbit): \(T^2 = {{c1::\dfrac{4\pi^2}{GM}r^3}}\)", tags=["formula"]),
        B(r"In an elliptical orbit, where does the satellite move fastest?",
          r"At the point <b>closest</b> to the central body.", bd="orbits",
          extra=r"Angular momentum is conserved: \(r_pv_p = r_av_a\)."),
        B(r"Why is a satellite's angular momentum about the planet conserved?",
          r"Gravity points toward the planet's center (a central force), so it exerts <b>no torque</b> "
          r"about that point."),
        B(r"Is a satellite's <b>linear</b> momentum conserved in orbit?",
          r"<b>No.</b> Its velocity keeps changing direction, because gravity is an unbalanced external force on it."),
        C(r"Total mechanical energy of a satellite–planet system in a circular orbit: "
          r"\(E = {{c1::-\dfrac{GMm}{2r}}}\)", tags=["formula"],
          extra=r"\(K = \tfrac12\dfrac{GMm}{r}\) plus \(U_G = -\dfrac{GMm}{r}\). A negative total means the "
                r"satellite is bound."),
        C(r"Escape speed from the surface of a planet of mass \(M\), radius \(R\): \(v_{esc} = "
          r"{{c1::\sqrt{\dfrac{2GM}{R}}}}\)", tags=["formula"],
          extra=r"From \(\tfrac12mv^2 - \dfrac{GMm}{R} = 0\)."),
        B(r"A satellite moves to a higher circular orbit. What happens to its <b>speed</b>?",
          r"It <b>decreases</b> (\(v = \sqrt{GM/r}\))."),
        B(r"A satellite moves to a higher circular orbit. What happens to its <b>period</b>?",
          r"It <b>increases</b> (\(T \propto r^{3/2}\))."),
        B(r"A satellite moves to a higher circular orbit. What happens to the system's total mechanical energy?",
          r"It <b>increases</b> (becomes less negative)."),
    ]),
])
