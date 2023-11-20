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
        msg = "Identité remarquable avec "
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
        inbox1 = "Savez-vous comment montrer "
        inbox2 = "géométriquement la troisième "
        inbox3 = "identité remarquable ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
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

        z_E = Dot(plane.n2p(1 + 2j), color=YELLOW)
        z_F = Dot(plane.n2p(1 + 1j), color=YELLOW)
        z_G = Dot(plane.n2p(2 + 1j), color=YELLOW)
        small_square_affixes = [z_E, z_F, z_G]
        self.play(*[Write(z) for z in small_square_affixes])
        self.wait()        
        
        E, F, G = [1, 2, 0], [1, 1, 0], [2, 1, 0]
        small_square_vertices = [C, E, F, G]
        CEFG = Polygon(*small_square_vertices, color=RED, fill_color=RED)
        self.play(Write(CEFG))
        self.wait()

        self.play(CEFG.animate.set_fill(RED, 0.8))
        self.wait()
        
        AB = Line(z_A.get_center(), z_B.get_center())
        AB_brace = Brace(AB)
        AB_txt = AB_brace.get_tex("a")
        #AB_txt = BraceLabel(AB_brace, "a", color=GREEN)

        BG_brace = BraceBetweenPoints(B, G)
        BG_txt = BG_brace.get_tex(r"a - b")

        GC_brace = BraceBetweenPoints(G, C)
        GC_txt = GC_brace.get_tex("b")

        # CE = Line(z_C.get_center(), z_E.get_center())
        # CE_brace = Brace(CE)
        CE_brace = BraceBetweenPoints(C, E)
        CE_txt = CE_brace.get_tex("b")
        
        # ED = Line(z_E.get_center(), z_D.get_center())
        # ED_brace = Brace(ED)
        ED_brace = BraceBetweenPoints(E, D)
        ED_txt = ED_brace.get_tex("a - b")
        
        # AD = plane.get_vertical_line(D)
        DA_brace = BraceBetweenPoints(D, A)
        DA_txt = DA_brace.get_tex("a")
        #AD_txt = BraceLabel(AD_brace, "a", color=GREEN)

        braces = [
            AB_brace, # GREEN
            BG_brace, # WHITE
            GC_brace, # RED
            CE_brace, # RED
            ED_brace, # WHITE
            DA_brace  # GREEN
        ]
        txts = [
            AB_txt, # GREEN
            BG_txt, # WHITE
            GC_txt, # RED
            CE_txt, # RED 
            ED_txt, # WHITE
            DA_txt  # GREEN
        ]

        colors = ["GREEN", "WHITE", "RED", "RED", "WHITE", "GREEN"]
        
        self.play(
            *[Write(braces[i], color=colors[i]) for i in range(len(braces))],
            *[Write(txts[i], color=colors[i]) for i in range(len(txts))],
        )
        self.wait()
        
        # #CE = Line(z_E.get_center(), z_C.get_center())
        # CE_brace = BraceBetweenPoints(C, E)
        # CE_txt = CE_brace.get_tex("b")
        # self.play(
        #     Write(CE_brace),
        #     Write(CE_txt)
        # )
        # self.wait()
        

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

        move_up_2_right = [
            ABCD, CEFG,
            z_A, z_B, z_C, z_D,
            z_E, z_F, z_G, z_H,
            *braces,
            *txts
        ]
        
        self.play(
            AHED.animate.shift(UP + 2 * LEFT),
            *[m.animate.shift(UP + 2 * RIGHT) for m in move_up_2_right],
            BGFH.animate.shift(DOWN).rotate(PI / 2).shift(4 * LEFT),
        )
        self.wait()

        z_Dp = Dot(plane.n2p(-4 + 3j), color=YELLOW)
        z_Ap = Dot(plane.n2p(-4 - 1j), color=YELLOW)
        z_Hpl = Dot(plane.n2p(-1 - 1j), color=YELLOW)
        z_Ep = Dot(plane.n2p(-1 + 3j), color=YELLOW)
        
        z_Gp = Dot(plane.n2p(-4 - 1j), color=YELLOW)
        z_Fp = Dot(plane.n2p(-4 - 2j), color=YELLOW)
        z_Hpr = Dot(plane.n2p(-1 - 2j), color=YELLOW)
        z_Bp = Dot(plane.n2p(-1 - 1j), color=YELLOW)

        dots_p = [z_Dp, z_Ap, z_Hpl, z_Ep, z_Fp, z_Hpr]

        A_p, Hpl = [-4, -1, 0], [-1, -2, 0]
        Ep, Dp = [-1, 3, 0], [-4, 3, 0]

        new_A, new_H = [0, -1, 0], [3, -1, 0]
        new_E, new_D = [3, 3, 0], [0, 3, 0]
        new_AHED_list = [new_A, new_H, new_E, new_D]
        new_AHED = Polygon(*new_AHED_list, color=BLUE)

        Bp, Gp, Fp = [-1, -1, 0], [-4, -1, 0], [-4, -2, 0]

        new_B, new_G, new_F = [4, -1, 0], [4, 2, 0], [3, 2, 0]
        new_BGFH_list = [new_B, new_G, new_F, new_H]
        new_BGFH = Polygon(*new_BGFH_list, color=WHITE)

        #new_FH = Line(z_Fp.get_center(), z_Hpr.get_center())
        #new_FH_brace = Brace(new_FH)
        FHp_brace = BraceBetweenPoints(Fp, Hpl)
        FHp_txt = FHp_brace.get_tex("a - b")

        #new_EH = Line(z_Ep.get_center(), z_Hpr.get_center())
        EHpl_brace = BraceBetweenPoints(Hpl, Ep)
        #new_EH_brace = Brace(new_EH)
        EHpl_txt = EHpl_brace.get_tex("a + b")
        
        self.play(
            *[Write(d) for d in dots_p],
            new_AHED.animate.set_fill(BLUE, 0.8),
            new_BGFH.animate.set_fill(WHITE, 0.8),
            Write(FHp_brace),
            Write(FHp_txt),
            ReplacementTransform(DA_brace, EHpl_brace),
            ReplacementTransform(DA_txt, EHpl_txt),
            FadeOut(ABCD),
            FadeOut(CEFG),
            FadeOut(z_C)
        )
        self.wait()

        inbox1 = "On a bien l'identité remarquable"
        inbox2 = r"(a + b)(a - b) = a^2 - b^2"
        msg_text = r"\mbox{" + f"{inbox1}" + r"}\\"
        msg_text += f"{inbox2}"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )

        colors = [GREEN, WHITE, RED, RED, WHITE, GREEN]
        full_braces = braces + [FHp_brace, EHpl_brace]
        full_colors = colors + [WHITE, ORANGE]
        full_txts = txts + [FHp_txt, EHpl_txt]
        to_replace = full_braces + full_txts
        n = len(full_braces)
        self.play(
            Write(msg.next_to(title_rep, 3*DOWN)),
            *[
                full_braces[i]
                .animate
                .set_color(full_colors[i]) for i in range(n)
            ],
            *[
                full_txts[i]
                .animate
                .set_color(full_colors[i]) for i in range(n)
            ]
        )
        self.wait(3)

        identity = r"(a - b)(a + b) = a^2 - b^2"
        amb = MathTex(identity)
        self.play(
            *[ReplacementTransform(r, amb) for r in to_replace],
        )        
        self.wait()

        self.play(amb.animate.shift(5 * DOWN))
        self.wait()
        
        boxed_res = SurroundingRectangle(amb)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
            Write(boxed_res)
        )
        self.wait()
        
        disp_sub(self, lang='fr')
