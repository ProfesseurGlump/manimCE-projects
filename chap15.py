from manim import *
import manim
from math import e, pi
import math
from PIL import Image

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



def targets_to_write(text, ref, size=1, direction=DOWN):
    #text = [Text(t) for t in text if isinstance(t, str)]
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



class SectionAQuestion1(Scene):
    def construct(self):
        msg1 = "Logarithme népérien"
        title1 = Title(f"{msg1}")
        self.add(title1.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question1 = Title("Question 1")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait()
        

        q1 = Tex(
            "Sachant que \(4\ln(2) - 3\ln(4) + \ln(k) = 0\), trouver \(k\)."
        )

        b1 = SurroundingRectangle(q1, color=BLUE, buff=0.2)

        mobj1 = VGroup(b1, q1)

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
            Write(mobj1.next_to(title1, 1.75 * DOWN))
        )
        self.wait(4)

        solution1 = Title("Solution 1")
        
        p1 = MathTex(r"\ln(2^4) - \ln(4^3) + \ln(k) = 0")

        self.play(
            ReplacementTransform(question1, solution1),
            Write(p1.next_to(mobj1, DOWN))
        )
        self.wait(3)
        

        p11 = MathTex(r"\ln\left(\dfrac{2^4}{4^3}\right) + \ln(k) = 0")

        self.play(
            Write(p11.next_to(p1, DOWN)),
        )
        self.wait(3)

        p12 = MathTex(
            r"\ln\left(\dfrac{4^2}{4^3}\right) + \ln(k) = 0"
        )

        self.play(
            Write(p12.next_to(p11, DOWN)),
        )
        self.wait()

        p13 = MathTex(
            r"-\ln(4) + \ln(k) = 0"
        )

        self.play(
            Write(p13.next_to(p12, DOWN)),
        )
        self.wait()

        p14 = MathTex(
            r"\ln\left(\dfrac{k}{4}\right) = 0"
        )

        self.play(
            ReplacementTransform(p1, p14.next_to(mobj1, DOWN)),
        )
        self.wait()

        
        p15 = MathTex(
            r"\dfrac{k}{4} = 1"
        )

        self.play(
            ReplacementTransform(p11, p15.next_to(p14, DOWN)),
        )
        self.wait()

        p16 = MathTex(
            r"k = 4"
        )

        self.play(
            ReplacementTransform(p12, p16.next_to(p15, DOWN)),
        )
        self.wait()

        
        all_terms = Group(p1, p11, p12, p13, p14, p15)
        box_res = SurroundingRectangle(p16)
        self.play(
            FadeOut(all_terms),
            Write(box_res)
        )
        self.wait()
        

        disp_sub(self, lang="fr")



class SectionAQuestion21(Scene):
    def construct(self):
        msg21 = "Division de polynômes"
        title21 = Title(f"{msg21}")
        self.add(title21.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question21 = Title("Question 2.1")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title21, question21)
        )
        self.wait()
        

        q21 = Tex(
            "Montrer que \(p(x) = 2x^3 - 3x^2 + 8x + 5\) est divisible par \(2x + 1\)."
        )

        b21 = SurroundingRectangle(q21, color=BLUE, buff=0.2)

        mobj21 = VGroup(b21, q21)

        self.play(
            img2.animate.shift(2.5 * RIGHT + 1.25 * UP).scale(0.75),
            Write(mobj21.next_to(title21, 1.75 * DOWN))
        )
        self.wait(4)

        solution21 = Title("Solution 2.1")
        
        p21 = MathTex(r"p(x) = (2x + 1)(ax^2 + bx + c)")

        self.play(
            ReplacementTransform(question21, solution21),
            Write(p21.next_to(mobj21, DOWN))
        )
        self.wait(3)
        

        p22 = MathTex(r"p(x) = 2ax^3 + 2bx^2 + 2cx + ax^2 + bx + c")

        self.play(
            Write(p22.next_to(p21, DOWN)),
        )
        self.wait(3)

        p23 = MathTex(
            r"p(x) = 2ax^3 + (2b + a)x^2 + (2c + b)x + c"
        )

        self.play(
            Write(p23.next_to(p22, DOWN)),
        )
        self.wait()

        p24 = MathTex(
            r"2x^3 - 3x^2 + 8x + 5 = 2ax^3 + (2b + a)x^2 + (2c + b)x + c"
        )

        self.play(
            Write(p24.next_to(p23, DOWN)),
        )
        self.wait()

        p25 = MathTex(
            r"a = 1, 2b + 1 = - 3\Rightarrow b = -2, c = 5"
        )

        self.play(
            ReplacementTransform(p21, p25.next_to(mobj21, DOWN)),
        )
        self.wait()

        
        p26 = MathTex(
            r"p(x) = (2x + 1)(x^2 - 2x + 5)"
        )

        self.play(
            ReplacementTransform(p22, p26.next_to(p25, DOWN)),
        )
        self.wait()

        p27 = MathTex(
            r"2x^3 - 3x^2 + 8x + 5 = (2x + 1)(x^2 - 2x + 5)"
        )

        self.play(
            ReplacementTransform(p23, p27.next_to(p26, DOWN)),
        )
        self.wait()

        
        all_terms = Group(p21, p22, p24, p24, p25, p26)
        box_res = SurroundingRectangle(p27)
        self.play(
            FadeOut(all_terms),
            Write(box_res)
        )
        self.wait()
        

        disp_sub(self, lang="fr")
        


