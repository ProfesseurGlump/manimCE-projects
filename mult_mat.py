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
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        def disp_ABCdetails(A, B, AB_details, AB_result, switch):
            abcdetails = Group(
                A, B, AB_details, AB_result
            ).arrange_in_grid(
                rows=2,
                cols=2,
                buff=1.25,
                #row_alignments="c"
            )
            if switch == 1: self.play(FadeIn(abcdetails))
            elif switch == -1: self.play(FadeOut(abcdetails))
            self.wait(0.5)

        def somme(L):
            S = 0
            for i in range(len(L)):
                S += L[i]
            return S
        
        def multiply_matrix(ent_A, ent_B):
            nb_A_cols = len(ent_A[0][:])
            nb_B_rows = len(ent_B[:][0])
            if nb_A_cols != nb_B_rows: return False
            else:
                nb_AB_rows = len(ent_A[:][0])
                nb_AB_cols = len(ent_B[0][:])
                ent_AB = []
                for i in range(nb_AB_rows):
                    AB_row_i = []
                    for k in range(nb_AB_cols):
                        AB_ij = [
                            ent_A[i][j] * ent_B[j][k]
                            for j in range(nb_AB_cols)
                        ]
                        AB_row_i.append(somme(AB_ij))
                    ent_AB.append(AB_row_i)
            return ent_AB

        def test_values():
            ent_A = [
                [1, 2],
                [3, 4]
            ]
            
            
            A = Matrix(ent_A)
        
            ent_B = [
                [5, 6],
                [7, 8]
            ]

            B = Matrix(ent_B)

            ent_AB = multiply_matrix(ent_A, ent_B)
            AB_result = Matrix(ent_AB)

            # dispAB = Group(
            #     A, B, AB
            # ).arrange_in_grid(
            #     buff=0.75,
            #     rows=1,
            #     cols=3
            # )
            # self.play(FadeIn(dispAB))
            # self.wait(2)
            
            c00 = f"{ent_A[0][0]}" + r"\times " + f"{ent_B[0][0]} + "
            c00 += f"{ent_A[0][1]}" + r"\times " + f"{ent_B[1][0]}"
            c01 = f"{ent_A[0][0]}" + r"\times " + f"{ent_B[0][1]} + "
            c01 += f"{ent_A[0][1]}" + r"\times " + f"{ent_B[1][1]}"
            c10 = f"{ent_A[1][0]}" + r"\times " + f"{ent_B[0][0]} + "
            c10 += f"{ent_A[1][1]}" + r"\times " + f"{ent_B[1][0]}"
            c11 = f"{ent_A[1][0]}" + r"\times " + f"{ent_B[0][1]} + "
            c11 += f"{ent_A[1][1]}" + r"\times " + f"{ent_B[1][1]}"
            
            ent_AB_details = [[c00], [c01], [c10], [c11]]

            AB_details = Matrix(ent_AB_details)
            

            d00 = MathTex("5\times 1 + 6\times 3")
            d01 = MathTex("5\times 2 + 6\times 4")
            d10 = MathTex("7\times 1 + 8\times 3")
            d11 = MathTex("7\times 2 + 8\times 4")
            
            ent_BA_details = [[d00], [d01], [d10], [d11]]
            
            BA_details = Matrix(ent_BA_details)
            
            ent_BA = multiply_matrix(ent_A=ent_B, ent_B=ent_A)
            
            BA_result = Matrix(ent_BA)

            return A, B, AB_details, AB_result, BA_details, BA_result
        
        A, B, AB_details, AB_result, BA_details, BA_result = test_values()
        disp_ABCdetails(A, B, AB_details, AB_result, 1)
        
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

            
        # Éléments du détail du produit AB
        ent_AB_details = AB_details.get_entries()
        AB_details_00_fix = SurroundingRectangle(ent_AB_details[0])
        AB_details_01_fix = SurroundingRectangle(ent_AB_details[1])
        AB_details_10_fix = SurroundingRectangle(ent_AB_details[2])
        AB_details_11_fix = SurroundingRectangle(ent_AB_details[3])
        AB_details_fix = [
            SurroundingRectangle(ent_AB_details[i]) for i in range(4)
        ]
        AB_details_move = [
            SurroundingRectangle(ent_AB_details[i]) for i in range(4)
        ]
        
        # Éléments du résultat du produit AB
        ent_AB_result = AB_result.get_entries()
        AB_result_00_fix = SurroundingRectangle(ent_AB_result[0])
        AB_result_01_fix = SurroundingRectangle(ent_AB_result[1])
        AB_result_10_fix = SurroundingRectangle(ent_AB_result[2])
        AB_result_11_fix = SurroundingRectangle(ent_AB_result[3])
        AB_result_fix = [
            SurroundingRectangle(ent_AB_result[i]) for i in range(4)
        ]
        AB_result_move = [
            SurroundingRectangle(ent_AB_result[i]) for i in range(4)
        ]
        
        #####################
        # Ligne 1 colonne 1 #
        #####################

        # STEP 1: Encadre A[0:], B[:0] 
        self.play(
            Write(A_row_fix[0]),
            Write(B_col_fix[0]),
        )
        self.wait(0.45)

        # STEP 2: Envoie les cadres A[0:] et B[:0] sur AB_details[0:0]
        self.play(
            ReplacementTransform(A_row_move[0], AB_details_fix[0]),
            ReplacementTransform(B_col_move[0], AB_details_fix[0])
        )
        self.wait(0.3)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 3: Envoie les cadres AB_details[0:0] sur AB_result[0:0]
        self.play(
            ReplacementTransform(AB_details_move[0], AB_result_fix[0])
        )
        self.wait(0.3)
        AB_details_move[0] = SurroundingRectangle(ent_AB_details[0])

        # STEP 4: Déplace
        # 1) B[:0] vers B[:1]
        # 2) AB_details[0:0] vers AB_details[0:1]
        # 3) AB_result[0:0] vers AB_result[0:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(AB_details_fix[0], AB_details_fix[1]),
            ReplacementTransform(AB_result_fix[0], AB_result_fix[1])
        )
        self.wait(0.3)
        B_col_fix[0] = SurroundingRectangle(B.get_columns()[0])
        

        #####################
        # Ligne 1 colonne 2 #
        #####################
        
        # STEP 5: Envoie les cadres A[0:] et B[:1] sur AB_details[0:1]
        self.play(
            ReplacementTransform(A_row_move[0], AB_details_fix[1]),
            ReplacementTransform(B_col_move[1], AB_details_fix[1])
        )
        self.wait(0.3)
        A_row_move[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])

        # STEP 6: Envoie les cadres AB_details[0:1] sur AB_result[0:1]
        self.play(
            ReplacementTransform(AB_details_move[1], AB_result_fix[1])
        )
        self.wait(0.3)
        AB_details_move[1] = SurroundingRectangle(ent_AB_details[1])
        
        # STEP 7: Déplace
        # 1) A[0:] vers A[1:]
        # 2) B[:1] vers B[:0]
        # 3) AB_details[0:1] vers AB_details[1:0]
        # 4) AB_result[0:1] vers AB_result[1:0]
        self.play(
            ReplacementTransform(A_row_fix[0], A_row_fix[1]),
            ReplacementTransform(B_col_fix[1], B_col_fix[0]),
            ReplacementTransform(AB_details_fix[0], AB_details_fix[2]),
            ReplacementTransform(AB_details_fix[1], AB_details_fix[2]),
            ReplacementTransform(AB_result_fix[0], AB_result_fix[2]),
            ReplacementTransform(AB_result_fix[1], AB_result_fix[2]),
        )
        self.wait(0.3)
        A_row_fix[0] = SurroundingRectangle(A.get_rows()[0])
        B_col_fix[1] = SurroundingRectangle(B.get_columns()[1])

        
        # STEP 8: envoie les cadres A[:1] et B[:0] sur AB_details[1:0]
        self.play(
            ReplacementTransform(A_row_move[1], AB_details_fix[2]),
            ReplacementTransform(B_col_move[0], AB_details_fix[2]),
        )
        self.wait(0.3)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 9: Envoie les cadres AB_details[1:0] sur AB_result[1:0]
        self.play(
            ReplacementTransform(AB_details_move[2], AB_result_fix[2])
        )
        self.wait(0.3)
        AB_details_move[2] = SurroundingRectangle(ent_AB_details[2])
        
        # STEP 10: Déplace
        # 1) B[:0] vers B[:1]
        # 2) AB_details[1:0] vers AB_details[1:1]
        # 3) AB_result[1:0] vers AB_result[1:1]
        self.play(
            ReplacementTransform(B_col_fix[0], B_col_fix[1]),
            ReplacementTransform(AB_details_fix[2], AB_details_fix[3]),
            ReplacementTransform(AB_details_fix[1], AB_details_fix[3]),
            ReplacementTransform(AB_details_fix[0], AB_details_fix[3]),
            ReplacementTransform(AB_result_fix[2], AB_result_fix[3]),
            ReplacementTransform(AB_result_fix[1], AB_result_fix[3]),
            ReplacementTransform(AB_result_fix[0], AB_result_fix[3])
        )
        self.wait(0.3)
        B_col_fix[0] = SurroundingRectangle(B.get_columns()[0])

        # STEP 11: envoie les cadres A[:1] et B[:1] sur AB_details[1:1]
        self.play(
            ReplacementTransform(A_row_move[1], AB_details_fix[3]),
            ReplacementTransform(B_col_move[1], AB_details_fix[3]),
        )
        self.wait(0.3)
        A_row_move[1] = SurroundingRectangle(A.get_rows()[1])
        B_col_move[1] = SurroundingRectangle(B.get_columns()[1])
        
        # STEP 12: Envoie les cadres AB_details[1:1] sur AB_result[1:1]
        self.play(
            ReplacementTransform(AB_details_move[3], AB_result_fix[3])
        )
        self.wait(0.3)
        AB_details_move[2] = SurroundingRectangle(ent_AB_details[2])
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
