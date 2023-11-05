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


class LinearAlgebra(Scene):
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

        v1_name, v1_coord = "v_1", [5, 3, 1]
        v1 = vect_text(name=v1_name, coordinates=v1_coord)

        v2_name, v2_coord = "v_2", [7, -2, 2]
        v2 = vect_text(name=v2_name, coordinates=v2_coord)

        v3_name, v3_coord = "v_3", [-11, 12, -4]
        v3 = vect_text(name=v3_name, coordinates=v3_coord)
        
        inbox = "Considérons la famille de vecteurs de "
        msg_text = "\\mbox{" + f"{inbox}" + "}"
        msg_text += "\\mathbb{R}^3"
        msg = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg),
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
            ReplacementTransform(msg, msg2)
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
        
        inbox3 = "Autrement dit, si "
        msg_text = r"\mbox{"
        msg_text += f"{inbox3}"
        msg_text += r"} \det(A) \neq 0 \\"
        inbox4 = "alors la famille sera libre."
        msg_text += r"\mbox{"
        msg_text += f"{inbox4}"
        msg4 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        
        inbox5 = "Et si "
        
        msg_text = r"\mbox{"
        
        msg_text += f"{inbox5}"
        
        msg_text += r"} \det(A) = 0 \\"
        
        inbox6 = "alors la famille sera liée."
        
        msg_text += r"\mbox{"
        
        msg_text += f"{inbox6}"
        
        msg5 = MathTex(
            msg_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=40
        )
        self.play(
            Write(A.next_to(msg2, 4*UP)),
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

        A_mat = Matrix(ent_A)
        
        lignes = ["L_1", "L_2", "L_3"]
        op_ent = [[ligne] for ligne in lignes]
        OP = Matrix(op_ent)

        det_op = Group(A_mat, OP).arrange(buff=1.5)
        
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

        
        ent_A2 = [
            [0, -3, 9],
            [0, -8, 24],
            [1, 2, -4]
        ]
        A2 = Matrix(ent_A2)

        
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
        
        lignes = ["L_1 - 5L_3", "L_2 - 3L_3", "L_3"]
        op_ent2 = [[L] for L in lignes]
        OP2 = Matrix(op_ent2)

        det_op2 = Group(A2, OP2).arrange(buff=1.5)
        
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
        det_A = get_det_text(B, determinant=0, initial_scale_factor=1)

        self.play(
            FadeOut(OP2_L_1),
            FadeOut(A2_L_1),
            FadeOut(OP2_L_2),
            FadeOut(A2_L_2),
            FadeOut(det_op2),
            Write(det_A),
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
        
        v1_name, v1_coord = "v_1", [5, 3, 1]
        v1 = vect_text(name=v1_name, coordinates=v1_coord)

        v2_name, v2_coord = "v_2", [7, -2, 2]
        v2 = vect_text(name=v2_name, coordinates=v2_coord)

        v3_name, v3_coord = "v_3", [-11, 12, -4]
        v3 = vect_text(name=v3_name, coordinates=v3_coord)

        
        inbox8 = "forment une famille liée dans "
        msg8_text = r"\mbox{"
        msg8_text += f"{inbox8}"
        msg8_text += r"} \mathbb{R}^3"
        msg8 = MathTex(
            msg8_text,
            tex_template=TexFontTemplates.french_cursive,
            font_size=37
        )
        self.play(
            Write(msg7.next_to(det_A, DOWN)),
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
        A3 = Matrix(ent_A3)

        lignes = [r"\frac{1}{3}L_1", r"0,125L_2", "L_3"]
        op_ent3 = [[L] for L in lignes]
        OP3 = Matrix(op_ent3)

        A3_L_2 = SurroundingRectangle(A3.get_rows()[1])
        OP3_L_2 = SurroundingRectangle(OP3.get_rows()[1])
        A3_L_1 = SurroundingRectangle(A3.get_rows()[0])
        OP3_L_1 = SurroundingRectangle(OP3.get_rows()[0])

        det_op3 = Group(A3, OP3).arrange(buff=1.5)
        
        self.play(
            FadeOut(det_A),
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

