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
    like_svg_path = "/Users/dn/Documents/pics/svg/like.svg"
    sub_svg_path = "/Users/dn/Documents/pics/svg/subscribe.svg"
    jpg_png_path = "/Users/dn/Documents/pics/png/sabonner.png"
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
    sub_svg_path = "/Users/dn/Documents/pics/svg/subscribe.svg"
    sub_pic = SVGMobject(sub_svg_path)
    self.play(
        FadeIn(
            sub_pic.scale(svg_scale).to_edge(2.5*UP)
        )
    )
    return sub_pic


    
def put_like_logo(self, sub_pic, svg_scale=0.25):
    like_svg_path = "/Users/dn/Documents/pics/svg/like.svg"
    like_pic = SVGMobject(like_svg_path)
    self.play(
        FadeIn(
            like_pic.scale(svg_scale).next_to(sub_pic, LEFT)
        )
    )
    return like_pic


    
def put_youtube_short_logo(self, sub_pic, svg_scale=0.25):
    youtube_short_path = "/Users/dn/Documents/pics/svg/Youtube_shorts.svg"
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
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(3)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 3))
    self.wait(3)
        
    self.play(ReplacementTransform(part, full), run_time=3)
    self.wait(3)
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
    self.wait(3)
    self.play(FadeOut(prob), FadeOut(area))



    
