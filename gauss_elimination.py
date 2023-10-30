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

    
def disp_bell_curv_area(self, axe, curve, x_interval, qx, px, dir):
    area = axe.get_area(curve, x_range=x_interval)
    self.play(FadeIn(area))
    
    if dir == 1:
        msg = f"\Phi({qx}) = "
        msg += "\mathbb{P}(X \leqslant "
        msg += f"{qx}) = {px}"
    elif dir == 0:
        msg = "\mathbb{P}("
        msg += f"{-qx} \leqslant X "
        msg += f"\leqslant {qx}) = "
        msg += f"2\Phi({qx}) - 1 = "
        msg += f"{2*px}-1"
    elif dir == -1:
        msg = "\mathbb{P}(X \geqslant "
        msg += f"{qx}) = 1 - \Phi({qx}) = 1 - {px}"
        
    prob = MathTex(msg)
    self.play(Create(prob.scale(0.75)))
    self.wait(.5)
    self.play(FadeOut(prob), FadeOut(area))


def get_mat(init_ent, inv_ent, op_ent):
    colors = [RED, GREEN, BLUE]
    entries = [init_ent[i] + inv_ent[i] + op_ent[i] for i in range(3)]
    mat = Matrix(
        entries,
        v_buff = 1.3,
        h_buff = 1.85
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


class GaussElimination(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Inversion de matrice "
        title = Title(f"{msg} avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        init_ent = [
            [1, 1, 0],
            [0, 1, -1],
            [1, 1, 1]]

        A = Matrix(init_ent)
        det_A = get_det_text(A, determinant=1, initial_scale_factor=0.75)
        self.add(A)
        self.play(Write(det_A))
        self.wait(0.5)
        self.play(Unwrite(det_A))
        self.wait(0.25)

        inv_ent = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]

        I = Matrix(inv_ent)
        
        lignes = ["L_1", "L_2", "L_3"]
        op_ent = [[ligne] for ligne in lignes]

        separator1 = Line(
        LEFT * 0.65 + UP * 1.25,
        LEFT * 0.65 + DOWN * 1.25,
        color=ORANGE
        )
        separator2 = Line(
        RIGHT * 2.55 + UP * 1.25,
        RIGHT * 2.55 + DOWN * 1.25,
        color=ORANGE
        )
        
        g = get_mat(init_ent, inv_ent, op_ent)
        self.play(ReplacementTransform(A, g))
        #self.play(FadeIn(g))
        
        self.play(Create(separator1), Create(separator2))
        self.wait(0.5)

        init_ent2 = [
            [1, 1, 0],
            [0, 1, -1],
            [0, 0, 1]]
        
        inv_ent2 = [
            [1, 0, 0],
            [0, 1, 0],
            [-1, 0, 1]]

        lignes = ["L_1", "L_2", "L_3 - L_1"]
        op_ent2 = [[L] for L in lignes]
        
        g2 = get_mat(init_ent2, inv_ent2, op_ent2)
        line3g2 = SurroundingRectangle(g2.get_rows()[2])
        self.play(Write(line3g2))
        self.play(ReplacementTransform(g, g2))
        self.wait(0.5)
        
        init_ent3 = [
            [1, 0, 1],
            [0, 1, -1],
            [0, 0, 1]]
        
        inv_ent3 = [
            [1, -1, 0],
            [0, 1, 0],
            [-1, 0, 1]]

        lignes = ["L_1 - L_2", "L_2", "L_3"]
        op_ent3 = [[L] for L in lignes]
        
        g3 = get_mat(init_ent3, inv_ent3, op_ent3)
        line1g3 = SurroundingRectangle(g3.get_rows()[0])
        self.play(ReplacementTransform(line3g2, line1g3))
        self.play(ReplacementTransform(g2, g3))
        self.wait(0.5)

        init_ent4 = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
        
        inv_ent4 = [
            [2, -1, -1],
            [-1, 1,  1],
            [-1, 0, 1]]

        B = Matrix(inv_ent4)

        lignes = ["L_1 - L_3", "L_2 + L_3", "L_3"]
        op_ent4 = [[L] for L in lignes]
        
        g4 = get_mat(init_ent4, inv_ent4, op_ent4)
        line2g4 = SurroundingRectangle(g4.get_rows()[1])
        line1g4 = SurroundingRectangle(g4.get_rows()[0])
        self.play(Write(line2g4))
        self.wait()
        self.play(ReplacementTransform(line1g3, line1g4))
        self.wait()
        self.play(ReplacementTransform(g3, g4))
        self.wait(0.5)
        self.play(
            Unwrite(separator1),
            Unwrite(separator2),
            Unwrite(line2g4),
            Unwrite(line1g4),
            Unwrite(g4)
        )
        self.wait(0.25)

        init_ent = [
            [1, 1, 0],
            [0, 1, -1],
            [1, 1, 1]]

        A = Matrix(init_ent)

        inv_ent4 = [
            [2, -1, -1],
            [-1, 1,  1],
            [-1, 0, 1]]

        B = Matrix(inv_ent4)
        
        inv_ent = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]

        I = Matrix(inv_ent)

        abi = Group(A, B, I).arrange_in_grid(buff=1)
        self.play(FadeIn(abi))
        self.wait(0.5)
        
        A_row1 = SurroundingRectangle(A.get_rows()[0])

        B_col1 = SurroundingRectangle(B.get_columns()[0])
        id_ent = I.get_entries()
        #id_ent[0].set_color(YELLOW)
        I_11 = SurroundingRectangle(id_ent[0])
        self.play(
            Write(A_row1),
            Write(B_col1),
            Write(I_11)
        )
        self.wait(0.5)

        B_col2 = SurroundingRectangle(B.get_columns()[1])
        # id_ent[0].set_color(WHITE)
        # id_ent[1].set_color(YELLOW)
        I_12 = SurroundingRectangle(id_ent[1])
        self.play(
            ReplacementTransform(B_col1, B_col2),
            ReplacementTransform(I_11, I_12)
        )
        self.wait(0.5)

        B_col3 = SurroundingRectangle(B.get_columns()[2])
        # id_ent[1].set_color(WHITE)
        # id_ent[2].set_color(YELLOW)
        I_13 = SurroundingRectangle(id_ent[2])
        self.play(
            ReplacementTransform(B_col2, B_col3),
            ReplacementTransform(I_12, I_13)
        )
        self.wait(0.5)


        A_row2 = SurroundingRectangle(A.get_rows()[1])

        B_col1 = SurroundingRectangle(B.get_columns()[0])
        # id_ent[2].set_color(WHITE)
        # id_ent[3].set_color(YELLOW)
        I_21 = SurroundingRectangle(id_ent[3])
        self.play(
            ReplacementTransform(A_row1, A_row2),
            ReplacementTransform(B_col3, B_col1),
            ReplacementTransform(I_13, I_21)
        )
        self.wait(0.35)

        B_col2 = SurroundingRectangle(B.get_columns()[1])
        # id_ent[3].set_color(WHITE)
        # id_ent[4].set_color(YELLOW)
        I_22 = SurroundingRectangle(id_ent[4])
        self.play(
            ReplacementTransform(B_col1, B_col2),
            ReplacementTransform(I_21, I_22)
        )
        self.wait(0.5)

        B_col3 = SurroundingRectangle(B.get_columns()[2])
        # id_ent[4].set_color(WHITE)
        # id_ent[5].set_color(YELLOW)
        I_23 = SurroundingRectangle(id_ent[5])
        self.play(
            ReplacementTransform(B_col2, B_col3),
            ReplacementTransform(I_22, I_23)
        )
        self.wait(0.5)


        A_row3 = SurroundingRectangle(A.get_rows()[2])

        B_col1 = SurroundingRectangle(B.get_columns()[0])
        # id_ent[5].set_color(WHITE)
        # id_ent[6].set_color(YELLOW)
        I_31 = SurroundingRectangle(id_ent[6])
        self.play(
            ReplacementTransform(A_row2, A_row3),
            ReplacementTransform(B_col3, B_col1),
            ReplacementTransform(I_23, I_31)
        )
        self.wait(0.35)

        B_col2 = SurroundingRectangle(B.get_columns()[1])
        # id_ent[6].set_color(WHITE)
        # id_ent[7].set_color(YELLOW)
        I_32 = SurroundingRectangle(id_ent[7])
        self.play(
            ReplacementTransform(B_col1, B_col2),
            ReplacementTransform(I_31, I_32)
        )
        self.wait(0.5)

        B_col3 = SurroundingRectangle(B.get_columns()[2])
        # id_ent[7].set_color(WHITE)
        # id_ent[8].set_color(YELLOW)
        I_33 = SurroundingRectangle(id_ent[8])
        self.play(
            ReplacementTransform(B_col2, B_col3),
            ReplacementTransform(I_32, I_33)
        )
        self.wait(0.5)
        
        disp_sub(self, lang='fr')

        
