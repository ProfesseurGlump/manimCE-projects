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

    

class ComplexNumbers(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Nombres complexes "
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

        d0 = Dot(plane.n2p(2 + 0j), color=YELLOW)
        msg0 = "z_0 = 2"
        l0 = MathTex(msg0, font_size=25).next_to(d0, UR, 0.1)
        v0 = Vector([2, 0], color=RED)
        
        d1 = Dot(plane.n2p(1j), color=YELLOW)
        msg1 = "z_1 = i"
        l1 = MathTex(msg1, font_size=25).next_to(d1, UR, 0.1)
        v1 = Vector([0, 1], color=GREEN)

        d2 = Dot(plane.n2p(2+1j), color=YELLOW)
        msg2 = "z_2 = z_0 + z_1"
        l2 = MathTex(msg2, font_size=25).next_to(d2, UR, 0.1)
        v2 = Vector([2, 1], color=PINK)
        
        dots, labels, vectors = [d0, d1, d2], [l0, l1, l2], [v0, v1, v2]

        def write_dot_lab_vect(dots, labels, vectors):
            for i in range(len(dots)):
                self.play(Write(dots[i]))
                self.wait(0.2)
                self.play(Write(labels[i]))
                self.wait(0.2)
                self.play(Write(vectors[i]))
                self.wait(0.2)

        write_dot_lab_vect(dots, labels, vectors)

        msg2 = "z_2 = 2 + i"
        eval_l2 = MathTex(msg2, font_size=25).next_to(d2, UR, 0.1)
        self.play(ReplacementTransform(l2, eval_l2))
        self.wait(0.2)

        msg0_bar = "\\overline{z_0} = 2 = z_0"
        l0_bar = MathTex(msg0_bar, font_size=25).next_to(d0, UR, 0.1)
        self.play(ReplacementTransform(l0, l0_bar))
        self.wait(0.2)
        
        d1_bar = Dot(plane.n2p(-1j), color=YELLOW)
        msg1_bar = "\overline{z_1} = -i"
        l1_bar = MathTex(msg1_bar, font_size=25).next_to(d1_bar, DR, 0.1)
        v1_bar = Vector([0, -1], color=GREEN)

        d2_bar = Dot(plane.n2p(2-1j), color=YELLOW)
        msg2_bar = "\\overline{z_2} = \\overline{z_0 + z_1}"
        l2_bar = MathTex(msg2_bar, font_size=25).next_to(d2_bar, DR, 0.1)
        v2_bar = Vector([2, -1], color=PINK)
        
        dots, labels = [d1_bar, d2_bar], [l1_bar, l2_bar]
        vectors = [v1_bar, v2_bar]

        write_dot_lab_vect(dots, labels, vectors)

        msg2_bar = "\\overline{z_2} = \\overline{z_0} + \\overline{z_1}"
        conj_l2 = MathTex(msg2_bar, font_size=25).next_to(d2_bar, DR, 0.1)
        self.play(ReplacementTransform(l2_bar, conj_l2))
        self.wait(0.25)

        msg2_bar = "\\overline{z_2} = 2 - i"
        eval_conj_l2 = MathTex(msg2_bar, font_size=25).next_to(d2_bar, DR, 0.1)
        self.play(ReplacementTransform(conj_l2, eval_conj_l2))
        self.wait(0.25)


        d3 = Dot(plane.n2p(2j), color=YELLOW)
        msg3 = "z_3 = z_0z_1"
        l3 = MathTex(msg3, font_size=25).next_to(d3, UR, 0.1)
        v3 = Vector([0, 2], color=RED)

        d4 = Dot(plane.n2p(-1+0j), color=YELLOW)
        msg4 = "z_4 = (z_1)^2"
        l4 = MathTex(msg4, font_size=25).next_to(d4, UL, 0.1)
        v4 = Vector([-1, 0], color=GREEN)

        d5 = Dot(plane.n2p(-1+2j), color=YELLOW)
        msg5 = "z_5 = z_2z_1"
        l5 = MathTex(msg5, font_size=25).next_to(d5, UL, 0.1)
        v5 = Vector([-1, 2], color=BLUE)

        d6 = Dot(plane.n2p(1+2j), color=YELLOW)
        msg6 = "z_6 = \\overline{z_2}z_1"
        l6 = MathTex(msg6, font_size=25).next_to(d6, DR, 0.1)
        v6 = Vector([1, 2], color=BLUE)

        dots, labels = [d3, d4, d5, d6], [l3, l4, l5, l6]
        vectors = [v3, v4, v5, v6]

        write_dot_lab_vect(dots, labels, vectors)

        eval_z_3 = "z_3 = 2i"
        eval_l3 = MathTex(eval_z_3, font_size=25).next_to(d3, UR, 0.1)
        self.play(ReplacementTransform(l3, eval_l3))
        self.wait(0.2)

        eval_z_4 = "z_4 = i^2"
        eval_l4 = MathTex(eval_z_4, font_size=25).next_to(d4, UL, 0.1)
        self.play(ReplacementTransform(l4, eval_l4))
        self.wait(0.2)

        eval_z_5 = "z_5 = i(2 + i)"
        eval_l5 = MathTex(eval_z_5, font_size=25).next_to(d5, UL, 0.1)
        self.play(ReplacementTransform(l5, eval_l5))
        self.wait(0.2)

        eval_z_6 = "z_6 = i(2-i)"
        eval_l6 = MathTex(eval_z_6, font_size=25).next_to(d6, DR, 0.1)
        self.play(ReplacementTransform(l6, eval_l6))
        self.wait(0.2)


        eval_z_4_2 = "z_4 = -1"
        eval_l4_2 = MathTex(eval_z_4_2, font_size=25).next_to(d4, UL, 0.1)
        self.play(ReplacementTransform(eval_l4, eval_l4_2))
        self.wait(0.2)

        eval_z_5_2 = "z_5 = -1 + 2i"
        eval_l5_2 = MathTex(eval_z_5_2, font_size=25).next_to(d5, UL, 0.1)
        self.play(ReplacementTransform(eval_l5, eval_l5_2))
        self.wait(0.2)

        eval_z_6_2 = "z_6 = 1 + 2i"
        eval_l6_2 = MathTex(eval_z_6_2, font_size=25).next_to(d6, DR, 0.1)
        self.play(ReplacementTransform(eval_l6, eval_l6_2))
        self.wait(0.2)

        
        disp_sub(self, lang='fr')

        