class HeadTailExpectedValue1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))
        sub_pic = put_sub_logo(self)

        initial_sum = MathTex(
            "\mathbb{E}(X) = \sum_{i\in\mathbb{N}}p_ix_i"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()

        title_ex1 = Title("Exemple 1 : pièce de monnaie")
        self.play(ReplacementTransform(title, title_ex1))
        like_logo = put_like_logo(self, sub_pic)
        
        example1 = MathTable(
            [[0, 1],
             [r"\dfrac{1}{2}", r"\dfrac{1}{2}"]],
            row_labels=[MathTex("x_i"), MathTex("p_i")],
            col_labels=[Text("Pile"), Text("Face")]
        )
        
        esp1 = MathTex(
            r"\mathbb{E}(X)",
            "=",
            r"0\times\dfrac{1}{2}",
            "+",
            r"1\times\dfrac{1}{2}",
            r"\mathbb{E}(X) = \dfrac{1}{2}"
        )
        
        esp1.set_color(GREEN)
        for i in range(5):
            esp1[i].move_to(LEFT*(3 - i) + DOWN*3)

        esp1[-1].move_to(LEFT*2 + DOWN*4)
        result = esp1[-1]
        
        self.play(Write(example1.scale(0.85)))
        self.play(Write(esp1[0:2]))
        
        for j in range(2, 4):
            filled_xi = example1.get_highlighted_cell(
                (2, j),
                color=RED
            )
            filled_pi = example1.get_highlighted_cell(
                (3, j),
                color=RED
            )
            circled_xi = example1.get_cell(
                (2, j),
                color=GREEN
            )
            circled_pi = example1.get_cell(
                (3, j),
                color=GREEN
            )
            
            example1.add(
                filled_xi, filled_pi,
                circled_xi, circled_pi
            )
            
            ej = VGroup(
                example1.get_cell((2, j)),
                example1.get_cell((3, j))
            )
            
            self.play(TransformFromCopy(ej, esp1[2*(j-1)]))
            if j == 2: self.play(Write(esp1[3]))
            self.wait(3)
            example1.remove(
                    filled_xi, filled_pi,
                    circled_xi, circled_pi
            )
            
        result = SurroundingRectangle(esp1[-1])
        
        self.play(Write(result))
        self.play(Write(esp1[-1]))
        self.wait(3)

        # C-x C-t transpose line
        self.play(Unwrite(result))
        self.play(Unwrite(esp1))
        self.play(Unwrite(example1))
        self.play(Unwrite(initial_sum))
        self.wait(2)

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_ex1, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class HeadTailExpectedValue1bis(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))

        initial_sum = MathTex(
            "\mathbb{E}(X) = \sum_{i\in\mathbb{N}}p_ix_i"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()

        title_ex1 = Title("Exemple 1 : pièce de monnaie truquée")
        self.play(ReplacementTransform(title, title_ex1))
        
        example1 = MathTable(
            [[0, 1],
             [r"q", r"p"]],
            row_labels=[MathTex("x_i"), MathTex("p_i")],
            col_labels=[Text("Pile"), Text("Face")]
        )
        
        esp1 = MathTex(
            r"\mathbb{E}(X)",
            "=",
            r"0\times q",
            "+",
            r"1\times p",
            r"\mathbb{E}(X) = p"
        )
        
        esp1.set_color(GREEN)
        for i in range(5):
            esp1[i].move_to(LEFT*(3 - i) + DOWN*3)

        esp1[-1].move_to(LEFT*2 + DOWN*4)
        result = esp1[-1]
        
        self.play(Write(example1.scale(0.85)))
        self.play(Write(esp1[0:2]))
        
        for j in range(2, 4):
            filled_xi = example1.get_highlighted_cell(
                (2, j),
                color=RED
            )
            filled_pi = example1.get_highlighted_cell(
                (3, j),
                color=RED
            )
            circled_xi = example1.get_cell(
                (2, j),
                color=GREEN
            )
            circled_pi = example1.get_cell(
                (3, j),
                color=GREEN
            )
            
            example1.add(
                filled_xi, filled_pi,
                circled_xi, circled_pi
            )
            
            ej = VGroup(
                example1.get_cell((2, j)),
                example1.get_cell((3, j))
            )
            
            self.play(TransformFromCopy(ej, esp1[2*(j-1)]))
            if j == 2: self.play(Write(esp1[3]))
            self.wait(3)
            example1.remove(
                    filled_xi, filled_pi,
                    circled_xi, circled_pi
            )
            
        result = SurroundingRectangle(esp1[-1])
        
        self.play(Write(result))
        self.play(Write(esp1[-1]))
        self.wait(3)

        # C-x C-t transpose line
        self.play(Unwrite(result))
        self.play(Unwrite(esp1))
        self.play(Unwrite(example1))
        self.play(Unwrite(initial_sum))
        self.wait(2)

        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_ex1, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


        
class HeadTailExpectedValue1ter(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))
        sub_pic = put_sub_logo(self)

        initial_sum = MathTex(
            "\mathbb{E}(X) = \sum_{i\in\mathbb{N}}p_ix_i"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()

        title_ex1 = Title("On lance 2 fois un pièce de monnaie truquée")
        self.play(ReplacementTransform(title, title_ex1.scale(0.75)))

        cadre = Paragraph(
            "On s'intéresse au nombre de fois",
            "où on obtient pile.",
            "Cette fois on code 1 pour pile",
            "et 0 pour face.",
            "Mais au fait, combien y a-t-il",
            "d'issues ?",
            "Écris-le en commentaire !"
        )
        
        for phrase in cadre:
            self.play(Write(phrase))
            self.wait(0.1)

        self.play(FadeOut(cadre))
        example1 = MathTable(
            [[0, 1, 2],
             [r"q^2", r"2pq", r"p^2"]],
            row_labels=[MathTex("x_i"), MathTex("p_i")],
        )
        
        esp1 = MathTex(
            r"\mathbb{E}(X)",
            "=",
            r"0\times q^2",
            "+",
            r"1\times 2pq",
            "+",
            r"2\times p^2",
            r"\mathbb{E}(X) = 2p^2 + 2pq"
        )
        
        esp1.set_color(GREEN)
        for i in range(7):
            esp1[i].move_to(LEFT*(3 - i) + DOWN*3)

        esp1[-1].move_to(LEFT*2 + DOWN*4)
        result = esp1[-1]
        
        self.play(Write(example1.scale(0.85)))
        self.play(Write(esp1[0:2]))
        
        for j in range(2, 5):
            filled_xi = example1.get_highlighted_cell(
                (1, j),
                color=RED
            )
            filled_pi = example1.get_highlighted_cell(
                (2, j),
                color=RED
            )
            circled_xi = example1.get_cell(
                (1, j),
                color=GREEN
            )
            circled_pi = example1.get_cell(
                (2, j),
                color=GREEN
            )
            
            example1.add(
                filled_xi, filled_pi,
                circled_xi, circled_pi
            )
            
            ej = VGroup(
                example1.get_cell((1, j)),
                example1.get_cell((2, j))
            )
            
            self.play(TransformFromCopy(ej, esp1[2*(j-1)]))
            if j % 2 == 0: self.play(Write(esp1[j + 1]))
            self.wait(0.25)
            example1.remove(
                    filled_xi, filled_pi,
                    circled_xi, circled_pi
            )
        
        result = SurroundingRectangle(esp1[-1])
        self.play(Write(esp1[-1]))
        self.play(Write(result))
        self.wait()
        self.play(Unwrite(result))
        
        simplify = MathTex(
            r"\mathbb{E}(X) = 2p^2 + 2pq\\",
            r"\mathbb{E}(X) = 2p(p + q)\\",
            r"p + q = 1\Rightarrow \mathbb{E}(X) = 2p"
        )

        simplify.set_color(GREEN)
        for i in range(len(simplify)):
            simplify[i].move_to(LEFT*2 + DOWN*4)
        self.wait(.75)

        # C-x C-t transpose line
        title_simple = Title("Simplification")
        self.play(ReplacementTransform(title_ex1, title_simple))
        self.wait(0.15)
        self.play(ReplacementTransform(esp1[-1], simplify[1]))
        self.wait(0.15)
        simplify[-1].move_to(LEFT + DOWN*5)
        result = SurroundingRectangle(simplify[-1])
        self.play(Write(simplify[-1]))
        self.play(Write(result))
        self.wait(0.15)
        self.play(Unwrite(result))
        self.play(Unwrite(simplify[-1]))
        self.play(Unwrite(simplify[-2]))
        self.play(Unwrite(esp1[-2]))
        self.play(Unwrite(esp1[-3]))
        self.play(Unwrite(esp1[-4]))
        self.play(Unwrite(esp1[-5]))
        self.play(Unwrite(esp1[-6]))
        self.play(Unwrite(esp1[-7]))
        self.play(Unwrite(esp1[-8]))
        self.play(Unwrite(example1))
        self.play(Unwrite(initial_sum))
        self.wait(0.15)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_simple, title_end.scale(0.75)))
        disp_sub(self, lang='fr')


