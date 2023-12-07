from manim import *
import manim
from math import e, pi
import math


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


def binomial_dens_def():
    phrase = [r"En théorie des probabilités, "]
    phrase += [r"la loi Binomiale, du nom du "]
    phrase += [r"coefficient binomial intervenant "]
    phrase += [r"dans la formule de son calcul, "]
    phrase += [r"désigne la loi de probabilité d'une "]
    phrase += [r"variable aléatoire discrète qui compte "]
    phrase += [r"le nombre \(k\) de succès dans une "]
    phrase += [r"répétition de \(n\) épreuves de Bernoulli."]
    phrase += [r"\[\mathbb{P}(X = k) = \binom{n}{k}p^k(1 - p)^{n - k}\]"]
    phrase_tex = [Tex(p).scale(0.85) for p in phrase]
    return phrase_tex



def binomial_cmf_def():
    phrase = [r"La loi Binomiale de paramètres \((n, p)\), "]
    phrase += [r"avec \(\mathbb{P}(X = k) = \binom{n}{k}p^k(1 - p)^{n - k}\) "]
    phrase += [r"a pour fonction de répartition "]
    centered = r"\[F(x) = q\mathbb{I}_{[0 ; n[}(x) "
    centered += r"\sum_{k = 0}^{\lfloor x \rfloor}\binom{n}{k}p^k(1 - p)^{n - k} "
    centered += r"+ \mathbb{I}_{[n ; +\infty[}(x)\]"
    phrase += [centered]
    phrase_tex = [Tex(p).scale(0.85) for p in phrase]
    return phrase_tex



def factorial(n):
    if n < 0: return False
    elif n == 0 or n == 1: return 1
    else: return n * factorial(n - 1)

def binom(n, k):
    if n < k: return False
    else: return factorial(n) // ( factorial(k) * factorial(n - k) )

    
def binomial_density(ax_ref, ax_pos,n=2, p=0.5):
    q = 1 - p
    ax = Axes(
        x_range=[0, n+1],
        y_range=[0, 1],
        x_length=16,
        y_length=9,
        axis_config={"include_numbers": True}
    ).scale(0.5).next_to(ax_ref, ax_pos)

    n_lab = MathTex(
        f"(n ; p) \simeq ({n} ; {round(p, 4)})",
        color=RED
    ).next_to(ax_ref, 0.5 * DOWN)
    
    Ax_0 = ax.coords_to_point(0,0)
    dotAx_0 = Dot(Ax_0, fill_opacity=1, color=GREEN)

    bin_dens = [q**n]
    max_bin_dens = q**n
    Ay_0 = ax.coords_to_point(0,q**n)
    dotAy_0 = Dot(Ay_0, fill_opacity=1, color=GREEN)
    y_0_lab = r"q^{" + f"{n}" + r"} \simeq " + f"{round(q**n, 4)}"
    Ay_0_lab = MathTex(
        y_0_lab,
        color=GREEN
    ).scale(0.75).next_to(Ay_0, UL)
    vert_Ay_0 = ax.get_vertical_line(
        Ay_0,
        line_config={"dashed_ratio": 0.85},
        color=GREEN
    )
    
    Acoords = [Ax_0, Ay_0]
    Adots = [dotAx_0, dotAy_0]
    Alabs = [n_lab, Ay_0_lab]
    Alines = [vert_Ay_0]

    for k in range(1, n):
        Ax = ax.coords_to_point(k, 0)
        Acoords += [Ax]
        dotAx = Dot(Ax, fill_opacity=1, color=GREEN)
        Adots += [dotAx]
        
        binom_n_k = binom(n, k)
        p_k = binom_n_k * p**k * q**(n - k)
        bin_dens += [p_k]
        if p_k > max_bin_dens: max_bin_dens = p_k
        Ay = ax.coords_to_point(k, p_k)
        Acoords += [Ay]
        dotAy = Dot(Ay, fill_opacity=1, color=GREEN)
        Adots += [dotAy]
        
        Alab = r"\binom{" + f"{n}" + r"}{" + f"{k}"
        Alab += r"}" + f"{round(p, 2)}^" + r"{" + f"{k}"
        Alab += r"}" + f"{round(q, 2)}^" + r"{" + f"{n - k}" + r"}"
        A_lab = MathTex(
            f"{Alab} \simeq {round(p_k, 2)}",
            color=GREEN
        ).scale(0.75)
        
        vert_Ay = ax.get_vertical_line(
            Ay,
            line_config={"dashed_ratio": 0.85},
            color=GREEN
        )
        Alines += [vert_Ay]

    max_index = bin_dens.index(max_bin_dens)
    Alab = r"\binom{" + f"{n}" + r"}{" + f"{max_index}"
    Alab += r"}" + f"{round(p, 2)}^" + r"{" + f"{max_index}"
    Alab += r"}" + f"{round(q, 2)}^" + r"{" + f"{n - max_index}" + r"}"
    # len(Acoord) = 2 * bin_dens
    A_max_lab = MathTex(
            f"{Alab} \simeq {round(max_bin_dens, 2)}",
            color=GREEN
        ).scale(0.75)
    if (max_bin_dens - bin_dens[max_index - 1]) < 0.2:
        A_max_lab.next_to(Acoords[2 * max_index + 1], 3 * UP)
    else: A_max_lab.next_to(Acoords[2 * max_index + 1], 1.5 * UP)
    Alabs += [A_max_lab]
    
    Ax_n = ax.coords_to_point(n,0)
    Acoords += [Ax_n]
    dotAx_n = Dot(Ax_n, fill_opacity=1, color=GREEN)
    Adots += [dotAx_n]
    
    Ay_n = ax.coords_to_point(n, p**n)
    Acoords += [Ay_n]
    dotAy_n = Dot(Ay_n, fill_opacity=1, color=GREEN)
    Adots += [dotAy_n]

    p_n_txt = r"p^{" + f"{n}" + r"} \simeq " + f"{round(p**n, 4)}"
    Ay_n_lab = MathTex(
        p_n_txt,
        color=GREEN
    ).scale(0.75).next_to(Ay_n, UR)
    Alabs += [Ay_n_lab]
    
    vert_Ay_n = ax.get_vertical_line(
        Ay_n,
        line_config={"dashed_ratio": 0.85},
        color=GREEN
    )
    Alines += [vert_Ay_n]

    f = f"f(x) = " + r"\binom{" + f"{n}" + r"}{" + f"{k}"
    f += r"}" + f"{round(p, 4)}" + r"^{\lfloor x \rfloor}"
    f += f"{round(q, 4)}" + r"^{" + f"{n}"
    f += r"- \lfloor x \rfloor}"
    f_lab = MathTex(
        f,
        color=GREEN
    ).scale(0.85).next_to(ax, 2.5 * DOWN)

    Alabs += [f_lab]
    
    return ax, Adots, Alines, Alabs




