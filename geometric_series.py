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


class GeometricSeries(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Suite géométrique avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        plane = ComplexPlane().add_coordinates()
        # self.play(Write(plane))
        # self.wait()
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment démontrer "
        inbox2 = "géométriquement pourquoi les suites "
        inbox3 = "géométriques sont géométriques ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(2.5)

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_question,
                title_clap.scale(0.75)
            )
        )
        self.wait()

        title_rep = Title("Regardez jusqu'au bout pour la réponse")
        self.play(
            ReplacementTransform(
                title_clap,
                title_rep.scale(0.75)
            ),
            FadeOut(msg)
        )
        self.wait()

        # STEP 1: create dots for the main triangle
        z_A = Dot(plane.n2p(-2 - 0j), color=YELLOW)
        A = [-2, 0, 0]
        self.play(Write(z_A))
        self.wait()
        
        z_B = Dot(plane.n2p(-1 + 0j), color=YELLOW)
        B = [-1, 0, 0]
        self.play(Write(z_B))
        self.wait()
        AB = Line(z_A.get_center(), z_B.get_center())
        AB_brace = Brace(AB)
        AB_text = BraceLabel(AB, r"1")
        self.play(
            Write(AB),
            Write(AB_brace),
            Write(AB_text)
        )
        self.wait()
        
        z_C = Dot(plane.n2p(-1 + 2j), color=YELLOW)
        C = [-1, 2, 0]
        BC = Line(z_B.get_center(), z_C.get_center())
        BC_brace = BraceBetweenPoints(B, C)
        BC_text = MathTex(r"a")
        self.play(
            Write(BC),
            Write(z_C),
            Write(BC_brace),
            Write(BC_text.next_to(BC_brace, RIGHT))
        )
        self.wait()

        AC = Line(z_C.get_center(), z_A.get_center())
        AC_brace = BraceBetweenPoints(C, A)
        AC_text = MathTex(r"\sqrt{1 + a^2}")
        self.play(
            Write(AC),
            Write(AC_brace),
            Write(AC_text.next_to(AC_brace, 0.05 * UL))
        )
        self.wait()
        
        z_D = Dot(plane.n2p(0.5 + 0j), color=YELLOW)
        D = [0.5, 0, 0]
        BC_copy1 = Line(z_B.get_center(), z_C.get_center())
        AD = Line(z_A.get_center(), z_D.get_center())
        self.play(
            ReplacementTransform(BC_copy1, AD),
            Write(z_D)
        )
        self.wait()
        
        z_E = Dot(plane.n2p(3 + 0j), color=YELLOW)
        E = [3, 0, 0]
        DE = Line(z_D.get_center(), z_E.get_center())
        BC_copy2 = Line(z_B.get_center(), z_C.get_center())
        BE_brace = BraceBetweenPoints(B, E)
        BE_text = MathTex(r"x")
        self.play(
            ReplacementTransform(BC_copy2, DE),
            Write(z_E),
            Write(BE_brace),
            Write(BE_text.next_to(BE_brace, DOWN))
        )
        self.wait()

        CE = Line(z_E.get_center(), z_C.get_center())
        CE_brace = BraceBetweenPoints(E, C)
        CE_text = MathTex(r"\sqrt{a^2 + x^2")
        self.play(
            Write(CE),
            Write(CE_brace),
            Write(CE_text.next_to(CE_brace, 0.05 * UP))
        )
        self.wait()
        
        main_triangle_affixes = [z_A, z_E, z_C]
        left_triangle_affixes = [z_A, z_B, z_C]
        right_triangle_affixes = [z_B, z_E, z_C]
        

        # STEP 2: create the main triangles
        ABC = Polygon(*[A, B, C], color=BLUE)
        BEC = Polygon(*[B, E, C], color=WHITE)
        AEC = Polygon(*[A, E, C], color=RED)

        big_hyp1 = MathTex(r"(1 + x)^2 = 1 + a^2 + a^2 + x^2")
        big_hyp2 = MathTex(r"1 + 2x + x^2 = 1 + 2a^2 + x^2")
        big_hyp3 = MathTex(r"x  = a^2")
        self.play(
            Write(big_hyp1.next_to(BE_text, DOWN))
        )
        self.wait(2)
        self.play(
            ReplacementTransform(big_hyp1, big_hyp2.next_to(BE_text, DOWN))
        )
        self.wait(2)
        self.play(
            ReplacementTransform(big_hyp2, big_hyp3.next_to(BE_text, DOWN))
        )
        self.wait(2)
        new_BE_text = MathTex(r"a^2")
        new_CE_text = MathTex(r"\sqrt{a^2 + a^4}")
        old  = [BE_text, big_hyp3, CE_text]
        new = [
            new_BE_text.next_to(BE_brace, DOWN),
            new_BE_text.next_to(BE_brace, DOWN),
            new_CE_text.next_to(CE_brace, 0.05 * UP)
        ]
        
        self.play(
            *[ReplacementTransform(old[i], new[i]) for i in range(len(old))]
        )
        self.wait(1)

        new_CE_texts = [r"\sqrt{a^2(1 + a^2)}", r"a\sqrt{1 + a^2}"]
        n = [MathTex(t) for t in new_CE_texts]
        o = [new[-1], n[0]]
        self.play(
            *[ReplacementTransform(
                o[i],
                n[i].next_to(CE_brace, 0.05 * UP)
            ) for i in range(len(o))]
        )
        self.wait(2)
        
        # everything = [
        #     z_A, z_B, z_C, z_D, z_E,
        #     AB, BC, AC, AD, DE, CE,
        #     AB_brace, BC_brace, AC_brace, BE_brace, CE_brace,
        #     AB_text, BC_text, AC_text, BE_text, CE_text,
        #     n[0], n[1], o[0], o[1]
        # ]
        # self.play(
        #     *[FadeOut(e) for e in everything]
        # )
        # self.wait(0.25)

        # z_F = Dot(plane.n2p(-1 - 4j), color=YELLOW)
        # F = [-1, -4, 0]
        # BF = Line(z_B.get_center(), z_F.get_center())
        # BF_brace = BraceBetweenPoints(B, F)
        # BF_text = MathTex(r"a^2")
        # AF = Line(z_A.get_center(), z_F.get_center())
        # AF_brace = Brace(AF)
        # AF_text = MathTex(r"\sqrt{1 + a^4}")
        # F_built = [
        #     z_F,
        #     BF,
        #     BF_brace,
        #     BF_text.next_to(BF_brace, UP),
        #     AF,
        #     AF_brace,
        #     AF_text.next_to(AF_brace, UP),
        # ]
        # self.play(
        #     *[f.animate.rotate(PI/2) for f in F_built]
        # )
        # self.wait()
        
        # z_A = Dot(plane.n2p(0 - 6j), color=YELLOW)
        # A = [0, -6, 0]
        # z_B = Dot(plane.n2p(0 - 5j), color=YELLOW)
        # B = [0, -5, 0]
        # z_C = Dot(plane.n2p(-2 - 5j), color=YELLOW)
        # C = [-2, -5, 0]
        # z_D = Dot(plane.n2p(0 - 1j), color=YELLOW)
        # D = [0, -1, 0]
        # z_E = Dot(plane.n2p(4 - 5j), color=YELLOW)
        # E = [4, -5, 0]
        # z_F = Dot(plane.n2p(0 + 11j), color=YELLOW)
        # F = [0, 11, 0]

        # ABC = Polygon(*[A, B, C])
        # BDC = Polygon(*[B, D, C])
        # AEB = Polygon(*[A, E, B])
        # BEF = Polygon(*[B, E, F])

        # everything = [
        #     z_A, z_B, z_C, z_D, z_E, z_F,
        #     ABC, BDC, AEB, BEF
        # ]
        # self.play(
        #     *[Write(e) for e in everything]
        # )
        # self.wait()
        
        # BF = Line(z_B.get_center(), z_F.get_center())
        # BF_brace = Brace(BF)
        # BF_text = MathTex(r"x")
        # EF = Line(z_E.get_center(), z_F.get_center())
        # EF_brace = Brace(EF)
        # EF_text = MathTex(r"\sqrt{a^4 + x^2}")
        # AF_brace = BraceBetweenPoints(A, F)
        # AF_text = MathTex(r"1 + a^4 + a^4 + x^2 = 1 + 2x + x^2")
        # F_built = [
        #     BF,
        #     BF_brace,
        #     BF_text.next_to(BF_brace, UP),
        #     EF,
        #     EF_brace,
        #     EF_text.next_to(EF_brace, DOWN),
        #     AF_brace,
        #     AF_text.next_to(AF_brace, 2 * UP)
        # ]
        # self.play(
        #     *[Write(g) for g in F_built]
        # )
        # self.wait()
        # AF_text2 = MathTex(r"2a^4 = 2x")
        # self.play(
        #     ReplacementTransform(
        #         AF_text,
        #         AF_text2.next_to(AF_brace, 2 * UP)
        #     )
        # )
        # self.wait()
        # AF_text3 = MathTex(r"a^4 = x")
        # self.play(
        #     ReplacementTransform(
        #         AF_text2,
        #         AF_text3.next_to(AF_brace, 2 * UP)
        #     )
        # )
        # self.wait()
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait()
        
        disp_sub(self, lang='fr')