class HeadTailProbabilityTree(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Arbre de probabilités")
        self.add(title.scale(0.85))
        


        title_ex1 = Title("On lance 2 fois une pièce de monnaie truquée")
        self.play(ReplacementTransform(title, title_ex1.scale(0.75)))

        cadre = Paragraph(
            "On s'intéresse au nombre de fois",
            "où on obtient pile.",
            "Cette fois on code 1 pour pile",
            "et 0 pour face.",
            "Mais au fait, combien y a-t-il",
            "d'issues ?",
            "Écris-le en commentaire !"
        )

        for phrase in cadre:
            self.play(Write(phrase))
            self.wait(0.075)

        self.play(FadeOut(cadre))

        
        G = nx.Graph()
        
        children = ["F", "P"]
        g_c = ["FF", "PF", "FP", "PP"]
        results = ["0 + 0", "1 + 0", "0 + 1", "1 + 1"]
        
        G.add_node("")
        
        for i in range(2):
            G.add_node(children[i])
            G.add_edge("", children[i])

        arbre_0 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            vertex_config={
                "P": {"fill_color": GREEN},
                "F": {"fill_color": RED}
            },
            edge_config={
                ("", "P"): {"stroke_color": GREEN},
                ("", "F"): {"stroke_color": RED}
            },
            root_vertex=""
        )

        proba_0 = MathTex(
            r"P(\mbox{Obtenir pile}) = p",
            r"P(\mbox{Obtenir face}) = q = 1 - p"
        )

        proba_0[0].move_to(LEFT*2+DOWN*3).set_color(GREEN)
        proba_0[1].move_to(RIGHT*1.25+DOWN*4).set_color(RED)
        
        title_tir1 = Title("Lancer n°1")
        self.play(ReplacementTransform(title_ex1, title_tir1))
        self.play(Write(arbre_0))
        for prob in proba_0:
            self.play(Write(prob.scale(0.75)))
            self.wait(0.075)

        for prob in proba_0:
            self.play(Unwrite(prob))
            
        for i in range(4):
            G.add_node(g_c[i])
            G.add_edge(children[i%2], g_c[i])
            

        arbre_1 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            vertex_config={
                "P": {"fill_color": GREEN},
                "PP": {"fill_color": GREEN},
                "PF": {"fill_color": ORANGE},
                "F": {"fill_color": RED},
                "FP": {"fill_color": ORANGE},
                "FF": {"fill_color": RED}
            },
            edge_config={
                ("", "P"): {"stroke_color": GREEN},
                ("P", "PP"): {"stroke_color": GREEN},
                ("P", "PF"): {"stroke_color": ORANGE},
                ("", "F"): {"stroke_color": RED},
                ("F", "FP"): {"stroke_color": ORANGE},
                ("F", "FF"): {"stroke_color": RED}
            },
            root_vertex=""
        )

        proba_1 = MathTex(
            r"P(PP) = P(P)\times P(P) = p^2",
            r"P(PF) = P(P)\times P(F) = pq",
            r"P(FP) = P(F)\times P(P) = qp",
            r"P(FF) = P(F)\times P(F) = q^2"
        )

        proba_1[0].move_to(LEFT*2+DOWN*3).set_color(GREEN)
        proba_1[1].move_to(LEFT*1.5+DOWN*3.5).set_color(ORANGE)
        proba_1[2].move_to(RIGHT*1.5+DOWN*4).set_color(ORANGE)
        proba_1[3].move_to(RIGHT*2+DOWN*4.5).set_color(RED)
        
        title_tir2 = Title("Lancer n°2")
        self.play(ReplacementTransform(title_tir1, title_tir2))
        self.play(ReplacementTransform(arbre_0, arbre_1))
        for prob in proba_1:
            self.play(Write(prob.scale(0.75)))
            self.wait(0.075)
        for prob in proba_1:
            self.play(Unwrite(prob))
        
        for i in range(4):
            G.add_node(results[i])
            G.add_edge(g_c[i], results[i])

        arbre_2 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            root_vertex=""
        )
        
        title_nb_pil = Title("On compte le nombre de piles")
        self.play(ReplacementTransform(title_tir2, title_nb_pil))
        self.play(ReplacementTransform(arbre_1, arbre_2))
        self.wait(0.15)

        
        esp1 = MathTex(
            r"X\in\{0, 1, 2}",
            r"P(X = 0) = q^2",
            r"P(X = 1) = 2pq",
            r"P(X = 2) = p^2",
            r"\mathbb{E}(X)",
            "=",
            r"0\times q^2",
            "+",
            r"1\times 2pq",
            "+",
            r"2\times p^2",
            r"\mathbb{E}(X) = 2p^2 + 2pq",
            r"\mathbb{E}(X) = 2p(p + q)",
            r"\mathbb{E}(X) = 2p"
        )

        
        arbre_3 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            vertex_config={
                "0 + 0": {"fill_color": RED},
                "FF": {"fill_color": RED},
                "F": {"fill_color": RED},
            },
            edge_config={
                ("FF", "0 + 0"): {"stroke_color": RED},
                ("F", "FF"): {"stroke_color": RED},
                ("", "F"): {"stroke_color": RED},
            },
            root_vertex=""
        )
        
        title_0_pil = Title("X = 0 pile donc 2 faces")
        self.play(ReplacementTransform(title_nb_pil, title_0_pil))
        self.play(ReplacementTransform(arbre_2, arbre_3))
        esp1[1].move_to(LEFT + DOWN*3).set_color(RED)
        self.play(Write(esp1[1]))
        self.wait(.15)

        arbre_4 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            vertex_config={
                "0 + 1": {"fill_color": ORANGE},
                "FP": {"fill_color": ORANGE},
                "F": {"fill_color": RED},
                "1 + 0": {"fill_color": ORANGE},
                "PF": {"fill_color": ORANGE},
                "P": {"fill_color": GREEN}
            },
            edge_config={
                ("FP", "0 + 1"): {"stroke_color": ORANGE},
                ("FP", "F"): {"stroke_color": GREEN},
                ("", "F"): {"stroke_color": RED},
                ("PF", "1 + 0"): {"stroke_color": ORANGE},
                ("PF", "P"): {"stroke_color": RED},
                ("", "P"): {"stroke_color": GREEN},
            },
            root_vertex=""
        )

        title_1_pil = Title("X = 1 pile donc 1 face")
        self.play(ReplacementTransform(title_0_pil, title_1_pil))
        self.play(ReplacementTransform(arbre_3, arbre_4))
        esp1[2].move_to(LEFT + DOWN*3)
        self.play(ReplacementTransform(esp1[1], esp1[2].set_color(ORANGE)))
        self.wait(.15)

        arbre_5 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            vertex_config={
                "1 + 1": {"fill_color": GREEN},
                "PP": {"fill_color": GREEN},
                "P": {"fill_color": GREEN}
            },
            edge_config={
                ("PP", "1 + 1"): {"stroke_color": GREEN},
                ("PP", "P"): {"stroke_color": GREEN},
                ("", "P"): {"stroke_color": GREEN},
            },
            root_vertex=""
        )

        title_2_pil = Title("X = 2 piles donc 0 face")
        self.play(ReplacementTransform(title_1_pil, title_2_pil))
        self.play(ReplacementTransform(arbre_4, arbre_5))
        esp1[3].move_to(LEFT + DOWN*3)
        self.play(ReplacementTransform(esp1[2], esp1[3].set_color(GREEN)))
        self.wait(.15)
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_2_pil, title_end.scale(0.75)))
        disp_sub(self, lang='fr')



