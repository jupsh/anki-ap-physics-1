from cards import B, C, Section, Unit

UNIT = Unit(1, "Kinematics", [
    Section("1.1", "Scalars and Vectors in One Dimension", [
        B(r"What is the difference between a <b>scalar</b> and a <b>vector</b>?",
          r"A <b>scalar</b> has magnitude only (e.g. 5 kg). A <b>vector</b> has magnitude <i>and</i> "
          r"direction (e.g. 5 m/s east).",
          extra=r"Vectors are written with an arrow: \(\vec v\). Their magnitude is \(|\vec v|\) or just \(v\)."),
        B(r"<b>Distance</b> vs. <b>displacement</b>: which is a scalar and which is a vector?",
          r"Distance is a <b>scalar</b>. Displacement is a <b>vector</b>."),
        B(r"<b>Speed</b> vs. <b>velocity</b>: which is a scalar and which is a vector?",
          r"Speed is a <b>scalar</b>. Velocity is a <b>vector</b>."),
        B(r"Is <b>acceleration</b> a scalar or a vector?",
          r"A <b>vector</b>."),
        B(r"In one dimension, how is the <b>direction</b> of a vector shown?",
          r"By its <b>sign</b> (+ or −), relative to a positive direction you choose.",
          extra=r"Choose and state your positive direction before solving. Up = + is common, but any "
                r"choice works if you stick with it."),
        C(r"A negative velocity means the object moves {{c1::in the negative direction}}. "
          r"It does <i>not</i> by itself mean the object is {{c2::slowing down}}."),
        B(r"How is instantaneous <b>speed</b> related to instantaneous <b>velocity</b>?",
          r"Speed is the magnitude of velocity: \(\text{speed} = |\vec v|\).",
          extra=r"This is not true of averages: <b>average</b> speed (distance / time) can differ from the "
                r"magnitude of average velocity (displacement / time)."),
    ]),

    Section("1.2", "Displacement, Velocity, and Acceleration", [
        B(r"An object moves from \(x = 0\) to \(x = 5\text{ m}\), then back to \(x = 2\text{ m}\). "
          r"What <b>distance</b> did it travel?",
          r"\(8\text{ m}\) (5 m forward + 3 m back)", bd="number_line", tags=["problem"]),
        B(r"An object moves from \(x = 0\) to \(x = 5\text{ m}\), then back to \(x = 2\text{ m}\). "
          r"What is its <b>displacement</b>?",
          r"\(\Delta x = +2\text{ m}\)", bd="number_line", tags=["problem"],
          extra=r"Displacement depends only on where you start and end."),
        C(r"Displacement: \(\Delta x = {{c1::x_f - x_i}}\)"),
        C(r"Average velocity: \(\bar v = {{c1::\dfrac{\Delta x}{\Delta t}}}\)", tags=["formula"]),
        C(r"Average speed \(= {{c1::\dfrac{\text{total distance}}{\Delta t}}}\)", tags=["formula"]),
        C(r"Average acceleration: \(\bar a = {{c1::\dfrac{\Delta v}{\Delta t}}}\)", tags=["formula"],
          extra=r"Acceleration is how fast <i>velocity</i> changes, in speed or in direction."),
        B(r"What is the SI unit of acceleration?",
          r"\(\text{m/s}^2\)"),
        B(r"How can you tell from the signs of \(v\) and \(a\) whether an object is speeding up or slowing down?",
          r"<b>Same sign:</b> speeding up.<br><b>Opposite signs:</b> slowing down.",
          extra=r"Example: \(v = -3\text{ m/s}\), \(a = -2\text{ m/s}^2\) is speeding up (in the − direction)."),
        B(r"Can an object have <b>zero velocity</b> but <b>nonzero acceleration</b>? Give an example.",
          r"Yes. A ball thrown straight up has \(v = 0\) at the top, but \(a = g\) downward.",
          extra=r"If \(a\) were 0 at the top, the ball would just stay there."),
        B(r"What condition must hold to use the kinematic equations?",
          r"<b>Constant acceleration</b> over the interval you apply them to."),
        C(r"Kinematics, no displacement term: \(v_x = {{c1::v_{x0} + a_x t}}\)", tags=["formula"]),
        C(r"Kinematics, no final velocity: \(x = x_0 + {{c1::v_{x0}t + \tfrac{1}{2}a_x t^2}}\)",
          tags=["formula"]),
        C(r"Kinematics, no time: \(v_x^2 = {{c1::v_{x0}^2 + 2a_x(x - x_0)}}\)", tags=["formula"],
          extra=r"Use this one when time is neither given nor asked for."),
        C(r"With constant acceleration, average velocity is \(\bar v = {{c1::\dfrac{v_0 + v}{2}}}\)",
          tags=["formula"]),
        B(r"What is the magnitude and direction of the acceleration of an object in <b>free fall</b> near "
          r"Earth's surface?",
          r"\(g \approx 9.8\text{ m/s}^2\) (AP allows \(10\text{ m/s}^2\)), pointing <b>down</b>.",
          extra=r"“Free fall” means gravity is the only force: going up, at the top, and coming down."),
        B(r"Without air resistance, does a heavier object fall with a greater acceleration?",
          r"<b>No.</b> All objects in free fall have the same acceleration \(g\)."),
        B(r"A ball is dropped from rest. How fast is it moving after \(2.0\text{ s}\)? \((g = 10\text{ m/s}^2)\)",
          r"\(v = gt = 20\text{ m/s}\)", tags=["problem"]),
        B(r"A ball is dropped from rest. How far does it fall in \(2.0\text{ s}\)? \((g = 10\text{ m/s}^2)\)",
          r"\(d = \tfrac12gt^2 = 20\text{ m}\)", tags=["problem"]),
        B(r"A ball is thrown straight up at \(20\text{ m/s}\). How long does it take to reach the top? "
          r"\((g = 10\text{ m/s}^2)\)",
          r"\(t = v_0/g = 2\text{ s}\)", tags=["problem"],
          extra=r"By symmetry, it takes another 2 s to fall back to the launch height."),
        B(r"A ball is thrown straight up at \(20\text{ m/s}\). How high does it rise? \((g = 10\text{ m/s}^2)\)",
          r"\(h = \dfrac{v_0^2}{2g} = 20\text{ m}\)", tags=["problem"]),
    ]),

    Section("1.3", "Representing Motion", [
        B(r"On a position–time graph, what does the slope of a <b>secant</b> line between two points represent?",
          r"The <b>average velocity</b> over that interval.", bd="xt_graph"),
        B(r"On a position–time graph, what does the slope of the <b>tangent</b> line at a point represent?",
          r"The <b>instantaneous velocity</b> at that moment.", bd="xt_graph"),
        B(r"On a velocity–time graph, what does the <b>slope</b> represent?",
          r"<b>Acceleration</b>.", bd="vt_graph"),
        B(r"On a velocity–time graph, what does the <b>area</b> between the curve and the time axis represent?",
          r"<b>Displacement</b>.", bd="vt_graph"),
        B(r"On an acceleration–time graph, what does the area under the curve represent?",
          r"The <b>change in velocity</b>, \(\Delta v\)."),
        B(r"An object starts with positive velocity and has constant positive acceleration. What shape "
          r"are its \(x\)–\(t\), \(v\)–\(t\), and \(a\)–\(t\) graphs?",
          r"\(x\)–\(t\): parabola curving upward<br>\(v\)–\(t\): straight line with slope \(a\)<br>"
          r"\(a\)–\(t\): horizontal line",
          bd="motion_graphs"),
        B(r"What does a <b>curved</b> position–time graph tell you?",
          r"The velocity is changing, so the object is <b>accelerating</b>."),
        B(r"A position–time graph is <b>concave up</b>. What is the sign of the acceleration?",
          r"<b>Positive</b>: the slope (velocity) keeps increasing."),
        B(r"What does a <b>horizontal</b> line on a position–time graph mean?",
          r"The object is at <b>rest</b> (\(v = 0\))."),
        B(r"What does a <b>horizontal</b> line on a velocity–time graph mean?",
          r"<b>Constant velocity</b> (\(a = 0\))."),
        B(r"The dots mark an object's position at equal time intervals. Is it speeding up, slowing down, "
          r"or moving at constant speed?",
          r"<b>Speeding up.</b> It covers more distance in each interval, so its acceleration points in "
          r"the direction of motion.",
          fd="motion_diagram"),
        B(r"On a velocity–time graph, what does area <b>below</b> the time axis represent?",
          r"<b>Negative</b> displacement.",
          extra=r"Net displacement = (area above) − (area below)."),
        B(r"How do you find the total <b>distance</b> traveled from a velocity–time graph?",
          r"Add the <b>absolute values</b> of all the areas, above and below the axis."),
        B(r"On a velocity–time graph, how do you spot the moment an object <b>changes direction</b>?",
          r"Where the graph <b>crosses</b> the time axis (\(v\) changes sign).",
          extra=r"Don't look for where the slope is zero. That is where \(a = 0\), which is a different thing."),
    ]),

    Section("1.4", "Reference Frames and Relative Motion", [
        B(r"What is a <b>reference frame</b>?",
          r"The coordinate system (and observer) that you measure motion relative to.",
          extra=r"Position and velocity depend on the frame. A seated train passenger has \(v = 0\) in "
                r"the train's frame but \(v = 30\text{ m/s}\) in the ground's frame."),
        C(r"Relative velocity: "
          r"\(\vec v_{A\text{ rel }C} = {{c1::\vec v_{A\text{ rel }B} + \vec v_{B\text{ rel }C}}}\)",
          tags=["formula"]),
        B(r"A boat points straight across a river and moves at \(4\text{ m/s}\) relative to the water. "
          r"The current is \(3\text{ m/s}\). What is the boat's speed relative to the ground?",
          r"\(5\text{ m/s}\) (a 3-4-5 triangle)",
          bd="relative_motion", tags=["problem"],
          extra=r"Its direction is \(\tan^{-1}(3/4) \approx 37^\circ\) downstream of straight across."),
        B(r"A boat aims straight across a river. Does the current change how long it takes to cross?",
          r"<b>No.</b> Crossing time depends only on the velocity component across the river. The current "
          r"only carries the boat downstream."),
        B(r"Two observers move at <b>constant velocity</b> relative to each other. Do they measure the same "
          r"acceleration for an object?",
          r"<b>Yes.</b> Their velocity measurements differ by a constant, so the change in velocity is the same.",
          extra=r"That's why Newton's laws hold in every inertial frame."),
        B(r"A ball is dropped inside a train moving at constant velocity. What path does a <b>rider</b> see?",
          r"Straight down."),
        B(r"A ball is dropped inside a train moving at constant velocity. What path does someone standing on "
          r"the <b>ground</b> see?",
          r"A <b>parabola</b>. The ball keeps the train's horizontal velocity as it falls."),
        B(r"Two cars approach each other head-on at \(20\text{ m/s}\) and \(30\text{ m/s}\) (ground frame). How "
          r"fast does each driver see the other approaching?",
          r"\(50\text{ m/s}\)", tags=["problem"]),
    ]),

    Section("1.5", "Vectors and Motion in Two Dimensions", [
        C(r"A vector of magnitude \(A\) at angle \(\theta\) above the \(+x\)-axis has components "
          r"\(A_x = {{c1::A\cos\theta}}\) and \(A_y = {{c2::A\sin\theta}}\)",
          d="vector_components", tags=["formula"]),
        C(r"Magnitude from components: \(A = {{c1::\sqrt{A_x^2 + A_y^2}}}\)", tags=["formula"]),
        C(r"Direction from components: \(\theta = {{c1::\tan^{-1}\!\left(\dfrac{A_y}{A_x}\right)}}\)",
          tags=["formula"]),
        B(r"How do you add two vectors <b>graphically</b>?",
          r"Place them <b>tip-to-tail</b>. The resultant runs from the first vector's tail to the last "
          r"vector's tip."),
        B(r"How do you add two vectors using <b>components</b>?",
          r"Add the \(x\) components together and the \(y\) components together. The sums are the "
          r"resultant's components."),
        B(r"What is the key idea behind <b>projectile motion</b>?",
          r"The horizontal and vertical motions are <b>independent</b>.", bd="projectile"),
        C(r"Projectile motion (no air resistance): \(a_x = {{c1::0}}\) and \(a_y = {{c2::-g}}\)",
          d="projectile", tags=["formula"]),
        B(r"What is a projectile's <b>velocity</b> at the top of its path?",
          r"Purely horizontal: \(v_y = 0\), but \(v = v_x \ne 0\)."),
        B(r"What is a projectile's <b>acceleration</b> at the top of its path?",
          r"\(g\) downward, the same as at every other point."),
        B(r"One ball is dropped and another is launched horizontally from the same height at the same "
          r"time. Which lands first?",
          r"<b>They land together.</b> Horizontal velocity has no effect on vertical motion."),
        C(r"On level ground with no air resistance, range is greatest at a launch angle of "
          r"\({{c1::45^\circ}}\)."),
        C(r"On level ground, complementary launch angles (e.g. 30° and 60°) at the same speed give "
          r"{{c1::the same range}}."),
        B(r"How long does a projectile launched <b>horizontally</b> from height \(h\) take to land?",
          r"\[t = \sqrt{\frac{2h}{g}}\]",
          extra=r"The same as the drop time, because \(v_{y0} = 0\)."),
        B(r"A ball rolls off a \(5\text{ m}\) high table at \(3\text{ m/s}\). How long is it in the air? "
          r"\((g = 10\text{ m/s}^2)\)",
          r"\(t = \sqrt{2(5)/10} = 1\text{ s}\)", tags=["problem"]),
        B(r"A ball rolls off a \(5\text{ m}\) high table at \(3\text{ m/s}\) and is in the air for \(1\text{ s}\). "
          r"How far from the table does it land?",
          r"\(\Delta x = v_x t = 3\text{ m}\)", tags=["problem"]),
        C(r"A projectile launched at speed \(v_0\) and angle \(\theta\) above horizontal has "
          r"\(v_{x0} = {{c1::v_0\cos\theta}}\) and \(v_{y0} = {{c2::v_0\sin\theta}}\)", tags=["formula"]),
        C(r"Time for a projectile launched at \(v_0\), angle \(\theta\), to reach the top: "
          r"\(t = {{c1::\dfrac{v_0\sin\theta}{g}}}\)", tags=["formula"]),
    ]),
])
