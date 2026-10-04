from cards import B, C, Section, Unit

UNIT = Unit(5, "Torque and Rotational Dynamics", [
    Section("5.1", "Rotational Kinematics", [
        C(r"Arc length and angle (\(\theta\) in radians): \(s = {{c1::r\theta}}\)", d="rot_kinematics",
          tags=["formula"]),
        B(r"What is one <b>radian</b>?",
          r"The angle whose arc length equals the radius."),
        C(r"\(1\text{ revolution} = {{c1::2\pi}}\text{ rad}\)"),
        C(r"Angular velocity: \(\omega = {{c1::\dfrac{\Delta\theta}{\Delta t}}}\), measured in {{c2::rad/s}}",
          tags=["formula"]),
        C(r"Angular acceleration: \(\alpha = {{c1::\dfrac{\Delta\omega}{\Delta t}}}\), measured in {{c2::rad/s²}}",
          tags=["formula"]),
        B(r"Which rotation direction is usually taken as positive?",
          r"<b>Counterclockwise</b>."),
        C(r"Rotational kinematics (constant \(\alpha\)): \(\omega = {{c1::\omega_0 + \alpha t}}\)",
          tags=["formula"]),
        C(r"Rotational kinematics (constant \(\alpha\)): \(\theta = \theta_0 + {{c1::\omega_0t + \tfrac12\alpha t^2}}\)",
          tags=["formula"]),
        C(r"Rotational kinematics (constant \(\alpha\)): \(\omega^2 = {{c1::\omega_0^2 + 2\alpha\,\Delta\theta}}\)",
          tags=["formula"]),
        B(r"For a <b>rigid body</b> rotating about a fixed axis, which quantities are the same for every point?",
          r"\(\theta\), \(\omega\), and \(\alpha\).",
          extra=r"Linear speed and arc length are different for each point because they depend on \(r\)."),
        B(r"A wheel starts from rest with \(\alpha = 2\text{ rad/s}^2\). What is \(\omega\) after \(5\text{ s}\)?",
          r"\(\omega = \alpha t = 10\text{ rad/s}\)", tags=["problem"]),
        B(r"A wheel starts from rest with \(\alpha = 2\text{ rad/s}^2\). Through what angle does it turn in \(5\text{ s}\)?",
          r"\(\Delta\theta = \tfrac12\alpha t^2 = 25\text{ rad}\)", tags=["problem"]),
        B(r"Convert \(60\text{ rpm}\) to rad/s.",
          r"\(60\text{ rev/min} = 1\text{ rev/s} = 2\pi\text{ rad/s}\)", tags=["problem"]),
    ]),

    Section("5.2", "Connecting Linear and Rotational Motion", [
        C(r"Tangential speed of a point at radius \(r\): \(v = {{c1::r\omega}}\)", d="linear_vs_rotational",
          tags=["formula"]),
        C(r"Tangential acceleration of a point at radius \(r\): \(a_t = {{c1::r\alpha}}\)", tags=["formula"]),
        C(r"Centripetal acceleration in terms of angular speed: \(a_c = {{c1::\omega^2r}}\)", tags=["formula"]),
        B(r"Two kids ride a merry-go-round, one near the center and one at the edge. Which has the larger "
          r"angular speed?",
          r"<b>Neither</b>. Every point on a rigid body has the same \(\omega\)."),
        B(r"Two kids ride a merry-go-round, one near the center and one at the edge. Which has the larger "
          r"linear speed?",
          r"The kid at the <b>edge</b>, since \(v = r\omega\).", bd="linear_vs_rotational"),
        B(r"Why must angles be in <b>radians</b> in \(s = r\theta\) and \(v = r\omega\)?",
          r"The radian is defined as arc length ÷ radius. Degrees and revolutions don't have that property."),
        B(r"A rope unwinds without slipping from a spool of radius \(R\) spinning at \(\omega\). How fast does "
          r"the rope move?",
          r"\(v = R\omega\)"),
    ]),

    Section("5.3", "Torque", [
        C(r"Torque: \(\tau = {{c1::rF\sin\theta}}\), where \(\theta\) is the angle between \(\vec r\) and \(\vec F\)",
          tags=["formula"],
          extra=r"\(\vec r\) runs from the rotation axis to the point where the force is applied."),
        C(r"Torque in terms of lever arm: \(\tau = {{c1::r_\perp F}}\)", tags=["formula"]),
        B(r"What is the <b>lever arm</b> (moment arm) of a force?",
          r"The <b>perpendicular distance</b> from the rotation axis to the force's line of action.",
          bd="torque_lever_arm"),
        B(r"Where and how should you push a door to get the most torque?",
          r"At the edge <b>farthest from the hinge</b>, pushing <b>perpendicular</b> to the door."),
        B(r"Name two ways to push on a door that produce <b>zero</b> torque about the hinge.",
          r"Push <b>at the hinge</b>, or push <b>along the door</b> toward or away from the hinge.",
          extra=r"In both cases the lever arm is zero."),
        B(r"What is the SI unit of torque?",
          r"N·m"),
        B(r"Torque and energy can both be written in N·m. Why isn't torque written in joules?",
          r"Torque isn't energy. The joule is reserved for energy and work."),
        B(r"A \(50\text{ N}\) force is applied perpendicular to a wrench, \(0.3\text{ m}\) from the bolt. What "
          r"is the torque?",
          r"\(\tau = 0.3(50) = 15\text{ N·m}\)", tags=["problem"]),
        B(r"A \(50\text{ N}\) force is applied \(0.3\text{ m}\) from a bolt, at \(30^\circ\) to the wrench. What "
          r"is the torque?",
          r"\(\tau = 0.3(50)\sin30^\circ = 7.5\text{ N·m}\)", tags=["problem"]),
        B(r"When calculating the torque from gravity on an extended object, where does the force act?",
          r"At the object's <b>center of mass</b>."),
    ]),

    Section("5.4", "Rotational Inertia", [
        C(r"Rotational inertia of point masses: \(I = {{c1::\sum m_ir_i^2}}\)", tags=["formula"],
          extra=r"\(r_i\) is each mass's perpendicular distance from the axis."),
        B(r"What is the SI unit of rotational inertia?",
          r"kg·m²"),
        B(r"What does rotational inertia measure?",
          r"An object's resistance to <b>angular acceleration</b>."),
        B(r"Besides total mass, what does an object's rotational inertia depend on?",
          r"How the mass is <b>distributed relative to the axis</b>. More mass farther from the axis means "
          r"a larger \(I\)."),
        B(r"Rotational inertia of a thin <b>hoop</b> (ring) about its central axis?",
          r"\(I = MR^2\)", bd="rot_inertia_shapes"),
        B(r"Rotational inertia of a solid <b>disk</b> (cylinder) about its central axis?",
          r"\(I = \tfrac12MR^2\)", bd="rot_inertia_shapes"),
        B(r"Rotational inertia of a solid <b>sphere</b> about an axis through its center?",
          r"\(I = \tfrac25MR^2\)", bd="rot_inertia_shapes"),
        B(r"Rotational inertia of a thin <b>rod</b> about an axis through its <b>center</b>?",
          r"\(I = \tfrac1{12}ML^2\)", bd="rot_inertia_shapes"),
        B(r"Rotational inertia of a thin <b>rod</b> about an axis through one <b>end</b>?",
          r"\(I = \tfrac13ML^2\)", bd="rot_inertia_shapes"),
        B(r"A hoop and a solid disk have the same mass and radius. Which has the larger rotational inertia?",
          r"The <b>hoop</b>. All of its mass is at distance \(R\) from the axis.",
          extra=r"The AP exam gives shape formulas when you need them. Being able to rank them by reasoning "
                r"is what matters."),
        C(r"Parallel-axis theorem: \(I = {{c1::I_{cm} + Md^2}}\)", d="parallel_axis", tags=["formula"],
          extra=r"\(d\) is the distance from the center-of-mass axis to the new, parallel axis."),
        B(r"For a given object, about which axis (among parallel axes) is its rotational inertia smallest?",
          r"The axis through its <b>center of mass</b>."),
        B(r"Two \(1\text{ kg}\) masses sit on a massless rod, each \(0.5\text{ m}\) from the center. What is "
          r"\(I\) about the center?",
          r"\(I = 2(1)(0.5)^2 = 0.5\text{ kg·m}^2\)", tags=["problem"]),
    ]),

    Section("5.5", "Rotational Equilibrium and Newton's First Law in Rotational Form", [
        C(r"An extended object is in static equilibrium when {{c1::\(\Sigma\vec F = 0\)}} and "
          r"{{c2::\(\Sigma\tau = 0\)}}."),
        B(r"State Newton's first law in rotational form.",
          r"An object's angular velocity stays constant unless a nonzero <b>net external torque</b> acts on it."),
        C(r"A seesaw balances when \({{c1::m_1gd_1}} = {{c2::m_2gd_2}}\)", d="seesaw", tags=["formula"],
          extra=r"The heavier mass has to sit closer to the pivot."),
        B(r"In a static equilibrium problem, where is the smartest place to choose the pivot?",
          r"At a point where an <b>unknown force</b> acts. That force's lever arm is zero, so it drops out "
          r"of the torque equation."),
        B(r"A \(30\text{ kg}\) child sits \(2\text{ m}\) from a seesaw's pivot. Where must a \(40\text{ kg}\) child "
          r"sit to balance?",
          r"\(30(2) = 40d \Rightarrow d = 1.5\text{ m}\) on the other side", tags=["problem"]),
        B(r"Can an object have \(\Sigma\vec F = 0\) but \(\Sigma\tau \ne 0\)?",
          r"<b>Yes</b>, with a <b>couple</b>: two equal and opposite forces that don't act along the same line.",
          extra=r"Turning a steering wheel with both hands is an example. The center of mass stays put, "
                r"but the object starts to rotate."),
    ]),

    Section("5.6", "Newton's Second Law in Rotational Form", [
        C(r"Newton's second law for rotation: \(\alpha = {{c1::\dfrac{\Sigma\tau}{I}}}\)", tags=["formula"]),
        B(r"A mass \(m\) hangs from a rope wrapped around a pulley (rotational inertia \(I\), radius \(R\)). "
          r"What is the hanging mass's acceleration?",
          r"\[a = \frac{mg}{m + I/R^2}\]",
          bd="massive_pulley",
          extra=r"Combine \(mg - T = ma\), \(TR = I\alpha\), and \(a = R\alpha\)."),
        B(r"Why does a mass hanging from a pulley that has mass accelerate at less than \(g\)?",
          r"The rope tension slows the mass, and that tension is what spins up the pulley. Some of the "
          r"gravitational energy goes into the pulley's rotation."),
        B(r"For a rope over a pulley that has mass and is accelerating, is the tension the same on both sides?",
          r"<b>No.</b> The difference in tension produces the net torque on the pulley.",
          extra=r"Only an ideal, massless pulley has equal tensions."),
        B(r"A net torque of \(10\text{ N·m}\) acts on a wheel with \(I = 2\text{ kg·m}^2\). What is its "
          r"angular acceleration?",
          r"\(\alpha = 10/2 = 5\text{ rad/s}^2\)", tags=["problem"]),
        B(r"The same torque acts on a hoop and on a solid disk of equal mass and radius. Which gets the "
          r"larger angular acceleration?",
          r"The <b>disk</b>, because it has the smaller \(I\)."),
        C(r"Linear → rotational analogues: \(x \to {{c1::\theta}}\), \(v \to {{c2::\omega}}\), "
          r"\(a \to {{c3::\alpha}}\), \(m \to {{c4::I}}\), \(F \to {{c5::\tau}}\)"),
    ]),
])