class TetrahedralDie(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Arbre de probabilités")
        self.add(title.scale(0.85))
        svg_scale = 0.25
        sub_pic = put_sub_logo(self)
        
        initial_sum = MathTex(
            "\sum_{i}p_i = 1"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait(0.1)

        title_ex1 = Title("Exemple 1 : On lance un dé classique à 4 faces")
        self.play(ReplacementTransform(title, title_ex1.scale(0.75)))
        like_pic = put_like_logo(self, sub_pic)
        
        cadre = Paragraph(
            "On s'intéresse à la face",
            "du dessus.",
            "Donc un nombre entier",
            "entre 1 et 4 inclus."
        )

        for phrase in cadre:
            self.play(Write(phrase))
            self.wait(0.075)

        self.play(FadeOut(cadre))
        self.wait(0.05)
        
        G = nx.Graph()
        
        children = list(range(1, 5))
        
        G.add_node("")
        
        for i in range(4):
            G.add_node(children[i])
            G.add_edge("", children[i])

        arbre_0 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            root_vertex=""
        )

        proba_0 = MathTex(
            r"P(4) = \dfrac{1}{4}",
            r"P(3) = \dfrac{1}{4}",
            r"P(2) = \dfrac{1}{4}",
            r"P(1) = \dfrac{1}{4}"
        )

        proba_0[0].move_to(LEFT*3+DOWN*1.5)
        proba_0[1].move_to(LEFT*1.25+DOWN*1.5)
        proba_0[2].move_to(RIGHT*.75+DOWN*1.5)
        proba_0[3].move_to(RIGHT*2.5+DOWN*1.5)
        
        self.play(Write(arbre_0))
        for prob in proba_0:
            self.play(Write(prob.scale(0.75)))
            self.wait(0.15)

        for prob in proba_0:
            self.play(Unwrite(prob))
            self.wait(0.05)

        self.play(FadeOut(arbre_0))
        self.wait(0.05)
        
        msg = "Exemple 2 : On lance un autre dé (spécial) à 4 faces"
        title_ex2 = Title(msg)
        self.play(ReplacementTransform(title_ex1, title_ex2.scale(0.75)))
        youtube_short_pic = put_youtube_short_logo(self, sub_pic)
        self.wait(0.05)
        
        cadre = Paragraph(
            "Ce dé a la particularité",
            "que chaque chiffre a une",
            "probabilité proportionnelle",
            "de se réaliser.",
            "Saurez-vous deviner sa loi ?",
            "Écris-la dans les commentaires !"
        )

        
        for phrase in cadre:
            self.play(Write(phrase))
            self.wait(0.075)

        self.play(FadeOut(cadre))
        self.wait(0.05)
        
        G = nx.Graph()
        
        children = list(range(1, 5))
        
        G.add_node("")
        
        for i in range(4):
            G.add_node(children[i])
            G.add_edge("", children[i])

        arbre_0 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            root_vertex=""
        )

        proba_0 = MathTex(
            r"P(4) = p_4",
            r"P(3) = p_3",
            r"P(2) = p_2",
            r"P(1) = p_1"
        )

        proba_0[0].move_to(LEFT*3+DOWN*1.5)
        proba_0[1].move_to(LEFT*1.25+DOWN*1.5)
        proba_0[2].move_to(RIGHT*.75+DOWN*1.5)
        proba_0[3].move_to(RIGHT*2.5+DOWN*1.5)
        
        self.play(Write(arbre_0))
        for prob in proba_0:
            self.play(Write(prob.scale(0.75)))
            self.wait(0.0875)
            
        calc_proba = MathTex(
            r"\sum_{i = 1}^4p_i = 1",
            r"p_1 + p_2 + p_3 + p_4 = 1",
            r"p_1 + 2p_1 + 3p_1 + 4p_1 = 1",
            r"p_1(1 + 2 + 3 + 4) = 1",
            r"p_1 = \dfrac{1}{10}"
        )
        
        for cp in calc_proba: cp.move_to(LEFT*1.5+DOWN*2.5)
        self.play(TransformFromCopy(proba_0, calc_proba[0]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[0], calc_proba[1]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[1], calc_proba[2]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[2], calc_proba[3]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[3], calc_proba[4]))
        self.wait(.3)
            
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_ex2, title_end.scale(0.75)))
        
        
        disp_sub(self, lang='fr')
        


