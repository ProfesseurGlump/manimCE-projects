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


# Section A Part 1
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

        
# Section A Part 2
class SectionAQuestion6(Scene):
    def construct(self):
        msg1 = "Géométrie dans l'espace"
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
        
        question1 = Title("Question 6")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait(3)
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Trouver l'équation de la droite "
        phrases = [phrase1]

        phrase2 = r"d'intersection entre les plans "
        phrases += [phrase2]

        phrase3 = r"d'équations \(x + 2y - z = 5\) "
        phrases += [phrase3]

        phrase4 = r"et \(-3x - y + z = 1\)."
        phrases += [phrase4]
        
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait(3)
        self.wait(3)

        solution1 = Title("Solution 6")
        
        p1 = MathTex(
            r"x + 2y - z = 5\quad (E_1)",
        ).next_to(solution1, 2 * DOWN)
        p2 = MathTex(
            r"-3x - y + z = 1\quad (E_2)",
        ).next_to(p1, DOWN)

        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
            *[Write(p) for p in [p1, p2]]
        )
        self.wait(2)

        A = Dot().next_to(p2[0], 0.5 * DOWN + LEFT)
        B = Dot().next_to(p2[-1], 0.5 * DOWN + RIGHT)
        sep_line = Line(A, B)
        self.play(Write(sep_line))
        self.wait(2)
        
        p3 = MathTex(
            r"5y - 2z = 16\quad (3E_1 + E_2)"
        ).next_to(sep_line, DOWN)
        p4 = MathTex(
            r"\Rightarrow y = \dfrac{2}{5}z + \dfrac{16}{5}"
        ).next_to(p3, DOWN)
    
        self.play(
            Write(p3),
            Write(p4)
        )
        self.wait(2)

        plug_in12 = r"x + 2\left(\dfrac{2}{5}z + \dfrac{16}{5}\right) - z "
        plug_in12 += r"= 5\quad (E_1)"
        p12 = MathTex(plug_in12).next_to(solution1, 2 * DOWN)

        plug_in13 = r"\Rightarrow x = \dfrac{1}{5}z + \dfrac{9}{5}"
        p13 = MathTex(plug_in13).next_to(p12, DOWN)

        p32 = MathTex(r"z = z")
        
        self.play(
            ReplacementTransform(p1, p12),
            ReplacementTransform(p2, p13),
            ReplacementTransform(sep_line, p4.next_to(p13, 2 * DOWN)),
            ReplacementTransform(p3, p32.next_to(p4, 2 * DOWN))
        )
        self.wait(3)

        line1 = MathTex(
            r"x = \dfrac{1}{5}t + \dfrac{9}{5}"
        ).next_to(solution1, 2 * DOWN)
        line2 = MathTex(
            r"y = \dfrac{2}{5}t + \dfrac{16}{5}"
        ).next_to(line1, 2 * DOWN)
        line3 = MathTex(
            r"z = t"
        ).next_to(line2, 2 * DOWN)
        line4 = MathTex(r"t\in\mathbb{R}").next_to(line3, 2 * DOWN)
        
        self.play(
            ReplacementTransform(p12, line1),
            ReplacementTransform(p13, line2),
            ReplacementTransform(p4, line3),
            ReplacementTransform(p32, line4),
        )
        self.wait(3)
        
        disp_sub(self, lang="fr")


