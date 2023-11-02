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

    
class MultiplyMatrix(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Multiplication de matrices "
        title = Title(f"{msg} Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        def disp_ABC_details(A, B, C, C_details, switch):
            abc_details = Group(
                A, B, C, C_details
            ).arrange_in_grid(buff=1.25)
            if switch == 1: self.play(FadeIn(abc_details))
            elif switch == -1: self.play(FadeOut(abc_details))
            self.wait(0.5)
        

        def test_values():
            ent_A_22 = [
                [1, 2],
                [3, 4]
            ]

            A_22 = Matrix(ent_A_22)
        
            ent_B_22 = [
                [4, 3],
                [2, 1]
            ]

            B_22 = Matrix(ent_B_22)

                        
            ent_AB_22 = [
                [8, 5],
                [20, 13]
            ]

            C_22 = Matrix(ent_AB_22)

            c00 = "1\\times 4 + 3\\times 2"
            c01 = "3\\times 4 + 4\\times 2"
            c10 = "1\\times 3 + 3\\times 1"
            c11 = "1\\times 4 + 3\\times 2"

            ent_C_details = [
                [c00],
                [c01],
                [c10],
                [c11]
            ]
            
            C_details = Matrix(ent_C_details)
            
            ent_BA_22 = [
                [13, 20],
                [5, 8]
            ]
            
            D_22 = Matrix(ent_BA_22)
            
            d00 = "4\\times 1 + 3\\times 3"
            d01 = "4\\times 2 + 3\\times 4"
            d10 = "2\\times 1 + 1\\times 3"
            d11 = "2\\times 2 + 1\\times 4"
            
            ent_D_details = [
                [d00],
                [d01],
                [d10],
                [d11]
            ]
            
            D_details = Matrix(ent_D_details)
            
            return A_22, B_22, C_22, C_details, D_22, D_details

        A, B, C, C_details, D, D_details = test_values()
        disp_ABC_details(A, B, C, C_details, 1)
        
        # Lignes de A
        A_row0_fix = SurroundingRectangle(A.get_rows()[0])
        A_row1_fix = SurroundingRectangle(A.get_rows()[1])
        A_row_fix = [A_row0_fix, A_row1_fix]
        
        A_row0_move = SurroundingRectangle(A.get_rows()[0])
        A_row1_move = SurroundingRectangle(A.get_rows()[1])
        A_row_move = [A_row0_move, A_row1_move]

        # Colonnes de B
        B_col0_fix = SurroundingRectangle(B.get_columns()[0])
        B_col1_fix = SurroundingRectangle(B.get_columns()[1])
        B_col_fix = [B_col0_fix, B_col1_fix]

        B_col0_move = SurroundingRectangle(B.get_columns()[0])
        B_col1_move = SurroundingRectangle(B.get_columns()[1])
        B_col_move = [B_col0_move, B_col1_move]

            
        # Éléments du produit AB
        ent_C = C.get_entries()
        C_00_fix = SurroundingRectangle(ent_C[0])
        C_01_fix = SurroundingRectangle(ent_C[1])
        C_10_fix = SurroundingRectangle(ent_C[2])
        C_11_fix = SurroundingRectangle(ent_C[3])
        C_elts_fix = [
            C_00_fix, C_01_fix,
            C_10_fix, C_11_fix
        ]

        ent_C_details = C_details.get_entries()
        C_details_00_fix = SurroundingRectangle(ent_C_details[0])
        C_details_01_fix = SurroundingRectangle(ent_C_details[1])
        C_details_10_fix = SurroundingRectangle(ent_C_details[2])
        C_details_11_fix = SurroundingRectangle(ent_C_details[3])
        C_details_elts_fix = [
            C_details_00_fix, C_details_01_fix,
            C_details_10_fix, C_details_11_fix
        ]

        C_details_00_move = SurroundingRectangle(ent_C_details[0])
        C_details_01_move = SurroundingRectangle(ent_C_details[1])
        C_details_10_move = SurroundingRectangle(ent_C_details[2])
        C_details_11_move = SurroundingRectangle(ent_C_details[3])
        C_details_elts_move = [
            C_details_00_move, C_details_01_move,
            C_details_10_move, C_details_11_move
        ]
        
        #####################
        # Ligne 1 colonne 1 #
        #####################

        # STEP 1: Encadre A[0:], B[:0]
        self.play(
            Write(A_row_fix[0]),
            Write(B_col_fix[0]),
        )
        self.wait(2.5)

        # STEP 2: Envoie les cadres
        # 1) A[0:] et B[:0] sur C_details[0]
        self.play(
            ReplacementTransform(A_row_move[0], C_details_elts_fix[0]),
            ReplacementTransform(B_col_move[0], C_details_elts_fix[0])
        )
        self.wait(2.5)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 3: Déplace
        # 1) C_details[0] sur C[0:0]
        self.play(
            ReplacementTransform(C_details_elts_move[0], C_elts_fix[0]),
        )
        self.wait(2.5)
        C_details_elts_move[0] = SurroundingRectangle(ent_C_details[0])
        

        #####################
        # Ligne 1 colonne 2 #
        #####################

        # STEP 4: Déplace
        # 1) B[0:] vers B[1:]
        # 2) C_details[0] vers C_details[1]
        # 3) C[0:0] vers C[0:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(
                C_details_elts_fix[0],
                C_details_elts_fix[1]
            ),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[1])
        )
        self.wait(2.5)
        B_col_fix[0] = SurroundingRectangle(B.get_columns()[0])
        
        # STEP 5: Envoie les cadres
        # 1) A[0:] et B[:1] sur C_details[1]
        self.play(
            ReplacementTransform(A_row_move[0], C_details_elts_fix[1]),
            ReplacementTransform(B_col_move[1], C_details_elts_fix[1])
        )
        self.wait(2.5)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])

        # STEP 5: Déplace
        # 1) C_details[1] vers C[0:1]
        self.play(
            ReplacementTransform(C_details_elts_move[1], C_elts_fix[1]),
        )
        self.wait(2.5)

        # STEP 6:
        # 2) A[0:] vers A[1:]
        # 3) B[:1] vers B[:0]
        # 4) C[0:1] vers C[1:0]
        self.play(
            ReplacementTransform(A_row_fix[0], A_row_fix[1]),
            ReplacementTransform(B_col_fix[1], B_col_fix[0]),
            ReplacementTransform(
                C_details_elts_fix[0],
                C_details_elts_fix[2]
            ),
            ReplacementTransform(
                C_details_elts_fix[1],
                C_details_elts_fix[2]
            ),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[2]),
            ReplacementTransform(C_elts_fix[1], C_elts_fix[2]),
        )
        self.wait(2.5)
        B_col_fix[1] = SurroundingRectangle(B.get_columns()[1])
        
        # STEP 7: envoie les cadres
        # 1) A[:1] et B[:0] sur C_details[2]
        self.play(
            ReplacementTransform(A_row_move[1], C_details_elts_fix[2]),
            ReplacementTransform(B_col_move[0], C_details_elts_fix[2]),
        )
        self.wait(0.9)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 8: Envoie
        # 1) C_details[2] sur C[1:0]
        self.play(
            ReplacementTransform(C_details_elts_move[2], C_elts_fix[2]),
        )
        self.wait(2.5)

        # STEP 9: Déplace
        # 1) B[:0] vers B[:1]
        # 2) C_details[2] vers C_details[3]
        # 2) C[1:0] vers C[1:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(
                C_details_elts_fix[0],
                C_details_elts_fix[3]
            ),
            ReplacementTransform(
                C_details_elts_fix[1],
                C_details_elts_fix[3]
            ),
            ReplacementTransform(
                C_details_elts_fix[2],
                C_details_elts_fix[3]
            ),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[3]),
            ReplacementTransform(C_elts_fix[1], C_elts_fix[3]),
            ReplacementTransform(C_elts_fix[2], C_elts_fix[3])
        )
        self.wait(2.5)
        
        # STEP 10: envoie les cadres A[:1] et B[:1] sur C_details[3]
        self.play(
            ReplacementTransform(A_row_move[1], C_details_elts_fix[3]),
            ReplacementTransform(B_col_move[1], C_details_elts_fix[3]),
        )
        self.wait(2.5)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])

        # STEP 11: envoie C_details[3] sur C[1:1]
        self.play(
            ReplacementTransform(
                C_details_elts_move[3],
                C_elts_fix[3]
            ),
        )
        self.wait(2.5)

        disp_sub(self, lang='fr')

        