class TetrahedralDie2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Jouons au dé")
        self.add(title.scale(0.85))
        svg_scale = 0.25
        sub_pic = put_sub_logo(self, svg_scale)
        
        initial_sum = MathTex(
            "\sum_{i}p_i = 1"
        )
        # self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        # self.wait(0.1)

        title_ex1 = Title("Exemple 1 : On lance un dé classique à 4 faces")
        self.play(ReplacementTransform(title, title_ex1.scale(0.75)))
        like_pic = put_like_logo(sub_pic)
        
        cadre = Paragraph(
            "On s'intéresse à la face",
            "du dessus.",
            "Donc un nombre entier",
            "entre 1 et 4 inclus."
        )

        # for phrase in cadre:
        #     self.play(Write(phrase))
        #     self.wait(0.075)

        # self.play(FadeOut(cadre))
        # self.wait(0.05)
        
        s1, s2, s3, s4 = [Square() for _ in range(1, 5)]

        self.play(*[Write(o) for o in [s1, s2, s3, s4]])
        s3.move_to(2*DOWN)
        
        self.play(
            s1.animate.next_to(s3, 13*UP),
            s2.animate.next_to(s3, 2.5*UP),
            s4.animate.next_to(s3, 2.5*DOWN)
        )

        t1, t2, t3, t4 = [Tex(f"${i+1}$").scale(2) for i in range(4)]

        t1.move_to(s1)
        t2.move_to(s2)
        t3.move_to(s3)
        t4.move_to(s4)

        self.play(*[Write(o) for o in [t1, t2, t3, t4]])
        self.wait()
        
        msg = "Exemple 2 : On lance un autre dé (spécial) à 4 faces"
        title_ex2 = Title(msg)
        self.play(ReplacementTransform(title_ex1, title_ex2.scale(0.75)))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(svg_scale)
        self.play(
            FadeIn(
                youtube_shorts.next_to(sub_pic, RIGHT)
            )
        )
        self.wait(0.05)
        
        cadre = Paragraph(
            "Ce dé a la particularité",
            "que chaque chiffre a une",
            "probabilité proportionnelle",
            "de se réaliser.",
            "Saurez-vous deviner sa loi ?",
            "Écris-la dans les commentaires !"
        )

        
        # for phrase in cadre:
        #     self.play(Write(phrase))
        #     self.wait(0.075)

        # self.play(FadeOut(cadre))
        # self.wait(0.05)
        
        G = nx.Graph()
        
        children = list(range(1, 5))
        
        G.add_node("")
        
        for i in range(4):
            G.add_node(children[i])
            G.add_edge("", children[i])

        arbre_0 = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            labels=True,
            root_vertex=""
        )

        proba_0 = MathTex(
            r"P(4) = p_4",
            r"P(3) = p_3",
            r"P(2) = p_2",
            r"P(1) = p_1"
        )

        proba_0[0].move_to(LEFT*3+DOWN*1.5)
        proba_0[1].move_to(LEFT*1.25+DOWN*1.5)
        proba_0[2].move_to(RIGHT*.75+DOWN*1.5)
        proba_0[3].move_to(RIGHT*2.5+DOWN*1.5)
        
        self.play(Write(arbre_0))
        for prob in proba_0:
            self.play(Write(prob.scale(0.75)))
            self.wait(0.0875)
            
        calc_proba = MathTex(
            r"\sum_{i = 1}^4p_i = 1",
            r"p_1 + p_2 + p_3 + p_4 = 1",
            r"p_1 + 2p_1 + 3p_1 + 4p_1 = 1",
            r"p_1(1 + 2 + 3 + 4) = 1",
            r"p_1 = \dfrac{1}{10}"
        )
        
        for cp in calc_proba: cp.move_to(LEFT*1.5+DOWN*2.5)
        self.play(TransformFromCopy(proba_0, calc_proba[0]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[0], calc_proba[1]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[1], calc_proba[2]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[2], calc_proba[3]))
        self.wait(.3)
        self.play(ReplacementTransform(calc_proba[3], calc_proba[4]))
        self.wait(.3)
            
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_ex2, title_end.scale(0.75)))
        
        self.play(
            FadeIn(
                sub_pic.to_edge(2.5*DOWN)
            )
        )
        
        self.play(
            FadeIn(
                like_pic.next_to(sub_pic, LEFT)
            )
        )
        
        self.play(
            FadeIn(
                youtube_shorts.next_to(sub_pic, RIGHT)
            )
        )
        
        disp_sub(self, lang='fr')


        
        
