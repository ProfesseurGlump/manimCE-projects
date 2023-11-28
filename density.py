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
        sub_scale = 0.8 
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


def replace_and_write(self, old, new, pos_ref, duration, **lines_and_scales):
    to_be_continued = False
    m, n = len(old), len(new)
    min_mn = m
    keys = lines_and_scales.keys()
    
    if m < n:
        to_be_continued = True
        min_mn = m
    elif m > n:
        self.play(*[FadeOut(old[i]) for i in range(n, m)])
        to_be_continued = False
        min_mn = n
    else: min_mn = m
    
    if lines_and_scales == {}:
        self.play(
            ReplacementTransform(
                old[0], new[0].next_to(pos_ref, 3 * DOWN)
            ),
            *[
                ReplacementTransform(
                    old[i],
                    new[i].next_to(new[i-1], DOWN)
                ) for i in range(1, min_mn)
            ]
        )
        if to_be_continued:
            self.play(
                *[
                    Write(new[i].next_to(new[i-1], DOWN)
                          ) for i in range(min_mn, n)
                ]
            )
    else:
        self.play(
            *[
                ReplacementTransform(
                old[0],
                new[0].scale(
                    lines_and_scales['0']
                ).next_to(pos_ref, 3 * DOWN)
                ) for i in range(1) if '0' in keys
              ],
            *[
                ReplacementTransform(
                old[0],
                new[0].next_to(pos_ref, 3 * DOWN)
                ) for i in range(1) if '0' not in keys
              ],
            *[
                ReplacementTransform(
                    old[i],
                    new[i].scale(
                        lines_and_scales[str(i)]
                    ).next_to(new[i - 1], DOWN)
                ) for i in range(1, min_mn) if str(i) in keys
            ],
            *[
                ReplacementTransform(
                    old[i],
                    new[i].next_to(new[i-1], DOWN)
                ) for i in range(1, min_mn) if str(i) not in keys
            ],
        )
        if to_be_continued:
            self.play(
                *[
                    Write(
                        new[i].scale(
                            lines_and_scales[str(i)]).next_to(
                                new[i - 1], DOWN)
                    ) for i in range(min_mn, n) if str(i) in keys
                ],
                *[
                    Write(
                        new[i].next_to(new[i - 1], DOWN)
                    ) for i in range(min_mn, n) if not str(i) in keys
                ],
            )
    
    self.wait(duration)


    
    
def cursive_msg(phrase, sep, font_size=40):
    inboxes = phrase.split(sep)
    msg = inbox_msg(*inboxes, font_size=font_size)
    return msg




def density_def_recall():
    definition = [r"Rappel : "]
    definition += [r"Soit \(X\) une v.a.r : on dit que X "]
    definition += [r"admet une densité \(f\) si sa fonction "]
    definition += [r"de répartition \(F\) est continue et "]
    definition += [r"s'écrire sous la forme : "]
    centered_expr = r"\[\forall x\in\mathbb{R}, F(x) = "
    centered_expr += r"\int_{-\infty}^xf(t)dt\]"
    definition += [centered_expr]
    definition += [r"avec : "]
    definition += [r"\[1. f \geqslant 0\] "]
    centered = r"\[2. f\in\mathcal{C}^0\backslash\mathcal{D} "
    centered += r"\quad \mathbb{P}(x\in\mathcal{D}) = 0\]"
    definition += [centered]
    definition += [r"\[3. \int_{-\infty}^{+\infty}f(t)dt = 1\]"]
        
    density_def_msg = [Tex(d) for d in definition]
    
    return density_def_msg




def prob_def_recall():
    definition = [r"Rappel : "]
    definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
    definition += [r"un espace probabilisé et"]
    centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
    centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
    definition += [centered_expr]
    definition += [r"une variable aléatoire discrète. Alors, "]
    definition += [r"avec la convention \(s^0 = 1\), "]
    centered_expr = r"\[G_X : s\mapsto \mathbb{E}(s^X) = "
    centered_expr += r"\sum_{k = 0}^{+\infty}\mathbb{P}_X(\{n\})s^k\]"
    definition += [centered_expr]
    definition += [r"est définie et continue sur \([-1;1]\) "]
    definition += [r"(c'est-à-dire continue sur \(]-1;1[\), "]
    definition += [r"continue à droite en \(-1\) et "]
    definition += [r"continue à gauche en \(1\))."]
        
    prob_def_msg = [Tex(d) for d in definition]
    
    return prob_def_msg




def expectation_def_recall():
    definition = [r"Rappel : "]
    centered_expr = r"\[G_X(s) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"\mathbb{P}_X(\{k\})s^k\]"
    definition += [centered_expr]
    centered_expr = r"\[G'_X(s) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k\mathbb{P}_X(\{k\})s^{k - 1}\]"
    definition += [centered_expr]
    centered_expr = r"\[G'_X(1) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k\mathbb{P}_X(\{k\})1^{k - 1}\]"
    definition += [centered_expr]
    centered_expr = r"\[G'_X(1) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k\mathbb{P}_X(\{k\}) = \mathbb{E}(X)\]"
    definition += [centered_expr]
        
    exp_def_msg = [Tex(d) for d in definition]
    
    return exp_def_msg




