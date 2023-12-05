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
    centered_expr += r"\mathbb{P}(X\leqslant x)\]"
    definition += [centered_expr]
    centered_expr = r"\[F(x) = \int_{-\infty}^xf(t)dt\]"
    definition += [centered_expr]
    definition += [r"avec : "]
    definition += [r"1. \(f \geqslant 0\) i.e \(f\) est positive"]
    centered = r"\[2. \, f\in\mathcal{C}^0\backslash\mathcal{D} "
    centered += r"\quad \mathbb{P}(x\in\mathcal{D}) = 0\]"
    definition += [centered]
    definition += [r"i.e \(f\) est continue presque partout "]
    definition += [r"et discontinue sur un ensemble "]
    definition += [r"au plus dénombrable de mesure nulle."]
    definition += [r"\[3. \, \int_{-\infty}^{+\infty}f(t)dt = 1\]"]
    definition += [r"i.e l'aire sous le graphe de \(f\) vaut 1"]
        
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



def cmf_computation(a, b):
    cmf_msgs = [r"\[\int_{-\infty}^{+\infty}f(t)dt = 1\]"]
    cmf_msg = r"\[\int_{-\infty}^{+\infty}\dfrac{1}{"
    cmf_msg += f"{b - a}" + r"}\mathbb{I}_{["
    cmf_msg += f"{a}" + r";" + f"{b}" + r"]}(t)dt\]"
    cmf_msgs += [cmf_msg]
    cmf_msg = r"\[\dfrac{1}{" + f"{b - a}" + r"}\int_{"
    cmf_msg += f"{a}" + r"}^{" + f"{b}" + r"}dt = "
    cmf_msg += r"\dfrac{1}{" + f"{b - a}" + r"}\times "
    cmf_msg += f"{b - a}" + r"\]"
    cmf_msgs += [cmf_msg] 
    cmf_text = [
        Tex(
            cmf_msg,
            color=BLUE
        ).scale(0.75) for cmf_msg in cmf_msgs
    ]
    return cmf_text


def targets_to_write(text, ref, size=2, direction=DOWN):
    n = len(text)
    # Create a list of target objects
    targets = [text[0].next_to(ref, size * direction)]
    targets += [
        text[i].next_to(
            text[i - 1],
            size * direction
        ) for i in range(1, n)
    ]
    return text


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
            (ax, 2 * DOWN),
        ]
        labelA_1 = labelA_1.scale(0.75)
        labelA_2_x = labelA_2_x.scale(0.75)
    else:
        Alab_pos = [
            (dotA_1, DOWN),
            (dotA_2_x, DOWN),
            (ax, 2 * DOWN),
        ]

    return ax, Adots, Alines, Alabels, Alab_pos


def generate_exponential_density_graph(ax_ref, ax_pos, theta, x_sup):
    # f(x) = theta * exp(-theta * x)
    ax = Axes(
        x_range=[0, x_sup],
        y_range=[0, theta],
        axis_config={"include_numbers": True}
    ).scale(0.65).next_to(ax_ref, ax_pos)

    exponential_density = f"f(x) = {theta}" + r"\exp(-"
    exponential_density += f"{theta}x)"
    exponential_density += r"\mathbb{I}_{[0; +\infty[}(x)"
    exponential = MathTex(
        exponential_density,
        color=GREEN
    ).scale(0.85)

    exp_dens_curve = ax.plot(
        lambda x: theta * e**(-theta * x), color=GREEN
    )
    
    exp_dens_lab = ax.get_graph_label(
        exp_dens_curve,
        exponential,
        x_val = 0,
        direction = 3 * DOWN
    )

    x_interval = [0, x_sup]
    exp_area = ax.get_area(
        exp_dens_curve,
        x_range=x_interval
    )
    
    return ax, exp_dens_curve, exp_dens_lab, exp_area


