from manim import *
import manim
import networkx as nx
from math import e, pi


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


    
def disp_bell_curv_area(self, axe, curve, x_interval, qx, px, dir):
    area = axe.get_area(curve, x_range=x_interval)
    self.play(FadeIn(area))
    self.wait(0.4)
    
    if dir == 1:
        msg2 = f"\Phi({qx:.3f}) = "
        msg2 += "\mathbb{P}(X \leqslant "
        msg2 += f"{qx:.3f}) = {px:.3f}"
        msg1 = f"\Phi({qx:.3f}) = "
        msg1 += "\mathbb{P}(X \leqslant "
        msg1 += f"{qx:.3f}) = \int_" + "{-\infty}"
        msg1 += "^{" + f"{qx:.3f}" + "}f(x)dx"
    elif dir == 0:
        msg2 = "\mathbb{P}("
        msg2 += f"{-qx:.3f} \leqslant X "
        msg2 += f"\leqslant {qx:.3f}) = "
        msg2 += f"2\Phi({qx:.3f}) - 1 = "
        msg2 += f"{2*px - 1:.3f}"
        msg1 = "\mathbb{P}("
        msg1 += f"{-qx:.3f} \leqslant X "
        msg1 += f"\leqslant {qx:.3f}) = "
        msg1 += "\int_{" + f"{-qx:.3f}" + "}"
        msg1 += "^{" + f"{qx:.3f}" + "}f(x)dx"
    elif dir == -1:
        msg2 = "\mathbb{P}(X \geqslant "
        msg2 += f"{qx:.3f}) = 1 - \Phi({qx:.3f}) = {1 - px:.3f}"
        msg1 = "\mathbb{P}(X \geqslant "
        msg1 += f"{qx:.3f}) = \int_" + "{" + f"{qx:.3f}" + "}"
        msg1 += "^{+\infty}f(x)dx"

    prob1, prob2 = MathTex(msg1), MathTex(msg2)
    self.play(
        FadeIn(prob1.scale(.85).next_to(axe, UP))
    )
    self.wait(0.4)
    self.play(ReplacementTransform(prob1, prob2.scale(0.75)))
    self.wait(0.4)
    self.play(
        FadeOut(prob1),
        FadeOut(prob2),
        FadeOut(area)
    )



    
class BellCurve(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-5, 5],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=2),
            Create(bell_curve, run_time=2.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-5, -1.645],
            qx=-1.645, px=0.05, dir=1
        )
        self.wait(2.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[1.645, 5],
            qx=1.645, px=0.95, dir=-1
        )
        self.wait(2.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-1.645, 1.645],
            qx=1.645, px=0.95, dir=0
        )
        self.wait(2.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        


class BellCurve2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-5, 5],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=2),
            Create(bell_curve, run_time=2.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-5, 2.576],
            qx=2.576, px=0.995, dir=1
        )
        self.wait(2.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.576, 5],
            qx=-2.576, px=0.005, dir=-1
        )
        self.wait(2.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.576, 2.576],
            qx=2.576, px=0.995, dir=0
        )
        self.wait(2.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        
class BellCurve3(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-5, 5],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=2),
            Create(bell_curve, run_time=2.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-5, 2.326],
            qx=2.326, px=0.99, dir=1
        )
        self.wait(2.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.326, 5],
            qx=-2.326, px=0.01, dir=-1
        )
        self.wait(2.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.326, 2.326],
            qx=2.326, px=0.99, dir=0
        )
        self.wait(2.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
class BellCurve4(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-4, 4],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=0.5),
            Create(bell_curve, run_time=0.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, 1.96],
            qx=1.96, px=0.975, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[1.96, 4],
            qx=1.96, px=0.975, dir=-1
        )
        self.wait(0.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-1.96, 4],
            qx=-1.96, px=0.025, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, -1.96],
            qx=-1.96, px=0.025, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-1.96, 1.96],
            qx=1.96, px=0.975, dir=0
        )
        self.wait(0.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        

class BellCurve5(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-4, 4],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=0.5),
            Create(bell_curve, run_time=0.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, 1.645],
            qx=1.645, px=0.95, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, 1.96],
            qx=1.96, px=0.975, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, 2.326],
            qx=2.326, px=0.99, dir=1
        )
        self.wait(0.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, 2.576],
            qx=2.576, px=0.995, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[2.576, 4],
            qx=2.576, px=0.995, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[2.326, 4],
            qx=2.326, px=0.99, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[1.96, 4],
            qx=1.96, px=0.975, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[1.645, 4],
            qx=1.645, px=0.95, dir=-1
        )
        self.wait(0.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class BellCurve6(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Courbe en cloche (loi normale)")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        ax = Axes(
            x_range=[-4, 4],
            y_range=[-0.1, 0.5]
        ).scale(0.65)

        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=RED
        )

        self.play(
            Create(ax, run_time=0.5),
            Create(bell_curve, run_time=0.5)
        )
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density).scale(0.85)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, -2.576],
            qx=-2.576, px=0.005, dir=1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, -2.326],
            qx=-2.326, px=0.01, dir=1
        )
        self.wait(0.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, -1.96],
            qx=-1.96, px=0.025, dir=1
        )
        self.wait(0.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-4, -1.645],
            qx=-1.645, px=0.05, dir=1
        )
        self.wait(0.5)
        
        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.576, 4],
            qx=-2.576, px=0.005, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-2.326, 4],
            qx=-2.326, px=0.01, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-1.96, 4],
            qx=-1.96, px=0.025, dir=-1
        )
        self.wait(0.5)

        disp_bell_curv_area(
            self, ax, bell_curve,
            x_interval=[-1.645, 4],
            qx=-1.645, px=0.05, dir=-1
        )
        self.wait(0.5)
        # C-x C-t transpose line
        

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        

        
        

        