class SectionAQuestion22(Scene):
    def construct(self):
        msg22 = "Division de polynômes"
        title22 = Title(f"{msg22}")
        self.add(title22.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question22 = Title("Question 2.2")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title22, question22)
        )
        self.wait()
        

        q22 = Tex(
            "Trouver toutes les racines de \(p(x) = 2x^3 - 3x^2 + 8x + 5\)."
        )

        b22 = SurroundingRectangle(q22, color=BLUE, buff=0.2)

        mobj22 = VGroup(b22, q22)

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
            Write(mobj22.next_to(title22, 1.75 * DOWN))
        )
        self.wait(4)

        solution22 = Title("Solution 2.2")
        
        p21 = MathTex(r"p(x) = 0 \iff (2x + 1)(x^2 - 2x + 5) = 0")

        self.play(
            ReplacementTransform(question22, solution22),
            Write(p21.next_to(mobj22, DOWN))
        )
        self.wait(3)
        

        txt22 = r"(2x + 1)(x^2 - 2x + 5) = 0\iff 2x + 1 = 0"
        txt22 += r"\mbox{ ou } x^2 - 2x + 5 = 0"
        p22 = MathTex(txt22)

        self.play(
            Write(p22.next_to(p21, DOWN)),
        )
        self.wait(3)

        p23 = MathTex(
            r"2x + 1 = 0\Rightarrow x = -\dfrac{1}{2}"
        )

        self.play(
            Write(p23.next_to(p22, DOWN)),
        )
        self.wait()

        txt24 = r"x^2 - 2x + 5 = 0 ? \Rightarrow "
        txt24 += r"\Delta = (-2)^2 - 4\times 5\times 1 < 0"
        p24 = MathTex(txt24)

        self.play(
            Write(p24.next_to(p23, DOWN)),
        )
        self.wait()

        p25 = MathTex(
            r"\Delta < 0\Rightarrow (x^2 - 2x + 5) \neq 0"
        )

        self.play(
            ReplacementTransform(p21, p25.next_to(mobj22, DOWN)),
        )
        self.wait()

        
        p26 = MathTex(
            r"p(x) = 0 \iff x = -\dfrac{1}{2}"
        )

        self.play(
            ReplacementTransform(p22, p26.next_to(p25, DOWN)),
        )
        self.wait()

        p27 = MathTex(
            r"S = \left\{-\dfrac{1}{2}\right\}"
        )

        self.play(
            ReplacementTransform(p23, p27.next_to(p26, DOWN)),
        )
        self.wait()

        
        all_terms = Group(p21, p22, p24, p24, p25, p26)
        box_res = SurroundingRectangle(p27)
        self.play(
            FadeOut(all_terms),
            Write(box_res)
        )
        self.wait()
        

        disp_sub(self, lang="fr")
        
        