def variance_def_recall():
    definition = [r"Rappel : "]
    centered_expr = r"\[G_X(s) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"\mathbb{P}_X(\{k\})s^k\]"
    definition += [centered_expr]
    centered_expr = r"\[G'_X(s) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k\mathbb{P}_X(\{k\})s^{k - 1}\]"
    definition += [centered_expr]
    centered_expr = r"\[G'_X(1) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k\mathbb{P}_X(\{k\}) = \mathbb{E}(X)\]"
    definition += [centered_expr]
    centered_expr = r"\[G''_X(s) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k(k - 1)\mathbb{P}_X(\{k\})s^{k - 2}\]"
    definition += [centered_expr]
    centered_expr = r"\[G''_X(1) = \sum_{k = 0}^{+\infty}"
    centered_expr += r"k(k - 1)\mathbb{P}_X(\{k\})1^{k - 2}\]"
    definition += [centered_expr]
    centered_expr = r"\[G''_X(1) = \mathbb{E}(X^2) - "
    centered_expr += r"G'_X(1)\]"
    definition += [centered_expr]
    centered_expr = r"\[\mathbb{V}(X) = G''_X(1) + G'_X(1) "
    centered_expr += r"- \left[G'_X(1)\right]^2\]"
    definition += [centered_expr]
    
    var_def_msg = [Tex(d) for d in definition]
    
    return var_def_msg




def generate_uniform_density_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b):
    c = 1 / (b - a)
    y_sup = c + 0.25
    ax = Axes(
        x_range=[x_inf, x_sup],
        y_range=[y_inf, y_sup],
        axis_config={"include_numbers": True}
    ).scale(0.65).next_to(ax_ref, ax_pos)
    
    A_0 = ax.coords_to_point(x_inf,0)
    dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)

    A_1 = ax.coords_to_point(a,0)
    dotA_1 = Dot(A_1, fill_opacity=1, color=RED)
    labelA_1 = MathTex(r"a = " + f"{a}", color=GREEN)
    A_0A_1 = Line(A_0, A_1, color=GREEN)
        
    A_2 = ax.coords_to_point(a,c)
    dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)        
    vert_A_2 = ax.get_vertical_line(
        A_2,
        line_config={"dashed_ratio": 0.85},
        color=RED
    )
        
    A_3 = ax.coords_to_point(b,c)
    dotA_3 = Dot(A_3, fill_opacity=1, color=GREEN)
        
    A_2A_3 = Line(A_2, A_3, color=GREEN)
    vert_A_3 = ax.get_vertical_line(
        A_3,
        line_config={"dashed_ratio": 0.85},
        color=RED
    )
        
    A_4 = ax.coords_to_point(b,0)
    dotA_4 = Dot(A_4, fill_opacity=1, color=RED)
    labelA_4 = MathTex(r"b = " + f"{b}", color=GREEN)

    A_5 = ax.coords_to_point(x_sup,0)
    dotA_5 = Dot(A_5, fill_opacity=1, color=GREEN)
    A_4A_5 = Line(A_4, A_5, color=GREEN)

    Adots = [dotA_0, dotA_1, dotA_2, dotA_3, dotA_4, dotA_5]
    Alines = [A_0A_1, vert_A_2, A_2A_3, vert_A_3, A_4A_5]

    if b - a == 1:
        uniform_density = r"f(x) = "
    else:
        uniform_density = r"f(x) = \dfrac{1}{"
        uniform_density += f"{b - a}" + r"}"
        
    uniform_density += r"\mathbb{I}_{["
    uniform_density += f"{a};{b}" + r"]}(x)"
    uniform = MathTex(
        uniform_density,
        color=GREEN
    ).scale(0.85)
    
    Alabels = [labelA_1, uniform, labelA_4]
    if b - a < 1.1:
        Alab_pos = [
            (dotA_1, 0.1 * LEFT + DOWN),
            (ax, 3 * DOWN),
            (dotA_4, 0.1 * RIGHT + DOWN)
        ]
        labelA_1 = labelA_1.scale(0.75)
        labelA_4 = labelA_4.scale(0.75)
    else:
        Alab_pos = [
            (dotA_1, DOWN),
            (ax, 3 * DOWN),
            (dotA_4, DOWN)
        ]

    polygon_list = [A_1, A_2, A_3, A_4]
    A_1A_2A_3A_4 = Polygon(*polygon_list, fill_opacity=1, color=BLUE, stroke_color=BLUE)

    return ax, Adots, Alines, Alabels, Alab_pos, A_1A_2A_3A_4




