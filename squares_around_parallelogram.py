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


class AlfinioFlores(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Un pavage d'Alfinio Flores avec "
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
        inbox2 = "géométriquement le théorème "
        inbox3 = "d'Alfinio Flores ?"
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

        # STEP 1: create dots for the main parallelogram
        z_A = Dot(plane.n2p(-1 - 0j), color=YELLOW)
        z_B = Dot(plane.n2p(1 + 0j), color=YELLOW)
        z_C = Dot(plane.n2p(2 + 1j), color=YELLOW)
        z_D = Dot(plane.n2p(0 + 1j), color=YELLOW)
        main_parallelogram_affixes = [z_A, z_B, z_C, z_D]
        self.play(*[Write(z) for z in main_parallelogram_affixes])
        self.wait()

        # STEP 2: create the main parallelogram 
        A, B = [-1, 0, 0], [1, 0, 0]
        C, D = [2, 1, 0], [0, 1, 0]
        main_parallelogram_vertices = [A, B, C, D]
        ABCD = Polygon(*main_parallelogram_vertices, color=RED)
        self.play(
            Write(ABCD),
        )
        self.wait()

        # STEP 3: fill it
        self.play(
            ABCD.animate.set_fill(RED, 0.8)
        )
        self.wait()

        
        # STEP 4: create dots and squares
        z_G = Dot(plane.n2p(2 - 1j), color=YELLOW)
        z_H = Dot(plane.n2p(3 + 0j), color=YELLOW)
        right_square_affixes = [z_G, z_H]
        G, H = [2, -1, 0], [3, 0, 0]
        
        z_I = Dot(plane.n2p(2 + 3j), color=YELLOW)
        z_J = Dot(plane.n2p(0 + 3j), color=YELLOW)
        up_square_affixes = [z_I, z_J]
        I, J = [2, 3, 0], [0, 3, 0]

        z_K = Dot(plane.n2p(-1 + 2j), color=YELLOW)
        z_L = Dot(plane.n2p(-2 + 1j), color=YELLOW)
        left_square_affixes = [z_K, z_L]
        K, L = [-1, 2, 0], [-2, 1, 0]

        z_E = Dot(plane.n2p(-1 - 2j), color=YELLOW)
        z_F = Dot(plane.n2p(1 - 2j), color=YELLOW)
        down_square_affixes = [z_F, z_E]
        E, F = [-1, -2, 0], [1, -2, 0]

        squares_affixes = down_square_affixes + right_square_affixes
        squares_affixes += up_square_affixes + left_square_affixes
        self.play(*[Write(z) for z in squares_affixes])
        self.wait()        

        BGHC = Polygon(*[B, G, H, C], color=GREEN)
        CIJD = Polygon(*[C, I, J, D], color=GREEN)
        DKLA = Polygon(*[D, K, L, A], color=GREEN)
        ABFE = Polygon(*[A, B, F, E], color=GREEN)
        squares = [BGHC, CIJD, DKLA, ABFE]
        
        self.play(*[Write(s) for s in squares])
        self.wait()
        
        # STEP 5: create squares centers
        z_M = Dot(plane.n2p(0 - 1j), color=YELLOW)
        z_N = Dot(plane.n2p(2 - 0j), color=YELLOW)
        z_O = Dot(plane.n2p(1 + 2j), color=YELLOW)
        z_P = Dot(plane.n2p(-1 + 1j), color=YELLOW)

        center_affixes = [z_M, z_N, z_O, z_P]
        M, N = [0, -1, 0], [2, 0, 0]
        O, P = [1, 2, 0], [-1, 1, 0]
        center_vertices = [M, N, O, P]
        square_centers = Polygon(*center_vertices, color=BLUE)

        self.play(
            *[Write(z) for z in center_affixes],
        )
        self.wait()

        self.play(Write(square_centers))
        self.wait()
        
        inbox1 = "Les centres des carrés construits"
        inbox2 = "extérieurement sur les côtés d'un"
        inbox3 = "parallélogramme forment un carré."
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        
        self.play(
            Write(msg.next_to(title_rep, 2 * DOWN))
        )
        self.wait(5)

        
        

        inbox1 = "On a bien démontré le théorème"
        inbox2 = "d'Alfinio Flores"
        inboxes = [inbox1, inbox2]
        msg_end = inbox_msg(*inboxes, font_size=40)


        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(msg, msg_end.next_to(ABFE, 2 * DOWN)),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait()
        
        disp_sub(self, lang='fr')