class SectionAQuestion3(Scene):
    def construct(self):
        msg3 = "Suites géométriques"
        title3 = Title(f"{msg3}")
        self.add(title3.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question3 = Title("Question 3")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title3, question3)
        )
        self.wait()

        self.play(
            img2.animate.shift(2.5 * RIGHT + 1.25 * UP).scale(0.75),
        )
        self.wait()
        
        phrase1 = r"La somme des deux premiers termes d'une suite "
        phrases = [phrase1]
        
        phrase2 = r"géométrique est \(\dfrac{8}{9}\)."
        phrases += [phrase2]
        
        phrase3 = r"La somme de ses trois premiers termes vaut "
        phrase3 += r"\(\dfrac{26}{27}\)."
        phrases += [phrase3]
        
        phrase4 = r"Trouver les valeurs possibles pour le premier terme."
        phrases += [phrase4]
                  
        phrase5 = r"Calculer la somme de tous ses termes."
        phrases += [phrase5]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title3, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait()
        

        solution3 = Title("Solution 3")
        
        p3 = MathTex(r"u_0 + u_1 = \dfrac{8}{9}")

        self.play(
            ReplacementTransform(question3, solution3),
            FadeOut(*phr_tex),
            Write(p3.next_to(title3, DOWN)),
        )
        self.wait(3)
        

        p31 = MathTex(r"u_0 + u_1 + u_2 = \dfrac{26}{27}")

        self.play(
            Write(p31.next_to(p3, DOWN)),
        )
        self.wait(3)

        p32 = MathTex(
            r"u_0 + u_0\times q = \dfrac{8}{9}"
        )

        self.play(
            ReplacementTransform(p3, p32.next_to(title3, DOWN)),
        )
        self.wait(2)

        p33 = MathTex(
            r"u_0\times q^2= \dfrac{26}{27} - \dfrac{8}{9}"
        )

        self.play(
            ReplacementTransform(p31, p33.next_to(p32, DOWN)),
        )
        self.wait(2)

        p34 = MathTex(
            r"u_0(1 + q) = \dfrac{8}{9}"
        )

        self.play(
            ReplacementTransform(p32, p34.next_to(title3, DOWN)),
        )
        self.wait()

        
        p35 = MathTex(
            r"u_0q^2 = \dfrac{26}{27} - \dfrac{24}{27}"
        )

        self.play(
            p34.animate.shift(4 * LEFT),
            ReplacementTransform(p33, p35.next_to(p34, DOWN)),
        )
        self.wait()

        p36 = MathTex(
            r"u_0q^2 = \dfrac{2}{27}"
        )

        self.play(
            ReplacementTransform(p35, p36.next_to(p34, DOWN)),
        )
        self.wait()

        A = Dot().next_to(p36[0], 0.5 * DOWN + LEFT)
        B = Dot().next_to(p36[-1], 0.5 * DOWN + RIGHT)
        sep_line = Line(A, B)
        self.play(Write(sep_line))
        self.wait(2)

        quotient = r"\dfrac{u_0q^2}{u_0(1 + q)} = "
        quotient += r"\dfrac{2}{27}\times \dfrac{9}{8}"
        quot = MathTex(quotient)
        self.play(Write(quot.next_to(sep_line, DOWN)))
        self.wait(2)

        quotient2 = r"\dfrac{q^2}{1 + q} = \dfrac{1}{12}"
        quot2 = MathTex(quotient2)
        self.play(
            ReplacementTransform(quot, quot2.next_to(sep_line, DOWN))
        )
        self.wait(2)

        quotient3 = r"12q^2 = 1 + q"
        quot3 = MathTex(quotient3)
        self.play(
            ReplacementTransform(quot2, quot3.next_to(sep_line, DOWN))
        )
        self.wait(2)

        quotient4 = r"12q^2 - q - 1 = 0"
        quot4 = MathTex(quotient4)
        self.play(
            ReplacementTransform(quot3, quot4.next_to(sep_line, DOWN))
        )
        self.wait(2)

        delta = r"\Rightarrow\Delta = (-1)^2 - 4\times 12\times (-1)"
        d = MathTex(delta)
        self.play(
            Write(d.next_to(quot4, RIGHT))
        )
        self.wait()

        delta2 = r"\Rightarrow\Delta = 1 + 48"
        d2 = MathTex(delta2)
        self.play(
            ReplacementTransform(d, d2.next_to(quot4, RIGHT))
        )
        self.wait(1.5)

        delta3 = r"\Rightarrow\Delta = 49"
        d3 = MathTex(delta3)
        self.play(
            ReplacementTransform(
                d2,
                d3.next_to(quot4, RIGHT)
            ),
        )
        self.wait(1.5)

        qs = r"\Rightarrow q = \dfrac{1 \pm 7}{2\times 12}"
        q = MathTex(qs)
        self.play(
            Write(q.next_to(d3, DOWN))
        )
        self.wait(1.5)

        qs2 = r"\Rightarrow q \in\left\{ -\dfrac{1}{4}, \dfrac{1}{3}\right\}"
        q2 = MathTex(qs2)
        self.play(
            ReplacementTransform(q, q2.next_to(d3, DOWN))
        )
        self.wait(1.5)

        qsq = r"\Rightarrow q^2\in\left\{\dfrac{1}{9}, \dfrac{1}{16}\right\}"
        qsq_tex = MathTex(qsq)
        self.play(
            Write(qsq_tex.next_to(q2, RIGHT))
        )
        self.wait(2)

        disp_sub(self, lang="fr")

