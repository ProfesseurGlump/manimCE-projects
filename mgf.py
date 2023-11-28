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
                new[0].scale(lines_and_scales['0']).next_to(pos_ref, 3 * DOWN)
                ) for i in range(1) if '0' in lines_and_scales.keys()
              ],
            *[
                ReplacementTransform(
                old[0],
                new[0].next_to(pos_ref, 3 * DOWN)
                ) for i in range(1) if '0' not in lines_and_scales.keys()
              ],
            *[
                ReplacementTransform(
                    old[i],
                    new[i].scale(lines_and_scales[str(i)]).next_to(new[i - 1], DOWN)
                ) for i in range(1, min_mn) if str(i) in lines_and_scales.keys()
            ],
            *[
                ReplacementTransform(
                    old[i],
                    new[i].next_to(new[i-1], DOWN)
                ) for i in range(1, min_mn) if str(i) not in lines_and_scales.keys()
            ],
        )
        if to_be_continued:
            self.play(
                *[
                    Write(
                        new[i].scale(lines_and_scales[str(i)]).next_to(new[i - 1], DOWN)
                    ) for i in range(min_mn, n) if str(i) in lines_and_scales.keys()
                ],
                *[
                    Write(
                        new[i].next_to(new[i - 1], DOWN)
                    ) for i in range(min_mn, n) if not str(i) in lines_and_scales.keys()
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
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi de Bernoulli ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        definition = [r"Rappel : "]
        definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
        definition += [r"un espace probabilisé et"]
        centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
        centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
        definition += [centered_expr]
        definition += [r"une variable aléatoire discrète. Alors, "]
        definition += [r"\[M_X : t\mapsto \mathbb{E}(e^{tX}) = G_X(e^t)\]"]
        definition += [r"\[M_X(t) = \sum_{n = 0}^{+\infty}\mathbb{P}_X(\{n\})e^{tn}\]"]
        definition += [r"est définie et continue sur \(\mathbb{R}\)."]
        
        def_msg = [Tex(d) for d in definition]
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
        self.wait(5)

        bernoulli_prob = [r"Si \(X\) suit une loi de Bernoulli "]
        bernoulli_prob += [r"de paramètre \(p\) alors "]
        centered_expr = r"\[\mathbb{P}_X(\{0\}) = "
        centered_expr += r"\mathbb{P}(\{X = 0\}) = 1 - p\]"
        bernoulli_prob += [centered_expr]
        bernoulli_prob += [r"et"]
        centered_expr = r"\[\mathbb{P}_X(\{1\}) = "
        centered_expr += r"\mathbb{P}(\{X = 1\}) = p\]"
        bernoulli_prob += [centered_expr]
        ber_msg = [Tex(b) for b in bernoulli_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=ber_msg,
            pos_ref=title_rep,
            duration=5,
        )

        bernoulli_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \mathbb{P}_X(\{0\})\times e^{t\times 0}"
        centered_expr += r"+ \mathbb{P}_X(\{1\})\times e^t\]"
        bernoulli_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \mathbb{P}(\{X = 0\})"
        centered_expr += r"+ \mathbb{P}(\{X = 1\})\times e^t\]"
        bernoulli_mgf += [centered_expr]
        ber_mgf_msg = [Tex(b) for b in bernoulli_mgf]
        
        ber_mgf_end = MathTex(r"M_X(t) = (1 - p) + pe^t")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=ber_msg,
            new=ber_mgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(ber_mgf_end.next_to(ber_mgf_msg[-1], 7 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi de Bernoulli"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=ber_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(ber_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')

class Geometric(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi géométrique ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        definition = [r"Rappel : "]
        definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
        definition += [r"un espace probabilisé et"]
        centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
        centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
        definition += [centered_expr]
        definition += [r"une variable aléatoire discrète. Alors, "]
        definition += [r"\[M_X : t\mapsto \mathbb{E}(e^{tX}) = G_X(e^t)\]"]
        definition += [r"\[M_X(t) = \sum_{k = 0}^{+\infty}\mathbb{P}_X(\{k\})e^{tk}\]"]
        definition += [r"est définie et continue sur \(\mathbb{R}\) "]
        
        def_msg = [Tex(d) for d in definition]
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
        self.wait(5)

        geometric_prob = [r"Si \(X\) suit une loi géométrique "]
        geometric_prob += [r"de paramètre \(p\) alors "]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\mathbb{P}(\{X = k\}) = p(1 - p)^{k - 1}\]"
        geometric_prob += [centered_expr]
        geom_msg = [Tex(b) for b in geometric_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=geom_msg,
            pos_ref=title_rep,
            duration=5,
        )

        geometric_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"\mathbb{P}_X(\{k\})\times e^{tk}\]"
        geometric_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"\mathbb{P}(\{X = k\})\times e^{tk}\]"
        geometric_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"p(1 - p)^{k - 1}e^{tk}\]"
        geometric_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = pe^t\sum_{k = 1}^{+\infty}"
        centered_expr += r"(1 - p)^{k - 1}e^{t(k - 1)}\]"
        geometric_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = pe^t\sum_{k = 0}^{+\infty}"
        centered_expr += r"\left[e^t(1 - p)\right]^{k}\]"
        geometric_mgf += [centered_expr]
        geom_mgf_msg = [Tex(b) for b in geometric_mgf]

        geom_mgf_end = MathTex(r"M_X(t) = \dfrac{pe^t}{1 - (1 - p)e^t}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=geom_msg,
            new=geom_mgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(geom_mgf_end.next_to(geom_mgf_msg[-1], 7 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi géométrique"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=geom_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(geom_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')


class Binomial(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi binomiale ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        definition = [r"Rappel : "]
        definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
        definition += [r"un espace probabilisé et"]
        centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
        centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
        definition += [centered_expr]
        definition += [r"une variable aléatoire discrète. Alors, "]
        centered_expr = r"\[G_X : s\mapsto \mathbb{E}(e^{tX}) = "
        centered_expr += r"\sum_{k = 0}^{+\infty}\mathbb{P}_X(\{k\})e^{tk}\]"
        definition += [centered_expr]
        definition += [r"est définie et continue sur \(\mathbb{R}\) "]
        
        def_msg = [Tex(d) for d in definition]
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
        self.wait(5)

        binomial_prob = [r"Si \(X\) suit une loi binomiale "]
        binomial_prob += [r"de paramètre \(n\) et \(p\) alors "]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\mathbb{P}(\{X = k\})\]"
        binomial_prob += [centered_expr]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\binom{n}{k}p^k(1 - p)^{n - k}\]"
        binomial_prob += [centered_expr]
        bin_msg = [Tex(b) for b in binomial_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=bin_msg,
            pos_ref=title_rep,
            duration=5,
        )

        binomial_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}_X(\{k\})\times e^{tk}\]"
        binomial_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}(\{X = k\})\times e^{tk}\]"
        binomial_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\binom{n}{k}p^k(1 - p)^{n - k}e^{tk}\]"
        binomial_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\binom{n}{k}(pe^t)^k(1 - p)^{n - k}\]"
        binomial_mgf += [centered_expr]
        bin_mgf_msg = [Tex(b) for b in binomial_mgf]
        
        bin_mgf_end = MathTex(r"M_X(t) = \left[(1 - p) + pe^t\right]^n")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=bin_msg,
            new=bin_mgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(bin_mgf_end.next_to(bin_mgf_msg[-1], 7 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi binomiale"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=bin_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(bin_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')
        

class Poisson(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi de Poisson ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        definition = [r"Rappel : "]
        definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
        definition += [r"un espace probabilisé et"]
        centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
        centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
        definition += [centered_expr]
        definition += [r"une variable aléatoire discrète. Alors, "]
        centered_expr = r"\[G_X : s\mapsto \mathbb{E}(e^{tX}) = "
        centered_expr += r"\sum_{k = 0}^{+\infty}\mathbb{P}_X(\{k\})e^{tk}\]"
        definition += [centered_expr]
        definition += [r"est définie et continue sur \(\mathbb{R}\) "]
        
        def_msg = [Tex(d) for d in definition]
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
        self.wait(5)

        poisson_prob = [r"Si \(X\) suit une loi de Poisson "]
        poisson_prob += [r"de paramètre \(\lambda\) alors "]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\mathbb{P}(\{X = k\}) = "
        centered_expr += r"e^{-\lambda}\dfrac{\lambda^k}{k!}\]"
        poisson_prob += [centered_expr]
        pois_msg = [Tex(b) for b in poisson_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=pois_msg,
            pos_ref=title_rep,
            duration=5,
        )

        poisson_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"\mathbb{P}_X(\{k\})\times e^{tk}\]"
        poisson_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"\mathbb{P}(\{X = k\})\times e^{tk}\]"
        poisson_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"e^{-\lambda}\dfrac{\lambda^k}{k!}e^{tk}\]"
        poisson_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = e^{-\lambda}\sum_{k = 0}^{+\infty}"
        centered_expr += r"\dfrac{(\lambda s)^k}{k!}\]"
        poisson_mgf += [centered_expr]
        poisson_mgf += [r"\[M_X(t) = e^{-\lambda}e^{\lambda s}\]"]
        pois_mgf_msg = [Tex(b) for b in poisson_mgf]

        pois_mgf_end = MathTex(r"M_X(t) = e^{\lambda(s - 1)}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=pois_msg,
            new=pois_mgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(pois_mgf_end.next_to(pois_mgf_msg[-1], 7 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi de Poisson"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=pois_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(pois_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')
        

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
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi uniforme ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        definition = [r"Rappel : "]
        definition += [r"Soit \((\Omega, \mathcal{T}, \mathbb{P})\) "]
        definition += [r"un espace probabilisé et"]
        centered_expr = r"\[X : (\Omega, \mathcal{T})\to "
        centered_expr += r"(\mathbb{N}, \mathcal{P}(\mathbb{N}))\]"
        definition += [centered_expr]
        definition += [r"une variable aléatoire discrète. Alors, "]
        centered_expr = r"\[G_X : s\mapsto \mathbb{E}(e^{tX}) = "
        centered_expr += r"\sum_{k = 0}^{+\infty}\mathbb{P}_X(\{k\})e^{tk}\]"
        definition += [centered_expr]
        definition += [r"est définie et continue sur \(\mathbb{R}\) "]
        
        def_msg = [Tex(d) for d in definition]
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
        self.wait(5)

        uniform_prob = [r"Si \(X\) suit une loi uniforme "]
        uniform_prob += [r"de paramètre \(n\) alors "]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\mathbb{P}(\{X = k\})\]"
        uniform_prob += [centered_expr]
        centered_expr = r"\[\mathbb{P}_X(\{k\}) = "
        centered_expr += r"\dfrac{1}{n}\]"
        uniform_prob += [centered_expr]
        unif_msg = [Tex(b) for b in uniform_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=unif_msg,
            pos_ref=title_rep,
            duration=5,
        )

        uniform_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}_X(\{k\})\times e^{tk}\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}(\{X = k\})\times e^{tk}\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \sum_{k = 0}^n"
        centered_expr += r"\dfrac{1}{n}e^{tk}\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \dfrac{1}{n}\sum_{k = 0}^n"
        centered_expr += r"e^{tk}\]"
        uniform_mgf += [centered_expr]
        unif_mgf_msg = [Tex(b) for b in uniform_mgf]
        
        unif_mgf_end = MathTex(r"M_X(t) = \dfrac{1 - e^t{n + 1}}{n(1 - s)}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=unif_msg,
            new=unif_mgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(unif_mgf_end.next_to(unif_mgf_msg[-1], 7 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi uniforme"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=unif_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(unif_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')
        

        

class ContinuousUniform(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Fonction génératrice des moments avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.65))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        inbox1 = "Savez-vous comment calculer "
        inbox2 = "la fonction génératrice des "
        inbox3 = "moments de la loi uniforme continue ?"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)
        
        self.play(
            Write(msg.next_to(title_start, 3 * DOWN)),
            ReplacementTransform(
                title_start,
                title_question.scale(0.75)
            )
        )
        self.wait(3)

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

        uniform_prob = [r"Si \(X\) suit une loi uniforme "]
        uniform_prob += [r"sur l'intervalle [a ; b] alors "]
        centered_expr = r"\[f_X(x) = \dfrac{1}{b - a} "
        centered_expr += r"\mathbb{I}_{[a ; b]}(x)\]"
        uniform_prob += [centered_expr]
        
        uniform_prob += [r" avec "]
        
        centered_expr = r"\[\mathbb{I}_{[a ; b]}(x) = 1\iff "
        centered_expr += r"x\in [a ; b]\]"
        uniform_prob += [centered_expr]
        
        centered_expr = r"\[\mathbb{I}_{[a ; b]}(x) = 0\iff "
        centered_expr += r"x\not \in [a ; b]\]"
        uniform_prob += [centered_expr]
        
        unif_msg = [Tex(u) for u in uniform_prob]

        replace_and_write(
            self,
            old=def_msg,
            new=unif_msg,
            pos_ref=title_rep,
            duration=2.5,
        )

        box = SurroundingRectangle(unif_msg[2])
        self.play(Write(box))
        self.wait()
        self.play(FadeOut(box))
        self.wait()
        
        uniform_mgf = [r"\[M_X(t) = \mathbb{E}(e^{tX})\]"]
        centered_expr = r"\[M_X(t) = \int_{-\infty}^{+\infty} "
        centered_expr += r"f_X(x)\times e^{tx}dx\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \int_{a}^{b}\dfrac{1}{b - a} "
        centered_expr += r"\times e^{tx}dx\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \dfrac{1}{b - a}\int_{a}^{b} "
        centered_expr += r"e^{tx}dx\]"
        uniform_mgf += [centered_expr]
        centered_expr = r"\[M_X(t) = \dfrac{1}{b - a}\left[ "
        centered_expr += r"\dfrac{e^{tx}}{t}\right]_{a}^{b}\]"
        uniform_mgf += [centered_expr]
        
        unif_mgf_msg = [Tex(b) for b in uniform_mgf]
        
        unif_mgf_end = MathTex(r"M_X(t) = \dfrac{e^{bt} - e^{at}}{(b - a)t}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=unif_msg,
            new=unif_mgf_msg,
            pos_ref=title_rep,
            duration=2.5,
            #**lines_and_scales
        )

        self.play(Write(unif_mgf_end.next_to(unif_mgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des moments "
        inbox3 = "de la loi uniforme"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=unif_mgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=2.5,
        )

        self.play(unif_mgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        
        box_res = SurroundingRectangle(unif_mgf_end)
        title_end = Title("CLAP : Commentez Likez Abonnez-vous Partagez")
        self.play(
            Write(box_res),
            ReplacementTransform(
                title_rep,
                title_end.scale(0.75)
            ),
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')
        
        