class ExpectedValueEx2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "\mathbb{E}(X) = \sum_{i\in\mathbb{N}}p_ix_i"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait(0.5)
        
        title_ex2 = Title("Exemple 2 : dé à 4 faces")
        self.play(ReplacementTransform(title_ex1, title_ex2))
        x_vals = np.array([1, 2, 3, 4])
        y_vals = np.array([0.25, 0.25, 0.25, 0.25])
        example2 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x_i"), MathTex("p_i")],
            include_outer_lines=True
        )
        self.play(Write(example2.scale(0.85)))
        self.wait(2)
        self.play(FadeOut(example2))
        self.wait()
        
        property1 = MathTex(
            r"\mathbb{E}(X+a) = \mathbb{E}(X) + a\\",
            r"\sum_ip_i(x_i+a) = \sum_ip_ix_i + a\\"
        )
        title_prop1 = Title("Propriété 1")
        self.play(ReplacementTransform(title_ex2, title_prop1))

        for i in range(len(property1)):
            if i == 2:
                self.play(
                    Write(
                        property1[i].scale(0.75).shift(0.6*LEFT)
                    )
                )
            elif i == len(property1) - 1:
                self.play(
                    Write(
                        property1[i].shift(0.6*LEFT+DOWN)
                    )
                )
                result = SurroundingRectangle(property1[i])
                self.play(Write(result))
                self.wait(2)
            else:
                self.play(
                    Write(property1[i].shift(0.6*LEFT)
                          )
                )
            self.wait(3)    

        self.play(FadeOut(property1))
        self.play(Unwrite(result))
        self.wait(0.5)

        disp_sub(self, lang='fr')