class SectionAQuestion3Part2(Scene):
    def construct(self):
        msg3 = "Suites géométriques (suite)"
        title3 = Title(f"{msg3}")
        self.add(title3.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question3 = Title("Rappel de l'énoncé")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title3, question3)
        )
        self.wait()

        self.play(
            img2.animate.shift(3.5 * RIGHT + 1.25 * UP).scale(0.75),
        )
        self.wait()
        
        phrase1 = r"La somme des deux premiers termes d'une suite "
        phrases = [phrase1]
        
        phrase2 = r"géométrique est \(\dfrac{8}{9}\)."
        phrases += [phrase2]
        
        phrase3 = r"La somme de ses trois premiers termes vaut "
        phrase3 += r"\(\dfrac{26}{27}\)."
        phrases += [phrase3]
        
        phrase4 = r"Trouver les valeurs possibles pour le premier terme."
        phrases += [phrase4]
                  
        phrase5 = r"Calculer la somme de tous ses termes."
        phrases += [phrase5]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title3, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait()
        

        solution3 = Title(r"Cas où \(q = -\dfrac{1}{4}\)")
        
        p31 = MathTex(
            r"u_0\left(1 - \dfrac{1}{4}\right) = \dfrac{8}{9}"
        ).next_to(solution3, 2.5 * DOWN)
        
        p32 = MathTex(
            r"u_0\times \dfrac{1}{16} = \dfrac{2}{27}"
        ).next_to(p31, 2.5 * DOWN)

        self.play(
            ReplacementTransform(question3, solution3),
            img2.animate.shift(6 * LEFT + 0.5 * DOWN),
            *[FadeOut(*phr_tex)],
            Write(p31),
            Write(p32)
        )
        self.wait(4)

        
        p33 = MathTex(
            r"u_0\times \dfrac{3}{4} = \dfrac{8}{9}"
        ).next_to(solution3, 2.5 * DOWN)
        
        p34 = MathTex(
            r"u_0 = \dfrac{32}{27}"
        ).next_to(p33, 2.5 * DOWN)

        old = [p31, p32]
        new = [p33, p34]
        self.play(
            *[
                ReplacementTransform(
                    old[i],
                    new[i]
                ) for i in range(len(old))
            ]
        )
        self.wait(3)

        res = MathTex(r"u_n = u_0\times q^n")
        res_txt = r"\Rightarrow u_n = \dfrac{32}{27}\times "
        res_txt += r"\left(-\dfrac{1}{4}\right)^n"
        res2 = MathTex(res_txt)
        self.play(
            Write(res.next_to(p34, DOWN)),
            Write(res2.next_to(res, RIGHT))
        )
        self.wait(3)

        self.play(
            FadeOut(p33),
            p34.animate.next_to(img2, 3 * DOWN),
        )
        self.wait()

        self.play(
            FadeOut(res),
            FadeOut(res2),
        )
        self.wait()
        
        stxt = r"S_n = \sum_{k = 0}^nu_k = \dfrac{32}{27}\sum_{k = 0}^n"
        stxt += r"\left(-\dfrac{1}{4}\right)^n "
        sn = MathTex(stxt)
        self.play(
            Write(sn.next_to(p34, DOWN)),
        )
        self.wait(4)

        stxt2 = r"S_n = \dfrac{32}{27}\times "
        stxt2 += r"\dfrac{1 - \left(-\dfrac{1}{4}\right)^{n+1}}{1 - \left(-\dfrac{1}{4}\right)}"
        sn2 = MathTex(stxt2)
        self.play(
            Write(sn2.next_to(sn, DOWN))
        )
        self.wait(4)

        stxt3 = r"S_n = \dfrac{32}{27}"
        stxt3 += r"\dfrac{1 - \left(-\dfrac{1}{4}\right)^{n+1}}{\dfrac{5}{4}}"
        sn3 = MathTex(stxt3).next_to(p34, DOWN)
        
        stxt4 = r"= \dfrac{32}{27}\times "
        stxt4 += r"\dfrac{4}{5}\left(1 - \left(-\dfrac{1}{4}\right)^{n+1}\right)"
        sn4 = MathTex(stxt4).next_to(sn3, RIGHT)

        old = [sn, sn2]
        new = [sn3, sn4]
        self.play(
            *[
                ReplacementTransform(
                    old[i],
                    new[i]
                ) for i in range(len(old))
            ]
        )
        self.wait(4)

        mobj = Group(sn3, sn4)
        stxt5 = r"S_n = \dfrac{128}{135}"
        stxt5 += r"\left(1 - \left(-\dfrac{1}{4}\right)^{n+1}\right)"
        sn5 = MathTex(stxt5)
        self.play(
            ReplacementTransform(mobj, sn5.next_to(p34, DOWN))
        )
        self.wait(4)
    
        lim_txt = r"\vert q \vert < 1\Rightarrow \lim_{n\to\infty}q^n = 0"
        lim = MathTex(lim_txt)
        self.play(Write(lim.next_to(sn5, DOWN)))
        self.wait()

        lim_txt4 = r"\Rightarrow \lim_{n\to\infty}"
        lim_txt4 += r"\left(-\dfrac{1}{4}\right)^{n+1} = 0"
        lim_4 = MathTex(lim_txt4)
        self.play(
            Write(lim_4.next_to(lim, RIGHT))
        )
        self.wait(3)
        
        lim_sn = MathTex(r"\lim_{n\to\infty} S_n = \dfrac{128}{135}")
        self.play(Write(lim_sn.next_to(lim, DOWN)))
        self.wait(2)
        
        all_terms = Group(lim, lim_4, sn, sn2, sn3, sn4, sn5, lim_sn)
        final_res = MathTex(r"\sum_{n = 0}^{+\infty}u_n = \dfrac{128}{135}")
        box_res = SurroundingRectangle(final_res)
        mobj_final = VGroup(final_res, box_res)
        self.play(
            FadeOut(all_terms),
            Write(mobj_final.next_to(p34, DOWN))
        )
        self.wait()

        self.play(
            mobj_final.animate.next_to(p34, RIGHT),
            Write(SurroundingRectangle(p34))
        )
        self.wait(4)

        disp_sub(self, lang="fr")

        

