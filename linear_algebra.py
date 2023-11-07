from manim import *
import manim
import networkx as nx
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
    like_svg_path = "~/Documents/pics/svg/like.svg"
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    jpg_png_path = "~/Documents/pics/png/sabonner.png"
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        sub_pic = SVGMobject(sub_svg_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        sub_pic = ImageMobject(jpg_png_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(.5)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.add(like_pic.scale(sub_scale).next_to(sub_pic, LEFT))
    self.wait(0.1)



    
def put_sub_logo(self, svg_scale=0.25):
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    sub_pic = SVGMobject(sub_svg_path)
    self.play(
        FadeIn(
            sub_pic.scale(svg_scale).to_edge(2.5*UP)
        )
    )
    return sub_pic


    
def put_like_logo(self, sub_pic, svg_scale=0.25):
    like_svg_path = "~/Documents/pics/svg/like.svg"
    like_pic = SVGMobject(like_svg_path)
    self.play(
        FadeIn(
            like_pic.scale(svg_scale).next_to(sub_pic, LEFT)
        )
    )
    return like_pic


    
def put_youtube_short_logo(self, sub_pic, svg_scale=0.25):
    youtube_short_path = "~/Documents/pics/svg/Youtube_shorts.svg"
    youtube_shorts = SVGMobject(
        youtube_short_path,
        fill_opacity=1,
        fill_color=RED
    ).scale(svg_scale)
    self.play(
        FadeIn(
            youtube_shorts.next_to(sub_pic, RIGHT)
        )
    )
    return youtube_shorts


    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(2.5)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
        
    self.play(ReplacementTransform(part, full), run_time=2.5)
    self.wait(2.5)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)


    
def get_mat(init_ent, inv_ent, op_ent):
    colors = [RED, GREEN, BLUE]
    entries = [init_ent[i] + inv_ent[i] + op_ent[i] for i in range(3)]
    mat = Matrix(
        entries,
        v_buff = 1.5,
        h_buff = 1.5
    )

    ent_mat = mat.get_entries()
    for k in range(21):
        if k < 7:
            ent_mat[k].set_color(colors[0])
        elif k > 6 and k < 14:
            ent_mat[k].set_color(colors[1])
        elif k > 13 and k < 21:
            ent_mat[k].set_color(colors[2])
    
    return mat.scale(0.65)



def vect_text(name, coordinates):
    v_text = r"\overrightarrow{"
    v_text += f"{name}"
    v_text += r"} = \begin{pmatrix}"
    for x in coordinates:
        v_text += f"{x}"
        v_text += r"\\ "
    v_text += r"\end{pmatrix}"
    v = MathTex(v_text)
    return v


def family(*nc):
    v_names = [nc[i][0] for i in range(len(nc))]
    v_coords = [nc[i][1] for i in range(len(nc))]
    v = [vect_text(v_names[i], v_coords[i]) for i in range(len(nc))]
    return v
    


def vect2matrix(*v, name):
    A_text = f"{name} = " 
    A_text += r"\begin{bmatrix}"
    n = len(v)
    p = len(v[0])
    for j in range(p):
        for i in range(n):
            if i == n - 1:
                A_text += f"{v[i][j]}" + r"\\"
            else:
                A_text += f"{v[i][j]}" + r"&"
    A_text += r"\end{bmatrix}"
    A = MathTex(A_text)
    return A


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


    
class Family1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Algèbre linéaire")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        
        nc1 = ("v_1", [5, 3, 1])
        nc2 = ("v_2", [7, -2, 2])
        nc3 = ("v_3", [-11, 12, -4])
        
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = r"\mbox{" + f"{inbox}" + r"} \mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, DOWN)),
            Write(v3.next_to(v2, DOWN))
        )
        self.wait(2.5)
        
        inbox = "sont-ils libres dans "
        msg_text = r"\overrightarrow{v_1}, \overrightarrow{v_2}"
        msg_text += r"\mbox{ et } \overrightarrow{v_3} \mbox{ "
        msg_text += f"{inbox}"
        msg_text += r"}\mathbb{R}^3 ?"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            ReplacementTransform(msg, msg2.next_to(v3, DOWN))
        )
        self.wait(2)

        A_text = r"A = \begin{pmatrix}5&7&-11\\3&-2&12\\1&2&-4\end{pmatrix}"
        A = MathTex(A_text)
        
        inbox = "Cela revient à déterminer "
        msg_text = r"\mbox{"
        msg_text += f"{inbox}"
        msg_text += r"}\\"
        inbox2 = "si la matrice A est inversible."
        msg_text += r"\mbox{"
        msg_text += f"{inbox2}"
        msg_text += r"}\\"
        msg3 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        
        inbox = "Autrement dit, si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) \neq 0 \\"
        inbox2 = "alors la famille sera libre."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg4 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        
        inbox = "Et si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) = 0 \\"
        inbox2 = "alors la famille sera liée."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(A.next_to(title_start, 3*DOWN)),
            FadeOut(v3),
            ReplacementTransform(msg2, msg3.next_to(A, DOWN)),
            ReplacementTransform(v1, msg4.next_to(msg3, DOWN)),
            ReplacementTransform(v2, msg5.next_to(msg4, DOWN)),
        )
        self.wait(2)


        ent_A = [
            [5, 7, -11],
            [3, -2, 12],
            [1, 2, -4]
        ]

        A_mat = Matrix(
            ent_A,
            h_buff=1.5,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )
        
        lignes = ["L_1", "L_2", "L_3"]
        op_ent = [[ligne] for ligne in lignes]
        OP = Matrix(op_ent)

        det_op = Group(
            A_mat,
            OP
        ).arrange_in_grid(
            cols=2,
            buff=(.5, 1),
            row_alignments="c"
        )
        
        A_pivotL2 = SurroundingRectangle(A_mat.get_rows()[2])
        A_pivotL1 = SurroundingRectangle(A_mat.get_rows()[2])
        OP_pivotL2 = SurroundingRectangle(OP.get_rows()[2])
        OP_pivotL1 = SurroundingRectangle(OP.get_rows()[2])

        
        self.play(
            FadeOut(msg3),
            FadeOut(msg4),
            FadeOut(msg5),
            GrowFromCenter(det_op),
        )
        self.wait(2)

        self.play(
            Write(OP_pivotL1),
            Write(A_pivotL1)
        )
        self.wait(1.5)

        
        A_L_2 = SurroundingRectangle(A_mat.get_rows()[1])
        OP_L_2 = SurroundingRectangle(OP.get_rows()[1])
        A_L_1 = SurroundingRectangle(A_mat.get_rows()[0])
        OP_L_1 = SurroundingRectangle(OP.get_rows()[0])
        
        self.play(
            ReplacementTransform(A_pivotL2, A_L_2),
            ReplacementTransform(OP_pivotL2, OP_L_2),
            ReplacementTransform(A_pivotL1, A_L_1),
            ReplacementTransform(OP_pivotL1, OP_L_1),
        )
        self.wait(2)

        ent_A2 = [
            [0, -3, 9],
            [0, -8, 24],
            [1, 2, -4]
        ]
        A2 = Matrix(
            ent_A2,
            h_buff=1.5,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )

        
        lignes = ["L_1 - 5L_3", "L_2 - 3L_3", "L_3"]
        op_ent2 = [[L] for L in lignes]
        OP2 = Matrix(
            op_ent2,
            h_buff=2.75
        )

        det_op2 = Group(
            A2,
            OP2
        ).arrange_in_grid(
            cols=2,
            buff=(.5, 1),
            row_alignments="c"
        )
        
        A2_L_2 = SurroundingRectangle(A2.get_rows()[1])
        OP2_L_2 = SurroundingRectangle(OP2.get_rows()[1])
        A2_L_1 = SurroundingRectangle(A2.get_rows()[0])
        OP2_L_1 = SurroundingRectangle(OP2.get_rows()[0])
        
        self.play(
            ReplacementTransform(OP_L_2, OP2_L_2),
            ReplacementTransform(A_L_2, A2_L_2),
            ReplacementTransform(OP_L_1, OP2_L_1),
            ReplacementTransform(A_L_1, A2_L_1),
            ReplacementTransform(det_op, det_op2),
        )
        self.wait(2)

        ent_B = [
            [-3, 9],
            [-8, 24]
        ]
        B = Matrix(ent_B)
        #self.add(B)
        det_B = get_det_text(B, determinant=0, initial_scale_factor=1)

        self.play(
            FadeOut(OP2_L_1),
            FadeOut(A2_L_1),
            FadeOut(OP2_L_2),
            FadeOut(A2_L_2),
            FadeOut(det_op2),
            Write(det_B),
            Write(B)
        )
        self.wait(2)

        inbox7 = "Les vecteurs "
        msg7_text = r"\mbox{"
        msg7_text += f"{inbox7}"
        msg7_text += r"} "
        msg7 = MathTex(
            msg7_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        nc1 = ("v_1", [5, 3, 1])
        nc2 = ("v_2", [7, -2, 2])
        nc3 = ("v_3", [-11, 12, -4])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "forment une famille liée dans "
        msg8_text = r"\mbox{" + f"{inbox}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_B, DOWN)),
            Write(v1.next_to(msg7, DL)),
            Write(v2.next_to(v1, RIGHT)),
            Write(v3.next_to(v2, RIGHT)),
            Write(msg8.next_to(v2, DOWN)),
        )
        self.wait(1.5)

        ent_A3 = [
            [0, -1, 3],
            [0, -1, 3],
            [1, 2, -4]
        ]
        A3 = Matrix(
            ent_A3,
            v_buff=2,
            h_buff=1.5,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )

        lignes = [r"\frac{1}{3}L_1", r"\frac{1}{8}L_2", "L_3"]
        op_ent3 = [[L] for L in lignes]
        OP3 = Matrix(
            op_ent3,
            v_buff=2,
            h_buff=2.75,
        )

        A3_L_2 = SurroundingRectangle(A3.get_rows()[1])
        OP3_L_2 = SurroundingRectangle(OP3.get_rows()[1])
        A3_L_1 = SurroundingRectangle(A3.get_rows()[0])
        OP3_L_1 = SurroundingRectangle(OP3.get_rows()[0])

        det_op3 = Group(
            A3,
            OP3
        ).arrange_in_grid(
            cols=2,
            buff=(.5, 1),
            row_alignments="c"
        )
        
        self.play(
            FadeOut(det_B),
            FadeOut(B),
            FadeOut(msg7),
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
            FadeOut(msg8),
            GrowFromCenter(det_op3.next_to(A, DOWN))
        )
        self.wait(2)
        
        cl = r"-2\overrightarrow{v_1} + 3\overrightarrow{v_2} + "
        cl += r"\overrightarrow{v_3} = \overrightarrow{0}"
        self.play(
            Write(MathTex(cl).next_to(det_op3, DOWN))
        )
        self.wait(0.75)

        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class Family2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Algèbre linéaire")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        nc1 = ("v_1", [11, 3, -7])
        nc2 = ("v_2", [7, -2, 6])
        nc3 = ("v_3", [-3, -1, 0])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, DOWN)),
            Write(v3.next_to(v2, DOWN))
        )
        self.wait(2.5)
        
        inbox = "sont-ils libres dans "
        msg_text = r"\overrightarrow{v_1}, \overrightarrow{v_2}"
        msg_text += r"\mbox{ et } \overrightarrow{v_3} \mbox{ "
        msg_text += f"{inbox}"
        msg_text += r"}\mathbb{R}^3 ?"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            ReplacementTransform(msg, msg2.next_to(v3, DOWN))
        )
        self.wait(1)

        c1, c2, c3 = nc1[1], nc2[1], nc3[1]
        A = vect2matrix(c1, c2, c3, "A")
        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
        )
        self.wait(0.25)
        
        inbox = "Cela revient à déterminer "
        msg_text = r"\mbox{" + f"{inbox}" + r"}\\"
        inbox2 = "si la matrice A est inversible."
        msg_text += r"\mbox{" + f"{inbox2}" + r"}\\"
        msg3 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )

        self.play(
            Write(A.next_to(title_start, 3*DOWN)),
            ReplacementTransform(msg2, msg3.next_to(A, DOWN)),
        )
        self.wait(1)
        
        inbox3 = "Autrement dit, si "
        msg_text = r"\mbox{" + f"{inbox3}"
        msg_text += r"} \det(A) \neq 0 \\"
        inbox4 = "alors la famille sera libre."
        msg_text += r"\mbox{" + f"{inbox4}"
        msg4 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg4.next_to(msg3, DOWN))
        )
        
        inbox5 = "Et si "
        msg_text = r"\mbox{" + f"{inbox5}"
        msg_text += r"} \det(A) = 0 \\"
        inbox6 = "alors la famille sera liée."
        msg_text += r"\mbox{" + f"{inbox6}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg5.next_to(msg4, DOWN)),
        )
        self.wait(1)


        ent_A = [
            [11, 7, -3],
            [3, -2, -1],
            [-7, 6, 0]
        ]

        A_mat = Matrix(
            ent_A,
            h_buff=2.5,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )
        
        #colonnes = ["C_1", "C_2", "C_3"]
        #op_ent = [[C] for C in colonnes]
        op_ent = [["C_1", "C_2", "C_3"]]
        OP = Matrix(
            op_ent,
            h_buff=2.5
        )

        det_op = Group(OP, A_mat).arrange_in_grid(
            rows=2,
            cols=1,
            buff=(0.5, 0.25),
            col_alignments="c"
        )
        
        A_pivotC1C2 = SurroundingRectangle(A_mat.get_columns()[0])
        A_pivotC1C3 = SurroundingRectangle(A_mat.get_columns()[0])
        OP_pivotC1C2 = SurroundingRectangle(OP.get_columns()[0])
        OP_pivotC1C3 = SurroundingRectangle(OP.get_columns()[0])

        
        self.play(
            FadeOut(msg3),
            FadeOut(msg4),
            FadeOut(msg5),
            GrowFromCenter(det_op),
        )
        self.wait(2)

        self.play(
            Write(OP_pivotC1C2),
            Write(A_pivotC1C2)
        )
        self.wait(1.5)

        
        A_C_2 = SurroundingRectangle(A_mat.get_columns()[1])
        OP_C_2 = SurroundingRectangle(OP.get_columns()[1])
        A_C_3 = SurroundingRectangle(A_mat.get_columns()[2])
        OP_C_3 = SurroundingRectangle(OP.get_columns()[2])
        
        self.play(
            ReplacementTransform(A_pivotC1C2, A_C_2),
            ReplacementTransform(OP_pivotC1C2, OP_C_2),
            ReplacementTransform(A_pivotC1C3, A_C_3),
            ReplacementTransform(OP_pivotC1C3, OP_C_3),
        )
        self.wait(2)

        ent_A2 = [
            [11, 115, 3],
            [3, 4, 1],
            [-7, 0, 0]
        ]
        A2 = Matrix(
            ent_A2,
            h_buff=2.75,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )

        
        op_ent2 = [["C_1", "6C_1 + 7C_2", "-C_3"]]
        OP2 = Matrix(
            op_ent2,
            h_buff=2.75
        )

        det_op2 = Group(
            OP2,
            A2,
        ).arrange_in_grid(
            rows=2,
            cols=1,
            buff=(0.5, 0.25),
            col_alignments="c"
        )
        
        A2_C_2 = SurroundingRectangle(A2.get_columns()[1])
        OP2_C_2 = SurroundingRectangle(OP2.get_columns()[1])
        A2_C_3 = SurroundingRectangle(A2.get_columns()[2])
        OP2_C_3 = SurroundingRectangle(OP2.get_columns()[2])
        
        self.play(
            ReplacementTransform(OP_C_2, OP2_C_2),
            ReplacementTransform(A_C_2, A2_C_2),
            ReplacementTransform(OP_C_3, OP2_C_3),
            ReplacementTransform(A_C_3, A2_C_3),
            ReplacementTransform(det_op, det_op2),
        )
        self.wait(2)

        ent_B = [
            [115, 3],
            [4, 1]
        ]
        B = Matrix(ent_B)

        det_B = get_det_text(B, determinant=103, initial_scale_factor=1)

        self.play(
            FadeOut(OP2_C_2),
            FadeOut(A2_C_2),
            FadeOut(OP2_C_3),
            FadeOut(A2_C_3),
            FadeOut(det_op2),
            Write(det_B),
            Write(B)
        )
        self.wait(2)

        inbox7 = "Les vecteurs "
        msg7_text = r"\mbox{" + f"{inbox7}" + r"} "
        msg7 = MathTex(
            msg7_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        nc1 = ("v_1", [11, 3, -7])
        nc2 = ("v_2", [7, -2, 6])
        nc3 = ("v_3", [-3, -1, 0])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox8 = "forment une famille libre dans "
        msg8_text = r"\mbox{" + f"{inbox8}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_B, DOWN)),
            Write(v1.next_to(msg7, DL)),
            Write(v2.next_to(v1, RIGHT)),
            Write(v3.next_to(v2, RIGHT)),
            Write(msg8.next_to(v2, DOWN)),
        )
        self.wait(2.5)

        A_det = Matrix(
            ent_A,
            h_buff=1.25,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )
        
        det_A = r"\begin{vmatrix}11&7&-3\\3&-2&-1\\-7&6&0\end{vmatrix}"
        det_A += " = -721"
        det_A = MathTex(det_A)
        
        inbox9 = "Une famille libre de 3 vecteurs dans "
        msg9_text = r"\mbox{" + f"{inbox9}"
        msg9_text += r"} \mathbb{R}^3 \\ \mbox{"
        inbox10 = "est maximale donc c'est une base de "
        msg9_text += f"{inbox10}" + r"} \mathbb{R}^3"
        msg9 = MathTex(
            msg9_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            FadeOut(B),
            ReplacementTransform(det_B, det_A.next_to(A, DOWN)),
            ReplacementTransform(msg7, msg9.next_to(det_A, DOWN)),
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
class Family3(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Algèbre linéaire")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        nc1 = ("v_1", [1, 5, -4])
        nc2 = ("v_2", [8, -2, 6])
        nc3 = ("v_3", [10, 3, 2])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, DOWN)),
            Write(v3.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        inbox = "sont-ils libres dans "
        msg_text = r"\overrightarrow{v_1}, \overrightarrow{v_2}"
        msg_text += r"\mbox{ et } \overrightarrow{v_3} \mbox{ "
        msg_text += f"{inbox}"
        msg_text += r"}\mathbb{R}^3 ?"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            ReplacementTransform(msg, msg2.next_to(v3, DOWN))
        )
        self.wait(1)

        c1, c2, c3 = nc1[1], nc2[1], nc3[1]
        A = vect2matrix(c1, c2, c3, "A")
        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
        )
        self.wait(0.25)
        
        inbox = "Cela revient à déterminer "
        msg_text = r"\mbox{" + f"{inbox}" + r"}\\"
        inbox2 = "si la matrice A est inversible."
        msg_text += r"\mbox{" + f"{inbox2}" + r"}\\"
        msg3 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )

        self.play(
            Write(A.next_to(title_start, 3*DOWN)),
            ReplacementTransform(msg2, msg3.next_to(A, DOWN)),
        )
        self.wait(1)
        
        inbox = "Autrement dit, si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) \neq 0 \\"
        inbox2 = "alors la famille sera libre."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg4 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg4.next_to(msg3, DOWN))
        )
        
        inbox = "Et si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) = 0 \\"
        inbox2 = "alors la famille sera liée."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg5.next_to(msg4, DOWN)),
        )
        self.wait(1)


        ent_A = [
            [1, 8, 10],
            [5, -2, 3],
            [-4, 6, 2]
        ]

        A_mat = Matrix(ent_A)
        
        colonnes = ["C_1", "C_2", "C_3"]
        op_ent = [[C] for C in colonnes]
        OP = Matrix(op_ent)

        det_op = Group(A_mat, OP).arrange(buff=1.5)
        
        A_pivotC1C2 = SurroundingRectangle(A_mat.get_columns()[0])
        A_pivotC1C3 = SurroundingRectangle(A_mat.get_columns()[0])
        OP_pivotL1L2 = SurroundingRectangle(OP.get_rows()[0])
        OP_pivotL1L3 = SurroundingRectangle(OP.get_rows()[0])
        
        self.play(
            FadeOut(msg3),
            FadeOut(msg4),
            FadeOut(msg5),
            GrowFromCenter(det_op),
        )
        self.wait(2)

        self.play(
            Write(OP_pivotL1L2),
            Write(A_pivotC1C2),
            Write(OP_pivotL1L3),
            Write(A_pivotC1C3)
        )
        self.wait(2.5)

        
        ent_A2 = [
            [1, 0, 0],
            [5, -42, -47],
            [-4, 38, 42]
        ]
        A2 = Matrix(ent_A2)

        
        A_C_2 = SurroundingRectangle(A_mat.get_columns()[1])
        OP_L_2 = SurroundingRectangle(OP.get_rows()[1])
        A_C_3 = SurroundingRectangle(A_mat.get_columns()[2])
        OP_L_3 = SurroundingRectangle(OP.get_rows()[2])
        
        self.play(
            ReplacementTransform(A_pivotC1C2, A_C_2),
            ReplacementTransform(OP_pivotL1L2, OP_L_2),
            ReplacementTransform(A_pivotC1C3, A_C_3),
            ReplacementTransform(OP_pivotL1L3, OP_L_3),
            Write(OP_L_3),
        )
        self.wait(2)
        
        colonnes = ["C_1", "C_2 - 8C_1", "C_3 - 10C_1"]
        op_ent2 = [[C] for C in colonnes]
        OP2 = Matrix(op_ent2)

        det_op2 = Group(A2, OP2).arrange(buff=1)
        
        A2_C_2 = SurroundingRectangle(A2.get_columns()[1])
        OP2_L_2 = SurroundingRectangle(OP2.get_rows()[1])
        A2_C_3 = SurroundingRectangle(A2.get_columns()[2])
        OP2_L_3 = SurroundingRectangle(OP2.get_rows()[2])
        
        self.play(
            ReplacementTransform(OP_L_2, OP2_L_2),
            ReplacementTransform(A_C_2, A2_C_2),
            ReplacementTransform(OP_L_3, OP2_L_3),
            ReplacementTransform(A_C_3, A2_C_3),
            ReplacementTransform(det_op, det_op2),
        )
        self.wait(2)

        ent_B = [
            [-42, -47],
            [38, 42]
        ]
        B = Matrix(ent_B)
        #self.add(B)
        det_B = get_det_text(B, determinant=22, initial_scale_factor=1)

        self.play(
            FadeOut(OP2_L_2),
            FadeOut(A2_C_2),
            FadeOut(OP2_L_3),
            FadeOut(OP_L_3),
            FadeOut(A2_C_3),
            FadeOut(det_op2),
            Write(det_B),
            Write(B)
        )
        self.wait(2)

        inbox7 = "Les vecteurs "
        msg7_text = r"\mbox{" + f"{inbox7}" + r"} "
        msg7 = MathTex(
            msg7_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        nc1 = ("v_1", [1, 5, -4])
        nc2 = ("v_2", [8, -2, 6])
        nc3 = ("v_3", [10, 3, 2])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "forment une famille libre dans "
        msg8_text = r"\mbox{" + f"{inbox}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_B, DOWN)),
            Write(v1.next_to(msg7, DL)),
            Write(v2.next_to(v1, RIGHT)),
            Write(v3.next_to(v2, RIGHT)),
            Write(msg8.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        det_A = get_det_text(
            A_mat,
            determinant=22,
            initial_scale_factor=1
        )
        inbox = "Une famille libre de 3 vecteurs dans "
        msg9_text = r"\mbox{" + f"{inbox}"
        msg9_text += r"} \mathbb{R}^3 \\ \mbox{"
        inbox2 = "est maximale donc c'est une base de "
        msg9_text += f"{inbox2}" + r"} \mathbb{R}^3"
        msg9 = MathTex(
            msg9_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            ReplacementTransform(B, A_mat.next_to(A, DOWN)),
            ReplacementTransform(det_B, det_A.next_to(A, DOWN)),
            ReplacementTransform(msg7, msg9.next_to(det_A, DOWN)),
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        

class Family4(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Algèbre linéaire")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        nc1 = ("v_1", [6, -2, 7])
        nc2 = ("v_2", [10, -18, 3])
        nc3 = ("v_3", [2, 3, 4])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, DOWN)),
            Write(v3.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        inbox = "sont-ils libres dans "
        msg_text = r"\overrightarrow{v_1}, \overrightarrow{v_2}"
        msg_text += r"\mbox{ et } \overrightarrow{v_3} \mbox{ "
        msg_text += f"{inbox}"
        msg_text += r"}\mathbb{R}^3 ?"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            ReplacementTransform(msg, msg2.next_to(v3, DOWN))
        )
        self.wait(1)

        c1, c2, c3 = nc1[1], nc2[1], nc3[1]
        A = vect2matrix(c1, c2, c3, "A")
        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
        )
        self.wait(0.25)
        
        inbox = "Cela revient à déterminer "
        msg_text = r"\mbox{" + f"{inbox}" + r"}\\"
        inbox2 = "si la matrice A est inversible."
        msg_text += r"\mbox{" + f"{inbox2}" + r"}\\"
        msg3 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )

        self.play(
            Write(A.next_to(title_start, 3*DOWN)),
            ReplacementTransform(msg2, msg3.next_to(A, DOWN)),
        )
        self.wait(1)
        
        inbox = "Autrement dit, si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) \neq 0 \\"
        inbox2 = "alors la famille sera libre."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg4 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg4.next_to(msg3, DOWN))
        )
        
        inbox = "Et si "
        msg_text = r"\mbox{" + f"{inbox}"
        msg_text += r"} \det(A) = 0 \\"
        inbox2 = "alors la famille sera liée."
        msg_text += r"\mbox{" + f"{inbox2}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(msg5.next_to(msg4, DOWN)),
        )
        self.wait(1)


        ent_A = [
            [6, 10, 2],
            [-2, -18, 3],
            [7, 5, 4]
        ]

        A_mat = Matrix(
            ent_A,
            left_bracket=r"\lvert",
            right_bracket=r"\rvert",
        )
        
        colonnes = ["C_1", "C_2", "C_3"]
        op_ent = [[C] for C in colonnes]
        OP = Matrix(op_ent)

        det_op = Group(A_mat, OP).arrange(buff=1.5)
        
        A_pivotC3C1 = SurroundingRectangle(A_mat.get_columns()[2])
        A_pivotC3C2 = SurroundingRectangle(A_mat.get_columns()[2])
        OP_pivotL3L1 = SurroundingRectangle(OP.get_rows()[2])
        OP_pivotL3L2 = SurroundingRectangle(OP.get_rows()[2])
        
        self.play(
            FadeOut(msg3),
            FadeOut(msg4),
            FadeOut(msg5),
            GrowFromCenter(det_op),
        )
        self.wait(2)

        self.play(
            Write(OP_pivotL3L1),
            Write(A_pivotC3C1),
            Write(OP_pivotL3L2),
            Write(A_pivotC3C2)
        )
        self.wait(2.5)

        
        ent_A2 = [
            [0, 0, 2],
            [-11, -33, 3],
            [-5, -15, 4]
        ]
        A2 = Matrix(ent_A2)

        
        A_C_1 = SurroundingRectangle(A_mat.get_columns()[0])
        OP_L_1 = SurroundingRectangle(OP.get_rows()[0])
        A_C_2 = SurroundingRectangle(A_mat.get_columns()[1])
        OP_L_2 = SurroundingRectangle(OP.get_rows()[1])
        
        self.play(
            ReplacementTransform(A_pivotC3C1, A_C_1),
            ReplacementTransform(OP_pivotL3L1, OP_L_1),
            ReplacementTransform(A_pivotC3C2, A_C_2),
            ReplacementTransform(OP_pivotL3L2, OP_L_2),
        )
        self.wait(2)
        
        colonnes = ["C_1 - 3C_3", "C_2 - 10C_3", "C_3"]
        op_ent2 = [[C] for C in colonnes]
        OP2 = Matrix(op_ent2)

        det_op2 = Group(A2, OP2).arrange(buff=1)
        
        A2_C_1 = SurroundingRectangle(A2.get_columns()[0])
        OP2_L_1 = SurroundingRectangle(OP2.get_rows()[0])
        A2_C_2 = SurroundingRectangle(A2.get_columns()[1])
        OP2_L_2 = SurroundingRectangle(OP2.get_rows()[1])
        
        self.play(
            ReplacementTransform(OP_L_1, OP2_L_1),
            ReplacementTransform(A_C_1, A2_C_1),
            ReplacementTransform(OP_L_2, OP2_L_2),
            ReplacementTransform(A_C_2, A2_C_2),
            ReplacementTransform(det_op, det_op2),
        )
        self.wait(2)

        ent_B = [
            [-11, -33],
            [-5, -15]
        ]
        B = Matrix(ent_B)
        #self.add(B)
        det_B = get_det_text(B, determinant=0, initial_scale_factor=1)

        self.play(
            FadeOut(OP2_L_1),
            FadeOut(A2_C_1),
            FadeOut(OP2_L_2),
            FadeOut(A2_C_2),
            FadeOut(det_op2),
            Write(det_B),
            Write(B)
        )
        self.wait(2)

        inbox7 = "Les vecteurs "
        msg7_text = r"\mbox{" + f"{inbox7}" + r"} "
        msg7 = MathTex(
            msg7_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        nc1 = ("v_1", [6, -2, 7])
        nc2 = ("v_2", [10, -18, 5])
        nc3 = ("v_3", [2, 3, 4])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "forment une famille liée dans "
        msg8_text = r"\mbox{" + f"{inbox}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_B, DOWN)),
            Write(v1.next_to(msg7, DL)),
            Write(v2.next_to(v1, RIGHT)),
            Write(v3.next_to(v2, RIGHT)),
            Write(msg8.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        det_A = get_det_text(
            A_mat,
            determinant=0,
            initial_scale_factor=1
        )

        ent_A = [
            [6, 10, 2],
            [-2, -18, 3],
            [7, 5, 4]
        ]

        A_mat = Matrix(ent_A)
        cl = r"3\overrightarrow{v_1} + \overrightarrow{v_2} - "
        cl += r"4\overrightarrow{v_3} = \overrightarrow{0}"

        self.play(
            ReplacementTransform(B, A_mat.next_to(A, DOWN)),
            ReplacementTransform(det_B, det_A.next_to(A, DOWN)),
            Write(MathTex(cl).next_to(det_A, DOWN))
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        

class Method2Family4(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Méthode du pivot de Gauss")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        nc1 = ("v_1", [6, -2, 7])
        nc2 = ("v_2", [10, -18, 3])
        nc3 = ("v_3", [2, 3, 4])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, DOWN)),
            Write(v3.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        inbox = "Pour montrer si c'est une famille libre ou pas, "
        msg_text = r"\mbox{" + f"{inbox}" + r"} \\"
        inbox2 = "on va résoudre le système avec la méthode du pivot."
        msg_text += r"\mbox{" + f"{inbox2}" + r"}"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        
        self.play(
            ReplacementTransform(msg, msg2.next_to(v3, DOWN))
        )
        self.wait(2)

        c1, c2, c3 = nc1[1], nc2[1], nc3[1]
        A = vect2matrix(c1, c2, c3, "A")
        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
            FadeOut(msg2)
        )
        self.wait(0.25)
        


        ent_A = [
            [6, 10, 2],
            [-2, -18, 3],
            [7, 5, 4]
        ]

        A_mat = Matrix(ent_A)

        ent_I = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

        I_mat = Matrix(ent_I)
        
        lignes = ["L_1", "L_2", "L_3"]
        op_ent = [[L] for L in lignes]
        OP = Matrix(op_ent)

        det_op = Group(
            A_mat,
            I_mat,
            OP
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=1
        )
        
        A_pivotL1L2 = SurroundingRectangle(A_mat.get_rows()[0])
        A_pivotL1L3 = SurroundingRectangle(A_mat.get_rows()[0])
        I_pivotL1L2 = SurroundingRectangle(I_mat.get_rows()[0])
        I_pivotL1L3 = SurroundingRectangle(I_mat.get_rows()[0])
        OP_pivotL1L2 = SurroundingRectangle(OP.get_rows()[0])
        OP_pivotL1L3 = SurroundingRectangle(OP.get_rows()[0])
        
        self.play(
            GrowFromCenter(det_op),
        )
        self.wait(2)

        self.play(
            Write(OP_pivotL1L2),
            Write(I_pivotL1L2),
            Write(A_pivotL1L2),
            Write(OP_pivotL1L3),
            Write(I_pivotL1L3),
            Write(A_pivotL1L3)
        )
        self.wait(2.5)

        
        A_L_2 = SurroundingRectangle(A_mat.get_rows()[1])
        I_L_2 = SurroundingRectangle(I_mat.get_rows()[1])
        OP_L_2 = SurroundingRectangle(OP.get_rows()[1])
        A_L_3 = SurroundingRectangle(A_mat.get_rows()[2])
        I_L_3 = SurroundingRectangle(I_mat.get_rows()[2])
        OP_L_3 = SurroundingRectangle(OP.get_rows()[2])
        
        self.play(
            ReplacementTransform(A_pivotL1L2, A_L_2),
            ReplacementTransform(I_pivotL1L2, I_L_2),
            ReplacementTransform(OP_pivotL1L2, OP_L_2),
            ReplacementTransform(A_pivotL1L3, A_L_3),
            ReplacementTransform(I_pivotL1L3, I_L_3),
            ReplacementTransform(OP_pivotL1L3, OP_L_3),
        )
        self.wait(2)

        ent_A2 = [
            [6, 10, 2],
            [0, -42, 11],
            [0, 40, -10]
        ]
        A2 = Matrix(ent_A2)

        ent_I2 = [
            [1, 0, 0],
            [1, 3, 0],
            [7, 0, -6]
        ]
        I2 = Matrix(ent_I2)

        
        lignes = ["L_1", "L_1 + 3L_2", "7L_1 - 6L_3"]
        op_ent2 = [[L] for L in lignes]
        OP2 = Matrix(op_ent2)

        det_op2 = Group(
            A2,
            I2,
            OP2
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=1
        )
        
        A2_L_2 = SurroundingRectangle(A2.get_rows()[1])
        I2_L_2 = SurroundingRectangle(I2.get_rows()[1])
        OP2_L_2 = SurroundingRectangle(OP2.get_rows()[1])
        A2_L_3 = SurroundingRectangle(A2.get_rows()[2])
        I2_L_3 = SurroundingRectangle(I2.get_rows()[2])
        OP2_L_3 = SurroundingRectangle(OP2.get_rows()[2])
        
        self.play(
            ReplacementTransform(OP_L_2, OP2_L_2),
            ReplacementTransform(I_L_2, I2_L_2),
            ReplacementTransform(A_L_2, A2_L_2),
            ReplacementTransform(OP_L_3, OP2_L_3),
            ReplacementTransform(I_L_3, I2_L_3),
            ReplacementTransform(A_L_3, A2_L_3),
            ReplacementTransform(det_op, det_op2),
        )
        self.wait(2)

        ent_A3 = [
            [6, 10, 2],
            [0, -42, 11],
            [0, 0, -7/2]
        ]
        A3 = Matrix(ent_A3)

        ent_I3 = [
            [1, 0, 0],
            [r"\frac{1}{3}", 1, 0],
            [r"\frac{167}{60}", 1, r"-\frac{21}{10}"]
        ]
        I3 = Matrix(ent_I3)

        
        lignes = ["L_1", "L_2/3", "7L_3/20 + L_2/3"]
        op_ent3 = [[L] for L in lignes]
        OP3 = Matrix(op_ent3)

        det_op3 = Group(
            A3,
            I3,
            OP3
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=1
        )

        A3_L_2 = SurroundingRectangle(A3.get_rows()[1])
        I3_L_2 = SurroundingRectangle(I3.get_rows()[1])
        OP3_L_2 = SurroundingRectangle(OP3.get_rows()[1])
        A3_L_3 = SurroundingRectangle(A3.get_rows()[2])
        I3_L_3 = SurroundingRectangle(I3.get_rows()[2])
        OP3_L_3 = SurroundingRectangle(OP3.get_rows()[2])

        self.play(
            ReplacementTransform(OP2_L_2, OP3_L_2),
            ReplacementTransform(I2_L_2, I3_L_2),
            ReplacementTransform(A2_L_2, A3_L_2),
            ReplacementTransform(OP2_L_3, OP3_L_3),
            ReplacementTransform(I2_L_3, I3_L_3),
            ReplacementTransform(A2_L_3, A3_L_3),
            ReplacementTransform(det_op2, det_op3),
        )
        self.wait(2)

        ent_A4 = [
            [42, 70, 0],
            [0, -42, 0],
            [0, 0, 1]
        ]
        A4 = Matrix(ent_A4)

        ent_I4 = [
            [1, 0, 0],
            [r"\frac{1}{3}", 1, 0],
            [r"-\frac{167}{210}", r"-\frac{2}{7}", r"\frac{3}{5}"]
        ]
        I4 = Matrix(ent_I4)

        
        lignes = ["7L_1 + 4L_3", "L_2 + 22L_3/7", "-2L_3/7"]
        op_ent4 = [[L] for L in lignes]
        OP4 = Matrix(op_ent4)

        det_op4 = Group(
            A4,
            I4,
            OP4
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=1
        )

        A4_L_1 = SurroundingRectangle(A4.get_rows()[0])
        A4_L_2 = SurroundingRectangle(A4.get_rows()[1])
        A4_L_3 = SurroundingRectangle(A4.get_rows()[2])

        I4_L_1 = SurroundingRectangle(I4.get_rows()[0])
        I4_L_2 = SurroundingRectangle(I4.get_rows()[1])
        I4_L_3 = SurroundingRectangle(I4.get_rows()[2])

        OP4_L_1 = SurroundingRectangle(OP4.get_rows()[0])
        OP4_L_2 = SurroundingRectangle(OP4.get_rows()[1])
        OP4_L_3 = SurroundingRectangle(OP4.get_rows()[2])
        
        
        self.play(
            Write(A4_L_1),
            Write(I4_L_1),
            Write(OP4_L_1),
            ReplacementTransform(OP3_L_2, OP4_L_2),
            ReplacementTransform(I3_L_2, I4_L_2),
            ReplacementTransform(A3_L_2, A4_L_2),
            ReplacementTransform(OP3_L_3, OP4_L_3),
            ReplacementTransform(I3_L_3, I4_L_3),
            ReplacementTransform(A3_L_3, A4_L_3),
            ReplacementTransform(det_op3, det_op4),
        )
        self.wait(2)
        
        inbox7 = "Les vecteurs "
        msg7_text = r"\mbox{" + f"{inbox7}" + r"} "
        msg7 = MathTex(
            msg7_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        
        nc1 = ("v_1", [6, -2, 7])
        nc2 = ("v_2", [10, -18, 5])
        nc3 = ("v_3", [2, 3, 4])
        v1, v2, v3 = family(nc1, nc2, nc3)
        
        inbox = "forment une famille liée dans "
        msg8_text = r"\mbox{" + f"{inbox}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_op4, DOWN)),
            Write(v1.next_to(msg7, DL)),
            Write(v2.next_to(v1, RIGHT)),
            Write(v3.next_to(v2, RIGHT)),
            Write(msg8.next_to(v2, DOWN)),
        )
        self.wait(2.5)
        
        det_A = get_det_text(
            A_mat,
            determinant=0,
            initial_scale_factor=1
        )

        ent_A = [
            [6, 10, 2],
            [-2, -18, 3],
            [7, 5, 4]
        ]

        A_mat = Matrix(ent_A)
        cl = r"3\overrightarrow{v_1} + \overrightarrow{v_2} - "
        cl += r"4\overrightarrow{v_3} = \overrightarrow{0}"

        self.play(
            Write(A_mat.next_to(A, DOWN)),
            FadeIn(det_A.next_to(A, DOWN)),
            Write(MathTex(cl).next_to(det_A, DOWN))
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

        
        
        
class ApplyMatrix1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Effet géométrique d'une matrice")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        plane = NumberPlane()
        
        nc1 = ("v_1", [0, 1])
        nc2 = ("v_2", [1, 1])
        v1, v2 = family(nc1, nc2)

        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^2"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        cs = [nc1[1], nc2[1]]
        vec1 = Vector(cs[0], color=RED)
        vec2 = Vector(cs[1], color=GREEN)
        lab1 = vec1.coordinate_label(color=RED)
        lab2 = vec2.coordinate_label(color=GREEN)
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, RIGHT)),
            Write(plane),
            *[Write(vec) for vec in [vec1, vec2]],
            # *[Write(lab) for lab in [lab1, lab2]],
            Write(lab1.next_to(vec1, UL)),
            Write(lab2.next_to(vec2, UR)),
        )
        self.wait(2.5)

        c1, c2 = nc1[1], nc2[1]
        A_text = vect2matrix(c1, c2, name="A")
        inbox = "Voici la matrice associée "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        msg2_origin = msg2
        self.play(
            ReplacementTransform(
                msg,
                msg2.next_to(title_start, 3*DOWN)
            ),
            FadeOut(v1),
            FadeOut(v2),
            Write(A_text.next_to(msg2, DOWN))
        )
        self.wait(2.5)

        mat_A = [[1, 0], [1, 1]]
        self.play(
            ApplyMatrix(mat_A, msg2),
            ApplyMatrix(mat_A, plane)
        )
        self.wait(2.5)


        inbox1 = "Que faut-il faire "
        inbox2 = "pour revenir en arrière ?"
        inbox3 = "Écrivez votre réponse "
        inbox4 = "dans les commentaires."
        inboxes = [inbox1, inbox2, inbox3, inbox4]
        msg3 = inbox_msg(inboxes, font_size=37)
        self.play(
            Write(msg3.next_to(vec1, 2*DOWN))
        )
        self.wait(3)

        inbox1 = "Il appliquer la matrice inverse."
        inbox2 = "Calculons-la."
        inboxes = [inbox1, inbox2]
        msg4 = inbox_msg(inboxes, font_size=37)
        self.play(
            ReplacementTransform(
                msg3,
                msg4.next_to(vec1, 3*DOWN)
            ),
        )
        self.wait(2.5)

        ent_A = [[0, 1], [1, 1]]
        A = Matrix(ent_A)
        
        ent_I = [[1, 0], [0, 1]]
        I = Matrix(ent_I)

        lignes = ["L_1", "L_2"]
        op_ent = [[L] for L in lignes]
        OP = Matrix(
            op_ent,
            h_buff=1.5
        )

        det_op = Group(
            A,
            I,
            OP
        ).arrange_in_grid(
            rows=1,
            cols=3,
            buff=(0.5, 0.5),
            #col_alignments="c"
        )

        
        self.play(
            GrowFromCenter(det_op.next_to(msg4, 2*DOWN)),
        )
        self.wait(0.5)

        
        ent_A2 = [[1, 1], [0, 1]]
        A2 = Matrix(ent_A2)
        
        ent_I2 = [[0, 1], [1, 0]]
        I2 = Matrix(ent_I2)
        
        ent_OP2 = [["L_2"], ["L_1"]]
        OP2 = Matrix(ent_OP2)

        det_op2 = Group(
            A2,
            I2,
            OP2
        ).arrange_in_grid(
            rows=1,
            cols=3,
            buff=(0.5, 0.5),
            #col_alignments="c"
        )
        
        
        self.play(
            ReplacementTransform(det_op, det_op2.next_to(msg4, 2*DOWN)),
        )
        self.wait(2)

        
        ent_A3 = [[1, 0], [0, 1]]
        A3 = Matrix(
            ent_A3,
        )
        
        ent_I3 = [[-1, 1], [1, 0]]
        I3 = Matrix(
            ent_I3,
        )
        
        ent_OP3 = [["L_2 - L_1"], ["L_1"]]
        OP3 = Matrix(
            ent_OP3,
            h_buff=1.75
        )

        det_op3 = Group(
            A3,
            I3,
            OP3
        ).arrange_in_grid(
            rows=1,
            cols=3,
            buff=(0.5, 0.5),
            #col_alignments="c"
        )
        
        
        self.play(
            ReplacementTransform(
                det_op2,
                det_op3.next_to(msg4, 2*DOWN)
            ),
        )
        self.wait(2)

        c1, c2 = [-1, 1], [1, 0]
        inv_A_text = vect2matrix(c1, c2, name=r"A^{-1}")
        inbox = "Voici la matrice inverse "
        msg_text = r"\mbox{" + f"{inbox}" + r"}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            ReplacementTransform(
                msg4,
                msg5.next_to(det_op3, DOWN)
            ),
            Write(inv_A_text.next_to(msg5, DOWN))
        )
        self.wait(2.5)

        mat_inv_A = [[-1, 1], [1, 0]]
        self.play(
            ApplyMatrix(mat_inv_A, msg2),
            ApplyMatrix(mat_inv_A, plane)
        )
        self.wait(2)

        vec3 = Vector([3, -2], color=PINK)
        lab3 = vec3.coordinate_label(color=PINK)
        
        vec4 = Vector([3, 0], color=ORANGE)
        lab4 = vec4.coordinate_label(color=ORANGE)
        
        vec5 = Vector([-3, 2], color=YELLOW)
        lab5 = vec5.coordinate_label(color=YELLOW)
        
        vec6 = Vector([-2, -2])
        lab6 = vec6.coordinate_label()

        vecs = [vec3, vec4, vec5, vec6]
        labs = [lab3, lab4, lab5, lab6]
        
        self.play(
            FadeOut(det_op3),
            *[Write(vec) for vec in vecs],
            *[Write(lab) for lab in labs],
        )
        self.wait(2)

        self.play(
            ApplyMatrix(mat_A, msg2),
            ApplyMatrix(mat_A, plane)
        )
        self.wait(2.5)

        self.play(
            ApplyMatrix(mat_inv_A, msg2),
            ApplyMatrix(mat_inv_A, plane)
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

class ApplyMatrix2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Effet géométrique d'une matrice")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)


        # C-x C-t transpose line

        plane = NumberPlane()
        
        nc1 = ("v_1", [1, 1])
        nc2 = ("v_2", [0, 1])
        v1, v2 = family(nc1, nc2)

        inbox = "Considérons la famille de vecteurs de "
        msg_text = r"\mbox{" + f"{inbox}" + r"}"
        msg_text += "\mathbb{R}^2"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        cs = [nc1[1], nc2[1]]
        vec1 = Vector(cs[0], color=RED)
        vec2 = Vector(cs[1], color=GREEN)
        lab1 = vec1.coordinate_label(color=RED)
        lab2 = vec2.coordinate_label(color=GREEN)
        self.play(
            Write(msg.next_to(title_start, 3*DOWN)),
            Write(v1.next_to(msg, DOWN)),
            Write(v2.next_to(v1, RIGHT)),
            Write(plane),
        )
        self.wait(1.75)

        self.play(
            Write(vec1),
            Write(lab1.next_to(vec1, UR)),
        )
        self.wait(0.75)
        
        self.play(
            Write(vec2),
            Write(lab2.next_to(vec2, UL)),
        )
        self.wait(0.75)
        
        c1, c2 = nc1[1], nc2[1]
        A_text = vect2matrix(c1, c2, name="A")
        inbox = "Voici la matrice associée "
        msg_text = r"\mbox{" + f"{inbox}" + r"}"
        msg2 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        msg2_origin = msg2
        self.play(
            ReplacementTransform(
                msg,
                msg2.next_to(title_start, 3*DOWN)
            ),
            FadeOut(v1),
            FadeOut(v2),
            Write(A_text.next_to(msg2, DOWN))
        )
        self.wait(2.5)

        mat_A = [[1, 0], [1, 1]]
        disp_A = Matrix(
            mat_A,
            h_buff=0.75
        )
        inbox1 = "Effet géométrique de"
        inbox2 = "la matrice A"
        inboxes = [inbox1, inbox2]
        msg_eff = inbox_msg(*inboxes, font_size=40)
        self.play(
            ReplacementTransform(
                lab2,
                msg_eff.next_to(vec2, UP)
            ),
            ReplacementTransform(
                lab1,
                disp_A.next_to(msg_eff, RIGHT)
            ),
            ApplyMatrix(mat_A, plane),
            ApplyMatrix(mat_A, msg2)
        )
        self.wait(3.5)

        inbox1 = "Que faut-il faire"
        inbox2 = " pour revenir en arrière ?"
        inbox3 = "Écrivez votre réponse"
        inbox4 = "dans les commentaires."
        inboxes = [inbox1, inbox2, inbox3, inbox4]
        msg3 = inbox_msg(*inboxes, font_size=40)
        self.play(
            Write(msg3.next_to(vec2, DOWN))
        )
        self.wait(3)

        inbox1 = "Il appliquer la matrice inverse."
        inbox2 = "Calculons-la."
        inboxes = [inbox1, inbox2]
        msg4 = inbox_msg(*inboxes, font_size=40)
        self.play(
            ReplacementTransform(
                msg3,
                msg4.next_to(vec2, DOWN)
            ),
        )
        self.wait(2.5)

        ent_A = [[1, 0], [1, 1]]
        A = Matrix(
            ent_A,
            h_buff=0.75
        )
        
        ent_I = [[1, 0], [0, 1]]
        I = Matrix(
            ent_I,
            h_buff=0.75
        )

        lignes = ["L_1", "L_2"]
        op_ent = [[L] for L in lignes]
        OP = Matrix(
            op_ent,
            h_buff=1.5
        )

        det_op = Group(
            A,
            I,
            OP
        ).arrange_in_grid(
            rows=1,
            cols=3,
            buff=(0.5, 0.5),
            #col_alignments="c"
        )

        
        self.play(
            GrowFromCenter(det_op.next_to(msg4, 2*DOWN)),
        )
        self.wait(0.5)

        ent_A2 = [[1, 0], [0, 1]]
        A2 = Matrix(
            ent_A2,
            h_buff=0.75
        )
        
        ent_I2 = [[1, 0], [-1, 1]]
        I2 = Matrix(
            ent_I2,
            h_buff=0.75
        )
        
        ent_OP2 = [["L_1"], ["L_2 - L_1"]]
        OP2 = Matrix(
            ent_OP2,
            h_buff=1.75
        )

        det_op2 = Group(
            A2,
            I2,
            OP2
        ).arrange_in_grid(
            rows=1,
            cols=3,
            buff=(0.5, 0.5),
            #col_alignments="c"
        )
        
        
        self.play(
            ReplacementTransform(
                det_op,
                det_op2.next_to(msg4, 2*DOWN)
            ),
        )
        self.wait(2)

        

        c1, c2 = [1, -1], [0, 1]
        inv_A_text = vect2matrix(c1, c2, name=r"A^{-1}")
        inbox = "Voici la matrice inverse "
        msg_text = r"\mbox{" + f"{inbox}" + r"}"
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            ReplacementTransform(
                msg4,
                msg5.next_to(det_op2, DOWN)
            ),
            Write(inv_A_text.next_to(msg5, DOWN))
        )
        self.wait(2.5)

        mat_inv_A = [[1, 0], [-1, 1]]
        disp_inv_A = Matrix(
            mat_inv_A,
            h_buff=0.75
        )
        inbox1 = "Effet géométrique de"
        inbox2 = "la matrice inverse de A"
        inboxes = [inbox1, inbox2]
        msg_eff_inv = inbox_msg(*inboxes, font_size=40)
        self.play(
            FadeOut(det_op2),
            ReplacementTransform(
                msg_eff,
                msg_eff_inv.next_to(vec1, DOWN)
            ),
            ReplacementTransform(
                disp_A,
                disp_inv_A.next_to(msg_eff_inv, DOWN)
            ),
            ApplyMatrix(mat_inv_A, msg2),
            ApplyMatrix(mat_inv_A, plane)
        )
        self.wait(2)

        self.play(
            FadeOut(msg_eff_inv),
            FadeOut(disp_inv_A),
        )
        self.wait(0.5)
        
        self.play(
            ApplyMatrix(mat_A, msg2),
            ApplyMatrix(mat_A, msg5),
            ApplyMatrix(mat_A, A_text),
            ApplyMatrix(mat_A, inv_A_text),
            ApplyMatrix(mat_A, plane)
        )
        self.wait(2.5)

        self.play(
            ApplyMatrix(mat_inv_A, msg2),
            ApplyMatrix(mat_inv_A, msg5),
            ApplyMatrix(mat_inv_A, A_text),
            ApplyMatrix(mat_inv_A, inv_A_text),
            ApplyMatrix(mat_inv_A, plane)
        )
        self.wait(2.5)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')