def generate_graph(ax_ref, ax_pos, x_inf, x_sup, y_inf, y_sup, *params, **df):
    # 1. f(x) = theta * exp(-theta * x)
    #           => params = [theta] df = {num : f, lab : LaTeX, col : colour}
    # 2. f(x) = (sigma * (2*pi)**0.5)**-1 * exp(-(x - mu)**2 / (2 * sigma**2))
                # params = [mu, sigma]
    # 3. f(x) = theta**p / Gamma(p) * exp**-theta*x * x**(p-1)
    #                      Gamma(p) = \int_0^{+\infty}exp(-x) * x**(p - 1)dx
    #                      params = [theta, p]
    # 4. f(x) = (2**(n/2) * Gamma(n / 2))**-1 * exp(-x/2) * x**(n/2-1)
    #                       params = [n]
    # 5. f(z) = z**(p-1) * (B(p, q) * (1 + z)**(p + q))**-1
                # avec Z = X / Y où X ~ Gamma(p) et Y ~ Gamma(q)
                # avec B(p, q) = Gamma(p) * Gamma(q) / Gamma(p+q)
                # params = [p, q]
    # 6. f(t) = t**(p-1) * (1 - t)**(q - 1) * (B(p, q))**-1
    #             params = [p, q]
    # 7. f(x) = (alpha / x_0) * (x_0 / x)**(alpha + 1)
    #             params = [alpha, x_0]
    ax = Axes(
        x_range=[x_inf, x_sup],
        y_range=[y_inf, y_sup],
        axis_config={"include_numbers": True}
    ).scale(0.65).next_to(ax_ref, ax_pos)

    expr = df["lab"]
    lab = MathTex(
        expr,
        color=df["graph_col"]
    ).scale(0.85)

    curve = ax.plot(df["num"], color=df["graph_col"])
    
    disp_lab = ax.get_graph_label(
        curve,
        lab,
        x_val = x_inf,
        direction = 3 * DOWN
    )

    x_interval = [x_inf, x_sup]
    area = ax.get_area(
        curve,
        x_range=x_interval,
        color=df["area_col"]
    )
    
    return ax, curve, disp_lab, area