class ExpectedValue2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "\mathbb{E}(X) = \sum_{i\in\mathbb{N}}p_ix_i"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()

        property2 = MathTex(
            r"\mathbb{E}(aX) = a\mathbb{E}(X)\\",
            r"\sum_ip_iax_i = a\sum_ip_ix_i\\"
        )
        title_prop2 = Title("Propriété 2")
        self.play(ReplacementTransform(title, title_prop2))

        for i in range(len(property2)):
            if i == 2:
                self.play(
                    Write(
                        property2[i].scale(0.75).shift(0.6*LEFT)
                    )
                )
            elif i == len(property2) - 1:
                self.play(
                    Write(
                        property2[i].shift(0.6*LEFT+DOWN)
                    )
                )
                result = SurroundingRectangle(property2[i])
                self.play(Write(result))
                self.wait(2)
            else:
                self.play(
                    Write(property2[i].shift(0.6*LEFT)
                          )
                )
            self.wait(3)    

        self.play(FadeOut(property2))
        self.play(Unwrite(result))
        self.wait()
        
        disp_sub(self, lang='fr')


class ExpectedValue3(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Espérance mathématique")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            r"\mathbb{E}(X+Y) = \mathbb{E}(X) + \mathbb{E}(Y)"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        property3 = MathTex(
            r"p_{ij} = P_{(X, Y)}(X = x_i, Y = y_j)\\",
            r"p_{i.} = \sum_jp_{ij} = P_X(X = x_i)\\",
            r"p_{.j} = \sum_ip_{ij} = P_Y(Y = y_j)\\",
            r"\mathbb{E}(X+Y) = \sum_{i,j}p_{ij}(x_i+y_j)\\",
            r"\sum_{i,j}p_{ij}x_i + \sum_{i,j}p_{ij}y_j\\",
            r"\sum_{i}x_i\sum_{j}p_{ij} + \sum_{j}y_j\sum_{i}p_{ij}\\",
            r"\mathbb{E}(X+Y) = \sum_{i}p_{i.}x_i + \sum_{j}p_{.j}y_j"
        )
        title_prop3 = Title("Propriété 3")
        self.play(ReplacementTransform(title, title_prop3))

        for i in range(len(property3)):
            if i == 2:
                self.play(
                    Write(
                        property3[i].scale(0.75).shift(0.6*LEFT)
                    )
                )
            elif i == len(property3) - 1:
                self.play(
                    Write(
                        property3[i].shift(0.6*LEFT+DOWN)
                    )
                )
                result = SurroundingRectangle(property3[i])
                self.play(Write(result))
                self.wait(2)
            else:
                self.play(
                    Write(property3[i].shift(0.6*LEFT)
                          )
                )
            self.wait(3)    

        self.play(FadeOut(property3))
        self.play(Unwrite(result))
        self.wait()
        
        disp_sub(self, lang='fr')