class SectionAQuestion3Part3(Scene):
    def construct(self):
        msg3 = "Suites géométriques (suite et fin)"
        title3 = Title(f"{msg3}")
        self.add(title3.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question3 = Title("Rappel de l'énoncé")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title3, question3)
        )
        self.wait()

        self.play(
            img2.animate.shift(3.5 * RIGHT + 1.25 * UP).scale(0.75),
        )
        self.wait()
        
        phrase1 = r"La somme des deux premiers termes d'une suite "
        phrases = [phrase1]
        
        phrase2 = r"géométrique est \(\dfrac{8}{9}\)."
        phrases += [phrase2]
        
        phrase3 = r"La somme de ses trois premiers termes vaut "
        phrase3 += r"\(\dfrac{26}{27}\)."
        phrases += [phrase3]
        
        phrase4 = r"Trouver les valeurs possibles pour le premier terme."
        phrases += [phrase4]
                  
        phrase5 = r"Calculer la somme de tous ses termes."
        phrases += [phrase5]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title3, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait()
        

        solution3 = Title(r"Cas où \(q = \dfrac{1}{3}\)")
        
        p31 = MathTex(
            r"u_0\left(1 + \dfrac{1}{3}\right) = \dfrac{8}{9}"
        ).next_to(solution3, 2.5 * DOWN)
        
        p32 = MathTex(
            r"u_0\times \dfrac{1}{9} = \dfrac{2}{27}"
        ).next_to(p31, 2.5 * DOWN)

        self.play(
            ReplacementTransform(question3, solution3),
            img2.animate.shift(6 * LEFT + 0.5 * DOWN),
            *[FadeOut(*phr_tex)],
            Write(p31),
            Write(p32)
        )
        self.wait(4)

        
        p33 = MathTex(
            r"u_0\times \dfrac{4}{3} = \dfrac{8}{9}"
        ).next_to(solution3, 2.5 * DOWN)
        
        p34 = MathTex(
            r"u_0 = \dfrac{2}{3}"
        ).next_to(p33, 2.5 * DOWN)

        old = [p31, p32]
        new = [p33, p34]
        self.play(
            *[
                ReplacementTransform(
                    old[i],
                    new[i]
                ) for i in range(len(old))
            ]
        )
        self.wait(3)

        res = MathTex(r"u_n = u_0\times q^n")
        res_txt = r"\Rightarrow u_n = \dfrac{2}{3}\times "
        res_txt += r"\left(\dfrac{1}{3}\right)^n"
        res2 = MathTex(res_txt)
        self.play(
            Write(res.next_to(p34, DOWN)),
            Write(res2.next_to(res, RIGHT))
        )
        self.wait(3)

        self.play(
            FadeOut(p33),
            p34.animate.next_to(img2, 3 * DOWN),
        )
        self.wait()

        self.play(
            FadeOut(res),
            FadeOut(res2),
        )
        self.wait()
        
        stxt = r"S_n = \sum_{k = 0}^nu_k = \dfrac{2}{3}\sum_{k = 0}^n"
        stxt += r"\left(\dfrac{1}{3}\right)^n "
        sn = MathTex(stxt)
        self.play(
            Write(sn.next_to(p34, DOWN)),
        )
        self.wait(4)

        stxt2 = r"S_n = \dfrac{2}{3}\times "
        stxt2 += r"\dfrac{1 - \left(\dfrac{1}{3}\right)^{n+1}}{1 - \left(\dfrac{1}{3}\right)}"
        sn2 = MathTex(stxt2)
        self.play(
            Write(sn2.next_to(sn, DOWN))
        )
        self.wait(4)

        stxt3 = r"S_n = \dfrac{2}{3}"
        stxt3 += r"\dfrac{1 - \left(\dfrac{1}{3}\right)^{n+1}}{\dfrac{2}{3}}"
        sn3 = MathTex(stxt3).next_to(p34, DOWN)
        
        stxt4 = r"= \dfrac{2}{3}\times "
        stxt4 += r"\dfrac{3}{2}\left(1 - \left(-\dfrac{1}{3}\right)^{n+1}\right)"
        sn4 = MathTex(stxt4).next_to(sn3, RIGHT)

        old = [sn, sn2]
        new = [sn3, sn4]
        self.play(
            *[
                ReplacementTransform(
                    old[i],
                    new[i]
                ) for i in range(len(old))
            ]
        )
        self.wait(4)

        mobj = Group(sn3, sn4)
        stxt5 = r"S_n = 1\times "
        stxt5 += r"\left(1 - \left(\dfrac{1}{3}\right)^{n+1}\right)"
        sn5 = MathTex(stxt5)
        self.play(
            ReplacementTransform(mobj, sn5.next_to(p34, DOWN))
        )
        self.wait(4)
    
        lim_txt = r"\vert q \vert < 1\Rightarrow \lim_{n\to\infty}q^n = 0"
        lim = MathTex(lim_txt)
        self.play(Write(lim.next_to(sn5, DOWN)))
        self.wait()

        lim_txt4 = r"\Rightarrow \lim_{n\to\infty}"
        lim_txt4 += r"\left(\dfrac{1}{3}\right)^{n+1} = 0"
        lim_4 = MathTex(lim_txt4)
        self.play(
            Write(lim_4.next_to(lim, RIGHT))
        )
        self.wait(3)
        
        lim_sn = MathTex(r"\lim_{n\to\infty} S_n = 1")
        self.play(Write(lim_sn.next_to(lim, DOWN)))
        self.wait(2)
        
        all_terms = Group(lim, lim_4, sn, sn2, sn3, sn4, sn5, lim_sn)
        final_res = MathTex(r"\sum_{n = 0}^{+\infty}u_n = 1")
        box_res = SurroundingRectangle(final_res)
        mobj_final = VGroup(final_res, box_res)
        self.play(
            FadeOut(all_terms),
            Write(mobj_final.next_to(p34, DOWN))
        )
        self.wait()

        self.play(
            mobj_final.animate.next_to(p34, RIGHT),
            Write(SurroundingRectangle(p34))
        )
        self.wait(4)

        disp_sub(self, lang="fr")

        
        