class SectionAQuestion7(Scene):
    def construct(self):
        msg1 = "Courbe dans le plan"
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
        
        question1 = Title("Question 7")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait(3)
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Une courbe est définie par l'équation "
        phrases = [phrase1]

        phrase2 = r"\[x^2 + 4y^2 - 2x + 16y + 13 = 0\]"
        phrases += [phrase2]

        phrase3 = r"Trouver les coordonnées des points sur "
        phrases += [phrase3]

        phrase4 = r"la courbe où la tangente est parallèle "
        phrases += [phrase4]
        
        phrase5 = r"à l'axe des abscisses (tangente horizontale)."
        phrases += [phrase5]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait(3)
        self.wait(3)

        solution1 = Title("Solution 7")

        
        p1 = MathTex(
            r"x^2 + 4y^2 - 2x + 16y + 13 = 0",
        ).next_to(solution1, 2 * DOWN)
        p12 = MathTex(
            r"(x - 1)^2 - 1 + (2y + 4)^2 - 16 + 13 = 0",
        ).next_to(p1, DOWN)
        p13 = MathTex(
            r"\Rightarrow (x - 1)^2 + 4(y + 2)^2 - 4 = 0",
        ).next_to(p12, DOWN)
        p14 = MathTex(
            r"\Rightarrow  (y + 2)^2 = 1 - \dfrac{1}{4}(x - 1)^2",
        ).next_to(p13, DOWN)
        p15 = MathTex(
            r"\Rightarrow  y = -2\pm\sqrt{1 - \dfrac{1}{4}(x - 1)^2}",
        ).next_to(p14, DOWN)
        

        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
            Write(p1),
            Write(p12),
            Write(p13),
            Write(p14),
            Write(p15)
        )
        self.wait(5)

        f1 = MathTex(
            r"f_1(x) = -2 - \sqrt{1 - \dfrac{1}{4}(x - 1)^2}"
        ).next_to(solution1, 2 * DOWN)
        f2 = MathTex(
            r"f_2(x) = -2 + \sqrt{1 - \dfrac{1}{4}(x - 1)^2}"
        ).next_to(f1, DOWN)

        self.play(
            ReplacementTransform(p1, f1),
            ReplacementTransform(p12, f2),
            FadeOut(p13, p14, p15)
        )
        self.wait(5)
        
        A = Dot().next_to(f2[0], DL)
        B = Dot().next_to(f2[-1], DR)
        sep_line = Line(A, B)
        self.play(Write(sep_line))
        self.wait(2)

        fi = r"f_{i}(x) = -2 + (-1)^{i}\sqrt{1 - \dfrac{1}{4}(x - 1)^2}"
        mfi = MathTex(fi).next_to(solution1, 2 * DOWN)
        fgroup = VGroup(f1, f2)
        
        fip = r"f_i'(x) = (-1)^{i}\dfrac{1}{2}\times \left(-\dfrac{1}{4}\right)"
        fip += r"\times 2(x - 1)\dfrac{1}{\sqrt{1 - \dfrac{1}{4}(x - 1)^2}}"
        mfip = MathTex(fip).next_to(sep_line, 2 * DOWN)
        self.play(
            ReplacementTransform(fgroup, mfi),
            Write(mfip)
        )
        self.wait(2)

        fip2 = r"f_i'(x) = (-1)^{i+1}"
        fip2 += r"\dfrac{x - 1}{4\sqrt{1 - \dfrac{1}{4}(x - 1)^2}}"
        mfip2 = MathTex(fip2).next_to(sep_line, 2 * DOWN)
        self.play(
            ReplacementTransform(mfip, mfip2),
            FadeOut(sep_line),
            mfip2.animate.next_to(mfi, 2 * DOWN)
        )
        self.wait(2)

        rem1 = Text(
            "La tangente est parallèle à l'axe des abscisses si \n"
            "et seulement si la dérivée s'annule.",
            color = WHITE,
        )

        b1 = SurroundingRectangle(rem1, color=BLUE, buff=0.2)

        mobj1 = VGroup(b1, rem1).next_to(mfip2, 2 * DOWN)
        self.play(Write(mobj1))
        self.wait(3)

        fip0 = r"f_i'(x) = 0\iff x = 1"
        mfip0 = MathTex(fip0).next_to(mfip2, 2 * DOWN)
        self.play(
            ReplacementTransform(mobj1, mfip0)
        )
        self.wait(2)

        sol = r"\Rightarrow (1 ; f_i(1))\in\{(1 ; -3) ; (1 ; -1)\}"
        msol = MathTex(sol).next_to(mfip0, DOWN)
        self.play(
            Write(msol)
        )
        self.wait(2)

        all_terms = Group(msol, mfip0, mfip2, mfi)
        final = r"S = \{(1 ; -3) ; (1 ; -1)\}"
        mfinal = MathTex(final)
        bfinal = SurroundingRectangle(mfinal, color=GREEN)
        mobjfinal = VGroup(bfinal, mfinal).next_to(solution1, 2 * DOWN)

        self.play(
            ReplacementTransform(all_terms, mobjfinal)
        )
        self.wait(4)

        axes = Axes(
            x_range = [-1, 3, 0.5],
            y_range = [-4, 1, 0.5],
            x_length = 8,
            axis_config = {"color": WHITE},
            # x_axis_config = {
            #     "numbers_to_include": {-1, 1, 3},
            # },
            # y_axis_config = {
            #     "numbers_to_include": {-1, -3},
            # },
            tips = False,
        )
        #axes_labels = axes.get_axis_labels()
        f1 = axes.plot(
            lambda x: -2 - np.sqrt(1 - 0.25*(x - 1)**2),
            x_range = [-1, 3],
            color=RED
        )

        tangent_f1 = axes.plot(
            lambda x: -3,
            x_range = [-1, 3],
            color=RED
        )
        
        f2 = axes.plot(
            lambda x: -2 + np.sqrt(1 - 0.25*(x - 1)**2),
            x_range = [-1, 3],
            color=GREEN
        )

        tangent_f2 = axes.plot(
            lambda x: -1,
            x_range = [-1, 3],
            color=GREEN
        )
        
        f1_label = axes.get_graph_label(
            f1,
            r"f_1(x) = -2 - \sqrt{1 - \dfrac{1}{4}(x - 1)^2}",
            x_val = 3,
            direction = 8 * DOWN + 2 * RIGHT
        )

        
        
        f2_label = axes.get_graph_label(
            f2,
            r"f_2(x) = -2 + \sqrt{1 - \dfrac{1}{4}(x - 1)^2}",
            x_val = 3,
            direction = 4 * UP + 2 * RIGHT
        )

        ax = axes.add_coordinates()
        
        M_1 = Dot(ax.coords_to_point(1, -3), color=RED)
        lines_1 = ax.get_lines_to_point(ax.c2p(1, -3))
                                        
        M_2 = Dot(ax.coords_to_point(1, -1), color=GREEN)
        lines_2 = ax.get_lines_to_point(ax.c2p(1, -1))
        # M_1 = Dot((1, -3, 0), color=RED)
        # M_2 = Dot((1, -1, 0), color=GREEN)
                                        
        plot = VGroup(
            axes,
            f1, f2,
            M_1, M_2,
            lines_1, lines_2,
            tangent_f1, tangent_f2
        ).scale(0.75)
        labels = VGroup(f1_label, f2_label)
        self.play(
            Write(plot.next_to(mobjfinal, DOWN)),
            Write(labels),
        )
        self.wait(5)
        
        disp_sub(self, lang="fr")
        