class NpremEntiers(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        title_prop3 = Title("Exemple 3")
        self.play(ReplacementTransform(title, title_prop3))

        property3 = MathTex(
            r"u_k = k^{2}\\",
            r"u_{k+1} - u_{k} = (k+1)^{2} - k^{2}\\",
            r"u_{k+1} - u_{k} = 2k + 1\\",
            r"S_n = \sum_{k = 0}^n(2k + 1)\\",
            r"S_n = 2\sum_{k = 0}^nk + (n + 1)\\",
            r"S_n = (n + 1)^2\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{(n + 1)^2 - (n + 1)}{2}\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{n^{2} + n}{2}\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{n(n + 1)}{2}\\",
        )
            
            
        for i in range(len(property3)):
            self.play(Write(property3[i].shift(0.6*LEFT+DOWN)))
            self.wait()    

        self.wait(3)
        self.play(FadeOut(property3))
        self.wait()
        disp_sub(self, lang='fr')
        

class NpremSquare(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        title_prop4 = Title("Exemple 4")
        self.play(ReplacementTransform(title, title_prop4))

        property4 = MathTex(
            r"u_k = k^{3}\\",
            r"u_{k+1} - u_{k} = (k+1)^{3} - k^{3}\\",
            r"u_{k+1} - u_{k} = 3k^2 + 3k + 1\\",
            r"S_n = \sum_{k = 0}^n(3k^2 + 3k + 1)\\",
            r"S_n = 3\sum_{k = 0}^nk^2 + 3\sum_{k = 0}^nk + (n + 1)\\",
            r"S_n = (n + 1)^3\\",
            r"\sum_{k = 0}^nk = \dfrac{n(n+1)}{2}\\",
            r"\sum_{k = 0}^nk^2 = \dfrac{2(n + 1)^3 - 3n(n+1) - 2(n + 1)}{6}\\",
            r"\sum_{k = 0}^nk^2 = \dfrac{n(n + 1)(2n + 1)}{6}\\",
        )
            
            
        for i in range(len(property4)):
            if i == len(property4) - 2:
                self.play(
                    Write(
                        property4[i].scale(0.8).shift(0.6*LEFT+DOWN)
                    )
                )
            elif i == len(property4) - 1:
                self.play(
                    Write(
                        property4[i].shift(0.6*LEFT+DOWN)
                    )
                )
                result = SurroundingRectangle(property4[i])
                self.play(Write(result))
                self.wait(2)
            else:
                self.play(
                    Write(
                        property4[i].shift(0.6*LEFT+DOWN)
                    )
                )
            self.wait()    

        self.wait(4)
        self.play(FadeOut(property4))
        self.play(Unwrite(result))
        self.wait()
        
        disp_sub(self, lang='fr')
        
        