class SectionAQuestion4(Scene):
    def construct(self):
        msg1 = "Probabilités conditionnelles"
        title1 = Title(f"{msg1}")
        self.add(title1.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question1 = Title("Question 4")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait()
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Considérer les événements \(A\) et \(B\) tels que "
        phrases = [phrase1]

        phrase2 = r"\(P(A) = 0,3\) et \(P(B) = 0,2\)."
        phrases += [phrase2]

        phrase3 = r"Sachant que \(P(A\cup B) = 3P(A\cap B)\),"
        phrases += [phrase3]

        phrase4 = r"trouver \(P(A|B)\) et \(P(A\cap \overline{B})\)."
        phrases += [phrase4]

        phrase5 = r"Les probabilités de \(A\) sachant \(B\) et "
        phrases += [phrase5]
        
        phrase6 = r"de \(A\) privé de \(B\) respectivement."
        phrases += [phrase6]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait()
        self.wait(3)

        solution1 = Title("Solution 4")
        
        p1 = MathTex(r"P(A|B) = \dfrac{P(A\cap B)}{P(B)}")

        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
            Write(p1.next_to(solution1, 2 * DOWN))
        )
        self.wait(2)

        p2 = MathTex(r"P(A\cap B) = P(A) + P(B) - P(A\cup B)")
    
        self.play(
            Write(p2.next_to(p1, DOWN)),
        )
        self.wait(2)

        p22 = MathTex(r"P(A\cap B) = P(A) + P(B) - 3P(A\cap B)")

        self.play(
            ReplacementTransform(p2, p22.next_to(p1, DOWN)),
        )
        self.wait()

        p23 = MathTex(r"4P(A\cap B) = P(A) + P(B)")

        self.play(
            ReplacementTransform(p22, p23.next_to(p1, DOWN)),
        )
        self.wait()

        p24 = MathTex(r"P(A\cap B) = 0,25\left(P(A) + P(B)\right)")

        self.play(
            ReplacementTransform(p23, p24.next_to(p1, DOWN)),
        )
        self.wait()

        p25 = MathTex(r"P(A\cap B) = 0,25(0,3 + 0,2)")

        self.play(
            ReplacementTransform(p24, p25.next_to(p1, DOWN)),
        )
        self.wait()
        

        p26 = MathTex(r"P(A\cap B) = 0,125")

        self.play(
            ReplacementTransform(p25, p26.next_to(p1, DOWN)),
        )
        self.wait()
        
        p12 = MathTex(r"P(A|B) = \dfrac{0,125}{0,2}")

        self.play(
            ReplacementTransform(p1, p12.next_to(solution1, 2 * DOWN)),
        )
        self.wait(2)
        

        
        p13 = MathTex(r"P(A|B) = 0,625")

        self.play(
            ReplacementTransform(p12, p13.next_to(solution1, 2 * DOWN)),
        )
        self.wait(2)

        p3 = MathTex(r"P(A) = P(A\cap B) + P(A\cap \overline{B})")

        self.play(
            Write(p3.next_to(p26, DOWN)),
        )
        self.wait()

        p32 = MathTex(r"P(A\cap \overline{B}) = P(A\cap B) - P(A)")
        self.play(
            ReplacementTransform(p3, p32.next_to(p2, DOWN)),
        )
        self.wait(2)

        p33 = MathTex(r"P(A\cap \overline{B}) = 0,625 - 0,3")
        self.play(
            ReplacementTransform(p32, p33.next_to(p2, DOWN)),
        )
        self.wait(2)

        p34 = MathTex(r"P(A\cap \overline{B}) = 0,325")
        self.play(
            ReplacementTransform(p33, p34.next_to(p2, DOWN)),
        )
        self.wait(2)

        self.play(
            p13.animate.next_to(solution1, 2 * DOWN),
        )
        self.play(p13.animate.shift(4 * LEFT))
        self.play(p26.animate.next_to(p13, 1.5 * RIGHT))
        self.play(p34.animate.next_to(p26, 1.5 * RIGHT))
        self.wait()

        
        self.play(
            Write(SurroundingRectangle(p13)),
            Write(SurroundingRectangle(p26)),
            Write(SurroundingRectangle(p34)),
        )
        self.wait(3)
        # all_terms = Group(p1, p11, p12, p13, p14, p15)
        # box_res = SurroundingRectangle(p16)
        # self.play(
        #     FadeOut(all_terms),
        #     Write(box_res)
        # )
        # self.wait()
        

        disp_sub(self, lang="fr")