class SectionAQuestion8(Scene):
    def construct(self):
        msg1 = "Intégration par parties"
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
        
        question1 = Title("Question 8")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait(3)
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Utiliser une intégration par parties "
        phrases = [phrase1]

        phrase2 = r"pour trouver les valeurs rationnelles de "
        phrases += [phrase2]

        phrase3 = r"\(a\) et \(b\) tels que "
        phrases += [phrase3]

        phrase4 = r"\[\int_1^9\sqrt{x}\ln(x)dx = a\ln(3) + b\]"
        phrases += [phrase4]
                
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait(3)
        self.wait(3)

        solution1 = Title("Solution 8")

        int1 = r"I = \int_1^9\sqrt{x}\ln(x)dx = a\ln(3) + b"
        mint1 = MathTex(int1).next_to(solution1, 2 * DOWN)
        
        u = r"u'(x) = \sqrt{x} = x^{\frac{1}{2}}\Rightarrow u(x) = "
        u += r"\dfrac{2}{3}x^{\frac{3}{2}}"
        mu = MathTex(u).next_to(mint1, DOWN)
        
        v = r"v(x) = \ln(x)\Rightarrow v'(x) = \dfrac{1}{x}"
        mv = MathTex(v).next_to(mu, DOWN)

        int2 = r"I = \left[u(x)v(x)\right]_1^9 "
        int2 += r"- \int_1^9u(x)v'(x)dx"
        mint2 = MathTex(int2).next_to(mv, DOWN)
    
            
        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
            Write(mint1),
            Write(mu),
            Write(mv),
            Write(mint2),
        )
        self.wait(4)


        int3 = r"I = \left[\dfrac{2}{3}x^{\frac{3}{2}}\ln(x)\right]_1^9 "
        int3 += r"- \int_1^9\dfrac{2}{3}x^{\frac{3}{2}}\dfrac{1}{x}dx"
        mint3 = MathTex(int3).next_to(mint1, DOWN)

        int4 = r"I = \dfrac{2}{3}\times 9^{\frac{3}{2}}\times\ln(9)"
        int4 += r"- \dfrac{2}{3}\int_1^9x^{\frac{1}{2}}dx"
        mint4 = MathTex(int4).next_to(mint3, DOWN)

        int5 = r"I = \dfrac{2}{3}\times 3^{3}\times 2\ln(3)"
        int5 += r"- \dfrac{2}{3}\left[\dfrac{2}{3}x^{\frac{3}{2}}\right]_1^9"
        mint5 = MathTex(int5).next_to(mint4, DOWN)

        self.play(
            ReplacementTransform(mu, mint3),
            ReplacementTransform(mv, mint4),
            ReplacementTransform(mint2, mint5),
        )
        self.wait(3)

        int6 = r"I = 2^2\times 3^{2}\ln(3) - "
        int6 += r"\left(\dfrac{2}{3}\right)^2(9^{\frac{3}{2}} - 1)"
        mint6 = MathTex(int6).next_to(mint1, DOWN)

        int7 = r"I = 36\ln(3) - "
        int7 += r"\dfrac{4}{9}(3^3 - 1)"
        mint7 = MathTex(int7).next_to(mint6, DOWN)

        int8 = r"I = 36\ln(3) - \dfrac{104}{9}"
        mint8 = MathTex(int8).next_to(mint7, DOWN)

        self.play(
            ReplacementTransform(mint3, mint6),
            ReplacementTransform(mint4, mint7),
            ReplacementTransform(mint5, mint8),
        )
        self.wait(3)

        all_terms = Group(
            mint8, mint7, mint6, mint5,
            mint4, mint3, mint2, mint1, 
        )

        final_res = MathTex(
            r"\int_1^9\sqrt{x}\ln(x)dx = 36\ln(3) - \dfrac{104}{9}"
        )
        final_box = SurroundingRectangle(final_res)
        final_mobj = VGroup(final_res, final_box).next_to(solution1, 2 * DOWN)

        self.play(
            ReplacementTransform(all_terms, final_mobj)
        )
        self.wait(3)
        
        disp_sub(self, lang="fr")


