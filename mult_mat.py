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


def multiply_matrix(ent_A, ent_B):
    nb_A_cols = len(ent_A[0][0:])
    nb_B_rows = len(ent_B[:])
    if nb_A_cols != nb_B_rows: return False
    else:
        nb_AB_rows = len(ent_A[0:][0:])
        nb_AB_cols = len(ent_B[0:][0])
        ent_AB = []
        for i in range(nb_AB_rows):
            AB_row_i = []
            for k in range(nb_AB_cols):
                AB_ij = [
                    ent_A[i][j] * ent_B[j][k]
                    for j in range(nb_A_cols)
                ]
                s_i = sum(AB_ij)
                AB_row_i.append(s_i)
            ent_AB.append(AB_row_i)
        return ent_AB


def product_details(ent_A, ent_B):
    nb_A_cols = len(ent_A[0])
    nb_AB_rows = len(ent_A[0:][0:])
    nb_AB_cols = len(ent_B[0:][0])
    ent_AB_details = []
    for i in range(nb_AB_rows):
        AB_row_i, s_i = [], ''
        for k in range(nb_AB_cols):
            AB_ij = [
                f"{ent_A[i][j]} " + r"\times " + f" {ent_B[j][k]}"
                for j in range(nb_A_cols)
            ]
            for j in range(len(AB_ij)):
                if j == 0: s_i += AB_ij[j]
                else: s_i += " + " + AB_ij[j]
            AB_row_i.append([s_i])
            s_i = " "
        ent_AB_details.append(AB_row_i)
    return ent_AB_details



def from_matrix_to_column(matrix):
    nb_rows = len(matrix[0:][0:])
    nb_cols = len(matrix[0])
    length = nb_rows + nb_cols
    vect = []
    for i in range(nb_rows):
        for j in range(nb_cols):
            vect.append(matrix[i][j])
    return vect



def disp_A_B_AB(ent_A, ent_B, buffer):
    ent_AB = multiply_matrix(ent_A, ent_B)
    print("AB =", ent_AB)
    A, B, AB = Matrix(ent_A), Matrix(ent_B), Matrix(ent_AB)
    dispAB = Group(
        A, B, AB
    ).arrange_in_grid(
        buff=buffer,
        rows=1,
        cols=3,
        row_alignment="c"
    )
    return dispAB



def surround_matrices_elts(matrices_group):
    
    matrices_rows_fix, matrices_rows_move = [], []
    matrices_cols_fix, matrices_cols_move = [], []
    matrices_elts_fix, matrices_elts_move = [], []
        
    for matrix in matrices_group:
        
        matrix_rows_fix = [SurroundingRectangle(matrix.get_rows()[i]) for i in range(len(matrix.get_rows()))]
        matrix_rows_move = [SurroundingRectangle(matrix.get_rows()[i]) for i in range(len(matrix.get_rows()))]
        matrices_rows_fix.append(matrix_rows_fix)
        matrices_rows_move.append(matrix_rows_move)
            
        matrix_cols_fix = [SurroundingRectangle(matrix.get_columns()[i]) for i in range(len(matrix.get_columns()))]
        matrix_cols_move = [SurroundingRectangle(matrix.get_columns()[i]) for i in range(len(matrix.get_columns()))]
        matrices_cols_fix.append(matrix_cols_fix)
        matrices_cols_move.append(matrix_cols_move)
            
        matrix_elts_fix = [SurroundingRectangle(matrix.get_entries()[i]) for i in range(len(matrix.get_entries()))]
        matrix_elts_move = [SurroundingRectangle(matrix.get_entries()[i]) for i in range(len(matrix.get_entries()))]
        matrices_elts_fix.append(matrix_elts_fix)
        matrices_elts_move.append(matrix_elts_move)

    fix_matrices = [matrices_rows_fix, matrices_cols_fix, matrices_elts_fix]
    move_matrices = [matrices_rows_move, matrices_cols_move, matrices_elts_move]
        
    return fix_matrices, move_matrices

    