def generate_uniform_cmf_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b):
    y_sup = 1.25
    ax = Axes(
        x_range=[x_inf, x_sup],
        y_range=[y_inf, y_sup],
        axis_config={"include_numbers": True}
    ).scale(0.65).next_to(ax_ref, ax_pos)
    
    A_0 = ax.coords_to_point(x_inf,0)
    dotA_0 = Dot(A_0, fill_opacity=1, color=BLUE)

    A_1 = ax.coords_to_point(a,0)
    dotA_1 = Dot(A_1, fill_opacity=1, color=BLUE)
    labelA_1 = MathTex(r"a = " + f"{a}", color=BLUE)
    A_0A_1 = Line(A_0, A_1, color=BLUE)

    A_2 = ax.coords_to_point(b,1)
    dotA_2 = Dot(A_2, fill_opacity=1, color=BLUE)
    A_1A_2 = Line(A_1, A_2, color=BLUE)
        
    A_2_x = ax.coords_to_point(b,0)
    dotA_2_x = Dot(A_2_x, fill_opacity=1, color=RED)
    labelA_2_x = MathTex(r"b = " + f"{b}", color=BLUE)
    vert_b = ax.get_vertical_line(
        A_2_x,
        line_config={"dashed_ratio": 0.85},
        color=RED
    )

    A_3 = ax.coords_to_point(x_sup,1)
    dotA_3 = Dot(A_3, fill_opacity=1, color=BLUE)
    A_2A_3 = Line(A_2, A_3, color=BLUE)

    Adots = [dotA_0, dotA_1, dotA_2, dotA_3]
    Alines = [A_0A_1, A_1A_2, vert_b, A_2A_3]

    
    if a > 0:
        num = r"x - " + f"{a}"
    elif a == 0:
        num = r"x"
    else:
        num = f"x + {-a}"

    if b - a == 1:
        uniform_cmf = f"F(x) = ({num})"
    else:
        uniform_cmf = r"F(x) = \dfrac{"
        uniform_cmf += f"{num}" + r"}{"
        uniform_cmf += f"{b - a}" + r"} "
        
    uniform_cmf += r"\mathbb{I}_{["
    uniform_cmf += f"{a}" + r" ; "
    uniform_cmf += f"{b}" + r"]}(x) "
    uniform_cmf += r"+ \mathbb{I}_{]" 
    uniform_cmf += f"{b}"
    uniform_cmf += r" ; +\infty[}(x)"
    
    uniform = MathTex(
        uniform_cmf,
        color=BLUE
    ).scale(0.85)
    
    Alabels = [labelA_1, labelA_2_x, uniform]
    n = len(Alabels)
    if b - a < 1.1:
        Alab_pos = [
            (dotA_1, 0.1 * LEFT + DOWN),
            (dotA_2_x, 0.1 * RIGHT + DOWN),
            (ax, 3 * DOWN),
        ]
        labelA_1 = labelA_1.scale(0.75)
        labelA_2_x = labelA_2_x.scale(0.75)
    else:
        Alab_pos = [
            (dotA_1, DOWN),
            (dotA_2_x, DOWN),
            (ax, 3 * DOWN),
        ]

    return ax, Adots, Alines, Alabels, Alab_pos




class Uniform1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Variables aléatoires à densité avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.75))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer | "
        phrase += "la fonction de densité de la | "
        phrase += "uniforme sur l'intervalle [a ; b] ? | "
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(1.5)

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_question,
                title_clap.scale(0.75)
            )
        )
        self.wait(.75)

        title_rep = Title("Regardez jusqu'au bout pour la réponse")
        self.play(
            ReplacementTransform(
                title_clap,
                title_rep.scale(0.75)
            ),
            FadeOut(msg)
        )
        self.wait(.75)

        def_msg = density_def_recall()
        n = len(def_msg)
        self.play(
            Write(def_msg[0].next_to(title_rep, 3 * DOWN))
        )
        self.wait()
        self.play(
            *[
                Write(
                    def_msg[i].next_to(
                        def_msg[i-1],
                        DOWN
                    )
                ) for i in range(1, n)
            ]
        )
        self.wait(2.5)

        uniform_prob = [r"\raggedleft Si \(X\) suit une loi de uniforme "]
        uniform_prob += [r"\raggedleft sur l'intervalle [a;b] alors "]
        uniform_prob += [r"\[\int_{-\infty}^{+\infty}f(t)dt = 1\]"]
        uniform_prob += [r"\[\Rightarrow \int_{a}^{b}cdt = 1\]"]
        uniform_prob += [r"\[\Rightarrow c(b - a) = 1\]"]

        split = r"\[\Rightarrow f(t) = \dfrac{1}{b - a} "
        split += r"\mathbb{I}_{[a; b]}(t)\]"
        uniform_prob += [split]
        
        uniform_prob += [r"avec "]
        uniform_prob += [r"\[\mathbb{I}_{[a; b]}(t) = 1\iff t\in [a; b]\]"]

        centered_expr = r"\[\mathbb{I}_{[a; b]}(t) = 0\iff "
        centered_expr += r"t \not \in [a; b]\]"
        uniform_prob += [centered_expr]
        
        unif_msg = [Tex(u) for u in uniform_prob]
        
        
        replace_and_write(
            self,
            old=def_msg,
            new=unif_msg,
            pos_ref=title_rep,
            duration=2.5,
        )
        box = SurroundingRectangle(unif_msg[-4])
        self.play(Write(box))
        self.wait()

        
        phrase = "On a bien calculé la fonction | "
        phrase += "de densité de la loi de probabilité | "
        phrase += "uniforme sur l'intervalle [a; b]"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        self.play(FadeOut(box))
        self.wait()
        
        replace_and_write(
            self,
            old=unif_msg,
            new=msg,
            pos_ref=title_rep,
            duration=2.5,
        )

        

        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 1.25, 0, 1
        ax_ref, ax_pos = msg[-1], 3 * DOWN
        graph_n_poly = generate_uniform_density_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax = graph_n_polygon[0]
        _, Adots, Alines, Alabels, Alab_pos, _ = graph_n_poly
        A_1A_2A_3A_4 = graph_n_poly[-1]
        n = len(Alabels)
        
        self.play(
            Create(ax, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(line) for line in Alines],
            *[
                Write(
                    Alabels[i].next_to(
                        Alab_pos[i][0],
                        Alab_pos[i][1],
                    )
                ) for i in range(n)
            ],
        )
        self.wait()

        cmf_msg = r"\[\int_{-\infty}^{+\infty}f(t)dt = 1 "
        cmf_msg += r"= \int_{-\infty}^{+\infty}\dfrac{1}{b - a}"
        cmf_msg += r"\mathbb{I}_{[a; b]}(t)dt\]"
        cmf = Tex(cmf_msg, color=BLUE).scale(0.75)
        box = SurroundingRectangle(Alabels[1])
        self.play(
            Write(box),
            FadeIn(A_1A_2A_3A_4),
            Write(cmf.next_to(A_1A_2A_3A_4, 4 * DOWN))
        )
        self.wait()
        self.play(
            *[FadeOut(t) for t in [A_1A_2A_3A_4, box, cmf]]
        )
        self.wait()
        
        
        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 1.25, 0, 2
        ax_ref, ax_pos = msg[-1], 3 * DOWN
        graph_n_poly = generate_uniform_density_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax = graph_n_poly[0]
        _, Bdots, Blines, Blabels, Blab_pos, _ = graph_n_poly
        B_1B_2B_3B_4 = graph_n_poly[-1]
        n = len(Blabels)
        
        self.play(
            *[
                ReplacementTransform(
                    Adots[i],
                    Bdots[i]
                ) for i in range(len(Bdots))
            ],
            *[
                ReplacementTransform(
                    Alines[i],
                    Blines[i]
                ) for i in range(len(Blines))
            ],
            *[
                ReplacementTransform(
                    Alabels[i],
                    Blabels[i].next_to(Blab_pos[i][0], Blab_pos[i][1])
                ) for i in range(len(Blab_pos))
            ],
        )
        self.wait()
        
        cmf_msg = r"\[\int_{-\infty}^{+\infty}f(t)dt = 1 "
        cmf_msg += r"= \int_{-\infty}^{+\infty}\dfrac{1}{b - a}"
        cmf_msg += r"\mathbb{I}_{[a; b]}(t)dt\]"
        cmf = Tex(cmf_msg, color=BLUE).scale(0.75)
        box = SurroundingRectangle(Blabels[1])
        self.play(
            Write(box),
            FadeIn(B_1B_2B_3B_4),
            Write(cmf.next_to(B_1B_2B_3B_4, 4 * DOWN))
        )
        self.wait()
        self.play(
            *[FadeOut(t) for t in [B_1B_2B_3B_4, box, cmf]]
        )
        self.wait()
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(1.5)
        
        disp_sub(self, lang='fr')



        
