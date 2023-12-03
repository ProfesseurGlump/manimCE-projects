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


def bernoulli_def():
    phrase = [r"En théorie des probabilités, "]
    phrase += [r"la loi de Bernoulli, du nom du "]
    phrase += [r"mathématicien suisse Jacques Bernoulli, "]
    phrase += [r"désigne la loi de probabilité d'une "]
    phrase += [r"variable aléatoire discrète qui prend "]
    phrase += [r"la valeur 1 avec la probabilité \(p\) et"]
    phrase += [r" 0 avec probabilité \(q = 1 - p\)."]
    phrase += [r"\[\mathbb{P}(X = x) = p^x(1 - p)^{1 - x}, x\in\{0, 1\}\]"]
    phrase_tex = [Tex(p).scale(0.85) for p in phrase]
    return phrase_tex


def bernoulli_density(ax_ref, ax_pos, p=0.5):
    q = 1 - p
    ax = Axes(
        x_range=[-1, 2],
        y_range=[0, 1.25],
        axis_config={"include_numbers": True}
    ).scale(0.65).next_to(ax_ref, ax_pos)
    
    A_0 = ax.coords_to_point(0,0)
    dotA_0 = Dot(A_0, fill_opacity=1, color=GREEN)

    A_1 = ax.coords_to_point(0,q)
    dotA_1 = Dot(A_1, fill_opacity=1, color=GREEN)
    A_1_lab = Tex(f"q = {round(q, 2)}", color=GREEN).next_to(A_1, UR)
    vert_A_1 = ax.get_vertical_line(
        A_1,
        line_config={"dashed_ratio": 0.85},
        color=GREEN
    )
    

    A_2 = ax.coords_to_point(1,0)
    dotA_2 = Dot(A_2, fill_opacity=1, color=GREEN)
    
    A_3 = ax.coords_to_point(1,p)
    dotA_3 = Dot(A_3, fill_opacity=1, color=GREEN)
    A_3_lab = Tex(f"p = {round(p, 2)}", color=GREEN).next_to(A_3, UR)
    vert_A_3 = ax.get_vertical_line(
        A_3,
        line_config={"dashed_ratio": 0.85},
        color=GREEN
    )

    f = f"f(x) = {round(p, 2)}" + r"^x" + f"{round(q, 2)}" + r"^{1-x}"
    f_lab = MathTex(f, color=GREEN).next_to(ax, 0.15 * DOWN)
    dots = [dotA_0, dotA_1, dotA_2, dotA_3]
    lines = [vert_A_1, vert_A_3]
    Alabels = [A_1_lab, A_3_lab, f_lab]
    
    return ax, dots, lines, Alabels

    
    

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



class Bernoulli(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Loi Bernoulli avec "
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
        phrase = "Savez-vous comment représenter | "
        phrase += "la fonction de densité de la | "
        phrase += "de Bernoulli ?  |"
        phrase += "On l'appelle aussi fonction de masse |"
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

        def_msg = bernoulli_def()
        n = len(def_msg)
        targets = targets_to_write(def_msg, title_rep, 3)
        # self.play(
        #     Write(def_msg[0].next_to(title_rep, 3 * DOWN))
        # )
        # self.wait()
        # self.play(
        #     *[
        #         Write(
        #             def_msg[i].next_to(
        #                 def_msg[i-1],
        #                 DOWN
        #             )
        #         ) for i in range(1, n)
        #     ]
        # )
        self.play(*[Write(t) for t in targets])
        self.wait(3)
        box = SurroundingRectangle(def_msg[-1])
        self.play(Write(box))
        self.wait()

        ax_ref, ax_pos = box, DOWN
        p_values = [i/5 for i in range(6)]
        bernoulli_dens_graphs = [
            bernoulli_density(ax_ref, ax_pos, p) for p in p_values
        ]
        for bernoulli_dens_graph in bernoulli_dens_graphs:
            ax = bernoulli_dens_graph[0]
            _, Adots, Alines, Alabels = bernoulli_dens_graph
            self.play(
                Create(ax, run_time=2),
                *[Write(d) for d in Adots],
                *[Create(line) for line in Alines],
                *[Write(Alabel) for Alabel in Alabels],
            )
            self.wait(2)
            everything = [ax] + Adots + Alines + Alabels
            self.play(
                *[FadeOut(t) for t in everything]
            )

        
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(1.5)
        
        disp_sub(self, lang='fr')
