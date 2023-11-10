from manim import *
import manim
import networkx as nx
from math import e, pi
import numpy as np

from char_creature import CharCreature, ShowBubble, RoundBubble

config.media_embed = True; config.media_width = "100%"
_RV = "-v WARNING -qm --progress_bar None --disable_caching Example"
_RI = "-v WARNING -s --progress_bar None --disable_caching Example"
_RV_mid = "-v WARNING -qm -r 1200,300 --progress_bar None --disable_caching Example"
_RI_mid = "-v WARNING -s -r 1200,300 --progress_bar None --disable_caching Example"

SCALE_FACTOR = 0.5
# flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


def disp_sub(self, lang):
    like_svg_path = "~/Documents/pics/svg/like.svg"
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    jpg_png_path = "~/Documents/pics/png/sabonner.png"
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        sub_pic = SVGMobject(sub_svg_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        sub_pic = ImageMobject(jpg_png_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(.5)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.add(like_pic.scale(sub_scale).next_to(sub_pic, LEFT))
    self.wait(0.1)



    
def put_sub_logo(self, svg_scale=0.25):
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    sub_pic = SVGMobject(sub_svg_path)
    self.play(
        FadeIn(
            sub_pic.scale(svg_scale).to_edge(2.5*UP)
        )
    )
    return sub_pic


    
def put_like_logo(self, sub_pic, svg_scale=0.25):
    like_svg_path = "~/Documents/pics/svg/like.svg"
    like_pic = SVGMobject(like_svg_path)
    self.play(
        FadeIn(
            like_pic.scale(svg_scale).next_to(sub_pic, LEFT)
        )
    )
    return like_pic


    
def put_youtube_short_logo(self, sub_pic, svg_scale=0.25):
    youtube_short_path = "~/Documents/pics/svg/Youtube_shorts.svg"
    youtube_shorts = SVGMobject(
        youtube_short_path,
        fill_opacity=1,
        fill_color=RED
    ).scale(svg_scale)
    self.play(
        FadeIn(
            youtube_shorts.next_to(sub_pic, RIGHT)
        )
    )
    return youtube_shorts


    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(2.5)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
        
    self.play(ReplacementTransform(part, full), run_time=2.5)
    self.wait(2.5)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)


def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(
        axes.c2p(
            x,
            function.underlying_function(x)
        )
    )
    result.add(line, dot)
    return result

    
class Curve1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1])
        ]
    
    
    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = ax.plot(
            lambda x: k / x,
            color=YELLOW_D,
            x_range=[k / 10, 10.0, 0.01],
            use_smoothing=False,
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                            (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(
            lambda x: x.move_to(
                ax.c2p(
                    t.get_value(),
                    k / t.get_value()
                )
            )
        )
        dot.set_z_index(10)

        self.add(ax, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k / 10))
        self.play(t.animate.set_value(5))
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        

class Curve2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(
            lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C
        )
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(
            ax.input_to_graph_point(2, curve_1),
            color=YELLOW
        )
        line_2 = ax.get_vertical_line(
            ax.i2gp(3, curve_1),
            color=YELLOW
        )

        riemann_area = ax.get_riemann_rectangles(
            curve_1,
            x_range=[0.3, 0.6],
            dx=0.03,
            color=BLUE,
            fill_opacity=0.5
        )
        area = ax.get_area(
            curve_2,
            [2, 3],
            bounded_graph=curve_1,
            color=GREY,
            opacity=0.5
        )

        self.play(
            Write(ax),
            Write(labels),
            Write(curve_1),
            Write(curve_2),
            Write(line_1),
            Write(line_2),
            Write(riemann_area),
            Write(area)
        )
        self.wait(3.5)

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class Derivatives1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)
        
        k = ValueTracker(-2) # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(
                x_range=[-2, 2, 0.5],
                x_length=4,
                y_range=[-9, 9, 2],
                y_length=9
            ).add_coordinates().shift(LEFT * 2)
        )

        
        func1 = plane1.plot(
            lambda x: (1 / 3) * x ** 3, x_range=[-2, 2], color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x) = \dfrac{1}{3}x^3")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(
                    k.get_value(),
                    func1.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(
                x_range=[-2, 2, 0.5],
                x_length=4,
                y_range=[-1, 5, 1],
                y_length=9
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: x ** 2, x_range=[-2, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex(r"f'(x) = x^2")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2,
                function=func2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text = (
            Tex("Pente : ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.add(
            moving_slope,
            moving_h_line,
            func2,
            slope_value,
            slope_value_text,
            dot
        )
        self.play(
            k.animate.set_value(3),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        k = ValueTracker(-2) # Tracking the end values of stuff to show
        
        plane1_2 = (
            NumberPlane(
                x_range=[-2.5, 2.5, 0.5],
                x_length=3.5,
                y_range=[-1, 1, 0.1],
                y_length=9
            ).add_coordinates().shift(LEFT * 2)
        )
        
        func1_2 = plane1_2.plot(
            lambda x: (1 / 3) * x ** 3 - x, x_range=[-2, 2], color=RED_C
        )
        func1_2_lab = (
            MathTex(r"f(x) = \dfrac{1}{3}x^3 - x")
            .set(width=2.5)
            .next_to(plane1_2, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope_2 = always_redraw(
            lambda: plane1_2.get_secant_slope_group(
                x=k.get_value(),
                graph=func1_2,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot_2 = always_redraw(
            lambda: Dot().move_to(
                plane1_2.c2p(
                    k.get_value(),
                    func1_2.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2_2 = (
            NumberPlane(
                x_range=[-2.5, 2.5, 0.5],
                x_length=3.5,
                y_range=[-0.5, 3, 0.5],
                y_length=9
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2_2 = always_redraw(
            lambda: plane2_2.plot(
                lambda x: x ** 2, x_range=[-2, k.get_value()], color=GREEN
            )
        )
        func2_2_lab = (
            MathTex(r"f'(x) = x^2 - 1")
            .set(width=2.5)
            .next_to(plane2_2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line_2 = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2_2,
                function=func2_2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text_2 = (
            Tex("Pente : ")
            .next_to(plane1_2, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value_2 = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2_2.underlying_function(k.get_value()))
            .next_to(slope_value_text_2, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                # DrawBorderThenFill(plane1_2),
                # DrawBorderThenFill(plane2_2),
                ReplacementTransform(plane1, plane1_2),
                ReplacementTransform(plane2, plane2_2),
                ReplacementTransform(func1, func1_2),
                ReplacementTransform(func1_lab, func1_2_lab),
                ReplacementTransform(func2_lab, func2_2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.play(
            ReplacementTransform(moving_slope, moving_slope_2),
            ReplacementTransform(moving_h_line, moving_h_line_2),
            ReplacementTransform(func2, func2_2),
            ReplacementTransform(slope_value, slope_value_2),
            ReplacementTransform(slope_value_text, slope_value_text_2),
            ReplacementTransform(dot, dot_2)
        )
        self.play(
            k.animate.set_value(2),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class Derivatives2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)
        
        k = ValueTracker(-np.pi) # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(
                x_range=[-3.5, 3.5, 1],
                x_length=3.75,
                y_range=[-1.25, 1.25, 0.25],
                y_length=6
            ).add_coordinates().shift(LEFT * 2)
        )

        
        func1 = plane1.plot(
            lambda x: np.sin(x), x_range=[-np.pi, np.pi], color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x) = \sin(x)")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(
                    k.get_value(),
                    func1.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(
                x_range=[-3.5, 3.5, 1],
                x_length=3.75,
                y_range=[-1.25, 1.25, 0.25],
                y_length=6
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: np.cos(x),
                x_range=[-np.pi, k.get_value()],
                color=GREEN
            )
        )
        func2_lab = (
            MathTex(r"f'(x) = \cos(x)")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2,
                function=func2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text = (
            Tex("Pente : ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.add(
            moving_slope,
            moving_h_line,
            func2,
            slope_value,
            slope_value_text,
            dot
        )
        self.play(
            k.animate.set_value(3),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        k = ValueTracker(0.05-np.pi/2) # Tracking the end values of stuff to show
        
        plane1_2 = (
            NumberPlane(
                x_range=[-1.15, 1.15, 0.5],
                x_length=3.75,
                y_range=[-2.5, 2.5, 0.5],
                y_length=6
            ).add_coordinates().shift(LEFT * 2)
        )
        
        func1_2 = plane1_2.plot(
            lambda x: np.tan(x),
            x_range=[-1.15, 1.15],
            color=RED_C
        )
        func1_2_lab = (
            MathTex(r"f(x) = \tan(x)")
            .set(width=2.5)
            .next_to(plane1_2, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope_2 = always_redraw(
            lambda: plane1_2.get_secant_slope_group(
                x=k.get_value(),
                graph=func1_2,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot_2 = always_redraw(
            lambda: Dot().move_to(
                plane1_2.c2p(
                    k.get_value(),
                    func1_2.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2_2 = (
            NumberPlane(
                x_range=[-1.15, 1.15, 0.5],
                x_length=3.75,
                y_range=[-0.5, 5, 1],
                y_length=6
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2_2 = always_redraw(
            lambda: plane2_2.plot(
                lambda x: 1 + np.tan(x) ** 2,
                x_range=[-1.15, k.get_value()],
                color=GREEN
            )
        )
        func2_2_lab = (
            MathTex(r"f'(x) = 1 + \tan(x)^2")
            .set(width=2.5)
            .next_to(plane2_2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line_2 = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2_2,
                function=func2_2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text_2 = (
            Tex("Pente : ")
            .next_to(plane1_2, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value_2 = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2_2.underlying_function(k.get_value()))
            .next_to(slope_value_text_2, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                ReplacementTransform(plane1, plane1_2),
                ReplacementTransform(plane2, plane2_2),
                ReplacementTransform(func1, func1_2),
                ReplacementTransform(func1_lab, func1_2_lab),
                ReplacementTransform(func2_lab, func2_2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.play(
            ReplacementTransform(moving_slope, moving_slope_2),
            ReplacementTransform(moving_h_line, moving_h_line_2),
            ReplacementTransform(func2, func2_2),
            ReplacementTransform(slope_value, slope_value_2),
            ReplacementTransform(slope_value_text, slope_value_text_2),
            ReplacementTransform(dot, dot_2)
        )
        self.play(
            k.animate.set_value(1),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')
        

class Derivatives3(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)
        
        k = ValueTracker(-np.pi) # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(
                x_range=[-2.5, 2.5, 1],
                x_length=3.75,
                y_range=[-0.25, 0.5, 0.25],
                y_length=6
            ).add_coordinates().shift(LEFT * 2)
        )

        
        func1 = plane1.plot(
            lambda x:
            np.exp(-x**2/2)/np.sqrt(2*np.pi),
            x_range=[-2.5, 2.5],
            color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(
                    k.get_value(),
                    func1.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(
                x_range=[-2.5, 2.5, 1],
                x_length=3.75,
                y_range=[-0.5, 0.5, 0.25],
                y_length=6
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: -x*np.exp(-x**2/2)/np.sqrt(2*np.pi),
                x_range=[-np.pi, k.get_value()],
                color=GREEN
            )
        )
        func2_lab = (
            MathTex(r"f'(x) = -x\dfrac{e^{-\frac{x^2}{2}}}{\sqrt{x}}")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2,
                function=func2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text = (
            Tex("Pente : ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.add(
            moving_slope,
            moving_h_line,
            func2,
            slope_value,
            slope_value_text,
            dot
        )
        self.play(
            k.animate.set_value(3),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        k = ValueTracker(0.05-np.pi/2) # Tracking the end values of stuff to show
        
        plane1_2 = (
            NumberPlane(
                x_range=[-1.15, 1.15, 0.5],
                x_length=3.75,
                y_range=[-2.5, 2.5, 0.5],
                y_length=6
            ).add_coordinates().shift(LEFT * 2)
        )
        
        func1_2 = plane1_2.plot(
            lambda x: np.tan(x),
            x_range=[-1.15, 1.15],
            color=RED_C
        )
        func1_2_lab = (
            MathTex(r"f(x) = \tan(x)")
            .set(width=2.5)
            .next_to(plane1_2, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope_2 = always_redraw(
            lambda: plane1_2.get_secant_slope_group(
                x=k.get_value(),
                graph=func1_2,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot_2 = always_redraw(
            lambda: Dot().move_to(
                plane1_2.c2p(
                    k.get_value(),
                    func1_2.underlying_function(k.get_value())
                )
            )
        )

        # Adding Mobjects for the second plane
        plane2_2 = (
            NumberPlane(
                x_range=[-1.15, 1.15, 0.5],
                x_length=3.75,
                y_range=[-0.5, 5, 1],
                y_length=6
            )
            .add_coordinates()
            .shift(RIGHT * 2)
        )

        func2_2 = always_redraw(
            lambda: plane2_2.plot(
                lambda x: 1 + np.tan(x) ** 2,
                x_range=[-1.15, k.get_value()],
                color=GREEN
            )
        )
        func2_2_lab = (
            MathTex(r"f'(x) = 1 + \tan(x)^2")
            .set(width=2.5)
            .next_to(plane2_2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line_2 = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2_2,
                function=func2_2,
                x=k.get_value(),
                width=4,
                color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text_2 = (
            Tex("Pente : ")
            .next_to(plane1_2, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value_2 = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2_2.underlying_function(k.get_value()))
            .next_to(slope_value_text_2, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                ReplacementTransform(plane1, plane1_2),
                ReplacementTransform(plane2, plane2_2),
                ReplacementTransform(func1, func1_2),
                ReplacementTransform(func1_lab, func1_2_lab),
                ReplacementTransform(func2_lab, func2_2_lab),
                run_time=5,
                lag_ratio=0.5
            )
        )
        self.play(
            ReplacementTransform(moving_slope, moving_slope_2),
            ReplacementTransform(moving_h_line, moving_h_line_2),
            ReplacementTransform(func2, func2_2),
            ReplacementTransform(slope_value, slope_value_2),
            ReplacementTransform(slope_value_text, slope_value_text_2),
            ReplacementTransform(dot, dot_2)
        )
        self.play(
            k.animate.set_value(1),
            run_time=15,
            rate_func=linear
        )
        self.wait()

        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        
class OmegaCreature(Scene):
    def __init__(
            self,
            eyes_scale=2.7,
            eyes_prop=[0.5, 0.05],
            eyes_buff=0.09,
            body_scale=7,
            color=RED,
            **kwargs
    ):
        body = MathTex(r"\Omega").scale(body_scales).set_color(color)
        super().__init__(
            body,
            eyes_scale=eyes_scale,
            eyes_prop=eyes_prop,
            eyes_buff=eyes_buff,
            **kwargs
        )
        
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)

    def construct(self):
        title_start = Title("Analyse")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)
        

        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')
