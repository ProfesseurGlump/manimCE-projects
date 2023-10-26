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

        d0 = Dot(plane.n2p(1 + 0j), color=YELLOW)
        l0 = MathTex("1").next_to(d0, UR, 0.1)
        
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        l1 = MathTex("2 + i").next_to(d1, UR, 0.1)
        
        d2 = Dot(plane.n2p(2j), color=YELLOW)
        l2 = MathTex("2i").next_to(d2, UR, 0.1)
        
        d3 = Dot(plane.n2p(-1 + 3j), color=YELLOW)
        l3 = MathTex("-1 + 3i").next_to(d3, UL, 0.1)
        
        d4 = Dot(plane.n2p(-3), color=YELLOW)
        l4 = MathTex("-3").next_to(d4, UL, 0.1)
        
        d5 = Dot(plane.n2p(-1 - 1j), color=YELLOW)
        l5 = MathTex("-1 - i").next_to(d5, DL, 0.1)
        
        d6 = Dot(plane.n2p(-3j), color=YELLOW)
        l6 = MathTex("-3i").next_to(d6, DL, 0.1)

        d7 = Dot(plane.n2p(2 - 3j), color=YELLOW)
        l7 = MathTex("2 - 3i").next_to(d7, DR, 0.1)

        dots = [d0, d1, d2, d3, d4, d5, d6, d7]
        for d in dots:
            self.play(Write(d))
            self.wait(0.25)
            
        labels = [l0, l1, l2, l3, l4, l5, l6, l7]
        self.play(*[Write(l) for l in labels])
        self.wait(0.5)

        v0 = Vector([1, 0], color=RED)
        msg0 = "\\lvert 1 \\rvert = 1"
        nl0 = MathTex(msg0, font_size=32.5).next_to(d0, UR, 0.1)
        
        v1 = Vector([2, 1], color=RED)
        msg1 = "\\lvert 2 + i \\rvert = \sqrt{5}"
        nl1 = MathTex(msg1, font_size=32.5).next_to(d1, UR, 0.1)
        
        v2 = Vector([0, 2], color=RED)
        msg2 = "\\lvert 2i \\rvert = 2"
        nl2 = MathTex(msg2, font_size=32.5).next_to(d2, UR, 0.1)

        v3 = Vector([-1, 3], color=RED)
        msg3 = "\\lvert -1 + 3i \\rvert = \sqrt{10}"
        nl3 = MathTex(msg3, font_size=32.5).next_to(d3, UL, 0.1)

        v4 = Vector([-3, 0], color=RED)
        msg4 = "\\lvert -3 \\rvert = 3"
        nl4 = MathTex(msg4, font_size=32.5).next_to(d4, UL, 0.1)

        v5 = Vector([-1, -1], color=RED)
        msg5 = "\\lvert -1 - i \\rvert = \sqrt{2}"
        nl5 = MathTex(msg5, font_size=32.5).next_to(d5, DL, 0.1)

        v6 = Vector([0, -3], color=RED)
        msg6 = "\\lvert -3i \\rvert = 3"
        nl6 = MathTex(msg6, font_size=32.5).next_to(d6, DL, 0.1)

        v7 = Vector([2, -3], color=RED)
        msg7 = "\\lvert 2 - 3i \\rvert = \sqrt{13}"
        nl7 = MathTex(msg7, font_size=32.5).next_to(d7, DR, 0.1)

        vectors = [v0, v1, v2, v3, v4, v5, v6, v7]
        new_labels = [nl0, nl1, nl2, nl3, nl4, nl5, nl6, nl7]
        self.play(*[Write(v) for v in vectors])
        self.wait(0.5)
        
        for i in range(len(new_labels)):
            self.play(ReplacementTransform(labels[i], new_labels[i]))
        self.wait()
        
        disp_sub(self, lang='fr')

        
