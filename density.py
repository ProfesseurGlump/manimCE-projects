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
    definition += [r"1. \(f\) positive. "]
    centered = r"2. \(f\) possède un nombre fini \\"
    centered += r"de points de discontinuité."
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


def generate_uniform_graph(x_inf, x_sup, y_inf, y_sup, a, b):
    c = 1 / (b - a)
    # y_inf, y_sup = -c * 0.1, c * 1.25

    ax = Axes(
        x_range=[x_inf, x_sup],
        y_range=[y_inf, y_sup],
        axis_config={"include_numbers": True}
    ).scale(0.65)
    
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
    
    uniform_density = r"f(x) = " + f"{c}"
    uniform_density += r"\times \mathbb{I}_{["
    uniform_density += f"{a};{b}" + r"]}(x)"
    uniform = MathTex(uniform_density, color=GREEN)
    
    Alabels = [labelA_1, uniform, labelA_4]
    Alab_pos = [(dotA_1, DOWN), (A_2A_3, 4 * UP), (dotA_4, DOWN)]

    return ax, Adots, Alines, Alabels, Alab_pos

class Uniform(Scene):
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
            duration=5,
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
            duration=5,
        )

        

        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, -0.1, 1.25, 0, 1
        ax, Adots, Alines, Alabels, Alab_pos = generate_uniform_graph(x_inf, x_sup, y_inf, y_sup, a, b)
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
        box = SurroundingRectangle(Alabels[1])
        self.play(Write(box))
        self.wait()
        self.play(FadeOut(box))
        self.wait()
        
        

        x_inf, x_sup, y_inf, y_sup, a, b = -1, 2, -0.1, 1.25, 0, 2
        ax, Bdots, Blines, Blabels, Blab_pos = generate_uniform_graph(x_inf, x_sup, y_inf, y_sup, a, b)
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
        box = SurroundingRectangle(Blabels[1])
        self.play(Write(box))
        self.wait()
        self.play(FadeOut(box))
        self.wait()
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            # Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(1.5)
        
        disp_sub(self, lang='fr')