class Uniform2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Loi uniforme continue sur [a ; b] avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.75))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer | "
        phrase += "la fonction de répartition de la | "
        phrase += "uniforme sur l'intervalle [a ; b] ? | "
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(1.5)

        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_question,
                title_clap.scale(0.75)
            )
        )
        self.wait(.75)

        title_rep = Title("Regardez jusqu'au bout pour la réponse")
        self.play(
            ReplacementTransform(
                title_clap,
                title_rep.scale(0.75)
            ),
            FadeOut(msg)
        )
        self.wait(.75)

        def_msg = density_def_recall()
        n = len(def_msg)
        self.play(
            Write(def_msg[0].next_to(title_rep, 3 * DOWN))
        )
        self.wait()
        self.play(
            *[
                Write(
                    def_msg[i].next_to(
                        def_msg[i-1],
                        DOWN
                    )
                ) for i in range(1, n)
            ]
        )
        self.wait(2.5)

        uniform_prob = [r"\raggedleft Si \(X\) suit une loi de uniforme "]
        uniform_prob += [r"\raggedleft sur l'intervalle [a;b] alors "]
        uniform_prob += [r"la fonction de répartition "]
        uniform_prob += [r"\[F(x) = \mathbb{P}(X\leqslant x) = \int_{-\infty}^{x}f(t)dt\]"]
        centered = r"\[F(x) = "
        centered += r"\dfrac{x - a}{b - a}\mathbb{I}_{[a ; b]}(x) "
        centered += r"+ \mathbb{I}_{]b ; +\infty[}(x)\]"
        uniform_prob += [centered]

        uniform_prob += [r"avec "]
        uniform_prob += [r"\[\mathbb{I}_{[a; b]}(x) = 1\iff x\in [a; b]\]"]

        centered_expr = r"\[\mathbb{I}_{[a; b]}(x) = 0\iff "
        centered_expr += r"x \not \in [a; b]\]"
        uniform_prob += [centered_expr]
        
        uniform_prob += [r"\[\mathbb{I}_{]b ; +\infty[}(x) = 1\iff x > b\]"]
        centered_expr = r"\[\mathbb{I}_{]b ; +\infty[}(x) = 0\iff "
        centered_expr += r"x \leqslant b\]"
        uniform_prob += [centered_expr]
        
        unif_msg = [Tex(u) for u in uniform_prob]
        
        
        replace_and_write(
            self,
            old=def_msg,
            new=unif_msg,
            pos_ref=title_rep,
            duration=2.5,
        )
        
        box = SurroundingRectangle(unif_msg[-6])
        ax_ref, ax_pos = unif_msg[-1], 3 * DOWN
        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 1.25, 0, 0.5
        cmf_graph = generate_uniform_cmf_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax_cmf_1 = cmf_graph[0]
        _, Adots, Alines, Alabels, Alab_pos = cmf_graph
        n = len(Alabels)
        
        self.play(
            Write(box),
            Create(ax_cmf_1, run_time=1.5),
            *[Write(d) for d in Adots],
            *[Write(l) for l in Alines],
            *[
                Write(
                    Alabels[i].next_to(
                        Alab_pos[i][0],
                        Alab_pos[i][1]
                    )
                ) for i in range(n)
            ]
        )
        self.wait()
        ax_ref, ax_pos = unif_msg[-1], 3 * DOWN
        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 1.25, -0.5, 1.5
        cmf_graph = generate_uniform_cmf_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax_cmf_2 = cmf_graph[0]
        _, Bdots, Blines, Blabels, Blab_pos = cmf_graph
        n = len(Blabels)
        self.play(
            ReplacementTransform(ax_cmf_1, ax_cmf_2),
            *[
                ReplacementTransform(
                    Adots[i],
                    Bdots[i]
                ) for i in range(len(Adots))
            ],
            *[
                ReplacementTransform(
                    Alines[i],
                    Blines[i]
                ) for i in range(len(Blines))
            ],
            *[
                ReplacementTransform(
                    Alabels[i],
                    Blabels[i].next_to(
                        Blab_pos[i][0],
                        Blab_pos[i][1]
                    )
                ) for i in range(len(Blabels))
            ]
        )
        self.wait()
        
        phrase = "On a bien calculé la fonction | "
        phrase += "de répartition de la loi de probabilité | "
        phrase += "uniforme sur l'intervalle [a; b]"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        self.play(
            FadeOut(box),
            *[FadeOut(Blabel) for Blabel in Blabels],
            *[FadeOut(d) for d in Bdots],
            *[FadeOut(l) for l in Blines],
            FadeOut(ax_cmf_2)
        )
        self.wait()
        
        replace_and_write(
            self,
            old=unif_msg,
            new=msg,
            pos_ref=title_rep,
            duration=2.5,
        )

        

        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 2.5, 0, 0.5
        ax_ref, ax_pos = msg[-1], 5 * DOWN
        graph_n_poly = generate_uniform_density_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax_density_1 = graph_n_poly[0]
        _, Adots, Alines, Alabels, Alab_pos, _ = graph_n_poly
        A_1A_2A_3A_4 = graph_n_poly[-1]
        n = len(Alabels)
        
        self.play(
            ReplacementTransform(ax_cmf_2, ax_density_1, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(line) for line in Alines],
            *[
                Write(
                    Alabels[i].next_to(
                        Alab_pos[i][0],
                        Alab_pos[i][1],
                    )
                ) for i in range(n)
            ],
        )
        self.wait()

        cmf_msg = r"\[\int_{-\infty}^{+\infty}f(t)dt = 1 "
        cmf_msg += r"= \int_{-\infty}^{+\infty}\dfrac{1}{b - a}"
        cmf_msg += r"\mathbb{I}_{[a; b]}(t)dt\]"
        cmf = Tex(cmf_msg, color=BLUE).scale(0.75)
        box = SurroundingRectangle(Alabels[1])
        self.play(
            Write(box),
            FadeIn(A_1A_2A_3A_4),
            Write(cmf.next_to(A_1A_2A_3A_4, 4 * DOWN))
        )
        self.wait()
        self.play(
            *[FadeOut(t) for t in [A_1A_2A_3A_4, box, cmf]]
        )
        self.wait()
        
        

        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, 0, 1.25, -0.5, 1.5
        ax_ref, ax_pos = msg[-1], 5 * DOWN
        graph_n_poly = generate_uniform_density_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, a, b)
        ax_density_2 = graph_n_poly[0]
        _, Bdots, Blines, Blabels, Blab_pos, _ = graph_n_poly
        B_1B_2B_3B_4 = graph_n_poly[-1]
        n = len(Blabels)
        
        self.play(
            ReplacementTransform(ax_density_1, ax_density_2),
            *[
                ReplacementTransform(
                    Adots[i],
                    Bdots[i]
                ) for i in range(len(Bdots))
            ],
            *[
                ReplacementTransform(
                    Alines[i],
                    Blines[i]
                ) for i in range(len(Blines))
            ],
            *[
                ReplacementTransform(
                    Alabels[i],
                    Blabels[i].next_to(
                        Blab_pos[i][0],
                        Blab_pos[i][1]
                    )
                ) for i in range(len(Blab_pos))
            ],
        )
        self.wait()
        
        cmf_msg = r"\[\int_{-\infty}^{+\infty}f(t)dt = 1 "
        cmf_msg += r"= \int_{-\infty}^{+\infty}\dfrac{1}{b - a}"
        cmf_msg += r"\mathbb{I}_{[a; b]}(t)dt\]"
        cmf = Tex(cmf_msg, color=BLUE).scale(0.75)
        box = SurroundingRectangle(Blabels[1])
        self.play(
            Write(box),
            FadeIn(B_1B_2B_3B_4),
            Write(
                cmf.next_to(
                    B_1B_2B_3B_4,
                    4 * DOWN
                )
            )
        )
        self.wait()
        self.play(
            *[FadeOut(t) for t in [B_1B_2B_3B_4, box, cmf]]
        )
        self.wait()
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(1.5)
        
        disp_sub(self, lang='fr')
        