class MultiplyMatrix1(Scene):
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

            
            c00 = f"{ent_A[0][0]}" + r"\times " + f"{ent_B[0][0]} + "
            c00 += f"{ent_A[0][1]}" + r"\times " + f"{ent_B[1][0]}"
            c01 = f"{ent_A[0][0]}" + r"\times " + f"{ent_B[0][1]} + "
            c01 += f"{ent_A[0][1]}" + r"\times " + f"{ent_B[1][1]}"
            c10 = f"{ent_A[1][0]}" + r"\times " + f"{ent_B[0][0]} + "
            c10 += f"{ent_A[1][1]}" + r"\times " + f"{ent_B[1][0]}"
            c11 = f"{ent_A[1][0]}" + r"\times " + f"{ent_B[0][1]} + "
            c11 += f"{ent_A[1][1]}" + r"\times " + f"{ent_B[1][1]}"
            
            ent_AB_details = [[c00], [c01], [c10], [c11]]

            # ent_AB_details = from_matrix_to_column(
            #     product_details(
            #         ent_A,
            #         ent_B
            #     )
            # )
            
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
        A_rows_fix = [SurroundingRectangle(A.get_rows()[i]) for i in range(2)]
        
        A_row0_move = SurroundingRectangle(A.get_rows()[0])
        A_row1_move = SurroundingRectangle(A.get_rows()[1])
        A_row_move = [A_row0_move, A_row1_move]
        A_rows_move = [SurroundingRectangle(A.get_rows()[i]) for i in range(2)]

        # Colonnes de B
        B_col0_fix = SurroundingRectangle(B.get_columns()[0])
        B_col1_fix = SurroundingRectangle(B.get_columns()[1])
        B_col_fix = [B_col0_fix, B_col1_fix]
        B_cols_fix = [SurroundingRectangle(B.get_columns()[i]) for i in range(2)]

        B_col0_move = SurroundingRectangle(B.get_columns()[0])
        B_col1_move = SurroundingRectangle(B.get_columns()[1])
        B_col_move = [B_col0_move, B_col1_move]
        B_cols_move = [SurroundingRectangle(B.get_columns()[i]) for i in range(2)]
            
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

        

