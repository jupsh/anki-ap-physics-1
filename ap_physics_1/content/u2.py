from cards import B, C, Section, Unit

UNIT = Unit(2, "Force and Translational Dynamics", [
    Section("2.1", "Systems and Center of Mass", [
        B(r"What is a <b>system</b> in physics?",
          r"Whatever object or group of objects you choose to analyze."),
        B(r"What is the difference between <b>internal</b> and <b>external</b> forces on a system?",
          r"<b>Internal</b> forces act between parts of the system. <b>External</b> forces come from "
          r"outside it.",
          extra=r"Moving the system boundary can turn an external force into an internal one. For two "
                r"blocks pushed together, their contact force is internal if the system is both blocks."),
        B(r"When can a system be modeled as a single object?",
          r"When its internal structure doesn't matter for the question. It can then be treated as a "
          r"point particle at its <b>center of mass</b>."),
        C(r"Center of mass of particles in one dimension: \(x_{cm} = {{c1::\dfrac{\sum m_i x_i}{\sum m_i}}}\)",
          d="center_of_mass", tags=["formula"],
          extra=r"The center of mass is always closer to the heavier mass."),
        B(r"A \(2\text{ kg}\) mass is at \(x = 0\) and a \(6\text{ kg}\) mass is at \(x = 4\text{ m}\). Where is the "
          r"center of mass?",
          r"\(x_{cm} = \dfrac{2(0) + 6(4)}{8} = 3\text{ m}\)", tags=["problem"]),
        B(r"Where is the center of mass of a uniform, symmetric object?",
          r"At its <b>geometric center</b>."),
        B(r"Does the center of mass have to be located on the material of the object?",
          r"<b>No.</b> The center of mass of a ring, for example, is in the empty middle."),
        B(r"Can <b>internal</b> forces change the velocity of a system's center of mass?",
          r"<b>No.</b> Only a net <b>external</b> force can: \(\Sigma\vec F_{ext} = m_{sys}\vec a_{cm}\).",
          extra=r"When a shell explodes mid-air, the center of mass of the fragments keeps following the "
                r"original parabola."),
    ]),

    Section("2.2", "Forces and Free-Body Diagrams", [
        B(r"What is a <b>force</b>?",
          r"A push or pull resulting from an <b>interaction between two objects</b>. It is a vector, "
          r"measured in newtons (N)."),
        C(r"\(1\text{ N} = 1\ {{c1::\text{kg}\cdot\text{m/s}^2}}\)"),
        B(r"Which forces belong on an object's free-body diagram?",
          r"Only the forces exerted <b>on that object</b> by other objects. Each one is drawn as an "
          r"arrow starting at the object and pointing the way the force acts."),
        B(r"Should the net force (or \(m\vec a\)) be drawn as its own arrow on a free-body diagram?",
          r"<b>No.</b> The net force is the vector sum of the forces already drawn."),
        B(r"A block is pushed to the right across a rough floor. What forces act on it, and in which "
          r"directions?",
          r"Gravity \(F_g\) down, normal force \(F_N\) up, applied force to the right, kinetic friction "
          r"\(f_k\) to the left (opposing the sliding).",
          bd="fbd_table"),
        B(r"A block rests on a rough incline. What three forces act on it?",
          r"<b>Gravity</b> (straight down), the <b>normal force</b> (perpendicular to the surface), and "
          r"<b>static friction</b> (up the slope, along the surface).",
          bd="fbd_incline"),
        C(r"On an incline at angle \(\theta\), the component of gravity <b>parallel</b> to the surface is "
          r"\({{c1::mg\sin\theta}}\) and the component <b>perpendicular</b> to it is \({{c2::mg\cos\theta}}\)",
          d="fbd_incline", tags=["formula"],
          extra=r"If nothing else pushes perpendicular to the surface, \(F_N = mg\cos\theta\)."),
        B(r"What is the acceleration of a block sliding down a <b>frictionless</b> incline at angle \(\theta\)?",
          r"\(a = g\sin\theta\), down the slope."),
        B(r"Why do we usually tilt the axes in incline problems?",
          r"So one axis points along the acceleration (along the slope). Then the acceleration has only "
          r"one nonzero component."),
        B(r"In AP Physics 1, which force acts <b>at a distance</b> rather than by contact?",
          r"<b>Gravity</b>. The others (normal, friction, tension, spring, buoyant) are contact forces."),
        B(r"Which direction does the <b>normal force</b> point?",
          r"<b>Perpendicular</b> to the contact surface, pushing away from it."),
        B(r"Is the normal force on an object always equal to \(mg\)?",
          r"<b>No.</b> It's whatever size keeps the object from going into the surface.",
          extra=r"\(F_N \ne mg\) on inclines, in accelerating elevators, or when another force pushes up or down."),
        B(r"How does the tension vary along an <b>ideal</b> (massless) rope?",
          r"It is the <b>same everywhere</b> along the rope."),
        B(r"What does an <b>ideal</b> (massless, frictionless) pulley do to the tension in a rope?",
          r"Nothing to its magnitude. It only <b>changes the rope's direction</b>."),
    ]),

    Section("2.3", "Newton's Third Law", [
        B(r"State <b>Newton's third law</b>.",
          r"If object A exerts a force on object B, then B exerts a force on A that is <b>equal in "
          r"magnitude</b> and <b>opposite in direction</b>: \(\vec F_{A\text{ on }B} = -\vec F_{B\text{ on }A}\).",
          bd="third_law"),
        B(r"Why don't the two forces of a Newton's third-law pair cancel?",
          r"They act on <b>different objects</b>. Forces only cancel when they act on the same object."),
        B(r"A book rests on a table. Are its weight and the normal force on it a third-law pair?",
          r"<b>No.</b> Both act on the book. Third-law partners always act on different objects."),
        B(r"A book rests on a table. What is the third-law partner of <b>Earth's gravitational pull on the book</b>?",
          r"The book's gravitational pull <b>on Earth</b>."),
        B(r"A book rests on a table. What is the third-law partner of <b>the table's normal force on the book</b>?",
          r"The book's downward push <b>on the table</b>."),
        B(r"A truck collides with a small car. Which one experiences the larger force?",
          r"<b>Neither.</b> The forces are equal in magnitude (third law)."),
        B(r"A truck collides with a small car. Which one has the larger acceleration?",
          r"The <b>car</b>. The forces are equal, and the car has less mass (\(a = F/m\))."),
        B(r"The cart pulls back on the horse as hard as the horse pulls forward on the cart. How can the "
          r"horse speed up?",
          r"Its motion depends only on forces <b>on the horse</b>. The ground pushes the horse forward "
          r"(friction) harder than the cart pulls it back."),
    ]),

    Section("2.4", "Newton's First Law", [
        B(r"State <b>Newton's first law</b>.",
          r"An object stays at rest, or keeps moving at constant velocity, unless a nonzero <b>net "
          r"external force</b> acts on it."),
        B(r"What is <b>inertia</b>?",
          r"An object's resistance to changes in its velocity."),
        B(r"What quantity measures an object's inertia?",
          r"Its <b>mass</b>."),
        B(r"What does <b>translational equilibrium</b> mean?",
          r"\(\Sigma\vec F = 0\), so \(\vec a = 0\). The object is at rest <b>or</b> moving at constant velocity."),
        B(r"Does a moving object need a net force to keep it moving?",
          r"<b>No.</b> A net force <i>changes</i> velocity. Constant velocity requires zero net force."),
        B(r"What is an <b>inertial reference frame</b>?",
          r"A frame that isn't accelerating, in which Newton's first law holds."),
        B(r"When a car brakes hard, passengers lurch forward. What force pushes them forward?",
          r"<b>None.</b> Their bodies keep moving at the original velocity while the car slows. The seatbelt "
          r"supplies the backward force that stops them."),
    ]),

    Section("2.5", "Newton's Second Law", [
        C(r"Newton's second law: \(\vec a_{sys} = {{c1::\dfrac{\Sigma\vec F}{m_{sys}}}}\)", tags=["formula"],
          extra=r"Apply it separately to each axis: \(\Sigma F_x = ma_x,\ \Sigma F_y = ma_y\)."),
        B(r"Which direction does an object's acceleration point?",
          r"In the direction of the <b>net force</b>. That may differ from the direction of the velocity."),
        B(r"An elevator <b>accelerates upward</b> at \(a\). What does a scale under a passenger of mass \(m\) read?",
          r"\(F_N = m(g + a)\), more than \(mg\). The passenger feels heavier.",
          bd="elevator",
          extra=r"A scale reads the normal force it exerts, not the gravitational force."),
        B(r"An elevator <b>accelerates downward</b> at \(a\) (with \(a \lt g\)). What does a scale under a "
          r"passenger of mass \(m\) read?",
          r"\(F_N = m(g - a)\), less than \(mg\)."),
        B(r"An elevator moves upward at <b>constant velocity</b>. What does a scale under a passenger of "
          r"mass \(m\) read?",
          r"\(F_N = mg\). Only acceleration changes the reading."),
        B(r"What does a scale read for a passenger in an elevator in <b>free fall</b>?",
          r"<b>Zero</b>. The passenger is apparently weightless."),
        C(r"Atwood machine (ideal pulley, \(m_1 > m_2\)): \(a = {{c1::\dfrac{(m_1 - m_2)g}{m_1 + m_2}}}\)",
          d="atwood", tags=["formula"],
          extra=r"Treat both masses as one system: the net external force is \((m_1 - m_2)g\) and the "
                r"total mass is \(m_1 + m_2\)."),
        B(r"Atwood machine with \(m_1 > m_2\): is the rope's tension greater than, less than, or equal to "
          r"\(m_2 g\)?",
          r"<b>Greater</b>. \(m_2\) accelerates upward, so \(T - m_2g = m_2a > 0\).",
          bd="atwood",
          extra=r"By the same reasoning, \(T \lt m_1g\). Exact value: \(T = \dfrac{2m_1m_2g}{m_1 + m_2}\)."),
        B(r"A force \(F\) pushes block \(m_1\), which pushes block \(m_2\), on a frictionless floor. What is "
          r"their acceleration?",
          r"\(a = \dfrac{F}{m_1 + m_2}\)",
          extra=r"Use the whole system to find \(a\) first."),
        B(r"A force \(F\) pushes block \(m_1\), which pushes block \(m_2\), on a frictionless floor. What "
          r"force does \(m_1\) exert on \(m_2\)?",
          r"\(F_{1\text{ on }2} = m_2a = \dfrac{m_2}{m_1 + m_2}F\)",
          extra=r"Find \(a\) from the whole system, then isolate \(m_2\): the only horizontal force on it "
                r"is the push from \(m_1\)."),
        B(r"A \(2\text{ kg}\) object has a net force of \(10\text{ N}\) on it. What is its acceleration?",
          r"\(5\text{ m/s}^2\), in the direction of the net force.", tags=["problem"]),
        B(r"You push a crate with \(20\text{ N}\) and it slides at <b>constant velocity</b>. How big is the "
          r"friction force?",
          r"\(20\text{ N}\). Constant velocity means \(\Sigma F = 0\).", tags=["problem"]),
    ]),

    Section("2.6", "Gravitational Force", [
        C(r"Newton's law of universal gravitation: \(F_g = {{c1::G\dfrac{m_1m_2}{r^2}}}\)",
          d="gravity_two_masses", tags=["formula"],
          extra=r"\(G = 6.67\times10^{-11}\ \text{N·m}^2/\text{kg}^2\)."),
        B(r"In \(F_g = Gm_1m_2/r^2\), what distance is \(r\)?",
          r"The distance between the objects' <b>centers</b>.", bd="gravity_two_masses"),
        B(r"If the distance between two masses <b>doubles</b>, what happens to the gravitational force?",
          r"It becomes \(\tfrac14\) as large (inverse square)."),
        B(r"If one of two masses <b>doubles</b>, what happens to the gravitational force between them?",
          r"It <b>doubles</b>."),
        C(r"Gravitational field strength at distance \(r\) from mass \(M\): \(g = {{c1::\dfrac{GM}{r^2}}}\)",
          tags=["formula"],
          extra=r"Units: N/kg, which equals m/s². Near Earth's surface, \(g \approx 9.8\text{ N/kg}\)."),
        B(r"A planet has twice Earth's mass and twice its radius. What is \(g\) at its surface?",
          r"\(g \propto M/R^2\), so \(g = \dfrac{2}{2^2}g_E = \tfrac12g_E\)", tags=["problem"]),
        B(r"What is the difference between <b>mass</b> and <b>weight</b>?",
          r"<b>Mass</b> (kg) measures inertia and is the same everywhere. <b>Weight</b> is the "
          r"gravitational force on an object, \(F_g = mg\) (N), and depends on location."),
        B(r"Astronauts on the ISS feel weightless. Is gravity zero there?",
          r"<b>No</b>, it's about 90% of its surface value. The astronauts and the station are both in "
          r"<b>free fall</b>, so the astronauts' apparent weight (normal force) is zero."),
        B(r"Why do all objects fall with the same acceleration (no air resistance)?",
          r"Gravitational mass equals inertial mass. \(F_g = mg\) and \(a = F/m\), so \(m\) cancels and \(a = g\)."),
    ]),

    Section("2.7", "Kinetic and Static Friction", [
        C(r"Kinetic friction: \(f_k = {{c1::\mu_k F_N}}\)", tags=["formula"]),
        C(r"Static friction: \(f_s {{c1::\le \mu_s F_N}}\)", tags=["formula"],
          extra=r"Static friction only gets as large as it needs to be to prevent sliding, up to \(\mu_sF_N\)."),
        B(r"A box sits at rest. You push it with a slowly increasing horizontal force. How does the static "
          r"friction force change before the box moves?",
          r"It <b>matches your push</b> exactly, up to its maximum \(\mu_sF_N\).",
          bd="friction_graph"),
        B(r"Once a pushed box starts sliding, how does the friction force compare to the maximum static "
          r"friction just before?",
          r"It <b>drops</b> to the constant value \(f_k = \mu_kF_N\), which is less than \(\mu_sF_N\).",
          bd="friction_graph"),
        B(r"Which is usually larger: \(\mu_s\) or \(\mu_k\)?",
          r"\(\mu_s\)",
          extra=r"That's why it's harder to get an object sliding than to keep it sliding."),
        B(r"Which direction does friction point?",
          r"Opposite to the <b>relative motion (or attempted relative motion)</b> between the surfaces.",
          extra=r"That isn't always opposite to the object's motion. When you walk, static friction on "
                r"your shoe points <b>forward</b>."),
        B(r"In the AP model, does kinetic friction depend on contact area or sliding speed?",
          r"<b>Neither.</b> It depends only on \(\mu_k\) and the normal force."),
        B(r"A block on an incline is just about to slip. How is \(\mu_s\) related to the angle \(\theta\)?",
          r"\(\mu_s = \tan\theta\)",
          extra=r"Set \(mg\sin\theta = \mu_smg\cos\theta\)."),
        B(r"A \(10\text{ kg}\) box slides across a level floor with \(\mu_k = 0.3\). How big is the friction "
          r"force? \((g = 10\text{ m/s}^2)\)",
          r"\(f_k = \mu_kmg = 30\text{ N}\)", tags=["problem"]),
        B(r"A box rests on a level floor with nothing pushing it sideways. How much static friction acts on it?",
          r"<b>Zero.</b> Nothing is trying to make it slide."),
    ]),

    Section("2.8", "Spring Forces", [
        C(r"Hooke's law: \(\vec F_s = {{c1::-k\Delta\vec x}}\)", tags=["formula"]),
        B(r"In Hooke's law \(\vec F_s = -k\Delta\vec x\), what does the minus sign mean?",
          r"The force is <b>restoring</b>: it points opposite the displacement, back toward equilibrium."),
        B(r"On a graph of spring force <b>magnitude</b> \(|F_s|\) vs. stretch \(x\), what does the slope represent?",
          r"The spring constant \(k\).", bd="spring_force_graph",
          extra=r"On a graph of the <i>signed</i> force \(F_s\) vs. displacement, the slope is \(-k\)."),
        B(r"On a graph of spring force magnitude \(|F_s|\) vs. stretch \(x\), what does the area under the line represent?",
          r"The elastic potential energy stored, \(\tfrac12kx^2\).", bd="spring_force_graph"),
        B(r"What are the SI units of the spring constant \(k\)?",
          r"N/m"),
        B(r"What does a large spring constant \(k\) tell you about a spring?",
          r"It is <b>stiff</b>: it takes more force to stretch it a given distance."),
        B(r"A \(2\text{ kg}\) mass hangs at rest from a spring with \(k = 200\text{ N/m}\). How far is the "
          r"spring stretched? \((g = 10\text{ m/s}^2)\)",
          r"\(kx = mg \Rightarrow x = 0.1\text{ m}\)", tags=["problem"]),
        C(r"Springs in <b>parallel</b>: \(k_{eq} = {{c1::k_1 + k_2}}\)", tags=["formula"],
          extra=r"Parallel springs are stiffer. Two identical springs give \(2k\)."),
        C(r"Springs in <b>series</b>: \(\dfrac{1}{k_{eq}} = {{c1::\dfrac{1}{k_1} + \dfrac{1}{k_2}}}\)",
          tags=["formula"],
          extra=r"Series springs are softer. Two identical springs give \(k/2\)."),
    ]),

    Section("2.9", "Circular Motion", [
        B(r"In uniform circular motion, which way does the <b>velocity</b> point?",
          r"<b>Tangent</b> to the circle.", bd="circular_motion"),
        B(r"In uniform circular motion, which way do the <b>acceleration</b> and the <b>net force</b> point?",
          r"Toward the <b>center</b> of the circle.", bd="circular_motion",
          extra=r"The speed is constant, but the direction keeps changing, so the object is accelerating."),
        C(r"Centripetal acceleration: \(a_c = {{c1::\dfrac{v^2}{r}}}\)", tags=["formula"]),
        C(r"Speed in uniform circular motion with period \(T\): \(v = {{c1::\dfrac{2\pi r}{T}}}\)",
          tags=["formula"]),
        B(r"Should “centripetal force” be drawn as its own arrow on a free-body diagram?",
          r"<b>No.</b> It is the <b>net inward force</b> from real forces such as tension, gravity, friction, "
          r"or the normal force."),
        B(r"A car rounds a flat, unbanked curve. Which force provides the centripetal force?",
          r"<b>Static friction</b> between the tires and the road."),
        B(r"What is the maximum speed for a car on a flat curve of radius \(r\) with coefficient \(\mu_s\)?",
          r"\(\mu_smg = \dfrac{mv^2}{r} \Rightarrow v_{max} = \sqrt{\mu_sgr}\)"),
        B(r"A cart rides on the inside of a vertical loop. Write \(\Sigma F = ma_c\) at the <b>top</b>.",
          r"\(mg + F_N = \dfrac{mv^2}{r}\) (both forces point down, toward the center)",
          bd="vertical_circle"),
        B(r"A cart rides on the inside of a vertical loop. Write \(\Sigma F = ma_c\) at the <b>bottom</b>.",
          r"\(F_N - mg = \dfrac{mv^2}{r}\) (the center is upward)",
          bd="vertical_circle"),
        B(r"What is the minimum speed at the top of a vertical loop of radius \(r\)?",
          r"\(v_{min} = \sqrt{gr}\), when \(F_N \to 0\) and gravity alone provides the centripetal force."),
        B(r"A ball whirled on a string is released. Which way does it go?",
          r"In a straight line <b>tangent</b> to the circle at the release point, not outward along the radius."),
        B(r"In a turning car you feel pushed toward the outside. Is there an outward force on you?",
          r"<b>No</b> (in an inertial frame). Your body tends to keep moving straight. The door pushes you "
          r"<b>inward</b> to make you turn."),
        B(r"On a frictionless banked curve, which force provides the centripetal force?",
          r"The <b>horizontal component of the normal force</b>."),
        C(r"Design speed for a frictionless banked curve at angle \(\theta\): \(\tan\theta = {{c1::\dfrac{v^2}{rg}}}\)",
          tags=["formula"]),
        B(r"In <b>non-uniform</b> circular motion (speed changing), what are the two components of acceleration?",
          r"<b>Centripetal</b>, \(v^2/r\) toward the center (changes direction), and <b>tangential</b>, "
          r"along the path (changes speed)."),
    ]),
])