class SectionAQuestion5(Scene):
    def construct(self):
        msg1 = "Nombres complexes"
        title1 = Title(f"{msg1}")
        self.add(title1.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/yt_logo_640_360.png",
        ).scale(.5)
        subscribe = ImageMobject(
            "/Users/dn/Documents/pics/png/subs640_360.png",
        ).scale(.5)

        img1, img2 = youtube_long, subscribe
        
        self.play(FadeIn(img1.to_edge(2.5 * UP)))
        self.wait(2)
        
        question1 = Title("Question 5")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait()
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Montrer les relations suivantes pour"
        phrases = [phrase1]

        phrase2 = r"tout nombre complexe :"
        phrases += [phrase2]

        phrase3 = r"1) \(z + \bar{z} = 2\Re(z)\)"
        phrases += [phrase3]

        phrase4 = r"2) \(z - \bar{z} = 2\imath \Im(z)\)"
        phrases += [phrase4]

        phrase5 = r"3) \(\Re(z) \leqslant \vert z \vert\)"
        phrases += [phrase5]
        
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait()
        self.wait(3)

        solution1 = Title("Solution 5")
        
        p1 = MathTex(
            r"1) z + \bar{z} = \Re(z) + \imath\Im(z) + ",
            r"\Re(z) - \imath\Im(z)"
        )

        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
            Write(p1.next_to(solution1, 2 * DOWN))
        )
        self.wait(2)

        p12 = MathTex(
            r"1) z + \bar{z} = 2\Re(z)"
        )
    
        self.play(
            ReplacementTransform(
                p1,
                p12.next_to(solution1, 2 * DOWN)
            ),
        )
        self.wait(2)

        p2 = MathTex(
            r"2) z - \bar{z} = \Re(z) + \imath\Im(z) - ",
            r"(\Re(z) - \imath\Im(z))"
        )

        self.play(
            p12.animate.shift(4.5 * LEFT),
            Write(p2.next_to(solution1, 4.5 * DOWN))
        )
        self.wait(2)

        p22 = MathTex(
            r"2) z - \bar{z} = \Re(z) + \imath\Im(z) - ",
            r"\Re(z) + \imath\Im(z)"
        )
    
        self.play(
            ReplacementTransform(
                p2,
                p22.next_to(solution1, 4.5 * DOWN)
            ),
        )
        self.wait(2)

        p23 = MathTex(
            r"2) z - \bar{z} = 2\imath\Im(z)",
        )
    
        self.play(
            ReplacementTransform(
                p22,
                p23.next_to(p12, 1.5 * RIGHT)
            ),
        )
        self.wait(2)
        
        p3 = MathTex(
            r"3) \vert z \vert^2 = z\bar{z}"
        )

        self.play(
            Write(p3.next_to(p23, DOWN))
        )
        self.wait()

        p32 = MathTex(
            r"3) \vert z \vert^2 = \left(\Re(z) + \imath\Im(z)\right)",
            r"\left(\Re(z) - \imath\Im(z)\right)"
        )

        self.play(
            ReplacementTransform(p3, p32.next_to(p23, DOWN))
        )
        self.wait()


        p33 = MathTex(
            r"3) \vert z \vert^2 = \left[\Re(z)\right]^2 + ",
            r"\left[\Im(z)\right]^2"
        )

        self.play(
            ReplacementTransform(p32, p33.next_to(p23, DOWN))
        )
        self.wait()

        p34 = MathTex(
            r"3) \vert z \vert^2 - \left[\Re(z)\right]^2 = ",
            r"\left[\Im(z)\right]^2 \geqslant 0"
        )

        self.play(
            ReplacementTransform(p33, p34.next_to(p23, DOWN))
        )
        self.wait()

        p35 = MathTex(
            r"3) \vert z \vert^2 \geqslant \left[\Re(z)\right]^2\Rightarrow ",
            r"\Re(z) \leqslant \vert z\vert"
        )

        self.play(
            ReplacementTransform(p34, p35.next_to(p23, DOWN))
        )
        self.wait()

        p36 = MathTex(
            r"3) \Re(z) \leqslant \vert z\vert"
        )

        self.play(
            ReplacementTransform(p35, p36.next_to(p23, 1.5 * RIGHT))
        )
        self.wait()

        olds = [p12, p23, p36]
        news = [
            r"z + \bar{z} = 2\Re(z)",
            r"z - \bar{z} = 2\Im(z)",
            r"\Re(z)\leqslant \vert z\vert"
        ]
        targets = [(p12, 0.125 * DOWN), (p23, 0.125 * DOWN), (p36, 0.125 * DOWN)]
        news_tex = [MathTex(n) for n in news]

        self.play(
            *[
                ReplacementTransform(
                    olds[i],
                    news_tex[i].next_to(targets[i][0], targets[i][1])
                ) for i in range(len(olds))
            ]
        )
        self.wait()
        
        self.play(
            *[Write(SurroundingRectangle(n)) for n in news_tex]
        )
        self.wait()
        
        disp_sub(self, lang="fr")

        
