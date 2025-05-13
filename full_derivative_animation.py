from manim import *

class FullDerivativeAnimation(ThreeDScene):
    def construct(self):
        # Scene 1: Derivative Intro
        title_box = RoundedRectangle(width=10, height=2.5, color=BLUE, fill_color=BLUE_E, fill_opacity=0.2)
        title = Text("What is a Derivative?", font_size=60, color=WHITE)
        subtitle = Text("Understanding the Slope of a Curve", font_size=36, color=YELLOW)

        title.move_to(UP * 0.5)
        subtitle.next_to(title, DOWN)

        title_group = VGroup(title, subtitle)
        title_box.surround(title_group, buff=0.5)

        underline = Line(
            start=subtitle.get_left() + DOWN * 0.2 + LEFT * 0.1,
            end=subtitle.get_right() + DOWN * 0.2 + RIGHT * 0.1,
            stroke_width=4,
            color=WHITE
        )

        # Animate Intro
        self.play(DrawBorderThenFill(title_box), run_time=1)
        self.wait(0.25)

        self.play(Write(title), run_time=1)
        self.wait(0.25)

        self.play(FadeIn(subtitle, shift=UP), run_time=2)
        self.play(Create(underline), run_time=0.5)
        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # Scene 2: Secant to Tangent

        # Axes and function
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-2, 12, 2],
            x_length=7,
            y_length=5,
            axis_config={"include_tip": True},
            x_axis_config={"numbers_to_include": [-4, -2, 2, 4]},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8]}
        ).shift(LEFT * 2)

        # Manual axis labels
        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex("f(x)").next_to(axes.y_axis.get_end(), UP, buff=0.15)

        axes_labels = VGroup(x_label, y_label)

        graph = axes.plot(lambda x: x ** 2, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2", x_val=3, direction=UR)
        graph_label.shift(UP * 0.5 + RIGHT * 0.5)

        self.play(FadeIn(axes, axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(0.5)

        # Dynamic secant
        h = ValueTracker(3.0)
        x_val = -2

        dot_A = always_redraw(lambda: Dot(axes.c2p(x_val, x_val ** 2), color=YELLOW))
        dot_B = always_redraw(lambda: Dot(axes.c2p(x_val + h.get_value(), (x_val + h.get_value()) ** 2), color=GREEN))

        label_A = always_redraw(lambda: MathTex("A", font_size=32).next_to(dot_A, LEFT))
        label_B = always_redraw(lambda: MathTex("B", font_size=32).next_to(dot_B, LEFT))

        secant_dynamic = always_redraw(lambda: Line(dot_A.get_center(), dot_B.get_center(), color=ORANGE))

        # Intro text
        intro_text = Text("A secant line connects two points on a curve.", font_size=28).to_edge(DOWN)
        intro_box = SurroundingRectangle(intro_text, color=WHITE, buff=0.3)

        self.play(FadeIn(intro_box, dot_A, label_A, dot_B, label_B))
        self.play(Write(intro_text, runtime=0.5), Create(secant_dynamic, run_time=2))
        self.wait(2)

        rate_title = Tex(r"\textbf{Average Rate of Change}", font_size=32)
        slope_formula = MathTex(r"\frac{f(x+h) - f(x)}{h}", font_size=40)

        rate_group = VGroup(rate_title, slope_formula).arrange(DOWN, buff=0.2)
        rate_group.to_edge(RIGHT).shift(DOWN * 0.75)

        # Slope text
        slope_text = Text("This represents the average rate of change between A and B.", font_size=28).to_edge(DOWN)
        slope_box = SurroundingRectangle(slope_text, color=WHITE, buff=0.3)

        self.play(FadeTransform(intro_text, slope_text), FadeTransform(intro_box, slope_box),
                  Write(rate_group, run_time=0.5))
        self.wait(2)

        # Approach text
        approach_text = Text("As point B moves closer to point A, the length of the secant approaches zero...",
                             font_size=28).to_edge(DOWN)
        approach_box = SurroundingRectangle(approach_text, color=WHITE, buff=0.3)

        deriv_title = Tex(r"\textbf{Instantaneous Rate of Change}", font_size=32)
        limit_eq = MathTex(r"\lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = f'(x)", font_size=40)

        deriv_group = VGroup(deriv_title, limit_eq).arrange(DOWN, buff=0.2)
        deriv_group.to_edge(RIGHT).shift(DOWN * 0.75)

        self.play(FadeTransform(slope_box, approach_box), FadeTransform(slope_text, approach_text),
                  h.animate.set_value(0.25), FadeTransform(rate_group, deriv_group), run_time=4)
        self.wait(2)

        # Tangent
        tangent_text = Text("As the secant collapses, it becomes the tangent — the derivative.", font_size=28).to_edge(
            DOWN)
        tangent_box = SurroundingRectangle(tangent_text, color=WHITE, buff=0.3)

        tangent_title = Tex(r"\textbf{The Derivative at a Point}", font_size=32)
        tangent_formula = MathTex(r"f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}", font_size=40)

        tangent_group = VGroup(tangent_title, tangent_formula).arrange(DOWN, buff=0.2)
        tangent_group.to_edge(RIGHT).shift(DOWN * 0.75)

        # Tangent / Slope Along the Curve
        x_tracker = ValueTracker(-2)

        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(x_tracker.get_value(), x_tracker.get_value() ** 2), color=YELLOW)
        )

        tangent_line = always_redraw(
            lambda: axes.plot(
                lambda x: (x_tracker.get_value()) ** 2 + 2 * x_tracker.get_value() * (x - x_tracker.get_value()),
                color=GREEN
            )
        )

        tangent_label = MathTex("f'(-2) = -4", font_size=36).next_to(moving_dot, LEFT).shift(DOWN * 0.5)

        self.play(
            FadeTransform(approach_text, tangent_text, run_time=3),
            FadeTransform(approach_box, tangent_box, run_time=3),
            FadeTransform(deriv_group, tangent_group, run_time=3),
            h.animate.set_value(0.0).set_run_time(1.5),
            Create(tangent_line).set_run_time(1.5),
            FadeIn(moving_dot).set_run_time(1.5),
            Write(tangent_label).set_run_time(1.5),
            FadeOut(dot_A).set_run_time(0.5),
            FadeOut(label_A).set_run_time(0.5),
            FadeOut(label_B).set_run_time(0.5),
            FadeOut(secant_dynamic).set_run_time(0.5)
        )

        self.play(FadeOut(dot_B), run_time=0.5)

        # Bottom label
        slope_readout = always_redraw(
            lambda: Text(
                f"Slope at x = {x_tracker.get_value():.1f} is {2 * x_tracker.get_value():.1f}",
                font_size=28
            ).to_edge(DOWN)
        )
        deriv_box = SurroundingRectangle(slope_readout, color=WHITE, buff=0.3)

        # initial table
        def make_table(data):
            return Table(
                data,
                include_outer_lines=True,
                line_config={"stroke_width": 1},
                element_to_mobject=lambda s: MathTex(s) if s in ["x", "f'(x)"] else Text(s)
            ).scale(0.6).to_edge(RIGHT).shift(DOWN * 0.5)

        table_data = [["x", "f'(x)"], ["-2", "-4"]]
        table = make_table(table_data)

        self.wait(1.5)
        self.play(FadeTransform(tangent_box, deriv_box), FadeTransform(tangent_text, slope_readout),
                  FadeTransform(tangent_group, table), run_time=3)
        self.wait(1.5)
        self.play(FadeOut(tangent_label))

        # Loop with x values and table updates
        for x_val in [-1, 0, 1, 2]:
            table_data.append([f"{x_val}", f"{2 * x_val}"])
            new_table = make_table(table_data)
            self.play(x_tracker.animate.set_value(x_val), FadeTransform(table, new_table), run_time=1.5)
            table = new_table
            self.wait(1.5)

        self.wait(4)

        # Fade Out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # Scene 3: Tangent Plane (3D)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-75 * DEGREES)

        # Axes
        axes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[0, 10],
            x_length=6, y_length=6, z_length=5,
        ).shift(IN * 2 + LEFT * 2)

        # Axis Labels
        x_label = MathTex("x")
        y_label = MathTex("y")
        z_label = MathTex("z")
        self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)

        x_label.add_updater(lambda m: m.move_to(self.camera.project_point(axes.x_axis.get_end()) + RIGHT * 0.3))
        y_label.add_updater(
            lambda m: m.move_to(self.camera.project_point(axes.y_axis.get_end()) + UP * 0.3 + RIGHT * 0.1))
        z_label.add_updater(lambda m: m.move_to(self.camera.project_point(axes.z_axis.get_end()) + UP * 0.3))

        self.add(axes)

        # Intro Text
        intro_text = Text("We’ve seen how a tangent line describes the slope of a curve.", font_size=28).to_edge(DOWN)
        intro_box = SurroundingRectangle(intro_text, color=WHITE, buff=0.3)
        self.add_fixed_in_frame_mobjects(intro_text, intro_box)
        self.play(FadeIn(intro_box), Write(intro_text))
        self.wait(2)

        # Transition to Surface
        self.play(FadeOut(intro_text), FadeOut(intro_box))
        next_text = Text("Now, let’s consider a surface in three dimensions.", font_size=28).to_edge(DOWN)
        next_box = SurroundingRectangle(next_text, color=WHITE, buff=0.3)
        self.add_fixed_in_frame_mobjects(next_text, next_box)
        self.play(FadeIn(next_box), FadeIn(next_text))
        self.wait(2)

        # Surface Definitions
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u ** 2 + v ** 2),
            u_range=[-2.5, 2.5], v_range=[-2.5, 2.5],
            resolution=(30, 30),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )

        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(1)

        # Moving point
        moving_point = always_redraw(lambda: Dot3D(
            axes.c2p(a_tracker.get_value(), b_tracker.get_value(),
                     a_tracker.get_value() ** 2 + b_tracker.get_value() ** 2),
            color=YELLOW,
            radius=0.06
        ))

        # Tangent plane
        moving_plane = always_redraw(lambda: Surface(
            lambda u, v: axes.c2p(
                u, v,
                a_tracker.get_value() ** 2 + b_tracker.get_value() ** 2
                + 2 * a_tracker.get_value() * (u - a_tracker.get_value())
                + 2 * b_tracker.get_value() * (v - b_tracker.get_value())
            ),
            u_range=[a_tracker.get_value() - 1, a_tracker.get_value() + 1],
            v_range=[b_tracker.get_value() - 1, b_tracker.get_value() + 1],
            resolution=(10, 10),
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],
        ))

        # Legend Elements
        blue_patch = Square(side_length=0.3, fill_color=BLUE_D, fill_opacity=0.6)
        red_patch = Square(side_length=0.3, fill_color=RED_D, fill_opacity=0.75)
        yellow_dot = Dot(radius=0.06, color=YELLOW)

        blue_label = Text("z = x² + y²", font_size=24)
        red_label = Text("Tangent Plane", font_size=24)

        blue_row = VGroup(blue_patch, blue_label).arrange(RIGHT, buff=0.2)
        red_row = VGroup(red_patch, red_label).arrange(RIGHT, buff=0.2)

        coord_label = always_redraw(lambda: Text(
            f"({a_tracker.get_value():.1f}, {b_tracker.get_value():.1f}, "
            f"{(a_tracker.get_value() ** 2 + b_tracker.get_value() ** 2):.2f})",
            font_size=24
        ).next_to(yellow_dot, RIGHT, buff=0.2))

        yellow_row = VGroup(yellow_dot, coord_label).arrange(RIGHT, buff=0.2)

        # Initial Legend
        initial_group = VGroup(blue_row.copy()).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        initial_box = SurroundingRectangle(initial_group, color=WHITE, buff=0.3)
        initial_legend = VGroup(initial_box, initial_group).to_corner(UR).shift(DOWN * 0.5)

        # Full Legend
        full_group = VGroup(blue_row, red_row, yellow_row).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        full_box = SurroundingRectangle(full_group, color=WHITE, buff=0.3)
        full_legend = VGroup(full_box, full_group).to_corner(UR).shift(DOWN * 0.5)

        # Add only the initial legend
        self.add_fixed_in_frame_mobjects(initial_legend)
        self.play(FadeIn(initial_legend))

        self.play(Create(surface))

        self.wait(1)

        # Slope / Tangent Plane
        self.play(FadeOut(next_text), FadeOut(next_box))
        slope_text = Text("The slope of the surface is described by the tangent plane.", font_size=28).to_edge(DOWN)
        slope_box = SurroundingRectangle(slope_text, color=WHITE, buff=0.3)
        self.add_fixed_in_frame_mobjects(slope_text, slope_box)
        self.play(FadeIn(slope_box), FadeIn(slope_text))
        self.wait(2)

        self.add_fixed_in_frame_mobjects(full_legend)
        self.play(FadeOut(initial_legend), FadeIn(full_legend))

        self.play(FadeIn(moving_point), Create(moving_plane))

        self.wait(2)

        # 360-degree camera spin
        self.begin_ambient_camera_rotation(rate=PI / 2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(2)

        # Move plane around
        move_text = Text("As the point moves, the tangent plane moves with it.", font_size=28).to_edge(DOWN)
        move_box = SurroundingRectangle(move_text, color=WHITE, buff=0.3)
        self.add_fixed_in_frame_mobjects(move_text, move_box)
        self.play(FadeOut(slope_text), FadeOut(slope_box), FadeIn(move_box), FadeIn(move_text))
        self.wait(1)

        self.play(a_tracker.animate.set_value(-1), b_tracker.animate.set_value(-1), run_time=2)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(2.5), b_tracker.animate.set_value(1.5), run_time=2)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(-1), b_tracker.animate.set_value(2), run_time=2)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(2), b_tracker.animate.set_value(-0.5), run_time=2)
        self.wait(0.5)

        # 360-degree camera spin
        self.begin_ambient_camera_rotation(rate=PI / 2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(1)

        # fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # Conclusion Scene
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(1)

        summary_box = RoundedRectangle(
            width=10, height=2.5, color=GREEN, fill_color=GREEN_E, fill_opacity=0.2
        )

        summary_title = Text("Key Idea:", font_size=60, color=WHITE)
        summary_text = Text(
            "The derivative is the slope — of a line or a plane — at a point.",
            font_size=36,
            color=YELLOW
        )

        summary_title.move_to(UP * 0.5)
        summary_text.next_to(summary_title, DOWN)

        summary_group = VGroup(summary_title, summary_text)
        summary_box.surround(summary_group, buff=0.5)

        self.play(DrawBorderThenFill(summary_box), run_time=1)
        self.play(Write(summary_title), run_time=1)
        self.play(FadeIn(summary_text, shift=UP), run_time=2)
        self.wait(1)

        # Fade out everything
        self.wait(1)
        self.play(FadeOut(VGroup(summary_box, summary_title, summary_text)), run_time=2)
        self.wait(1)
