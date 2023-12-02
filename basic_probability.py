from manim import *
from manim import XKCD
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


def targets_to_write(text, ref, size=2, direction=DOWN, scale=1):
    n = len(text)
    # Create a list of target objects
    targets = [text[0].next_to(ref, size * direction).scale(scale)]
    targets += [
        text[i].next_to(
            text[i - 1],
            size * direction
        ).scale(scale) for i in range(1, n)
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



class BooleanOperations(Scene):
    def construct(self):
        msg = "Opérations ensemblistes avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.75))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))
        
        ellipse1 = Ellipse(
            width=5, height=7,
            fill_opacity=0.5,
            color=PURE_BLUE,
            stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=DARK_BROWN).move_to(RIGHT)
    
        ellipse_group = Group(
            ellipse1,
            ellipse2
        ).move_to(UP * 2.75)
        self.play(FadeIn(ellipse_group))

        i = Intersection(
            ellipse1,
            ellipse2,
            color=GREEN,
            fill_opacity=0.5
        )
        self.play(
            i.animate.scale(0.25).move_to(
                3 * DL
            )
        )
        intersection_text = Text(
            "Intersection",
            font_size=30,
            color=GREEN
        ).next_to(
                i,
                0.75 * UP
            )
        i_formula_1 = r"A\cap B = \{x\in A "
        i_formula_1 += r"\mbox{ et } x\in B\}"
        i_math_1 = MathTex(
            i_formula_1,
            color=GREEN
        ).next_to(
            i,
            0.75 * DOWN
        ).scale(0.5)
        self.play(
            FadeIn(intersection_text),
            Write(i_math_1)
        )

        u = Union(
            ellipse1,
            ellipse2,
            color=RED,
            fill_opacity=0.5
        )
        union_text = Text(
            "Union",
            font_size=30,
            color=RED
        )
        self.play(
            u.animate.scale(0.25).next_to(
                i,
                10 * RIGHT,
                buff=union_text.height * 1.5
            )
        )
        union_text.next_to(
            u,
            UP * 0.75
        )
        u_formula_1 = r"A\cup B = \{x\in A "
        u_formula_1 += r"\mbox{ ou } x\in B\}"
        u_math_1 = MathTex(
            u_formula_1,
            color=RED
        ).next_to(
            u,
            0.75 * DOWN
        ).scale(0.5)
        self.play(
            FadeIn(union_text),
            Write(u_math_1)
        )

        e = Exclusion(
            ellipse1,
            ellipse2,
            color=YELLOW,
            fill_opacity=0.5
        )
        exclusion_text = Text(
            "Exclusion",
            font_size=30,
            color=YELLOW
        )
        self.play(
            e.animate.scale(0.25).next_to(
                u,
                3 * DOWN,
                buff=exclusion_text.height * 1.75
            )
        )
        exclusion_text.next_to(
            e,
            UP * 0.75,
        )
        e_formula_1 = r"(A\cup B)\setminus(A\cap B)"
        e_formula_1 += r" = (A\cap \overline{B})\cup "
        e_formula_1 += r"(\overline{A}\cap B)"
        e_math_1 = MathTex(
            e_formula_1,
            color=YELLOW
        ).next_to(
            e,
            0.75 * DOWN 
        ).scale(0.425)
        self.play(
            FadeIn(exclusion_text),
            Write(e_math_1)
        )

        d = Difference(
            ellipse1,
            ellipse2,
            color=ORANGE,
            fill_opacity=0.5
        )
        difference_text = Text(
            "Différence",
            font_size=30,
            color=ORANGE
        )
        self.play(
            d.animate.scale(0.25).next_to(
                i,
                3 * DOWN,
                buff=difference_text.height * 1.75
            )
        )
        difference_text.next_to(
            d,
            UP * 0.75
        )
        d_formula_1 = r"A\setminus B = "
        d_formula_1 += r"A\cap \overline{B}"
        d_math_1 = MathTex(
            d_formula_1,
            color=ORANGE
        ).next_to(
            d,
            0.75 * DOWN 
        ).scale(0.5)
        self.play(
            FadeIn(difference_text),
            Write(d_math_1)
        )

        i_formula_2 = r"P(A\cap B) = P(A) +  "
        i_formula_2 += r"P(B) - P(A\cup B)"
        i_math_2 = MathTex(
            i_formula_2,
            color=GREEN
        ).next_to(
            ellipse_group,
            8 * DOWN
        ).scale(0.425)
        self.play(Write(i_math_2))
        self.wait()

        u_formula_2 = r"P(A\cup B) = P(A) +  "
        u_formula_2 += r"P(B) - P(A\cap B)"
        u_math_2 = MathTex(
            u_formula_2,
            color=RED
        ).next_to(
            i_math_2,
            DOWN
        ).scale(0.425)
        self.play(Write(u_math_2))
        self.wait()

        e_formula_2 = r"P\left((A\cup B)\setminus(A\cap B)\right) "
        e_formula_2 += r" = P(A\cap \overline{B}) +  "
        e_formula_2 += r"P(\overline{A}\cap B)"
        e_math_2 = MathTex(
            e_formula_2,
            color=YELLOW
        ).next_to(
            u_math_2,
            # 0.75 * DOWN
            9 * DOWN
        ).scale(0.425)
        self.play(
            # ReplacementTransform(e_math_1, e_math_2)
            Write(e_math_2)
        )
        self.wait()
        
        d_formula_2 = r"P(A\setminus B) = "
        d_formula_2 += r"P(A\cap\overline{B})"
        d_math_2 = MathTex(
            d_formula_2,
            color=ORANGE
        ).next_to(
            e_math_2,
            DOWN
        ).scale(0.425)
        self.play(Write(d_math_2))
        self.wait()

        refs = [
            (i, i_math_1, i_math_2),
            (u, u_math_1, u_math_2),
            (e, e_math_1, e_math_2),
            (d, d_math_1, d_math_2)
        ]
        n = len(refs)
        targets = [
            refs[i][2].next_to(
                refs[i][0],
                0.75 * DOWN
            ).scale(0.825) for i in range(n)
        ]
        self.play(
            *[
                ReplacementTransform(
                    refs[i][1],
                    targets[i]
                ) for i in range(n)
            ]
        )
        self.wait()

        texts = [
            intersection_text,
            union_text,
            exclusion_text,
            difference_text
        ]
        everything = [refs[i][0] for i in range(n)]
        everything += [refs[i][1] for i in range(n)]
        everything += [refs[i][2] for i in range(n)]
        everything += [text for text in texts]
        everything += [ellipse_group]
        self.play(
            *[FadeOut(e) for e in everything]
        )
        self.wait()

        left_side = [
            r"\[A \cap A = A\quad ",
            r"\[A \cap B = B \cap A\quad ",
            r"\[A \cap (B \cap C) = (A \cap B) \cap C\quad ",
            r"\[A \cap \emptyset = \emptyset\quad ",
            r"\[A \cap \Omega = A\quad ",
            r"\[A \cap \overline{A} = \emptyset\quad ",
            r"\[B \subset A \Rightarrow A \cap B = B\quad ",
            r"\[A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\quad ",
            r"\[\overline{A \cap B} = \overline{A} \cup \overline{B}\quad ",
        ]

        right_side = [
            r"A \cup A = A\]",
            r"A \cup B = B \cup A\]",
            r"A \cup (B \cup C) = (A \cup B) \cup C\]",
            r"A \cup \emptyset = A\]",
            r"A \cup \Omega = \Omega\]",
            r"A \cup \overline{A} = \Omega\]",
            r"B \subset A \Rightarrow A \cup B = A\]",
            r"A \cup (B \cap C) = (A \cup B) \cap (A \cup C)\]",
            r"\overline{A \cup B} = \overline{A} \cap \overline{B}\]",
        ]

        mt = [Tex(lt + rt) for lt, rt in zip(left_side, right_side)]
        targets = targets_to_write(
            mt,
            title_start,
            size=3.5,
            direction=DOWN,
            scale=0.75
        )
        n = len(targets)
        
        for i in range(n):
            if i == 2:
                targets[i] = targets[i].scale(0.85)
            elif i == 7:
                targets[i] = targets[i].scale(0.75)
                
        self.play(*[Write(t) for t in targets])
        self.wait()


        self.play(*[FadeOut(t) for t in targets])
        self.wait()

        # Create rectangle representing probability fundamental space
        omega = Rectangle(
            width=8, height=6,
            color=XKCD.APRICOT,
            fill_opacity=0.25
        )
        
        set_A = Circle(
            radius=1,
            color=BLUE,
            fill_opacity=0.5
        ).move_to(LEFT)
        
        set_B = Circle(
            radius=1,
            color=WHITE,
            fill_opacity=0.5
        ).move_to(UP)
        
        set_C = Circle(
            radius=1,
            color=RED,
            fill_opacity=0.5
        ).move_to(RIGHT)

        initial_sets = [omega, set_A, set_B, set_C]
        
        # Create Intersections
        intersection_AB = Intersection(set_A, set_B, color=PURPLE)
        intersection_BC = Intersection(set_B, set_C, color=ORANGE)
        intersection_CA = Intersection(set_C, set_A, color=YELLOW)
        intersection_ABC = Intersection(set_A, set_B, set_C, color=GREEN)

        intersections = [
            intersection_AB,
            intersection_BC,
            intersection_CA,
            intersection_ABC
        ]

        # Create Unions
        union_AB = Union(set_A, set_B, color=PURPLE)
        union_BC = Union(set_B, set_C, color=ORANGE)
        union_CA = Union(set_C, set_A, color=YELLOW)
        union_ABC = Union(set_A, set_B, set_C, color=GREEN)

        unions = [
            union_AB,
            union_BC,
            union_CA,
            union_ABC
        ]

        # Mix inter-unions
        intersection_A_BC = Intersection(
            set_A,
            intersection_BC,
            color=XKCD.MANGO
        )
        union_AB_CA = Union(
            intersection_AB,
            intersection_CA,
            color=XKCD.ADOBE
        )
        union_A_BC = Union(
            set_A,
            intersection_BC,
            color=XKCD.ALGAE
        )
        intersection_AB_CA = Intersection(
            union_AB,
            union_CA,
            color=XKCD.ACIDGREEN
        )

        mix_inter_unions = [
            intersection_AB_CA,
            intersection_A_BC,
            union_AB_CA,
            union_A_BC
        ]
        
        # Create complements
        complement_A = Difference(omega, set_A, color=BLUE)
        complement_B = Difference(omega, set_B, color=WHITE)
        complement_C = Difference(omega, set_C, color=RED)
        complement_AB = Difference(omega, intersection_AB, color=PURPLE)
        complement_BC = Difference(omega, intersection_BC, color=ORANGE)
        complement_CA = Difference(omega, intersection_CA, color=YELLOW)
        complement_ABC = Difference(omega, intersection_ABC, color=GREEN)

        complements = [
            complement_A,
            complement_B,
            complement_C,
            complement_AB,
            complement_BC,
            complement_CA,
            complement_ABC
        ]
        
        # De Morgan's Laws
        # (1) (AnB)bar = Abar U Bbar
        # (2) (A U B)bar = Abar n Bbar
        union_Abar_Bbar = Union(
            complement_A,
            complement_B,
            color=XKCD.AMBER
        )
        inter_Abar_Bbar = Intersection(
            complement_A,
            complement_B,
            color=XKCD.AQUA
        )

        de_morgans = [union_Abar_Bbar]
        
        
        venn_diagram = VGroup(
            *initial_sets,
            *intersections,
            *unions,
            *mix_inter_unions,
            *complements,
            *de_morgans
        )

        label_Omega = MathTex(
            "\Omega",
            color=XKCD.APRICOT
        ).next_to(set_C, 4 * DR)
        label_A = Text("A", font_size=36, color=BLUE).next_to(set_A, LEFT)
        label_B = Text("B", font_size=36, color=WHITE).next_to(set_B, UP)
        label_C = Text("C", font_size=36, color=RED).next_to(set_C, RIGHT)

        labels = [label_Omega, label_A, label_B, label_C]
        self.play(Create(venn_diagram))
        self.play(*[Write(lab) for lab in labels])
        self.wait()
