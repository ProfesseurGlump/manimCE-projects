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
        msg = "Fonction génératrice des probabilités avec "
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
        phrase = "Savez-vous comment calculer | "
        phrase += "la fonction génératrice des | "
        phrase += "probabilités de la loi de Bernoulli ? | "
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)
        
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

        def_msg = prob_def_recall()
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

        bernoulli_pgf = [r"\[G_X(s) = \mathbb{E}(s^X)\]"]
        centered_expr = r"\[G_X(s) = \mathbb{P}_X(\{0\})\times s^0"
        centered_expr += r"+ \mathbb{P}_X(\{1\})\times s^1\]"
        bernoulli_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \mathbb{P}(\{X = 0\})\times s^0"
        centered_expr += r"+ \mathbb{P}(\{X = 1\})\times s^1\]"
        bernoulli_pgf += [centered_expr]
        ber_pgf_msg = [Tex(b) for b in bernoulli_pgf]
        
        ber_pgf_end = MathTex(r"G_X(s) = (1 - p) + ps")

        lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=ber_msg,
            new=ber_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            **lines_and_scales
        )

        self.play(Write(ber_pgf_end.next_to(ber_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la fonction | "
        phrase += "génératrice des probabilités | "
        phrase += "de la loi de Bernoulli"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=ber_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(ber_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(ber_pgf_end)
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
        msg = "Fonction génératrice des probabilités avec "
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
        inbox3 = "probabilités de la loi géométrique ?"
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

        def_msg = prob_def_recall()
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
        centered_expr += r"\mathbb{P}(\{X = k\}) = (1 - p)^{k - 1}p\]"
        geometric_prob += [centered_expr]
        geom_msg = [Tex(b) for b in geometric_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=geom_msg,
            pos_ref=title_rep,
            duration=5,
        )

        geometric_pgf = [r"\[G_X(s) = \mathbb{E}(s^X)\]"]
        centered_expr = r"\[G_X(s) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"\mathbb{P}_X(\{k\})\times s^k\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"\mathbb{P}(\{X = k\})\times s^k\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 1}^{+\infty}"
        centered_expr += r"p(1 - p)^{k - 1}s^k\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = ps\sum_{k = 1}^{+\infty}"
        centered_expr += r"(1 - p)^{k - 1}s^{k - 1}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = ps\sum_{k = 0}^{+\infty}"
        centered_expr += r"\left[s(1 - p)\right]^{k}\]"
        geometric_pgf += [centered_expr]
        geom_pgf_msg = [Tex(b) for b in geometric_pgf]

        geom_pgf_end = MathTex(r"G_X(s) = \dfrac{ps}{1 - s(1 - p)}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=geom_msg,
            new=geom_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(geom_pgf_end.next_to(geom_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la fonction | "
        phrase += "génératrice des probabilités | "
        phrase += "de la loi géométrique"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=geom_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(geom_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(geom_pgf_end)
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
        msg = "Fonction génératrice des probabilités avec "
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
        phrase = "Savez-vous comment calculer | "
        phrase += "la fonction génératrice des | "
        phrase = "probabilités de la loi binomiale ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        def_msg = prob_def_recall()
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

        binomial_pgf = [r"\[G_X(s) = \mathbb{E}(s^X)\]"]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}_X(\{k\})\times s^k\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}(\{X = k\})\times s^k\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\binom{n}{k}p^k(1 - p)^{n - k}s^k\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\binom{n}{k}(ps)^k(1 - p)^{n - k}\]"
        binomial_pgf += [centered_expr]
        bin_pgf_msg = [Tex(b) for b in binomial_pgf]
        
        bin_pgf_end = MathTex(r"G_X(s) = \left[(1 - p) + ps\right]^n")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=bin_msg,
            new=bin_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(bin_pgf_end.next_to(bin_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la fonction |"
        phrase += "génératrice des probabilités | "
        phrase += "de la loi binomiale"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=bin_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(bin_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(bin_pgf_end)
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
        msg = "Fonction génératrice des probabilités avec "
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
        phrase = "Savez-vous comment calculer | "
        phrase += "la fonction génératrice des | "
        phrase = "probabilités de la loi de Poisson ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        def_msg = prob_def_recall()
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

        poisson_pgf = [r"\[G_X(s) = \mathbb{E}(s^X)\]"]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"\mathbb{P}_X(\{k\})\times s^k\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"\mathbb{P}(\{X = k\})\times s^k\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^{+\infty}"
        centered_expr += r"e^{-\lambda}\dfrac{\lambda^k}{k!}s^k\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = e^{-\lambda}\sum_{k = 0}^{+\infty}"
        centered_expr += r"\dfrac{(\lambda s)^k}{k!}\]"
        poisson_pgf += [centered_expr]
        poisson_pgf += [r"\[G_X(s) = e^{-\lambda}e^{\lambda s}\]"]
        pois_pgf_msg = [Tex(b) for b in poisson_pgf]

        pois_pgf_end = MathTex(r"G_X(s) = e^{\lambda(s - 1)}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=pois_msg,
            new=pois_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(pois_pgf_end.next_to(pois_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la fonction | "
        phrase += "génératrice des probabilités | "
        phrase = "de la loi de Poisson"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=pois_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(pois_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(pois_pgf_end)
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
        msg = "Fonction génératrice des probabilités avec "
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
        inbox3 = "probabilités de la loi uniforme ?"
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

        def_msg = prob_def_recall()
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

        uniform_pgf = [r"\[G_X(s) = \mathbb{E}(s^X)\]"]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}_X(\{k\})\times s^k\]"
        uniform_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\mathbb{P}(\{X = k\})\times s^k\]"
        uniform_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \sum_{k = 0}^n"
        centered_expr += r"\dfrac{1}{n}s^k\]"
        uniform_pgf += [centered_expr]
        centered_expr = r"\[G_X(s) = \dfrac{1}{n}\sum_{k = 0}^n"
        centered_expr += r"s^k\]"
        uniform_pgf += [centered_expr]
        unif_pgf_msg = [Tex(b) for b in uniform_pgf]
        
        unif_pgf_end = MathTex(r"G_X(s) = \dfrac{1 - s^{n + 1}}{n(1 - s)}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=unif_msg,
            new=unif_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(unif_pgf_end.next_to(unif_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        inbox1 = "On a bien calculé la fonction "
        inbox2 = "génératrice des probabilités "
        inbox3 = "de la loi uniforme"
        inboxes = [inbox1, inbox2, inbox3]
        msg = inbox_msg(*inboxes, font_size=40)

        replace_and_write(
            self,
            old=unif_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        
        box_res = SurroundingRectangle(unif_pgf_end)
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
        

class UseCase1Ber(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer l'espérance | "
        phrase += "à partir de la fonction génératrice des | "
        phrase += "probabilités de la loi de Bernoulli ?"
        sep = "|"
        msg = cursive_msg(phrase, sep, 40)
        
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

        def_msg = expectation_def_recall()
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

        bernoulli_pgf = [r"\[G_X(s) = (1 - p) + ps\]"]
        bernoulli_pgf += [r"\[G'_X(s) = p\]"]
        bernoulli_pgf += [r"\[G'_X(1) = p\]"]
        ber_pgf_msg = [Tex(b) for b in bernoulli_pgf]
        
        ber_pgf_end = MathTex(r"G'_X(1) = p = \mathbb{E}(X)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=ber_msg,
            new=ber_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(ber_pgf_end.next_to(ber_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé l'espérance grâce à | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi de Bernoulli"
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)

        replace_and_write(
            self,
            old=ber_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(ber_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(ber_pgf_end)
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

        
class UseCase1Geom(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer | "
        phrase += "l'espérance à partir de la | "
        phrase += "fonction génératrice des | "
        phrase += "probabilités de la loi géométrique ? | "
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)
        
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

        def_msg = expectation_def_recall()
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
        centered_expr += r"\mathbb{P}(\{X = k\}) = (1 - p)^{k - 1}p\]"
        geometric_prob += [centered_expr]
        geom_msg = [Tex(b) for b in geometric_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=geom_msg,
            pos_ref=title_rep,
            duration=5,
        )

        geometric_pgf = [r"\[G_X(s) = \dfrac{ps}{1 - (1 - p)s}\]"]
        centered_expr = r"\[G'_X(s) = \dfrac{p\left[1 - (1 - p)s\right]"
        centered_expr += r"+ (1 - p)ps}{\left[1 - (1 - p)s\right]^2}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G'_X(s) = \dfrac{p - ps + p^2s + ps - p^2s}"
        centered_expr += r"{\left[1 - (1 - p)s\right]^2}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G'_X(s) = \dfrac{p}"
        centered_expr += r"{\left[1 - (1 - p)s\right]^2}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G'_X(1) = \dfrac{p}"
        centered_expr += r"{\left[1 - (1 - p)\right]^2}\]"
        geometric_pgf += [centered_expr]
        geometric_pgf += [r"\[G'_X(1) = \dfrac{p}{p^2}\]"]
        geom_pgf_msg = [Tex(b) for b in geometric_pgf]

        geom_pgf_end = MathTex(r"G'_X(1) = \dfrac{1}{p} = \mathbb{E}(X)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=geom_msg,
            new=geom_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(geom_pgf_end.next_to(geom_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        phrase = "On a bien calculé l'espérance | "
        phrase += "à partir de la fonction génératrice | "
        phrase += "des probabilités de la loi géométrique"
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)

        replace_and_write(
            self,
            old=geom_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(geom_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(geom_pgf_end)
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

        
        
class UseCase1Pois(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer l'espérance | "
        phrase += "la fonction génératrice des | "
        phrase += "probabilités de la loi de Poisson ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        def_msg = expectation_def_recall()
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

        poisson_pgf = [r"\[G_X(s) = e^{\lambda(s - 1)}\]"]
        centered_expr = r"\[G'_X(s) = \lambda \times "
        centered_expr += r"e^{\lambda(s - 1)}\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[G'_X(1) = \lambda \times "
        centered_expr += r"e^{\lambda(1 - 1)}\]"
        poisson_pgf += [centered_expr]
        pois_pgf_msg = [Tex(b) for b in poisson_pgf]

        pois_pgf_end = MathTex(r"G'_X(1) = \lambda = \mathbb{E}(X)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=pois_msg,
            new=pois_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(pois_pgf_end.next_to(pois_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé l'espérance avec | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi de Poisson"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=pois_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(pois_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(pois_pgf_end)
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


class UseCase1Bin(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer l'espérance | "
        phrase += "avec la fonction génératrice des | "
        phrase += "probabilités de la loi binomiale ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        
        def_msg = expectation_def_recall()
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

        binomial_pgf = [r"\[G_X(s) = \left[(1 - p) + ps\right]^n\]"]
        centered_expr = r"\[G'_X(s) = np\left[(1 - p) + "
        centered_expr += r"ps\right]^{n - 1}\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G'_X(1) = np\left[(1 - p) + "
        centered_expr += r"p\right]^{n - 1}\]"
        binomial_pgf += [centered_expr]
        binomial_pgf += [r"\[G'_X(1) = np(1 - p + p)^{n - 1}\]"]
        
        bin_pgf_msg = [Tex(b) for b in binomial_pgf]
        
        bin_pgf_end = MathTex(r"G'_X(1) = np = \mathbb{E}(X)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=bin_msg,
            new=bin_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(bin_pgf_end.next_to(bin_pgf_msg[-1], 6 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé l'espérance grâce à | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi binomiale"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=bin_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )

        self.play(
            bin_pgf_end.animate.next_to(msg, 2 * DOWN)
        )
        self.wait()
        box_res = SurroundingRectangle(bin_pgf_end)
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
        

class UseCase2Ber(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer la variance | "
        phrase += "à partir de la fonction génératrice des | "
        phrase += "probabilités de la loi de Bernoulli ?"
        sep = "|"
        msg = cursive_msg(phrase, sep, 40)
        
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

        def_msg = variance_def_recall()
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

        bernoulli_pgf = [r"\[G_X(s) = (1 - p) + ps\]"]
        bernoulli_pgf += [r"\[G'_X(s) = p\]"]
        bernoulli_pgf += [r"\[G'_X(1) = p\]"]
        bernoulli_pgf += [r"\[G''_X(s) = 0\]"]
        bernoulli_pgf += [r"\[G''_X(1) = 0\]"]
        centered = r"\[\mathbb{V}(X) = G''_X(1) + G'_X(1) "
        centered += r"- \left[G'_X(1)\right]^2\]"
        bernoulli_pgf += [centered]
        bernoulli_pgf += [r"\[\mathbb{V}(X) = 0 + p - p^2\]"]
        ber_pgf_msg = [Tex(b) for b in bernoulli_pgf]
        
        ber_pgf_end = MathTex(r"\mathbb{V}(X) = p(1 - p)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=ber_msg,
            new=ber_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(ber_pgf_end.next_to(ber_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la variance grâce à | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi de Bernoulli"
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)

        replace_and_write(
            self,
            old=ber_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(ber_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(ber_pgf_end)
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
        

class UseCase2Geom(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer | "
        phrase += "la variance à partir de la | "
        phrase += "fonction génératrice des | "
        phrase += "probabilités de la loi géométrique ? | "
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)
        
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

        def_msg = variance_def_recall()
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
        centered_expr += r"\mathbb{P}(\{X = k\}) = (1 - p)^{k - 1}p\]"
        geometric_prob += [centered_expr]
        geom_msg = [Tex(b) for b in geometric_prob]
                    
        replace_and_write(
            self,
            old=def_msg,
            new=geom_msg,
            pos_ref=title_rep,
            duration=5,
        )

        geometric_pgf = [r"\[G_X(s) = \dfrac{ps}{1 - (1 - p)s}\]"]
        centered_expr = r"\[G'_X(s) = \dfrac{p}"
        centered_expr += r"{\left[1 - (1 - p)s\right]^2}\]"
        geometric_pgf += [centered_expr]
        geometric_pgf += [r"\[G'_X(1) = \dfrac{1}{p}\]"]
        centered_expr = r"\[G''_X(s) = \dfrac{2p(1 - p)}"
        centered_expr += r"{\left[1 - (1 - p)s\right]^3}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G''_X(1) = \dfrac{2p(1 - p)}"
        centered_expr += r"{\left[1 - (1 - p)\right]^3}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[G''_X(1) = \dfrac{2(1 - p)}"
        centered_expr += r"{p^2}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = G''_X(1) + G'_X(1) "
        centered_expr += r"- \left[G'_X(1)\right]^2\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = \dfrac{2(1 - p)}"
        centered_expr += r"{p^2} +  \dfrac{1}{p} - \dfrac{1}"
        centered_expr += r"{p^2}\]"
        geometric_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = \dfrac"
        centered_expr += r"{2 - 2p + p - 1}{p^2}\]"
        geometric_pgf += [centered_expr]
        
        geom_pgf_msg = [Tex(b) for b in geometric_pgf]

        geom_pgf_end = MathTex(r"\mathbb{V}(X) = \dfrac{1 - p}{p^2}")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=geom_msg,
            new=geom_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(geom_pgf_end.next_to(geom_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        phrase = "On a bien calculé la variance | "
        phrase += "à partir de la fonction génératrice | "
        phrase += "des probabilités de la loi géométrique"
        sep = "|"
        msg = cursive_msg(phrase, sep, 42)

        replace_and_write(
            self,
            old=geom_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(geom_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(geom_pgf_end)
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
        

class UseCase2Bin(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer la variance | "
        phrase += "avec la fonction génératrice des | "
        phrase += "probabilités de la loi binomiale ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        
        def_msg = variance_def_recall()
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

        binomial_pgf = [r"\[G_X(s) = \left[(1 - p) + ps\right]^n\]"]
        centered_expr = r"\[G'_X(s) = np\left[(1 - p) + "
        centered_expr += r"ps\right]^{n - 1}\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G'_X(1) = np\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G''_X(s) = n(n - 1)p^2\left[(1 - p) + "
        centered_expr += r"ps\right]^{n - 2}\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G''_X(1) = n(n - 1)p^2(1 - p + "
        centered_expr += r"p)^{n - 2}\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[G''_X(1) = n(n - 1)p^2\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = G''_X(1) + G'_X(1) "
        centered_expr += r"- \left[G'_X(1)\right]^2\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = n(n - 1)p^2 + np "
        centered_expr += r"- n^2p^2\]"
        binomial_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = n^2p^2 - np^2 + np "
        centered_expr += r"- n^2p^2\]"
        binomial_pgf += [centered_expr]
        
        bin_pgf_msg = [Tex(b) for b in binomial_pgf]
        
        bin_pgf_end = MathTex(r"\mathbb{V}(X) = np(1 - p)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=bin_msg,
            new=bin_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(bin_pgf_end.next_to(bin_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé la variance grâce à | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi binomiale"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=bin_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )

        self.play(
            bin_pgf_end.animate.next_to(msg, 2 * DOWN)
        )
        self.wait()
        box_res = SurroundingRectangle(bin_pgf_end)
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
        

class UseCase2Pois(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "À quoi sert la fonction génératrice des probabilités avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start.scale(0.5))
        self.wait(2)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        
        title_question = Title("Défi pour vous")
        phrase = "Savez-vous comment calculer la variance | "
        phrase += "la fonction génératrice des | "
        phrase += "probabilités de la loi de Poisson ?"
        sep = "|"
        msg = cursive_msg(phrase, sep)
        
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

        def_msg = variance_def_recall()
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

        poisson_pgf = [r"\[G_X(s) = e^{\lambda(s - 1)}\]"]
        centered_expr = r"\[G'_X(s) = \lambda \times "
        centered_expr += r"e^{\lambda(s - 1)}\]"
        poisson_pgf += [centered_expr]
        poisson_pgf += [r"\[G'_X(1) = \lambda\]"]
        centered_expr = r"\[G''_X(s) = \lambda^2 \times "
        centered_expr += r"e^{\lambda(s - 1)}\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[G''_X(1) = \lambda^2 \times "
        centered_expr += r"e^{\lambda(1 - 1)}\]"
        poisson_pgf += [centered_expr]
        poisson_pgf += [r"\[G''_X(1) = \lambda^2\]"]
        centered_expr = r"\[\mathbb{V}(X) = G''_X(1) + G'_X(1) "
        centered_expr += r"- \left[G'_X(1)\right]^2\]"
        poisson_pgf += [centered_expr]
        centered_expr = r"\[\mathbb{V}(X) = \lambda^2 + \lambda "
        centered_expr += r"- \lambda^2\]"
        poisson_pgf += [centered_expr]
        pois_pgf_msg = [Tex(b) for b in poisson_pgf]

        pois_pgf_end = MathTex(r"\mathbb{V}(X) = \lambda = \mathbb{E}(X)")

        #lines_and_scales = {'1' : 0.75, '2' : 0.85}
        replace_and_write(
            self,
            old=pois_msg,
            new=pois_pgf_msg,
            pos_ref=title_rep,
            duration=5,
            #**lines_and_scales
        )

        self.play(Write(pois_pgf_end.next_to(pois_pgf_msg[-1], 2 * DOWN)))
        self.wait(2)
        
        phrase = "On a bien calculé l'espérance avec | "
        phrase += "la fonction génératrice des probabilités | "
        phrase += "de la loi de Poisson"
        sep = "|"
        msg = cursive_msg(phrase, sep)

        replace_and_write(
            self,
            old=pois_pgf_msg,
            new=msg,
            pos_ref=title_rep,
            duration=5,
        )
        self.play(pois_pgf_end.animate.next_to(msg, 2 * DOWN))
        self.wait()
        box_res = SurroundingRectangle(pois_pgf_end)
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
        
