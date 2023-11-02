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

        
        def disp_ABC(A, B, C, switch):
            abc = Group(A, B, C).arrange_in_grid(buff=1)
            if switch == 1: self.play(FadeIn(abc))
            elif switch == -1: self.play(FadeOut(abc))
            self.wait(0.5)
        
        # def get_matrix_rows(A, n):
        #     A_row_fix = [
        #         SurroundingRectangle(A.get_rows()[i])
        #         for i in range(n)
        #     ]
        #     A_row_move = [
        #         SurroundingRectangle(A.get_rows()[i])
        #         for i in range(n)
        #     ]
        #     return A_row_fix, A_row_move

        
        # def get_matrix_columns(A, n):
        #     A_col_fix = [
        #         SurroundingRectangle(A.get_columns()[j])
        #         for j in range(n)
        #     ]
        #     A_col_move = [
        #         SurroundingRectangle(A.get_columns()[j])
        #         for j in range(n)
        #     ]
        #     return A_col_fix, A_col_move


        # def get_matrix_elts(A, n):
        #     ent_A = A.get_entries()
        #     A_elts_fix = [
        #         SurroundingRectangle(ent_A[k])
        #         for k in range(n**2)
        #     ]
        #     return A_elts_fix

        
        # # Ligne 1 colonne 1
        # def get_row1_col1_mult(A, B, C):
        #     A_row_fix, A_row_move = get_matrix_rows(A, n=2)
        #     B_col_fix, B_col_move = get_matrix_columns(B, n=2)
        #     C_elts_fix = get_matrix_elts(C, n=2)

        #     # STEP 1: A Ligne 1 B Colonne 1
        #     self.play(
        #         Write(A_row_fix[0]),
        #         Write(B_col_fix[0])
        #     )
        #     self.wait(0.3)
        #     # STEP 2: Envoi A1:B:1 vers le résultat
        #     self.play(
        #         ReplacementTransform(A_row_move[0], C_elts_fix[0]),
        #         ReplacementTransform(B_col_move[0], C_elts_fix[0]),
        #     )
        #     self.wait(0.3)
        #     A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        #     B_col_move[0] = SurroundingRectangle(B.get_columns()[0])
        #     return A_row_move[0], B_col_move[0] 


        # # Ligne 1 colonne 2
        # def get_row1_col2_mult(A, B, C):
        #     A_row_fix, A_row_move = get_matrix_rows(A, n=2)
        #     B_col_fix, B_col_move = get_matrix_columns(B, n=2)
        #     C_elts_fix = get_matrix_elts(C, n=2)
        #     # STEP 3: décalage B c1c2 C c11c12
        #     self.play(
        #         ReplacementTransform(B_col_fix[0], B_col_fix[1]),
        #         FadeOut(B_col_fix[0]),
        #         ReplacementTransform(C_elts_fix[0], C_elts_fix[1]),
        #         FadeOut(C_elts_fix[0])
        #     )
        #     self.wait(0.15)
        #     # STEP 4: Envoi A1:B:2 vers le résultat
        #     self.play(
        #         ReplacementTransform(A_row_move[0], C_elts_fix[1]),
        #         ReplacementTransform(B_col_move[1], C_elts_fix[1])
        #     )
        #     self.wait(0.3)
        #     A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        #     B_col_move[0] = SurroundingRectangle(B.get_columns()[0])
        #     B_col_move[1] = SurroundingRectangle(B.get_columns()[1])
        #     return A_row_move[0], B_col_move[0], B_col_move[1]


        # # Ligne 2 colonne 1
        # def get_row2_col1_mult(A, B, C):
        #     A_row_fix, A_row_move = get_matrix_rows(A, n=2)
        #     B_col_fix, B_col_move = get_matrix_columns(B, n=2)
        #     C_elts_fix = get_matrix_elts(C, n=2)

        #     # STEP 5: décalage A1:A2: B:2B:1
        #     self.play(
        #         ReplacementTransform(A_row_fix[0], A_row_fix[1]),
        #         FadeOut(A_row_fix[0]),
        #         ReplacementTransform(B_col_fix[1], B_col_fix[0]),
        #         FadeOut(B_col_fix[1]),
        #         ReplacementTransform(C_elts_fix[1], C_elts_fix[2]),
        #         FadeOut(C_elts_fix[1])
        #     )
        #     self.wait(0.75)
        #     # STEP 6: envoi A2:B:1 vers le résultat
        #     self.play(
        #         ReplacementTransform(A_row_move[1], C_elts_fix[2]),
        #         ReplacementTransform(B_col_move[0], C_elts_fix[2]),
        #     )
        #     self.wait(0.3)
        #     A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        #     B_col_move[0] = SurroundingRectangle(B.get_columns()[0])
        #     B_col_move[1] = SurroundingRectangle(B.get_columns()[1])
        #     return A_row_move[1], B_col_move[0], B_col_move[1]

        
        # # Ligne 2 colonne 2
        # def get_row2_col2_mult(A, B, C):
        #     A_row_fix, A_row_move = get_matrix_rows(A, n=2)
        #     B_col_fix, B_col_move = get_matrix_columns(B, n=2)
        #     C_elts_fix = get_matrix_elts(C, n=2)
        #     # STEP 7: décalage B:1B:2 C[2]C[3]
        #     self.play(
        #         ReplacementTransform(B_col_fix[0], B_col_fix[1]),
        #         FadeOut(B_col_fix[0]),
        #         ReplacementTransform(C_elts_fix[2], C_elts_fix[3]),
        #         FadeOut(C_elts_fix[2])
        #     )
        #     self.wait(0.15)
        #     # STEP 8: envoi de A2:B:2 vers le résultat
        #     self.play(
        #         ReplacementTransform(A_row_move[1], C_elts_fix[3]),
        #         ReplacementTransform(B_col_move[1], C_elts_fix[3]),
        #     )
        #     self.wait(0.5)
        #     A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        #     B_col_move[1] = SurroundingRectangle(B.get_columns()[1])
        #     return A_row_move[1], B_col_move[1]
            
        # def mult_details(A, B, C, n=2):
        #     disp_ABC(A, B, C, 1)
        #     A_row_fix, A_row_move = get_matrix_rows(A, n=2)
        #     B_col_fix, B_col_move = get_matrix_columns(B, n=2)
        #     C_elts_fix = get_matrix_elts(C, n=2)
        #     A_row_move[0], B_col_move[0] = get_row1_col1_mult(A, B, C)
        #     A_row_move[0], B_col_move[0], B_col_move[1] = get_row1_col2_mult(A, B, C)
        #     A_row_move[1], B_col_move[0], B_col_move[1] = get_row2_col1_mult(A, B, C)
        #     A_row_move[1], B_col_move[1] = get_row2_col2_mult(A, B, C)
        #     self.wait()
        #     disp_ABC(A, B, C, -1)


        # def test_values():
        #     ent_A_22 = [
        #         [1, 2],
        #         [3, 4]
        #     ]

        #     A_22 = Matrix(ent_A_22)
        
        #     ent_B_22 = [
        #         [4, 3],
        #         [2, 1]
        #     ]

        #     B_22 = Matrix(ent_B_22)
        
        #     ent_AB_22 = [
        #         [8, 5],
        #         [20, 13]
        #     ]

        #     C_22 = Matrix(ent_AB_22)

        #     ent_BA_22 = [
        #         [13, 20],
        #         [5, 8]
        #         ]
            
        #     D_22 = Matrix(ent_BA_22)

        #     return A_22, B_22, C_22, D_22

        # A, B, C, D = test_values()
        # mult_details(A, B, C, n=2)
        # self.wait(2)
        # mult_details(B, A, A, n=2)

        # disp_sub(self, lang='fr')

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

            ent_BA_22 = [
                [13, 20],
                [5, 8]
                ]
            
            D_22 = Matrix(ent_BA_22)

            return A_22, B_22, C_22, D_22

        A, B, C, D = test_values()
        disp_ABC(A, B, C, 1)
        
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

        C_00_move = SurroundingRectangle(ent_C[0])
        C_01_move = SurroundingRectangle(ent_C[1])
        C_10_move = SurroundingRectangle(ent_C[2])
        C_11_move = SurroundingRectangle(ent_C[3])
        C_elts_move = [
            C_00_move, C_01_move,
            C_10_move, C_11_move
        ]

        #####################
        # Ligne 1 colonne 1 #
        #####################

        # STEP 1: Encadre A[0:], B[:0] et C[0:0]
        self.play(
            Write(A_row_fix[0]),
            Write(B_col_fix[0]),
            Write(C_elts_fix[0]),
        )
        self.wait(0.45)

        # STEP 2: Envoie les cadres A[0:] et B[:0] sur C[0:0]
        self.play(
            ReplacementTransform(A_row_move[0], C_elts_fix[0]),
            ReplacementTransform(B_col_move[0], C_elts_fix[0])
        )
        self.wait(0.3)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 3: Déplace
        # 1) B[:0] vers B[:1]
        # 2) C[0:0] vers C[0:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[1])
        )
        self.wait(0.3)
        B_col_fix[0] = SurroundingRectangle(B.get_columns()[0])
        

        #####################
        # Ligne 1 colonne 2 #
        #####################
        
        # STEP 4: Envoie les cadres A[0:] et B[:1] sur C[0:1]
        self.play(
            ReplacementTransform(A_row_move[0], C_elts_fix[1]),
            ReplacementTransform(B_col_move[1], C_elts_fix[1])
        )
        self.wait(0.3)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])

        # STEP 5: Déplace
        # 1) A[0:] vers A[1:]
        # 2) B[:1] vers B[:0]
        # 3) C[0:1] vers C[1:0]
        self.play(
            ReplacementTransform(A_row_fix[0], A_row_fix[1]),
            ReplacementTransform(B_col_fix[1], B_col_fix[0]),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[2]),
            ReplacementTransform(C_elts_fix[1], C_elts_fix[2]),
        )
        self.wait(0.3)
        A_row_fix[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_fix[1] = SurroundingRectangle(B.get_columns()[1])
        
        # STEP 6: envoie les cadres A[:1] et B[:0] sur C[1:0]
        self.play(
            ReplacementTransform(A_row_move[1], C_elts_fix[2]),
            ReplacementTransform(B_col_move[0], C_elts_fix[2]),
        )
        self.wait(0.3)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 7: Déplace
        # 1) B[:0] vers B[:1]
        # 2) C[1:0] vers C[1:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(C_elts_fix[2], C_elts_fix[3]),
            ReplacementTransform(C_elts_fix[1], C_elts_fix[3]),
            ReplacementTransform(C_elts_fix[0], C_elts_fix[3])
        )
        self.wait(0.3)
        B_col_fix[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 8: envoie les cadres A[:1] et B[:1] sur C[1:1]
        self.play(
            ReplacementTransform(A_row_move[1], C_elts_fix[3]),
            ReplacementTransform(B_col_move[1], C_elts_fix[3]),
        )
        self.wait(0.3)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])
        


        
