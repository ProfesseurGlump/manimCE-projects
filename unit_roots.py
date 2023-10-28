from manim import *
import manim
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
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        sub_pic = SVGMobject("/Users/dn/Documents/pics/svg/subscribe.svg")
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        sub_pic = ImageMobject("/Users/dn/Documents/pics/png/sabonner.png")
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(2.5)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.wait(2.5)

    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(2.5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(2.5)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 3))
    self.wait(2.5)
        
    self.play(ReplacementTransform(part, full), run_time=3)
    self.wait(2.5)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)

    

class UnitRoots(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Racines de l'unité "
        title = Title(f"{msg} avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        plane = ComplexPlane().add_coordinates()
        self.play(Write(plane))

        def equation_title(old_eq, new_msg, time):
            msg = new_msg
            new_eq = Title(f"{msg}")
            self.play(ReplacementTransform(old_eq, new_eq))
            self.wait(time)
            return new_eq

        old_eq, new_msg, time = title, "$z^{2} = 1$ ", 0.25
        new_eq = equation_title(old_eq, new_msg, time)
        
        def write_dots_labs(dots, labs, action):
            if action == 1:
                self.play(*[Write(d) for d in dots])
                self.wait(1.25)
                self.play(*[Write(l) for l in labs])
            elif action == -1:
                self.play(*[Unwrite(d) for d in dots])
                self.wait(0.5)
                self.play(*[Unwrite(l) for l in labs])

        d0 = Dot(plane.n2p(1 + 0j), color=YELLOW)
        msg0 = "z_0 = 1"
        l0 = MathTex(msg0, font_size=40).next_to(d0, UR, 0.1)
        
        d1 = Dot(plane.n2p(-1 + 0j), color=YELLOW)
        msg1 = "z_1 = -1"
        l1 = MathTex(msg1, font_size=40).next_to(d1, UL, 0.1)
        
        dots, labs, action = [d0, d1], [l0, l1], 1
        write_dots_labs(dots, labs, action)
        self.wait(0.5)

        dots, labs, action = [d0, d1], [l0, l1], -1
        write_dots_labs(dots, labs, action)
        self.wait(0.5)
        
        old_eq, new_msg, time = new_eq, "$z^{3} = 1$ ", 0.35
        new_eq = equation_title(old_eq, new_msg, time)

        d0 = Dot(plane.n2p(1 + 0j), color=YELLOW)
        msg0 = "z_0 = 1"
        l0 = MathTex(msg0, font_size=40).next_to(d0, UR, 0.1)
        
        d1 = Dot(plane.n2p(-0.5 + 0.866j), color=YELLOW)
        msg1 = "z_1 = -\\dfrac{1}{2} + i\\dfrac{\\sqrt{3}}{2}"
        l1 = MathTex(msg1, font_size=40).next_to(d1, UL, 0.1)

        d2 = Dot(plane.n2p(-0.5 - 0.866j), color=YELLOW)
        msg2 = "z_2 = -\\dfrac{1}{2} - i\\dfrac{\\sqrt{3}}{2}"
        l2 = MathTex(msg2, font_size=40).next_to(d2, DL, 0.1)

        dots, labs, action = [d0, d1, d2], [l0, l1, l2], 1
        write_dots_labs(dots, labs, action)
        
        triangle = RegularPolygon(n=3, start_angle=120*DEGREES, color=RED)
        self.wait(0.55)
        self.play(Write(triangle))
        
        dots, labs, action = [d0, d1, d2], [l0, l1, l2], -1
        write_dots_labs(dots, labs, action)
        self.wait(0.5)
        self.play(Unwrite(triangle))
        self.wait(0.5)

        old_eq, new_msg, time = new_eq, "$z^{4} = 1$ ", 0.45
        new_eq = equation_title(old_eq, new_msg, time)
        
        d0 = Dot(plane.n2p(1 + 0j), color=YELLOW)
        msg0 = "z_0 = 1"
        l0 = MathTex(msg0, font_size=40).next_to(d0, UR, 0.1)
        
        d1 = Dot(plane.n2p(1j), color=YELLOW)
        msg1 = "z_1 = i"
        l1 = MathTex(msg1, font_size=40).next_to(d1, UL, 0.1)

        d2 = Dot(plane.n2p(-1 + 0j), color=YELLOW)
        msg2 = "z_2 = -1"
        l2 = MathTex(msg2, font_size=40).next_to(d2, DL, 0.1)

        d3 = Dot(plane.n2p(-1j), color=YELLOW)
        msg3 = "z_3 = -i"
        l3 = MathTex(msg3, font_size=40).next_to(d3, DR, 0.1)
        
        dots, labs, action = [d0, d1, d2, d3], [l0, l1, l2, l3], 1
        write_dots_labs(dots, labs, action)
        
        unit_square = RegularPolygon(n=4, start_angle=90*DEGREES, color=RED)
        self.wait(0.55)
        self.play(Write(unit_square))
        
        dots, labs, action = [d0, d1, d2, d3], [l0, l1, l2, l3], -1
        write_dots_labs(dots, labs, action)
        self.wait(0.5)
        self.play(Unwrite(unit_square))
        self.wait(0.5)


        old_eq, new_msg, time = new_eq, "$z^{5} = 1$ ", 0.55
        new_eq = equation_title(old_eq, new_msg, time)
        
        d0 = Dot(plane.n2p(1 + 0j), color=YELLOW)
        msg0 = "z_0 = 1"
        l0 = MathTex(msg0, font_size=40).next_to(d0, UR, 0.1)
        
        d1 = Dot(plane.n2p(0.31 + 0.95j), color=YELLOW)
        msg1 = "z_1 = e^{\\dfrac{i2\\pi}{5}}}"
        l1 = MathTex(msg1, font_size=40).next_to(d1, UL, 0.1)

        d2 = Dot(plane.n2p(-0.81 + 0.59j), color=YELLOW)
        msg2 = "z_2 = e^{\\dfrac{i4\\pi}{5}}}"
        l2 = MathTex(msg2, font_size=40).next_to(d2, DL, 0.1)

        d3 = Dot(plane.n2p(-0.81 - 0.59j), color=YELLOW)
        msg3 = "z_3 = e^{\\dfrac{-i4\\pi}{5}}}"
        l3 = MathTex(msg3, font_size=40).next_to(d3, DR, 0.1)

        d4 = Dot(plane.n2p(0.31 - 0.95j), color=YELLOW)
        msg4 = "z_4 = e^{\\dfrac{-i2\\pi}{5}}}"
        l4 = MathTex(msg4, font_size=40).next_to(d4, DR, 0.1)
        
        dots, labs, action = [d0, d1, d2, d3, d4], [l0, l1, l2, l3, l4], 1
        write_dots_labs(dots, labs, action)
        
        pentagon = RegularPolygon(n=5, start_angle=72*DEGREES, color=RED)
        self.wait(0.55)
        self.play(Write(pentagon))
        
        dots, labs, action = [d0, d1, d2, d3, d4], [l0, l1, l2, l3, l4], -1
        write_dots_labs(dots, labs, action)
        self.wait(0.5)
        self.play(Unwrite(pentagon))
        self.wait(0.5)        
        
        disp_sub(self, lang='fr')

        