def targets_to_write(text, ref, size=1, direction=DOWN):
    n = len(text)
    # Create a list of target objects
    targets = [text[0].next_to(ref, (size + 2) * direction)]
    targets += [
        text[i].next_to(
            text[i - 1],
            size * direction
        ) for i in range(1, n)
    ]
    return text




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




class BinomialDensity(Scene):
    def construct(self):
        msg = "Loi Binomiale avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.75))
        self.wait(2)
        # youtube_long = SVGMobject(
        #     "/Users/dn/Documents/pics/svg/Youtube2017.svg",
        #     fill_opacity=1,
        #     fill_color=RED
        # ).scale(0.25)
        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment représenter | "
        phrase += "la fonction de densité de la | "
        phrase += "loi Binomiale ?  |"
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
        self.wait(1.5)

        title_rep = Title("Regardez jusqu'au bout pour la réponse")
        self.play(
            ReplacementTransform(
                title_clap,
                title_rep.scale(0.75)
            ),
            FadeOut(msg)
        )
        self.wait(1.5)

        def_msg = binomial_dens_def()
        n = len(def_msg)
        
        targets = targets_to_write(def_msg, title_rep)
        self.play(*[Write(t) for t in targets])
        self.wait(3)
        
        box = SurroundingRectangle(def_msg[-1])
        self.play(Write(box))
        self.wait(1)
        self.play(
            *[FadeOut(targets[i]) for i in range(len(targets) - 1)],
            youtube_long.animate.shift(5.75 * LEFT + 0.5 * UP).scale(2),
            *[t.animate.shift(5.25 * UP) for t in [box, targets[-1]]],
        )
        self.wait()

        ax_ref, ax_pos = box, 2 * DOWN
        
        
        for n in range(2, 11):
            p_values = [i/n for i in range(1, n)]
            binomial_dens_graphs = [
                binomial_density(ax_ref, ax_pos, n, p) for p in p_values
            ]
            for binomial_dens_graph in binomial_dens_graphs:
                ax = binomial_dens_graph[0]
                _, Adots, Alines, Alabels = binomial_dens_graph
                self.play(
                    Create(ax, run_time=0.1),
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
        self.wait(2)
        
        disp_sub(self, lang='fr')
        