class MultiplyMatrix2(Scene):
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

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_clap.scale(0.75)))
        self.wait()
        
        title_question = Title("Conditions de compatibilité")
        inbox1 = "À quelle(s) condition(s) un produit "
        inbox2 = "matriciel est-il compatible ?"
        inbox3 = "Écrivez-le dans les commentaires."
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            ReplacementTransform(title_clap, title_question.scale(0.75))
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

        title_rep = Title("Réponse")
        inbox1 = "Pour qu'un produit "
        inbox2 = "matriciel soit compatible,"
        inbox3 = "il faut que le nombre "
        inbox4 = "de colonnes de la matrice "
        inbox5 = "de gauche coïncide avec le "
        inbox6 = "nombre de lignes de la "
        inbox7 = "matrice de droite."
        inboxes = [
            inbox1, inbox2, inbox3,
            inbox4,
            inbox5, inbox6, inbox7
        ]
        msg2 = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            ReplacementTransform(
                msg,
                msg2.next_to(title_start, 3*DOWN)
            ),
            ReplacementTransform(title_clap, title_rep)
        )
        self.wait(5)

        self.play(
            FadeOut(msg2)
        )
        self.wait()
        
        ent_A = [[1, 2]]
        ent_B = [[1], [2]]
        ent_AB = multiply_matrix(ent_A, ent_B)
        ent_AB_details = product_details(ent_A, ent_B)
        vect_AB_details = from_matrix_to_column(
            product_details(
                ent_A,
                ent_B
            )
        )
        AB_details = Matrix(vect_AB_details)
        
        A, B, AB = Matrix(ent_A), Matrix(ent_B), Matrix(ent_AB)
        matrices_group = [A, B, AB_details, AB]
        dispAB = Group(
            *matrices_group
        ).arrange_in_grid(
            buff=0.5,
            rows=2,
            cols=2,
            row_alignment="c"
        )

        fix_matrices, move_matrices = surround_matrices_elts(matrices_group)
        
        matrices_rows_fix, matrices_cols_fix, matrices_elts_fix = fix_matrices
        A_rows_fix, B_rows_fix, AB_details_rows_fix, AB_rows_fix = matrices_rows_fix
        A_cols_fix, B_cols_fix, AB_details_cols_fix, AB_cols_fix = matrices_cols_fix
        A_elts_fix, B_elts_fix, AB_details_elts_fix, AB_elts_fix = matrices_elts_fix

        matrices_rows_move, matrices_cols_move, matrices_elts_move = move_matrices
        A_rows_move, B_rows_move, AB_details_rows_move, AB_rows_move = matrices_rows_move
        A_cols_move, B_cols_move, AB_details_cols_move, AB_cols_move = matrices_cols_move
        A_elts_move, B_elts_move, AB_details_elts_move, AB_elts_move = matrices_elts_move

        title_ex1 = Title("Premier exemple 1 x 2 fois 2 x 1")
        self.play(
            ReplacementTransform(
                title_rep, title_ex1
            ),
            FadeIn(dispAB),
            Write(A_rows_fix[0]),
            Write(B_cols_fix[0]),
            Write(AB_details_rows_fix[0]),
            Write(AB_rows_fix[0]),
        )
        self.wait(2.5)

        self.play(
            ReplacementTransform(A_rows_move[0], AB_details_rows_move[0]),
            ReplacementTransform(B_cols_move[0], AB_details_rows_move[0]),
        )
        self.wait(1.25)

        self.play(
            ReplacementTransform(AB_details_rows_move[0], AB_rows_move[0]),
        )
        self.wait(0.75)

        self.play(
            Unwrite(A_rows_fix[0]),
            Unwrite(B_cols_fix[0]),
            Unwrite(AB_details_rows_fix[0]),
            Unwrite(AB_rows_fix[0]),
            Unwrite(AB_details_rows_move[0]),
            Unwrite(AB_rows_move[0]),
        )
        self.wait(0.5)
                  
        ent_B_bis = [[1, 2]]
        B_bis = Matrix(ent_B_bis)
        ent_A_bis = [[1], [2]]
        A_bis = Matrix(ent_A_bis)
        ent_AB_bis = multiply_matrix(ent_A_bis, ent_B_bis)
        AB_bis = Matrix(ent_AB_bis)
        ent_AB_details_bis = product_details(ent_A_bis, ent_B_bis)
        
        vect_AB_details_bis = from_matrix_to_column(
            product_details(
                ent_A_bis,
                ent_B_bis
            )
        )
        AB_details_bis = Matrix(vect_AB_details_bis)
        matrices_group = [A_bis, B_bis, AB_details_bis, AB_bis]
        dispAB_bis = Group(
            *matrices_group
        ).arrange_in_grid(
            buff=0.5,
            rows=2,
            cols=2,
            row_alignment="c"
        )

        fix_matrices, move_matrices = surround_matrices_elts(matrices_group)
        
        matrices_rows_fix, matrices_cols_fix, matrices_elts_fix = fix_matrices
        A_rows_fix, B_rows_fix, AB_details_rows_fix, AB_rows_fix = matrices_rows_fix
        A_cols_fix, B_cols_fix, AB_details_cols_fix, AB_cols_fix = matrices_cols_fix
        A_elts_fix, B_elts_fix, AB_details_elts_fix, AB_elts_fix = matrices_elts_fix

        matrices_rows_move, matrices_cols_move, matrices_elts_move = move_matrices
        A_rows_move, B_rows_move, AB_details_rows_move, AB_rows_move = matrices_rows_move
        A_cols_move, B_cols_move, AB_details_cols_move, AB_cols_move = matrices_cols_move
        A_elts_move, B_elts_move, AB_details_elts_move, AB_elts_move = matrices_elts_move
        
        title_ex2 = Title("Deuxième exemple 2 x 1 fois 1 x 2")
        self.play(
            ReplacementTransform(
                title_ex1, title_ex2
            ),
            ReplacementTransform(dispAB, dispAB_bis),
        )
        self.wait(2)

        #####################
        # Ligne 1 colonne 1 #
        #####################

        # STEP 1: Encadre A[0:], B[:0] 
        self.play(
            Write(A_rows_fix[0]),
            Write(B_cols_fix[0]),
            # Write(AB_details_rows_fix[0]),
            # Write(AB_elts_fix[0]),
        )
        self.wait(1)

        # STEP 2: move to details
        self.play(
            ReplacementTransform(
                A_rows_move[0],
                AB_details_rows_move[0]
            ),
            ReplacementTransform(
                B_cols_move[0],
                AB_details_rows_move[0]
            ),
        )
        self.wait(1)
        A_rows_move[0] = SurroundingRectangle(A_bis.get_rows()[0])
        B_cols_move[0] = SurroundingRectangle(B_bis.get_columns()[0])
        
        # STEP 3: move to final product
        self.play(
            ReplacementTransform(
                AB_details_rows_move[0],
                AB_elts_fix[0]
            ),
        )
        self.wait(0.75)
        AB_details_rows_move[0] = SurroundingRectangle(AB_details_bis.get_rows()[0])

        # STEP 4:
        # 1) next column for B
        # 2) next row for AB_details
        # 3) next column for AB
        self.play(
            ReplacementTransform(
                B_cols_fix[0],
                B_cols_fix[1]
            ),
            ReplacementTransform(
                AB_details_rows_fix[0],
                AB_details_rows_fix[1]
            ),
            ReplacementTransform(
                AB_elts_fix[0],
                AB_elts_fix[1]
            ),
            # ReplacementTransform(
            #     AB_details_rows_move[0],
            #     AB_elts_fix[1]
            # ),
        )
        self.wait(0.25)
        B_cols_fix[0] = SurroundingRectangle(B_bis.get_columns()[0])

        # STEP 5:
        # A and B to AB_details
        self.play(
            ReplacementTransform(
                A_rows_move[0],
                AB_details_rows_fix[1]
            ),
            ReplacementTransform(
                B_cols_move[1],
                AB_details_rows_fix[1]
            ),
        )
        self.wait(0.5)
        A_rows_move[0] = SurroundingRectangle(A_bis.get_rows()[0])
        B_cols_move[1] = SurroundingRectangle(B_bis.get_columns()[1])

        # STEP 6:
        # Move from AB_details to AB
        self.play(
            ReplacementTransform(
                AB_details_rows_move[1],
                AB_elts_fix[1]
            ),
        )
        self.wait(0.25)
        AB_details_rows_move[1] = SurroundingRectangle(AB_details_bis.get_rows()[1])

        # STEP 7:
        # 1) 
        self.play(
            ReplacementTransform(
                A_rows_fix[0],
                A_rows_fix[1]
            ),
            ReplacementTransform(
                B_cols_fix[1],
                B_cols_fix[0]
            ),
            ReplacementTransform(
                AB_details_rows_fix[0],
                AB_details_rows_fix[2]
            ),
            ReplacementTransform(
                AB_details_rows_fix[1],
                AB_details_rows_fix[2]
            ),
            ReplacementTransform(
                AB_elts_fix[0],
                AB_elts_fix[2]
            ),
            ReplacementTransform(
                AB_elts_fix[1],
                AB_elts_fix[2]
            ),
        )
        self.wait(0.3)
        A_rows_fix[0] = SurroundingRectangle(A_bis.get_rows()[0])
        B_cols_fix[1] = SurroundingRectangle(B_bis.get_columns()[1])
        # self.play(
        #     Unwrite(A_rows_fix[0]),
        #     Unwrite(B_cols_fix[0]),
        #     Unwrite(AB_details_rows_fix[0]),
        #     Unwrite(AB_rows_fix[0]),
        #     Unwrite(AB_details_rows_move[0]),
        #     Unwrite(AB_rows_move[0]),
        # )
        # self.wait(0.5)


        ent_A = [[1, 2], [3, 4]]
        ent_B = [[5, 6], [7, 8]]
        ent_AB = multiply_matrix(ent_A, ent_B)
        ent_AB_details = product_details(ent_A, ent_B)
        
        vect_AB_details = from_matrix_to_column(
            product_details(
                ent_A,
                ent_B
            )
        )
        AB_details = Matrix(vect_AB_details)

        A, B, AB = Matrix(ent_A), Matrix(ent_B), Matrix(ent_AB)
        dispAB = Group(
            A, B, AB_details, AB
        ).arrange_in_grid(
            buff=0.5,
            rows=2,
            cols=2,
            row_alignment="c"
        )
        title_ex3 = Title("Troisième exemple 2 x 2 fois 2 x 2")
        self.play(
            ReplacementTransform(
                title_ex2, title_ex3
            ),
            ReplacementTransform(dispAB_bis, dispAB)
        )
        self.wait(5)

        ent_A_bis = [[1, 2], [3, 4], [5, 6]]
        ent_B_bis = [[7, 8, 9, 0], [1, 2, 3, 4]]
        ent_AB_bis = multiply_matrix(ent_A_bis, ent_B_bis)
        ent_AB_details_bis = product_details(ent_A_bis, ent_B_bis)
        
        vect_AB_details_bis = from_matrix_to_column(
            product_details(
                ent_A_bis,
                ent_B_bis
            )
        )
        AB_details_bis = Matrix(
            vect_AB_details_bis,
            h_buff=0.35
        )

        A_bis, B_bis = Matrix(ent_A_bis), Matrix(ent_B_bis)
        AB_bis = Matrix(
            ent_AB_bis,
            h_buff=1
        )
        dispAB_bis = Group(
            A_bis, B_bis, AB_details_bis, AB_bis
        ).arrange_in_grid(
            buff=0.35,
            rows=2,
            cols=2,
            row_alignment="c"
        )
        title_ex4 = Title("Quatrième exemple 3 x 2 fois 2 x 4")
        self.play(
            ReplacementTransform(
                title_ex3, title_ex4
            ),
            ReplacementTransform(dispAB, dispAB_bis)
        )
        self.wait(5)

        ent_A = [[1, 2], [3, 4], [5, 6], [7, 8]]
        ent_B = [[9, 0, 1], [2, 3, 4]]
        ent_AB = multiply_matrix(ent_A, ent_B)
        ent_AB_details = product_details(ent_A, ent_B)
        
        vect_AB_details = from_matrix_to_column(
            product_details(
                ent_A,
                ent_B
            )
        )
        AB_details = Matrix(vect_AB_details)

        A, B = Matrix(ent_A), Matrix(ent_B)
        AB = Matrix(ent_AB)
        dispAB = Group(
            A, B, AB_details, AB
        ).arrange_in_grid(
            buff=0.45,
            rows=2,
            cols=2,
            row_alignment="c"
        )
        title_ex5 = Title("Cinquième exemple 4 x 2 fois 2 x 3")
        self.play(
            ReplacementTransform(
                title_ex4, title_ex5
            ),
            ReplacementTransform(dispAB_bis, dispAB)
        )
        self.wait(5)

        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_ex5, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class MultiplyMatrixEx1(Scene):
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

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_start, title_clap.scale(0.75)))
        self.wait()
        
        title_question = Title("Conditions de compatibilité")
        inbox1 = "À quelle(s) condition(s) un produit "
        inbox2 = "matriciel est-il compatible ?"
        inbox3 = "Écrivez-le dans les commentaires."
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            ReplacementTransform(title_clap, title_question.scale(0.75))
        )
        self.wait(2.5)

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_question,
                title_clap.scale(0.75)
            )
        )
        self.wait(1)

        title_rep = Title("Réponse")
        inbox1 = "Pour qu'un produit "
        inbox2 = "matriciel soit compatible,"
        inbox3 = "il faut que le nombre "
        inbox4 = "de colonnes de la matrice "
        inbox5 = "de gauche coïncide avec le "
        inbox6 = "nombre de lignes de la "
        inbox7 = "matrice de droite."
        inboxes = [
            inbox1, inbox2, inbox3,
            inbox4,
            inbox5, inbox6, inbox7
        ]
        msg2 = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            ReplacementTransform(
                msg,
                msg2.next_to(title_start, 3*DOWN)
            ),
            ReplacementTransform(title_clap, title_rep)
        )
        self.wait(5)

        self.play(
            FadeOut(msg2)
        )
        self.wait(1)
        
        ent_A = [[1, 2]]
        ent_B = [[1], [2]]
        ent_AB = multiply_matrix(ent_A, ent_B)
        ent_AB_details = product_details(ent_A, ent_B)
        vect_AB_details = from_matrix_to_column(
            product_details(
                ent_A,
                ent_B
            )
        )
        AB_details = Matrix(vect_AB_details)
        
        A, B, AB = Matrix(ent_A), Matrix(ent_B), Matrix(ent_AB)
        matrices_group = [A, B, AB_details, AB]
        dispAB = Group(
            *matrices_group
        ).arrange_in_grid(
            buff=0.5,
            rows=2,
            cols=2,
            row_alignment="c"
        )

        fix_matrices, move_matrices = surround_matrices_elts(matrices_group)
        
        matrices_rows_fix, matrices_cols_fix, matrices_elts_fix = fix_matrices
        A_rows_fix, B_rows_fix, AB_details_rows_fix, AB_rows_fix = matrices_rows_fix
        A_cols_fix, B_cols_fix, AB_details_cols_fix, AB_cols_fix = matrices_cols_fix
        A_elts_fix, B_elts_fix, AB_details_elts_fix, AB_elts_fix = matrices_elts_fix

        matrices_rows_move, matrices_cols_move, matrices_elts_move = move_matrices
        A_rows_move, B_rows_move, AB_details_rows_move, AB_rows_move = matrices_rows_move
        A_cols_move, B_cols_move, AB_details_cols_move, AB_cols_move = matrices_cols_move
        A_elts_move, B_elts_move, AB_details_elts_move, AB_elts_move = matrices_elts_move

        title_ex1 = Title("Premier exemple ")
        self.play(
            ReplacementTransform(
                title_rep, title_ex1
            ),
            FadeIn(dispAB),
            Write(A_rows_fix[0]),
            Write(B_cols_fix[0]),
            # Write(AB_details_rows_fix[0]),
            # Write(AB_rows_fix[0]),
        )
        self.wait(5)

        title_ex1_bis = Title("À gauche matrice 1 ligne x 3 colonnes")
        self.play(
            ReplacementTransform(
                title_ex1, title_ex1_bis
            ),
            ReplacementTransform(A_rows_move[0], AB_details_rows_move[0]),
            ReplacementTransform(B_cols_move[0], AB_details_rows_move[0]),
        )
        self.wait(2.75)

        title_ex1_ter = Title("À droite matrice 3 lignes x 1 colonne")
        self.play(
            ReplacementTransform(
                title_ex1_bis, title_ex1_ter
            ),
            ReplacementTransform(AB_details_rows_move[0], AB_rows_move[0]),
        )
        self.wait(3)

        
        self.play(
            Unwrite(A_rows_fix[0]),
            Unwrite(B_cols_fix[0]),
            Unwrite(AB_details_rows_fix[0]),
            Unwrite(AB_rows_fix[0]),
            Unwrite(AB_details_rows_move[0]),
            Unwrite(AB_rows_move[0]),
        )
        self.wait(2)

        title_ex1_res = Title("Résultat une matrice 1 ligne x 1 colonne")
        inbox1 = "En fait ce produit matriciel "
        inbox2 = "pourrait être interprété, "
        inbox3 = "comme un produit scalaire "
        inbox4 = "entre deux vecteurs de  "
        inbox5 = "dimension 3 dans l'espace. "
        inboxes = [
            inbox1, inbox2,
            inbox3,
            inbox4, inbox5
        ]
        msg3 = inbox_msg(*inboxes, font_size=40)
        self.play(
            ReplacementTransform(
                title_ex1_ter, title_ex1_res
            ),
            Write(msg3.next_to(title_ex1_res, DOWN))
        )
        self.wait(5)
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(ReplacementTransform(title_ex1_res, title_end.scale(0.75)))
        disp_sub(self, lang='fr')
