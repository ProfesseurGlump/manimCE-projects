from manim import *
import manim
from math import e, pi
import math

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
    self.wait(.5)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.wait(.5)

    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(.5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(.5)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 3))
    self.wait(.5)
        
    self.play(ReplacementTransform(part, full), run_time=3)
    self.wait(.5)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)


    
def inbox_msg(*inboxes, font_size):
    msg_text = ""
    for inbox in inboxes:
        msg_text += r"\mbox{" + f"{inbox}" + r"} \\"
    msg = MathTex(
        msg_text,
        tex_template=TexFontTemplates.french_cursive,
        font_size=font_size
    )
    return msg


def get_regular_polygon(n_gon):
    angle = (360 / n_gon) * DEGREES
    poly_n_gon = RegularPolygon(
        n = n_gon,
        start_angle = angle,
        color = RED
    )
    return poly_n_gon    


class Id1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Identité remarquable "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        plane = ComplexPlane()
        self.play(Write(plane))
        self.wait()

        z_A = Dot(plane.n2p(-2 - 2j), color=YELLOW)
        z_B = Dot(plane.n2p(2 - 2j), color=YELLOW)
        z_C = Dot(plane.n2p(2 + 2j), color=YELLOW)
        z_D = Dot(plane.n2p(-2 + 2j), color=YELLOW)
        main_square_affixes = [z_A, z_B, z_C, z_D]
        self.play(*[Write(z) for z in main_square_affixes])
        self.wait()

        
        # reg_square = get_regular_polygon(n_gon=4)
        # scale_fact = 1
        # self.play(Write(reg_square.scale(scale_fact)))
        # self.wait()
        
        A, B = [-2, -2, 0], [2, -2, 0]
        C, D = [2, 2, 0], [-2, 2, 0]
        main_square_vertices = [A, B, C, D]
        ABCD = Polygon(*main_square_vertices, color=GREEN)
        self.play(Write(ABCD))
        self.wait()
        
        self.play(
            ABCD.animate.set_fill(GREEN, 0.8)
        )
        self.wait()

        AB = Line(z_A.get_center(), z_B.get_center())
        AB_brace = Brace(AB)
        AB_txt = AB_brace.get_text("a")
        #AB_txt = BraceLabel(AB_brace, "a", color=GREEN)

        AD = plane.get_vertical_line(D)
        AD_brace = BraceBetweenPoints(D, A)
        AD_txt = AD_brace.get_text("a")
        #AD_txt = BraceLabel(AD_brace, "a", color=GREEN)

        braces = [AB_brace, AD_brace]
        txts = [AB_txt, AD_txt]
        self.play(
            *[Write(b, color=GREEN) for b in braces],
            *[Write(t, color=GREEN) for t in txts]
        )
        self.wait()
        
        z_E = Dot(plane.n2p(1 + 2j), color=YELLOW)
        z_F = Dot(plane.n2p(1 + 1j), color=YELLOW)
        z_G = Dot(plane.n2p(2 + 1j), color=YELLOW)
        small_square_affixes = [z_E, z_F, z_G]
        self.play(*[Write(z) for z in small_square_affixes])
        self.wait()

        
        E, F, G = [1, 2, 0], [1, 1, 0], [2, 1, 0]
        #CE = Line(z_E.get_center(), z_C.get_center())
        CE_brace = BraceBetweenPoints(C, E)
        CE_txt = CE_brace.get_text("b")
        self.play(
            Write(CE_brace),
            Write(CE_txt)
        )
        self.wait()
        
        small_square_vertices = [C, E, F, G]
        CEFG = Polygon(*small_square_vertices, color=RED, fill_color=RED)
        self.play(Write(CEFG))
        self.wait()

        self.play(CEFG.animate.set_fill(RED, 0.8))
        self.wait()

        z_H = Dot(plane.n2p(1 - 2j), color=YELLOW)
        self.play(Write(z_H))
        self.wait()

        H = [1, -2, 0]
        left_rectangle_vertices = [A, H, E, D]
        AHED = Polygon(*left_rectangle_vertices, color=BLUE)
        right_rectangle_vertices = [B, G, F, H]
        BGFH = Polygon(*right_rectangle_vertices, color=WHITE)
        self.play(
            *[Write(r) for r in [AHED, BGFH]],
            *[r.animate.set_fill(YELLOW, 0.8) for r in [AHED, BGFH]],
        )
        self.wait()
        
        self.play(
            AHED.animate.set_fill(BLUE, 0.8),
            BGFH.animate.set_fill(WHITE, 0.8)
        )
        self.wait()


        self.play(
            AHED.animate.shift(UP + 2 * LEFT),
            CEFG.animate.shift(UR),
            BGFH.animate.shift(DOWN).rotate(PI / 2)
        )
        self.wait()

        fades_out = [
            ABCD, CEFG,
            z_A, z_B, z_C, z_D,
            z_E, z_F, z_G, z_H,
            AD_brace, AB_brace, CE_brace,
            AD_txt, AB_txt, CE_txt
        ]
        self.play(
            *[FadeOut(f) for f in fades_out],
            BGFH.animate.shift(4 * LEFT)
        )
        self.wait()

        
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_start,
                title_end.scale(0.75)
            )
        )
        
        disp_sub(self, lang='fr')
