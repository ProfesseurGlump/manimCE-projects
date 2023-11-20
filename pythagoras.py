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


class Pythagoras1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Démo de Zhoubi Suanjing avec "
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
        inbox3 = "de Pythagore façon Zhou Suanjing ?"
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

        # STEP 1: create dots for the main square
        z_A = Dot(plane.n2p(-2 - 2j), color=YELLOW)
        z_B = Dot(plane.n2p(2 - 2j), color=YELLOW)
        z_C = Dot(plane.n2p(2 + 2j), color=YELLOW)
        z_D = Dot(plane.n2p(-2 + 2j), color=YELLOW)
        main_square_affixes = [z_A, z_B, z_C, z_D]
        self.play(*[Write(z) for z in main_square_affixes])
        self.wait()

        # STEP 2: create the main square 
        A, B = [-2, -2, 0], [2, -2, 0]
        C, D = [2, 2, 0], [-2, 2, 0]
        main_square_vertices = [A, B, C, D]
        ABCD = Polygon(*main_square_vertices, color=GREEN)
        self.play(
            Write(ABCD),
        )
        self.wait()

        # STEP 3: fill it
        self.play(
            ABCD.animate.set_fill(GREEN, 0.8)
        )
        self.wait()

        
        # STEP 4: create dots and triangles
        z_E = Dot(plane.n2p(1 - 2j), color=YELLOW)
        z_F = Dot(plane.n2p(1 - 1j), color=YELLOW)
        z_G = Dot(plane.n2p(-2 - 1j), color=YELLOW)
        left_triangles_affixes = [z_E, z_F, z_G]
        
        z_H = Dot(plane.n2p(2 - 1j), color=YELLOW)
        z_I = Dot(plane.n2p(1 + 2j), color=YELLOW)
        right_triangles_affixes = [z_H, z_I]

        triangles_affixes = left_triangles_affixes + right_triangles_affixes
        self.play(*[Write(z) for z in triangles_affixes])
        self.wait()        
        
        E, F, G = [1, -2, 0], [1, -1, 0], [-2, -1, 0]
        H, I = [2, -1, 0], [1, 2, 0]

        left_down_triangle_vertices = [E, G, A]
        EGA = Polygon(
            *left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        EGA_copy = Polygon(
            *left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        left_up_triangle_vertices = [E, F, G]
        EFG = Polygon(
            *left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        EFG_copy = Polygon(
            *left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        right_down_triangle_vertices = [F, H, C]
        FHC = Polygon(
            *right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        FHC_copy = Polygon(
            *right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        right_up_triangle_vertices = [C, I, F]
        CIF = Polygon(
            *right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        CIF_copy = Polygon(
            *right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        triangles = [EGA, EFG, FHC, CIF]
        triangles_copy = [EGA_copy, EFG_copy, FHC_copy, CIF_copy]
        
        self.play(
            *[Write(t) for t in triangles],
            *[t.animate.set_fill(RED, 0.8) for t in triangles],
        )
        self.wait()

        
        # STEP 5: open and expand triangles
        
        self.play(
            CIF.animate.shift(3 * LEFT),
            *[z.animate.shift(3 * LEFT) for z in [z_C, z_I]],
            FadeOut(z_F),
            FHC.animate.shift(DOWN),
            *[z.animate.shift(DOWN) for z in [z_C, z_H]],
            EFG.animate.shift(3 * UP + RIGHT),
            *[z.animate.shift(3 * UP + RIGHT) for z in [z_E, z_G]],
        )
        self.wait()

        
        # STEP 6: move back
        
        self.play(
            CIF.animate.shift(3 * RIGHT),
            *[z.animate.shift(3 * RIGHT) for z in [z_C, z_I]],
            FadeIn(z_F),
            FHC.animate.shift(UP),
            *[z.animate.shift(UP) for z in [z_C, z_H]],
            EFG.animate.shift(3 * DOWN + LEFT),
            *[z.animate.shift(3 * DOWN + LEFT) for z in [z_E, z_G]],
        )
        self.wait()

        # STEP 7: new configuration with different triangle sizes

        move_z_EFI = [z_E, z_F, z_I]
        new_E, new_F, new_I = [-1, -2, 0], [-1, -1, 0], [-1, 2, 0]

        new_left_down_triangle_vertices = [new_E, G, A]
        new_EGA = Polygon(
            *new_left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        new_EGA_copy = Polygon(
            *new_left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        new_left_up_triangle_vertices = [new_E, new_F, G]
        new_EFG = Polygon(
            *new_left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        new_EFG_copy = Polygon(
            *new_left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        new_right_down_triangle_vertices = [new_F, H, C]
        new_FHC = Polygon(
            *new_right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        new_FHC_copy = Polygon(
            *new_right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        new_right_up_triangle_vertices = [C, new_I, new_F]
        new_CIF = Polygon(
            *new_right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        new_CIF_copy = Polygon(
            *new_right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        new_triangles = [new_EGA, new_EFG, new_FHC, new_CIF]
        new_triangles_copy = [new_EGA_copy, new_EFG_copy, new_FHC_copy, new_CIF_copy]
        n = len(new_triangles)
        
        self.play(
            *[m.animate.shift(2 * LEFT) for m in move_z_EFI],
            *[
                ReplacementTransform(
                    triangles[i],
                    new_triangles[i]
                ) for i in range(n)
            ],
            *[nt.animate.set_fill(RED, 0.8) for nt in new_triangles],
        )
        self.wait()

        # STEP 8: open and expand new triangles
        self.play(
            new_CIF.animate.shift(LEFT),
            *[z.animate.shift(LEFT) for z in [z_C, z_I]],
            FadeOut(z_F),
            new_FHC.animate.shift(DOWN),
            *[z.animate.shift(DOWN) for z in [z_C, z_H]],
            new_EFG.animate.shift(3 * RIGHT + 3 * UP),
            *[z.animate.shift(3 * RIGHT + 3 * UP) for z in [z_E, z_G]],
        )
        self.wait()

        # STEP 9: move back
        
        self.play(
            new_CIF.animate.shift(RIGHT),
            *[z.animate.shift(RIGHT) for z in [z_C, z_I]],
            FadeIn(z_F),
            new_FHC.animate.shift(UP),
            *[z.animate.shift(UP) for z in [z_C, z_H]],
            new_EFG.animate.shift(3 * LEFT + 3 * DOWN),
            *[z.animate.shift(3 * LEFT + 3 * DOWN) for z in [z_E, z_G]],
        )
        self.wait()

        # STEP 10: central configuration
        move_z_EI = [z_E, z_I]
        move_z_GH = [z_G, z_H]
        z_F = Dot(plane.n2p(0 + 0j), color=YELLOW)
        centered_E, centered_F, centered_I = [0, -2, 0], [0, 0, 0], [0, 2, 0]
        centered_G, centered_H = [-2, 0, 0], [2, 0, 0]
        
        centered_left_down_triangle_vertices = [centered_E, centered_G, A]
        centered_EGA = Polygon(
            *centered_left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        centered_EGA_copy = Polygon(
            *centered_left_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        centered_left_up_triangle_vertices = [centered_E, centered_F, centered_G]
        centered_EFG = Polygon(
            *centered_left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        centered_EFG_copy = Polygon(
            *centered_left_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        centered_right_down_triangle_vertices = [centered_F, centered_H, C]
        centered_FHC = Polygon(
            *centered_right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        centered_FHC_copy = Polygon(
            *centered_right_down_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        
        centered_right_up_triangle_vertices = [C, centered_I, centered_F]
        centered_CIF = Polygon(
            *centered_right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )
        centered_CIF_copy = Polygon(
            *centered_right_up_triangle_vertices,
            color=RED,
            fill_color=RED
        )

        centered_triangles = [centered_EGA, centered_EFG, centered_FHC, centered_CIF]
        centered_triangles_copy = [
            centered_EGA_copy,
            centered_EFG_copy,
            centered_FHC_copy,
            centered_CIF_copy
        ]
        n = len(centered_triangles)
        
        self.play(
            *[m.animate.shift(RIGHT) for m in move_z_EI],
            *[m.animate.shift(UP) for m in move_z_GH],
            Write(z_F),
            *[
                ReplacementTransform(
                    new_triangles[i],
                    centered_triangles[i]
                ) for i in range(n)
            ],
            *[nt.animate.set_fill(RED, 0.8) for nt in centered_triangles],
        )
        self.wait()

        # STEP 11: open and expand centered triangles
        self.play(
            centered_CIF.animate.shift(2 * LEFT),
            *[z.animate.shift(2 * LEFT) for z in [z_C, z_I]],
            FadeOut(z_F),
            centered_FHC.animate.shift(2 * DOWN),
            *[z.animate.shift(2 * DOWN) for z in [z_C, z_H]],
            centered_EFG.animate.shift(2 * RIGHT + 2 * UP),
            *[z.animate.shift(2 * RIGHT + 2 * UP) for z in [z_E, z_G]],
        )
        self.wait()

        # STEP 12: move back
        
        self.play(
            centered_CIF.animate.shift(2 * RIGHT),
            *[z.animate.shift(2 * RIGHT) for z in [z_C, z_I]],
            #FadeIn(z_F),
            centered_FHC.animate.shift(2 * UP),
            *[z.animate.shift(2 * UP) for z in [z_C, z_H]],
            centered_EFG.animate.shift(2 * LEFT + 2 * DOWN),
            *[z.animate.shift(2 * LEFT + 2 * DOWN) for z in [z_E, z_G]],
        )
        self.wait()


        inbox1 = "On a bien démontré le théorème"
        inbox2 = "de Pythagore selon la méthode"
        inbox3 = "de Zhou Suanjing"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)


        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(msg),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait()
        
        disp_sub(self, lang='fr')