class SectionAQuestion9(Scene):
    def construct(self):
        msg1 = "Densité de probabilité"
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
        
        question1 = Title("Question 9")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title1, question1)
        )
        self.wait(3)
        

        self.play(
            img2.animate.shift(2.5 * LEFT + 1.25 * UP).scale(0.75),
        )
        self.wait(2)
        
        phrase1 = r"Considérer la fonction \(f\) définie par "
        phrases = [phrase1]

        phrase2 = r"\[f(x) = 0,1x\mathbb{I}_{[0 ; 1]}(x) + "
        phrase2 += r"0,1(5x - 4)\mathbb{I}_{]1 ; 2]}(x) + "
        phrase2 += r"(ax + b)\mathbb{I}_{]2; c]}(x)\]"
        phrases += [phrase2]

        phrase3 = r"Avec \(\mathbb{I}_{A}(x) = 1\) si \(x\in A\) et 0 sinon. "
        phrases += [phrase3]
        
        phrase4 = r"1) Sachant que \(f\) est une fonction de densité de "
        phrases += [phrase4]

        phrase5 = r"probabilité continue d'une variable aléatoire \(X\), "
        phrases += [phrase5]
        
        phrase6 = r"trouver les valeurs de \(a, b\) et \(c\)."
        phrases += [phrase6]

        phrase7 = r"2) Ainsi déterminer la valeur du mode de \(X\)."
        phrases += [phrase7]
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = title1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait(3)
        self.wait(3)

        solution1 = Title("Solution 9.1")

        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
        )
        self.wait()
        
        phrase1 = r"La fonction \(f\) est affine par morceaux."
        phrases = [phrase1]

        phrase2 = r"Donc par Chasles on peut calculer son intégrale"
        phrases += [phrase2]

        phrase3 = r"sur chaque intervalle et sommer pour obtenir 1."
        phrases += [phrase3]
        
        
        phr_tex = [Tex(p) for p in phrases]
        for i, pt in enumerate(phr_tex):
            if i == 0: ref, pos = solution1, DOWN
            else: ref, pos = phr_tex[i - 1], DOWN
            self.play(Write(pt.next_to(ref, pos)))
            self.wait(3)
        self.wait(3)


        self.play(
            ReplacementTransform(question1, solution1),
            *[FadeOut(*phr_tex)],
        )
        self.wait()

        int1 = r"\int_0^10,1xdx = 0,1\left[\dfrac{x^2}{2}\right]_0^1"
        mint1 = MathTex(int1).next_to(solution1, 2 * DOWN)

        int12 = r"\int_0^10,1xdx = 0,1\times \dfrac{1}{2}"
        mint12 = MathTex(int12).next_to(mint1, DOWN)

        int13 = r"\int_0^10,1xdx = 0,05"
        mint13 = MathTex(int13).next_to(mint12, DOWN)

        self.play(
            Write(mint1),
            Write(mint12),
            Write(mint13)
        )
        self.wait(3)

        self.play(
            FadeOut(mint12),
            ReplacementTransform(mint1, mint13.next_to(solution1, 2 * DOWN)),
        )
        self.wait(2)

        int2 = r"\int_1^20,1(5x - 4)dx = "
        int2 += r"0,1\left[5\dfrac{x^2}{2} - 4x\right]_1^2"
        mint2 = MathTex(int2).next_to(mint13, DOWN)

        int22 = r"\int_1^20,1(5x - 4)dx = "
        int22 += r"0,1\times (10 - 8 - \dfrac{5}{2} + 4)"
        mint22 = MathTex(int22).next_to(mint2, DOWN)

        int23 = r"\int_1^20,1(5x - 4)dx = 0,35"
        mint23 = MathTex(int23).next_to(mint22, DOWN)

        self.play(
            Write(mint2),
            Write(mint22),
            Write(mint23),
            mint13.animate.shift(4 * LEFT + 0.25 * UP)
        )
        self.wait(4)

        self.play(
            FadeOut(mint22),
            ReplacementTransform(mint2, mint23.next_to(mint13, RIGHT)),
        )
        self.wait(2)

        int3 = r"\int_2^c(ax + b)dx = "
        int3 += r"\left[a\dfrac{x^2}{2} + bx\right]_2^c"
        mint3 = MathTex(int3).next_to(mint23, DOWN)

        int32 = r"\int_2^c(ax + b)dx = "
        int32 += r"\left(\dfrac{ac^2}{2} + bc - 2a - 2b\right)"
        mint32 = MathTex(int32).next_to(mint3, DOWN)

        int33 = r"\int_2^c(ax + b)dx = a\dfrac{(c^2 - 4)}{2} + b(c - 2)"
        mint33 = MathTex(int33).next_to(mint32, DOWN)

        self.play(
            Write(mint3),
            Write(mint32),
            Write(mint33),
        )
        self.wait(4)

        int34 = r"\int_2^c(ax + b)dx = (c - 2)"
        int34 += r"\left(\dfrac{a(c + 2)}{2} + b\right)"
        mint34 = MathTex(int34).next_to(mint23, DOWN)

        intf = r"\int_{\mathbb{R}}f(x)dx = 1\iff "
        intf += r"\int_2^c(ax + b)dx + \int_1^20,1(5x - 4)dx + "
        intf += r"\int_0^10,1xdx = 1"
        mintf = MathTex(intf).next_to(mint34, DOWN).scale(0.75)

        intf2 = r"\int_{\mathbb{R}}f(x)dx = 1\iff "
        intf2 += r"(c - 2)\left(\dfrac{a(c + 2)}{2} + b\right) + "
        intf2 += r"0,35 + 0,05 = 1"
        mintf2 = MathTex(intf2).next_to(mintf, DOWN).scale(0.85)

        self.play(
            FadeOut(mint13, mint23),
            ReplacementTransform(mint3, mint34),
            ReplacementTransform(mint32, mintf),
            ReplacementTransform(mint33, mintf2),
        )
        self.wait(4)

        intf3 = r"\int_{\mathbb{R}}f(x)dx = 1\iff "
        intf3 += r"(c - 2)\left(\dfrac{a(c + 2)}{2} + b\right) + "
        intf3 += r"0,4 = 1"
        mintf3 = MathTex(intf3).next_to(solution1, 2 * DOWN)

        intf4 = r"\int_{\mathbb{R}}f(x)dx = 1\iff "
        intf4 += r"(c - 2)\left(\dfrac{a(c + 2)}{2} + b\right) = 0.6"
        mintf4 = MathTex(intf4).next_to(mintf3, DOWN)

        c0 = r"Par continuité il faut que "
        c0 += r"\(f(2) = \lim_{x\to 2^{+}}f(x)\)"
        c0_tex = Tex(c0).next_to(mintf4, DOWN)

        c1 = r"Et que \(f(c) = \lim_{x\to c^{+}}f(x) = 0\)"
        c1_tex = Tex(c1).next_to(c0_tex, DOWN)
        
        self.play(
            ReplacementTransform(mint34, mintf3),
            ReplacementTransform(mintf, mintf4),
            ReplacementTransform(mintf2, c0_tex),
            Write(c1_tex)
        )
        self.wait(4)

        eq1 = r"2a + b = 0,6\quad (E_1)"
        meq1 = MathTex(eq1).next_to(solution1, 2 * DOWN)
        eq2 = r"(c - 2)\left(\dfrac{a(c + 2)}{2} + b\right) = 0.6\quad (E_2)"
        meq2 = MathTex(eq2).next_to(meq1, DOWN)
        eq3 = "ac + b = 0\quad (E_3)"
        meq3 = MathTex(eq3).next_to(meq2, DOWN)
        
        self.play(
            FadeOut(mintf3),
            ReplacementTransform(mintf4, meq1),
            ReplacementTransform(c0_tex, meq2),
            ReplacementTransform(c1_tex, meq3),
        )
        self.wait(4)

        A = Dot().next_to(meq3[0], DOWN + 5 * LEFT)
        B = Dot().next_to(meq3[-1], DOWN + 5 * RIGHT)
        sep_line = Line(A, B)
        self.play(Write(sep_line))
        self.wait(2)

        eq12 = r"b = 0,6 - 2a\quad (E_{12})"
        meq12 = MathTex(eq12).next_to(sep_line, DOWN)

        eq22 = r"(c - 2)\left(\dfrac{a(c + 2)}{2} + 0,6 - 2a\right) = "
        eq22 += r"0.6\quad (E_{22})"
        meq22 = MathTex(eq22).next_to(meq12, DOWN)

        eq32 = r"ac + 0,6 - 2a = 0\quad (E_{32})"
        meq32 = MathTex(eq32).next_to(meq22, DOWN)

        self.play(
            Write(meq12),
            Write(meq22),
            Write(meq32),
        )
        self.wait(3)


        eq23 = r"(c - 2)\left(\dfrac{a(c - 2)}{2} + 0,6\right) = "
        eq23 += r"0,6\quad (E_{23})"
        meq23 = MathTex(eq23).next_to(sep_line, DOWN)

        eq33 = r"a(c - 2) = -0,6\quad (E_{33})"
        meq33 = MathTex(eq33).next_to(meq23, DOWN)

        self.play(
            FadeOut(meq12),
            ReplacementTransform(meq22, meq23),
            ReplacementTransform(meq32, meq33),
        )
        self.wait(3)

        eq24 = r"(c - 2)(-0,3 + 0,6) = "
        eq24 += r"0.6\quad (E_{24})"
        meq24 = MathTex(eq24).next_to(sep_line, DOWN)

        eq25 = r"(c - 2)\times 0,3 = 0,6\quad (E_{25})"
        meq25 = MathTex(eq25).next_to(meq24, DOWN)

        self.play(
            ReplacementTransform(meq23, meq24),
            ReplacementTransform(meq33, meq25),
        )
        self.wait(2)

        eq26 = r"(c - 2) = 2\quad (E_{26})"
        meq26 = MathTex(eq26).next_to(sep_line, DOWN)

        eq27 = r"c = 4\quad (E_{27})"
        meq27 = MathTex(eq27).next_to(meq26, DOWN)

        self.play(
            ReplacementTransform(meq24, meq26),
            ReplacementTransform(meq25, meq27),
        )
        self.wait(2)

        eq34 = r"b = -4a = 0,6 - 2a\quad (E_{34})"
        meq34 = MathTex(eq34).next_to(sep_line, DOWN)

        eq35 = r"2a = -0,6\quad (E_{35})"
        meq35 = MathTex(eq35).next_to(meq34, DOWN)

        eq36 = r"a = -0,3\quad (E_{36})"
        meq36 = MathTex(eq36).next_to(meq35, DOWN)

        self.play(
            ReplacementTransform(meq2, meq27.next_to(meq1, DOWN)),
            ReplacementTransform(meq26, meq34),
            Write(meq35),
            Write(meq36),
        )
        self.wait(4)

        eq13 = r"b = 0,6 + 2\times 0,3\quad (E_{13})"
        meq13 = MathTex(eq13).next_to(sep_line, DOWN)

        eq14 = r"b = 1,2\quad (E_{14})"
        meq14 = MathTex(eq14).next_to(meq13, DOWN)

        self.play(
            ReplacementTransform(meq3, meq36.next_to(meq27, DOWN)),
            ReplacementTransform(meq34, meq13),
            ReplacementTransform(meq35, meq14),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(meq1, meq14.next_to(solution1, 2 * DOWN)),
            FadeOut(meq13, sep_line)
        )
        self.wait()

        all_terms = Group(meq14, meq27, meq36)
        
        sol = r"(a, b, c) = "
        sol += r"\left(-\dfrac{3}{10} ; \dfrac{6}{5} ;  4\right)"
        msol = MathTex(sol)
        bsol = SurroundingRectangle(msol)
        mobj_sol = VGroup(bsol, msol).next_to(solution1, 1.5 * DOWN)

        self.play(
            ReplacementTransform(all_terms, mobj_sol)
        )
        self.wait(4)

        axes = Axes(
            x_range = [0, 4, 0.5],
            y_range = [0, 0.625, 0.125],
            x_length = 10,
            axis_config = {"color": GREEN},
            x_axis_config = {
                "numbers_to_include": np.arange(0, 4, 1),
            },
            y_axis_config = {
                "numbers_to_include": np.arange(0, 0.6, 0.1),
            },
            tips = False,
        )
        #axes_labels = axes.get_axis_labels()
        f1 = axes.plot(
            lambda x: 0.1 * x,
            x_range = [0, 1],
            color=BLUE
        )

        
        f2 = axes.plot(
            lambda x: 0.1 * (5 * x - 4),
            x_range = [1, 2],
            color=WHITE
        )
        

        f3 = axes.plot(
            lambda x: -0.3 * x + 1.2,
            x_range = [2, 4],
            color=RED
        )
        
        f1_label = axes.get_graph_label(
            f1,
            r"f_1(x) = 0,1x\mathbb{I}_{[0, 1]}(x)",
            x_val = 0,
            direction = DOWN + 1.5 * LEFT
        ).scale(0.75)

        
        
        f2_label = axes.get_graph_label(
            f2,
            r"f_2(x) = 0,1(5x - 4)\mathbb{I}_{]1, 2]}(x)",
            x_val = 2,
            direction = 6 * DOWN
        ).scale(0.75)
        

        f3_label = axes.get_graph_label(
            f3,
            r"f_3(x) = (-0,3x + 1,2)\mathbb{I}_{]2, 4]}(x)",
            x_val = 4,
            direction = 0.5 * UP + 12 * RIGHT
        ).scale(0.75)

        ax = axes.add_coordinates()

        M_0 = Dot(ax.coords_to_point(0, 0), color=BLUE)
        
        M_1 = Dot(ax.coords_to_point(1, 0.1), color=BLUE)
        lines_1 = ax.get_lines_to_point(ax.c2p(1, 0.1))
                                        
        M_2 = Dot(ax.coords_to_point(2, 0.6), color=BLUE)
        lines_2 = ax.get_lines_to_point(ax.c2p(2, 0.6))

        M_3 = Dot(ax.coords_to_point(4, 0), color=BLUE)
                                        
        plot = VGroup(
            axes,
            f1, f2, f3,
            M_0, M_1, M_2, M_3,
            lines_1, lines_2,
        ).scale(0.65)
        labels = VGroup(f1_label, f2_label, f3_label)
        self.play(
            mobj_sol.animate.scale(0.65).shift(0.35 * UP),
            Write(plot.next_to(mobj_sol, DOWN)),
            Write(labels),
        )
        self.wait(5)
        
        disp_sub(self, lang="fr")

        