class Uniform3(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Lois uniformes continues sur [a ; b] avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.75))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))


        
        title_clap = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_start,
                title_clap.scale(0.75)
            )
        )
        self.wait(.75)


        def_msg = density_def_recall()
        n = len(def_msg)
        self.play(
            Write(def_msg[0].next_to(title_clap, 3 * DOWN))
        )
        self.wait()
        self.play(
            *[
                Write(
                    def_msg[i].next_to(
                        def_msg[i-1],
                        DOWN
                    )
                ) for i in range(1, n)
            ]
        )
        self.wait(2.5)

        #############################################################
        ##################### FIRST TRIAL ###########################
        #############################################################
        
        x_inf, x_sup, y_inf, y_sup = -2, 2, 0, 1.25
        a, b = -1.5, -0.5
        df_1_ax_ref, df_1_ax_pos = title_clap, 5 * DOWN
        graph_n_poly_1 = generate_uniform_density_graph(
            df_1_ax_ref, df_1_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_density_1_fix = graph_n_poly_1[0]
        ax_density_1_move = graph_n_poly_1[0]
        _, Adots_1, Alines_1, Alabels_1, Alab_pos_1, _ = graph_n_poly_1
        A_1A_2A_3A_4 = graph_n_poly_1[-1]

        dft_1_msg = f"Densité de la uniforme sur [{a} ; {b}]"
        density_title_1 = Title(dft_1_msg).scale(0.75)

        self.play(
            *[FadeOut(t) for t in def_msg],
            ReplacementTransform(
                title_clap,
                density_title_1
            ),
            Create(
                ax_density_1_move,
                run_time=2
            ),
            *[Write(d) for d in Adots_1],   
            *[Create(line) for line in Alines_1],
            *[
                Write(
                    Alabels_1[i].next_to(
                        Alab_pos_1[i][0],
                        Alab_pos_1[i][1],
                    )
                ) for i in range(len(Alabels_1))
            ],
        )
        self.wait(2)

        
        cmf_1_ax_ref, cmf_1_ax_pos = ax_density_1_fix, 9 * DOWN
        cmf_graph_1 = generate_uniform_cmf_graph(
            cmf_1_ax_ref, cmf_1_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_cmf_1 = cmf_graph_1[0]
        _, Bdots_1, Blines_1, Blabels_1, Blab_pos_1 = cmf_graph_1


        cmf_and_df_msg_1 = r"Densité et fonction de répartition "
        cmf_and_df_msg_1 += r"la loi \(\mathcal{U}\)(["
        cmf_and_df_msg_1 += f"{a}" + r" ; " + f"{b}" + r"])"
        cmf_and_df_title_1 = Title(cmf_and_df_msg_1).scale(0.65)
                
        
        self.play(
            FadeIn(A_1A_2A_3A_4),
            ReplacementTransform(
                density_title_1,
                cmf_and_df_title_1
            ),
            Create(
                ax_cmf_1,
                run_time=2
            ),
            *[Write(d) for d in Bdots_1],
            *[Write(l) for l in Blines_1],
            *[
                Write(
                    Blabels_1[i].next_to(
                        Blab_pos_1[i][0],
                        Blab_pos_1[i][1]
                    )
                ) for i in range(len(Blabels_1))
            ]
        )
        self.wait(2)

        #############################################################
        #################### SECOND TRIAL ###########################
        #############################################################
        
        a, b = -0.5, 0
        
        df_2_ax_ref, df_2_ax_pos = title_clap, 5 * DOWN
        graph_n_poly_2 = generate_uniform_density_graph(
            df_2_ax_ref, df_2_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_density_2_fix = graph_n_poly_2[0]
        ax_density_2_move = graph_n_poly_2[0]
        _, Adots_2, Alines_2, Alabels_2, Alab_pos_2, _ = graph_n_poly_2
        A_1A_2A_3A_4_2 = graph_n_poly_2[-1]

        dft2_msg = f"Densité de la uniforme sur [{a} ; {b}]"
        density_title_2 = Title(dft2_msg).scale(0.75)

        
        self.play(
            FadeOut(A_1A_2A_3A_4),
            ReplacementTransform(
                cmf_and_df_title_1,
                density_title_2
            ),
            ReplacementTransform(
                ax_density_1_move,
                ax_density_2_move,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Adots_1[i],
                    Adots_2[i]
                ) for i in range(len(Adots_2))
            ],   
            *[
                ReplacementTransform(
                    Alines_1[i],
                    Alines_2[i]
                ) for i in range(len(Alines_2))
            ],
            *[
                ReplacementTransform(
                    Alabels_1[i],
                    Alabels_2[i].next_to(
                        Alab_pos_2[i][0],
                        Alab_pos_2[i][1],
                    )
                ) for i in range(len(Alabels_2))
            ],
        )
        self.wait(2)

        cmf_2_ax_ref, cmf_2_ax_pos = ax_density_2_fix, 9 * DOWN
        cmf_graph_2 = generate_uniform_cmf_graph(
            cmf_2_ax_ref, cmf_2_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_cmf_2 = cmf_graph_2[0]
        _, Bdots_2, Blines_2, Blabels_2, Blab_pos_2 = cmf_graph_2

        cmf_and_df_msg_2 = r"Densité et fonction de répartition de la "
        cmf_and_df_msg_2 += r"loi \(\mathcal{U}\)"
        cmf_and_df_msg_2 += f"([{a} ; {b}])"
        cmf_and_df_title_2 = Title(cmf_and_df_msg_2).scale(0.65)
        
        self.play(
            FadeIn(A_1A_2A_3A_4_2),
            ReplacementTransform(
                density_title_2,
                cmf_and_df_title_2
            ),
            ReplacementTransform(
                ax_cmf_1,
                ax_cmf_2,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Bdots_1[i],
                    Bdots_2[i]
                ) for i in range(len(Bdots_1))
            ],
            *[
                ReplacementTransform(
                    Blines_1[i],
                    Blines_2[i]
                ) for i in range(len(Blines_1))],
            *[
                ReplacementTransform(
                    Blabels_1[i],
                    Blabels_2[i].next_to(
                        Blab_pos_2[i][0],
                        Blab_pos_2[i][1]
                    )
                ) for i in range(len(Alabels_2))
            ]
        )
        self.wait(2)

        #############################################################
        ##################### THIRD TRIAL ###########################
        #############################################################
        
        a, b = 0, 0.25
        df_3_ax_ref, df_3_ax_pos = title_clap, 5 * DOWN
        graph_n_poly_3 = generate_uniform_density_graph(
            df_3_ax_ref, df_3_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_density_3_fix = graph_n_poly_3[0]
        ax_density_3_move = graph_n_poly_3[0]
        _, Adots_3, Alines_3, Alabels_3, Alab_pos_3, _ = graph_n_poly_3
        A_1A_2A_3A_4_3 = graph_n_poly_3[-1]
        dft_3_msg = f"Densité de la uniforme sur [{a} ; {b}]"
        density_title_3 = Title(dft_3_msg).scale(0.75)
        
        self.play(
            FadeOut(A_1A_2A_3A_4_2),
            ReplacementTransform(
                cmf_and_df_title_2,
                density_title_3
            ),
            ReplacementTransform(
                ax_density_2_move,
                ax_density_3_move,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Adots_2[i],
                    Adots_3[i]
                ) for i in range(len(Adots_3))
            ],   
            *[
                ReplacementTransform(
                    Alines_2[i],
                    Alines_3[i]
                ) for i in range(len(Alines_3))
            ],
            *[
                ReplacementTransform(
                    Alabels_2[i],
                    Alabels_3[i].next_to(
                        Alab_pos_3[i][0],
                        Alab_pos_3[i][1],
                    )
                ) for i in range(len(Alabels_3))
            ],
        )
        self.wait(2)
        
        cmf_3_ax_ref, cmf_3_ax_pos = ax_density_3_fix, 9 * DOWN
        cmf_graph_3 = generate_uniform_cmf_graph(
            cmf_3_ax_ref, cmf_3_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_cmf_3 = cmf_graph_3[0]
        _, Bdots_3, Blines_3, Blabels_3, Blab_pos_3, = cmf_graph_3
        cmf_and_df_msg_3 = r"Densité et fonction de répartition de la loi \(\mathcal{U}\)"
        cmf_and_df_msg_3 += f"([{a} ; {b}])"
        cmf_and_df_title_3 = Title(cmf_and_df_msg_3).scale(0.65)
        
        self.play(
            FadeIn(A_1A_2A_3A_4_3),
            ReplacementTransform(
                density_title_3,
                cmf_and_df_title_3
            ),
            ReplacementTransform(
                ax_cmf_2,
                ax_cmf_3,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Bdots_2[i],
                    Bdots_3[i]
                ) for i in range(len(Bdots_3))
            ],
            *[
                ReplacementTransform(
                    Blines_2[i],
                    Blines_3[i]
                ) for i in range(len(Blines_3))],
            *[
                ReplacementTransform(
                    Blabels_2[i],
                    Blabels_3[i].next_to(
                        Blab_pos_3[i][0],
                        Blab_pos_3[i][1]
                    )
                ) for i in range(len(Blabels_3))
            ]
        )
        self.wait(2)

        #############################################################
        ##################### FOURTH TRIAL ##########################
        #############################################################
        
        a, b = 0.25, 0.75
        df_4_ax_ref, df_4_ax_pos = title_clap, 5 * DOWN
        graph_n_poly_4 = generate_uniform_density_graph(
            df_4_ax_ref, df_4_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_density_4_fix = graph_n_poly_4[0]
        ax_density_4_move = graph_n_poly_4[0]
        _, Adots_4, Alines_4, Alabels_4, Alab_pos_4, _ = graph_n_poly_4
        A_1A_2A_3A_4_4 = graph_n_poly_4[-1]
        dft_4_msg = f"Densité de la uniforme sur [{a} ; {b}]"
        density_title_4 = Title(dft_4_msg).scale(0.75)
        
        self.play(
            FadeOut(A_1A_2A_3A_4_3),
            ReplacementTransform(
                cmf_and_df_title_3,
                density_title_4
            ),
            ReplacementTransform(
                ax_density_3_move,
                ax_density_4_move,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Adots_3[i],
                    Adots_4[i]
                ) for i in range(len(Adots_4))
            ],   
            *[
                ReplacementTransform(
                    Alines_3[i],
                    Alines_4[i]
                ) for i in range(len(Alines_4))
            ],
            *[
                ReplacementTransform(
                    Alabels_3[i],
                    Alabels_4[i].next_to(
                        Alab_pos_4[i][0],
                        Alab_pos_4[i][1],
                    )
                ) for i in range(len(Alabels_4))
            ],
        )
        self.wait(2)
        
        cmf_4_ax_ref, cmf_4_ax_pos = ax_density_4_fix, 9 * DOWN
        cmf_graph_4 = generate_uniform_cmf_graph(
            cmf_4_ax_ref, cmf_4_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_cmf_4 = cmf_graph_4[0]
        _, Bdots_4, Blines_4, Blabels_4, Blab_pos_4, = cmf_graph_4
        cmf_and_df_msg_4 = r"Densité et fonction de répartition de la loi \(\mathcal{U}\)"
        cmf_and_df_msg_4 += f"([{a} ; {b}])"
        cmf_and_df_title_4 = Title(cmf_and_df_msg_4).scale(0.65)
        
        self.play(
            FadeIn(A_1A_2A_3A_4_4),
            ReplacementTransform(
                density_title_4,
                cmf_and_df_title_4
            ),
            ReplacementTransform(
                ax_cmf_3,
                ax_cmf_4,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Bdots_3[i],
                    Bdots_4[i]
                ) for i in range(len(Bdots_4))
            ],
            *[
                ReplacementTransform(
                    Blines_3[i],
                    Blines_4[i]
                ) for i in range(len(Blines_4))],
            *[
                ReplacementTransform(
                    Blabels_3[i],
                    Blabels_4[i].next_to(
                        Blab_pos_4[i][0],
                        Blab_pos_4[i][1]
                    )
                ) for i in range(len(Blabels_4))
            ]
        )
        self.wait(2)

        #############################################################
        ###################### FIFTH TRIAL ##########################
        #############################################################
        
        a, b = 0.75, 2
        df_5_ax_ref, df_5_ax_pos = title_clap, 5 * DOWN
        graph_n_poly_5 = generate_uniform_density_graph(
            df_5_ax_ref, df_5_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_density_5_fix = graph_n_poly_5[0]
        ax_density_5_move = graph_n_poly_5[0]
        _, Adots_5, Alines_5, Alabels_5, Alab_pos_5, _ = graph_n_poly_5
        A_1A_2A_3A_4_5 = graph_n_poly_5[-1]
        dft_5_msg = f"Densité de la uniforme sur [{a} ; {b}]"
        density_title_5 = Title(dft_5_msg).scale(0.75)
        
        self.play(
            FadeOut(A_1A_2A_3A_4_4),
            ReplacementTransform(
                cmf_and_df_title_4,
                density_title_5
            ),
            ReplacementTransform(
                ax_density_4_move,
                ax_density_5_move,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Adots_4[i],
                    Adots_5[i]
                ) for i in range(len(Adots_5))
            ],   
            *[
                ReplacementTransform(
                    Alines_4[i],
                    Alines_5[i]
                ) for i in range(len(Alines_5))
            ],
            *[
                ReplacementTransform(
                    Alabels_4[i],
                    Alabels_5[i].next_to(
                        Alab_pos_5[i][0],
                        Alab_pos_5[i][1],
                    )
                ) for i in range(len(Alabels_5))
            ],
        )
        self.wait(2)
        
        cmf_5_ax_ref, cmf_5_ax_pos = ax_density_5_fix, 9 * DOWN
        cmf_graph_5 = generate_uniform_cmf_graph(
            cmf_5_ax_ref, cmf_5_ax_pos,
            x_inf, x_sup,
            y_inf, y_sup,
            a, b
        )
        ax_cmf_5 = cmf_graph_5[0]
        _, Bdots_5, Blines_5, Blabels_5, Blab_pos_5, = cmf_graph_5
        cmf_and_df_msg_5 = r"Densité et fonction de répartition de la loi \(\mathcal{U}\)"
        cmf_and_df_msg_5 += f"([{a} ; {b}])"
        cmf_and_df_title_5 = Title(cmf_and_df_msg_5).scale(0.65)
        
        self.play(
            FadeIn(A_1A_2A_3A_4_5),
            ReplacementTransform(
                density_title_5,
                cmf_and_df_title_5
            ),
            ReplacementTransform(
                ax_cmf_4,
                ax_cmf_5,
                run_time=2
            ),
            *[
                ReplacementTransform(
                    Bdots_4[i],
                    Bdots_5[i]
                ) for i in range(len(Bdots_5))
            ],
            *[
                ReplacementTransform(
                    Blines_4[i],
                    Blines_5[i]
                ) for i in range(len(Blines_5))],
            *[
                ReplacementTransform(
                    Blabels_4[i],
                    Blabels_5[i].next_to(
                        Blab_pos_5[i][0],
                        Blab_pos_5[i][1]
                    )
                ) for i in range(len(Blabels_5))
            ]
        )
        self.wait(2)

        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                cmf_and_df_title_5,
                title_end.scale(0.75)
            ),
        )
        self.wait(2)
        
        disp_sub(self, lang='fr')
        
        
