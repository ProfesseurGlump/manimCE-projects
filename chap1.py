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



class ExamStyleQuestion1(Scene):
    def construct(self):
        msg = "Suites arithmétiques"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
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
        
        question = Title("Question")
        self.play(
            ReplacementTransform(img1, img2.to_edge(2.5 * UP)),
            ReplacementTransform(title_start, question)
        )
        self.wait(4)
        

        q1 = Text(
            "Le quatrième terme d'une suite arithmétique est 8.\n"
            "La somme de ses cinq premiers termes vaut 25.\n"
            "Trouver les cinq premiers termes.",
            color = WHITE,
        )

        b1 = SurroundingRectangle(q1, color=BLUE, buff=0.2)

        mobj1 = VGroup(b1, q1)

        self.play(
            img2.animate.shift(4.75 * LEFT + 0.5 * UP).scale(2),
            Write(mobj1)
        )
        self.wait(3)

        solution = Title("Solution")
        
        p1 = MathTex(r"u_3 = 8")
        p2 = MathTex(r"\sum_{k = 0}^4u_k = 25")

        self.play(
            ReplacementTransform(question, solution),
            Write(p1.next_to(mobj1, DOWN))
        )
        self.wait(3)
        
        self.play(Write(p2.next_to(p1, DOWN)))
        self.wait(3)

        p11 = MathTex(r"u_0 + 3r = 8")
        p21 = MathTex(
            r"u_0 + (u_0 + r) + (u_0 + 2r) + (u_0 + 3r) + (u_0 + 4r) = 25"
        )

        self.play(
            ReplacementTransform(p1, p11.next_to(mobj1, DOWN)),
            ReplacementTransform(p2, p21.next_to(p1, DOWN)),
        )
        self.wait(3)

        p22 = MathTex(
            r"5u_0 + (1 + 2 + 3 + 4)r = 25"
        )

        self.play(
            ReplacementTransform(p21, p22.next_to(p1, DOWN)),
        )
        self.wait(3)

        p23 = MathTex(
            r"5u_0 + 10r = 25"
        )

        self.play(
            ReplacementTransform(p22, p23.next_to(p1, DOWN)),
        )
        self.wait(3)

        p24 = MathTex(
            r"u_0 + 2r = 5"
        )

        self.play(
            ReplacementTransform(p23, p24.next_to(p1, DOWN)),
        )
        self.wait(3)

        A = Dot().next_to(p24[0], 0.5 * DOWN + LEFT)
        B = Dot().next_to(p24[-1], 0.5 * DOWN + RIGHT)
        sep_line = Line(A, B)
        self.play(Write(sep_line))
        self.wait(3)

        diff = MathTex(r"(u_0 + 3r) - (u_0 + 2r) = 8 - 5")
        self.play(Write(diff.next_to(sep_line, 0.5 * DOWN)))
        self.wait(3)

        diff2 = MathTex(r"u_0 + 3r - u_0 - 2r = 3")
        self.play(
            ReplacementTransform(
                diff,
                diff2.next_to(sep_line, 0.5 * DOWN)
            )
        )
        self.wait(3)

        diff3 = MathTex(r"r = 3")
        self.play(
            ReplacementTransform(
                diff2,
                diff3.next_to(sep_line, 0.5 * DOWN)
            )
        )
        self.wait(3)

        p12 = MathTex(r"u_0 + 3\times 3 = 8")
        p25 = MathTex(
            r"u_0 + 2\times 3 = 5"
        )

        self.play(
            ReplacementTransform(p11, p12.next_to(mobj1, DOWN)),
            ReplacementTransform(p24, p25.next_to(p1, DOWN)),
        )
        self.wait(3)

        p13 = MathTex(r"u_0 + 9 = 8")
        p26 = MathTex(
            r"u_0 + 6 = 5"
        )

        self.play(
            ReplacementTransform(p12, p13.next_to(mobj1, DOWN)),
            ReplacementTransform(p25, p26.next_to(p1, DOWN)),
        )
        self.wait(3)

        p14 = MathTex(r"u_0 = 8 - 9")
        p27 = MathTex(r"u_0 = 5 - 6")

        self.play(
            ReplacementTransform(p13, p14.next_to(mobj1, DOWN)),
            ReplacementTransform(p26, p27.next_to(p1, DOWN)),
        )
        self.wait(3)

        p15 = MathTex(r"u_0 = - 1")
        p28 = MathTex(r"\Rightarrow u_1 = -1 + 3")
        p3 = MathTex(r"\Rightarrow u_2 = -1 + 2\times 3")
        p4 = MathTex(r"\Rightarrow u_3 = -1 + 3\times 3")
        p5 = MathTex(r"\Rightarrow u_4 = -1 + 4\times 3")
        
        self.play(
            ReplacementTransform(p14, p15.next_to(mobj1, DOWN)),
        )
        self.wait(3)

        self.play(
            p15.animate.shift(5.5 * LEFT),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(p27, p28.next_to(p15, RIGHT)),
            ReplacementTransform(sep_line, p3.next_to(p28, RIGHT)),
            Write(p4.next_to(p28, DOWN)),
            ReplacementTransform(diff3, p5.next_to(p4, RIGHT)),
        )

        self.wait(3)

        all_terms = Group(p15, p28, p3, p4, p5)
        final = MathTex(r"(u_0, u_1, u_2, u_3, u_4) = (-1, 2, 5, 8, 11)")
        self.play(
            ReplacementTransform(all_terms, final.next_to(mobj1, 2 * DOWN))
        )
        self.wait(3)

        box = SurroundingRectangle(final)
        self.play(
            FadeOut(img2),
            mobj1.animate.shift(1.75 * UP),
            Write(box)
        )
        self.wait(3)

        disp_sub(self, lang="fr")