class Exo1a(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Norme 1 dans \(\mathbb{R}^2\) avec "
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
        phrase = [r"Savez-vous comment "]
        phrase += [r"représenter l'ensemble"]
        split = r"\[E = \{(x, y)\in\mathbb{R}^2 ; \lvert x \rvert "
        split += r" + \lvert y\rvert \leqslant 2\}\]"
        phrase += [split]
        msg = [Tex(p) for p in phrase]
        targets = targets_to_write(msg, title_start, 3)
        
        self.play(
            *[Write(t) for t in targets],
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(1)


        title_rep = Title("Regardez jusqu'au bout pour la réponse")
        self.play(
            ReplacementTransform(
                title_question,
                title_rep.scale(0.75)
            ),
            *[FadeOut(m) for m in msg]
        )
        self.wait(.75)

        # Case 1
        case_1 = "\((x, y)\in [0 ; 2]^2\)"
        title_case_1 = Title(case_1)

        texte = [r"Si \(x\geqslant 0\) alors \(\lvert x \rvert = x\)."]
        texte += [r"Idem pour \(y\) d'où \(\lvert y \rvert = y\)."]
        center = r"\[\lvert x\rvert + "
        center += r"\lvert y\rvert\leqslant 2"
        center += r"\Rightarrow y\leqslant 2 - x\]"
        texte += [center]
        
        texte_msg = [Tex(t) for t in texte]
        targets = targets_to_write(texte_msg, title_case_1, 3)

        self.play(
            ReplacementTransform(title_rep, title_case_1),
            *[FadeOut(m) for m in msg],
            *[Write(t) for t in targets]
        )
        
        ax = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            axis_config={"include_numbers": True}
        ).scale(0.5).next_to(texte_msg[-1], 3 * DOWN)

        A_0 = ax.coords_to_point(0,0)
        dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)
        
        A_1 = ax.coords_to_point(0,2)
        dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)
        
        A_0A_1 = Line(A_0, A_1, color=GREEN)
        
        A_2 = ax.coords_to_point(2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
        
        A_0A_2 = Line(A_0, A_2, color=GREEN)
        
        A_1A_2 = Line(A_1, A_2, color=GREEN)
        label_A_1A_2 = MathTex(r"y = -x + 2", color=GREEN)

        polygon_list = [A_0, A_1, A_2]
        Adots = [dotA_0, dotA_1, dotA_2]
        Alines = [A_0A_1, A_0A_2, A_1A_2]
        A_0A_1A_2 = Polygon(
            *polygon_list,
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        self.play(
            Create(ax, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(Aline) for Aline in Alines],
            Write(label_A_1A_2.next_to(A_0A_1, 0.5 * UP)),
            FadeIn(A_0A_1A_2)
        )
        self.wait(1)

        everything = [ax] + Adots + Alines
        everything += [label_A_1A_2, A_0A_1A_2] + targets
        self.play(
            *[FadeOut(e) for e in everything]
        )

        # Case 2
        case_2 = "\((x, y)\in [-2 ; 0] \\times [0 ; 2]\)"
        title_case_2 = Title(case_2)

        texte = [r"Si \(x\leqslant 0\) alors \(\lvert x \rvert = -x\)."]
        texte += [r"Si \(y\geqslant 0\) alors \(\lvert y \rvert = y\)."]
        center = r"\[\lvert x\rvert + "
        center += r"\lvert y\rvert\leqslant 2"
        center += r"\Rightarrow y\leqslant 2 + x\]"
        texte += [center]
        
        texte_msg = [Tex(t) for t in texte]
        targets = targets_to_write(texte_msg, title_case_2, 3)

        self.play(
            ReplacementTransform(title_case_1, title_case_2),
            *[Write(t) for t in targets]
        )
        
        ax = Axes(
            x_range=[-2, 0],
            y_range=[0, 2],
            axis_config={"include_numbers": True}
        ).scale(0.5).next_to(texte_msg[-1], 3 * DOWN)

        A_0 = ax.coords_to_point(0,0)
        dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)
        
        A_1 = ax.coords_to_point(0,2)
        dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)
        
        A_0A_1 = Line(A_0, A_1, color=GREEN)
        
        A_2 = ax.coords_to_point(-2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
        
        A_0A_2 = Line(A_0, A_2, color=GREEN)
        
        A_1A_2 = Line(A_1, A_2, color=GREEN)
        label_A_1A_2 = MathTex(r"y = x + 2", color=GREEN)

        polygon_list = [A_0, A_1, A_2]
        Adots = [dotA_0, dotA_1, dotA_2]
        Alines = [A_0A_1, A_0A_2, A_1A_2]
        A_0A_1A_2 = Polygon(
            *polygon_list,
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        self.play(
            Create(ax, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(Aline) for Aline in Alines],
            Write(label_A_1A_2.next_to(A_0A_1, 0.5 * UP)),
            FadeIn(A_0A_1A_2)
        )
        self.wait(1)

        
        everything = [ax] + Adots + Alines
        everything += [label_A_1A_2, A_0A_1A_2] + targets
        self.play(
            *[FadeOut(e) for e in everything]
        )
        
        # Case 3
        case_3 = "\((x, y)\in [-2 ; 0]^2\)"
        title_case_3 = Title(case_3)

        texte = [r"Si \(x\leqslant 0\) alors \(\lvert x \rvert = -x\)."]
        texte += [r"Si \(y\leqslant 0\) alors \(\lvert y \rvert = -y\)."]
        center = r"\[\lvert x\rvert + "
        center += r"\lvert y\rvert\leqslant 2"
        center += r"\Rightarrow y\geqslant -x - 2\]"
        texte += [center]
        
        texte_msg = [Tex(t) for t in texte]
        targets = targets_to_write(texte_msg, title_case_3, 3)

        self.play(
            ReplacementTransform(title_case_2, title_case_3),
            *[Write(t) for t in targets]
        )
        
        ax = Axes(
            x_range=[-2, 0],
            y_range=[-2, 0],
            axis_config={"include_numbers": True}
        ).scale(0.5).next_to(texte_msg[-1], 3 * DOWN)

        A_0 = ax.coords_to_point(0,0)
        dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)
        
        A_1 = ax.coords_to_point(0,-2)
        dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)
        
        A_0A_1 = Line(A_0, A_1, color=GREEN)
        
        A_2 = ax.coords_to_point(-2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
        
        A_0A_2 = Line(A_0, A_2, color=GREEN)
        
        A_1A_2 = Line(A_1, A_2, color=GREEN)
        label_A_1A_2 = MathTex(r"y = -x - 2", color=GREEN)

        polygon_list = [A_0, A_1, A_2]
        Adots = [dotA_0, dotA_1, dotA_2]
        Alines = [A_0A_1, A_0A_2, A_1A_2]
        A_0A_1A_2 = Polygon(
            *polygon_list,
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        self.play(
            Create(ax, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(Aline) for Aline in Alines],
            Write(label_A_1A_2.next_to(A_0A_1, 0.5 * UP)),
            FadeIn(A_0A_1A_2)
        )
        self.wait(1)

        everything = [ax] + Adots + Alines
        everything += [label_A_1A_2, A_0A_1A_2] + targets
        self.play(
            *[FadeOut(e) for e in everything]
        )
        
        # Case 4
        case_4 = "\((x, y)\in [0 ; 2] \\times [-2 ; 0]\)"
        title_case_4 = Title(case_4)

        texte = [r"Si \(x\geqslant 0\) alors \(\lvert x \rvert = x\)."]
        texte += [r"Si \(y\leqslant 0\) alors \(\lvert y \rvert = -y\)."]
        center = r"\[\lvert x\rvert + "
        center += r"\lvert y\rvert\leqslant 2"
        center += r"\Rightarrow y\geqslant x - 2\]"
        texte += [center]
        
        texte_msg = [Tex(t) for t in texte]
        targets = targets_to_write(texte_msg, title_case_4, 3)

        self.play(
            ReplacementTransform(title_case_3, title_case_4),
            *[Write(t) for t in targets]
        )
        
        ax = Axes(
            x_range=[0, 2],
            y_range=[-2, 0],
            axis_config={"include_numbers": True}
        ).scale(0.5).next_to(texte_msg[-1], 3 * DOWN)

        A_0 = ax.coords_to_point(0,0)
        dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)
        
        A_1 = ax.coords_to_point(0,-2)
        dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)
        
        A_0A_1 = Line(A_0, A_1, color=GREEN)
        
        A_2 = ax.coords_to_point(2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
        
        A_0A_2 = Line(A_0, A_2, color=GREEN)
        
        A_1A_2 = Line(A_1, A_2, color=GREEN)
        label_A_1A_2 = MathTex(r"y = x - 2", color=GREEN)

        polygon_list = [A_0, A_1, A_2]
        Adots = [dotA_0, dotA_1, dotA_2]
        Alines = [A_0A_1, A_0A_2, A_1A_2]
        A_0A_1A_2 = Polygon(
            *polygon_list,
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        self.play(
            Create(ax, run_time=2),
            *[Write(d) for d in Adots],   
            *[Create(Aline) for Aline in Alines],
            Write(label_A_1A_2.next_to(A_0A_1, 0.5 * UP)),
            FadeIn(A_0A_1A_2)
        )
        self.wait(1)
        
        everything = [ax] + Adots + Alines
        everything += [label_A_1A_2, A_0A_1A_2] + targets
        self.play(
            *[FadeOut(e) for e in everything]
        )

        final_case = "Dessinons l'ensemble E en entier"
        title_final_case = Title(final_case)
        self.play(
            ReplacementTransform(title_case_4, title_final_case)
        )
        
        ax = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 2.5],
            x_length=10,
            y_length=10,
            axis_config={"include_numbers": True}
        ).scale(0.75).next_to(texte_msg[-1], 3 * DOWN)

        A = ax.coords_to_point(0,0)
        dotA = Dot(A, fill_opacity=1, color=GREEN)

        # Case 1
        A_0 = ax.coords_to_point(2,0)
        dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)

        AA_0 = Line(A, A_0, color=GREEN)
        
        A_1 = ax.coords_to_point(0,2)
        dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)

        A_0A_1 = Line(A_0, A_1, color=GREEN)
        A_1A = Line(A_1, A, color=GREEN)

        AA_0A_1 = Polygon(
            *[A, A_0, A_1],
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )

        # Case 2
        A_2 = ax.coords_to_point(-2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
        
        A_1A_2 = Line(A_1, A_2, color=GREEN)
        A_2A = Line(A_2, A, color=GREEN)

        A_2 = ax.coords_to_point(-2,0)
        dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)

        A_1A_2A = Polygon(
            *[A_1, A_2, A],
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )

        # Case 3
        A_3 = ax.coords_to_point(0,-2)
        dotA_3 = Dot(A_3, fill_opacity=1, color=GREEN)
        A_2A_3 = Line(A_2, A_3, color=GREEN)
        A_3A = Line(A_3, A, color=GREEN)

        A_2A_3A = Polygon(
            *[A_2, A_3, A],
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        # Case 4
        A_3A_0 = Line(A_3, A_0, color=GREEN)
        A_3A_0A = Polygon(
            *[A_3, A_0, A],
            fill_opacity=1,
            color=GREEN,
            stroke_color=GREEN
        )
        
        Adots = [dotA, dotA_0, dotA_1, dotA_2, dotA_3]
        Alines = [
            AA_0, A_0A_1, A_1A,
            A_1A_2, A_2A, A_1A,
            A_2A_3, A_3A, A_2A,
            A_3A_0, AA_0, A_3A
        ]
        Apolygons = [AA_0A_1, A_1A_2A, A_2A_3A, A_3A_0A]

        self.play(
            Create(ax, run_time=0.5),
            *[Write(d) for d in [dotA, dotA_0, dotA_1]]
        )
        for i in range(4):
            self.play(
                *[Write(Adots[j]) for j in range(i, i + 1) if i > 2],
                *[Create(Alines[j]) for j in range(i, i + 3)],
                FadeIn(Apolygons[i])
            )
        self.wait(1)

        everything = [ax] + Adots + Alines + Apolygons
        

        norme = [r"Topologiquement on peut définir"]
        norme += [r"une norme appelée norme 1 telle que "]
        center = r"\[\lvert\lvert (x ; y)\rvert\rvert_{1} = "
        center += r"\lvert x \rvert + \lvert y \rvert\]"
        norme += [center]
        norm_msg = [Tex(n) for n in norme]
        norm_targets = targets_to_write(norm_msg, title_final_case, 3)

        self.play(
            *[Write(nt) for nt in norm_targets]
        )
        self.wait(1)

        boule = [r"Topologiquement on peut définir"]
        boule += [r"une boule fermée avec la norme 1 "]
        center = r"\[B_f\left((0;0) ; r\right) = "
        center += r"\left\{(x ; y)\in \mathbb{R}^2 ; "
        center += r"\lvert\lvert (x ; y)\rvert\rvert_{1} "
        center += r"\leqslant r\right\}\]"
        boule += [center]
        boule_msg = [Tex(b) for b in boule]
        boule_msg[-1] = boule_msg[-1].scale(0.85)
        boule_targets = targets_to_write(boule_msg, ax, 3)

        self.play(
            *[Write(boule_targets[i]) for i in range(2)],
        )

        replace_and_write(
            self,
            norm_msg,
            boule_msg[2:],
            title_final_case,
            2
        )

        self.play(
            *[e.animate.shift(3 * UP) for e in everything]
        )

        conclusion = [r"\[E = B_f\left((0 ; 0) ; 2\right)\]"]
        conclusion += [r"L'ensemble \(E\) est la boule "]
        conclusion += [r"centrée en l'origine, de rayon 2 "]
        conclusion += [r"définie selon la norme 1."]
        conclusion += [r"Que se passe-t-il si on change "]
        conclusion += [r"la norme utilisée ?"]
        conclusion_msg = [
            Tex(
                c,
                color=GREEN
            ).scale(0.85) for c in conclusion
        ]
        conc_targets = targets_to_write(conclusion_msg, ax, 3)

        replace_and_write(
            self,
            boule_msg[0:2],
            conclusion_msg,
            ax,
            0.5
        )
        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_final_case,
                title_end.scale(0.75)
            ),
        )
        self.wait(1.5)
        
        disp_sub(self, lang='fr')
