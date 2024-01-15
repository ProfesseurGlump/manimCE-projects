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

# def targets_to_write(text, ref, size=1, direction=DOWN):
#     text = [Text(t) for t in text if isinstance(t, str)]
#     for i in range(len(text)):
#         p = text[i]
#         if isinstance(p.text, str) and "10^" in p.text:
#             p.text = p.text.replace(r"10^" + f"{i}", r"10^{\{i\}}")
#     n = len(text)

#     targets = [text[0].next_to(ref, size * direction)]
#     targets += [
#         text[i].next_to(
#             text[i - 1],
#             size * direction
#         ) for i in range(1, n)
#     ]
#     return text


###################################################
##########            PART 1             ##########
##################################################

class Part1Scene1Differences(Scene):
    def construct(self):
        msg = "Connaissez-vous la magie de 2024 ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.65))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        A = MathTex(
            r"2024 =",
            r"2\times 1000",
            r" + ",
            r"0\times 100",
            r" + ",
            r"2\times 10",
            r" + ",
            r"4"
        )
        self.play(Write(A.scale(0.65).next_to(title_start, DOWN)))
        self.wait(4)

        txt1 = Text("Mais quelle est la différence avec 202,4 ?")
        self.play(Write(txt1.scale(0.5).next_to(A, DOWN)))
        self.wait(2)

        txt2 = Text("Après tout 2024 mL = 202,4 cL")
        self.play(Write(txt2.scale(0.5).next_to(txt1, DOWN)))
        self.wait(2)

        A2 = MathTex(
            r"202,4 =",
            r"2\times 100",
            r" + ",
            r"0\times 10",
            r" + ",
            r"2",
            r" + ",
            r"4\times\dfrac{1}{10}"
        )
        self.play(Write(A2.scale(0.65).next_to(txt2, DOWN)))
        self.wait(4)

        txt3 = Text("Mais quelle est la différence avec 20,24 ?")
        self.play(Write(txt3.scale(0.5).next_to(A2, DOWN)))
        self.wait(2)

        txt4 = Text("Après tout 202,4 cL = 20,24 dL")
        self.play(Write(txt4.scale(0.5).next_to(txt3, DOWN)))
        self.wait(2)

        A3 = MathTex(
            r"20,24 =",
            r"2\times 10",
            r" + ",
            r"0",
            r" + ",
            r"2\times\dfrac{1}{10}",
            r" + ",
            r"4\times\dfrac{1}{100}"
        )
        self.play(Write(A3.scale(0.65).next_to(txt4, DOWN)))
        self.wait(4)

        txt5 = Text("Mais quelle est la différence avec 2,024 ?")
        self.play(Write(txt5.scale(0.5).next_to(A3, DOWN)))
        self.wait(2)

        txt6 = Text("Après tout 20,24 dL = 2,024 L")
        self.play(Write(txt6.scale(0.5).next_to(txt5, DOWN)))
        self.wait(2)

        A4 = MathTex(
            r"2,024 =",
            r"2",
            r" + ",
            r"0\times\dfrac{1}{10}",
            r" + ",
            r"2\times\dfrac{1}{100}",
            r" + ",
            r"4\times\dfrac{1}{1000}"
        )
        self.play(Write(A4.scale(0.65).next_to(txt6, DOWN)))
        self.wait(4)


class Part1Scene2QuantitativelyVisually(Scene):
    def construct(self):
        msg = "Quantitativement ou visuellement ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.65))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        p = "Ces 4 nombres sont totalement différents "
        p += "quantitativement. "
        phrase = [p]
        p = "En effet, à chaque descente "
        p += "on a divisé par 10. "
        phrase += [p]
        p = "Ainsi le 4ème est mille fois "
        p += "moindre que le 1er. "
        phrase += [p]
        p = "Néanmoins, visuellement, "
        p += "si on oublie la virgule, "
        p += "on dirait les mêmes... "
        phrase += [p]
        p = "Précisément parce qu'ils utilisent "
        p += "les mêmes chiffres dans le même ordre."
        phrase += [p]
        p = "Les chiffres sont en quelque sorte les lettres "
        p += "disponibles dans un alphabet..."
        phrase += [p]
        p = "... un alphabet particulier à 10 symboles."
        phrase += [p]
        p = "C'est ce qu'on appelle système positionnel décimal."
        phrase += [p]
        p = "Parce que la position compte énormément..."
        phrase += [p]

        targets = targets_to_write(
            phrase,
            title_start,
            size=0.5
        )
        for t in targets:
            self.play(Write(t.scale(0.5)))
            self.wait(3)
        


class Part1Scene3NumbersAndWords(Scene):
    def construct(self):
        msg = "Si chiffre = lettre alors nombre = mot ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.65))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        p = "On a vu précédemment qu'on pouvait interpréter "
        p += "les chiffres comme des lettres. "
        phrase = [p]
        p = "On peut donc logiquement se dire que les nombres "
        p += "seraient alors des mots. "
        phrase += [p]
        p = "Pour les nombres entiers il y a juste une contrainte "
        p += "particulière. "
        phrase += [p]
        p = "Un nombre entier ne peut pas commencer par zéro."
        phrase += [p]
        p = "Précisément parce que le chiffre zéro désigne "
        p += "l'absence de quantité."
        phrase += [p]
        p = "Pour mieux comprendre cette subtilité nous allons "
        p += "observer attentivement..."
        phrase += [p]
        p = "... ce qu'il se passe lorsqu'on multiplie par 10 "
        p += "plusieurs fois."
        phrase += [p]
        p = "C'est ce qu'on appelle les puissances de 10."
        phrase += [p]
        p = "Ou encore les exponentiations en base 10."
        phrase += [p]

        targets = targets_to_write(
            phrase,
            title_start,
            size=0.5
        )
        for t in targets:
            self.play(Write(t.scale(0.5)))
            self.wait(3)
        
            
        
            
class Part1Scene4TenTable(Scene):
    def construct(self):
        msg = "Connaissez-vous la table de 10 ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))


        ten_table = [r"10\times " + f"{i} = {10*i}" for i in range(1, 10)]
        A = [MathTex(tt) for tt in ten_table]
        targets = targets_to_write(
            A,
            title_start
        )
        for t in targets:
            self.play(Write(t.scale(1)))
            self.wait(0.25)




class Part1Scene5SideEffects(Scene):
    def construct(self):
        msg = "Effets des multiplications par 10"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        p = "La multiplication d'un nombre entier par 10 "
        phrase = [p]

        p = "a pour effet d'ajouter un 0 à droite. "
        phrase += [p]

        p = "Mais que se passe-t-il si on multiplie 10 par 10 ?"
        phrase += [p]

        p = "On multiplie par 100 et donc "
        p += "on ajoute deux 0 à droite."
        phrase += [p]

        p = "Mais que se passe-t-il si on multiplie 100 par 10 ?"
        phrase += [p]

        p = "Ça revient à faire 10 fois 10 fois 10..."
        phrase += [p]
        
        p = "Donc on multiplie par 1000 et alors "
        p += "on ajoute trois 0 à droite."
        phrase += [p]

        p = "Vous devinez la suite ? "
        p += "Écrivez-la en commentaire."
        phrase += [p]
        
        targets = targets_to_write(
            phrase,
            title_start,
            size=0.5
        )
        for t in targets:
            self.play(Write(t.scale(0.65)))
            self.wait(3)

class Part1Scene6Powers(Scene):
    def construct(self):
        msg = "Puissances de 10"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.75))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        phrase = []
        for i in range(10):
            p = r"Dans " + f"{10**i} il y a {i} zéro"
            q = "s" if i > 1 else ""
            p += q
            p += " donc on écrit "
            p += r"\(10^{"
            p += f"{i}"
            p += r"} = 1\)"
            q = i * "0"
            p += q
            
            phrase += [p]

        powers = [Tex(p) for p in phrase]
        targets = targets_to_write(
            powers,
            title_start,
            size=0.25
        )
        for t in targets:
            self.play(Write(t.scale(0.75)))
            self.wait(2)


class Part1Scene7PositionnalBasicSystem(Scene):
    def construct(self):
        msg = "Le système positionnel décimal (ou la base 10)"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.85))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        A = MathTex(
            r"2024 =",
            r"4\times 10^0",
            r" + ",
            r"2\times 10^1",
            r" + ",
            r"0\times 10^2",
            r" + ",
            r"2\times 10^3"
        )
        self.play(Write(A.scale(0.85).next_to(title_start, DOWN)))
        self.wait(4)

        txt1 = Tex("Mais comment faire pour 202,4 ?")
        self.play(Write(txt1.scale(0.75).next_to(A, DOWN)))
        self.wait(2)

        txt2 = Tex("Et avec 20,24 ?")
        self.play(Write(txt2.scale(0.75).next_to(txt1, DOWN)))
        self.wait(2)

        txt3 = Tex("Et pour 2,024 ?")
        self.play(Write(txt3.scale(0.75).next_to(txt2, DOWN)))
        self.wait(2)

        txt4 = Tex("Le problème consiste à écrire les inverses.")
        self.play(Write(txt4.scale(0.75).next_to(txt3, DOWN)))
        self.wait(2)

        t = r"Par combien faut-il multiplier "
        t += r"\(\dfrac{1}{10}\) pour obtenir 1 ?"
        txt5 = Tex(t)
        self.play(Write(txt5.scale(0.75).next_to(txt4, DOWN)))
        self.wait(2)

        t = r"Par combien faut-il multiplier \(\dfrac{1}{10^2}\) "
        t += r"pour obtenir 1 ?"
        txt6 = Tex(t)
        self.play(Write(txt6.scale(0.75).next_to(txt5, DOWN)))
        self.wait(2)

        t = r"Par combien faut-il multiplier \(\dfrac{1}{10^3}\) "
        t += r"pour obtenir 1 ?"
        txt7 = Tex(t)
        self.play(Write(txt7.scale(0.75).next_to(txt6, DOWN)))
        self.wait(2)

        t = "Écrivez vos réponses en commentaire."
        txt8 = Text(t)
        self.play(Write(txt8.scale(0.5).next_to(txt7, DOWN)))
        self.wait(2)



class Part1Scene8EndOfPart1(Scene):
    def construct(self):
        msg = "La suite au prochain épisode"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.85))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        p = "Il y a encore beaucoup de choses à dire..."
        phrase = [p]

        p = "Mais ça sera pour un prochain épisode."
        phrase += [p]

        p = "Dites en commentaires ce que vous pensez "
        phrase += [p]

        p = "de ce nouveau format."
        phrase += [p]

        p = "Pour les impatient(e)s vous pouvez d'ores et déjà "
        phrase += [p]

        p = "vous procurer mon livre..."
        phrase += [p]
        
        p = r"Mon livre \emph{Manipuler les (nombres) réels} "
        phrase += [p]

        p = r"que je vous offre \textsc{gratuitement} !"
        phrase += [p]

        p = "Pour ce faire il vous suffit de remplir le "
        p += "petit formulaire "
        phrase += [p]

        p = "Google forms dans la description. "
        phrase += [p]

        phrase_tex = [Tex(p) for p in phrase]
        targets = targets_to_write(
            phrase_tex,
            title_start,
            size=.95
        )
        for t in targets:
            self.play(Write(t.scale(0.85)))
            self.wait(3)


###################################################
##########            PART 2             ##########
##################################################

class Part2Scene1WhatMultiplicand(Scene):
    def construct(self):
        msg = "Décalage de la virgule vers la droite"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.85))
        self.wait(2)


        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        t = r"Par combien faut-il multiplier "
        t += r"\(\dfrac{1}{10^1}\) pour obtenir 1 ?"
        txt1 = Tex(t)
        self.play(Write(txt1.scale(0.75).next_to(title_start, DOWN)))
        self.wait(2)

        t = r"Par \(10^1\) car "
        t += r"\(10^1\times\dfrac{1}{10^1} = 10\times 0,1 = 1 = 10^0\)"
        txt2 = Tex(t)
        self.play(Write(txt2.scale(0.75).next_to(txt1, DOWN)))
        self.wait(2)

        t = r"Par combien faut-il multiplier \(\dfrac{1}{10^2}\) "
        t += r"pour obtenir 1 ?"
        txt3 = Tex(t)
        self.play(Write(txt3.scale(0.75).next_to(txt2, DOWN)))
        self.wait(2)

        t = r"Par \(10^2\) car "
        t += r"\(10^2\times\dfrac{1}{10^2} = 100\times 0,01 = 1 = 10^0\)"
        txt4 = Tex(t)
        self.play(Write(txt4.scale(0.75).next_to(txt3, DOWN)))
        self.wait(2)
        
        t = r"Par combien faut-il multiplier \(\dfrac{1}{10^3}\) "
        t += r"pour obtenir 1 ?"
        txt5 = Tex(t)
        self.play(Write(txt5.scale(0.75).next_to(txt4, DOWN)))
        self.wait(2)

        t = r"Par \(10^3\) car "
        t += r"\(10^3\times\dfrac{1}{10^3} = 1000\times 0,001 = 1 = 10^0\)"
        txt6 = Tex(t)
        self.play(Write(txt6.scale(0.75).next_to(txt5, DOWN)))
        self.wait(2)

class Part2Scene1bis(Scene):
    def construct(self):
        msg = "Récapitulatif"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(0.85))
        self.wait()

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        t = r"\(10^1\times\dfrac{1}{10^1} = 10\times 0,1 = 1 = 10^0\)"
        txt1 = Tex(t)
        self.play(Write(txt1.scale(0.75).next_to(title_start, DOWN)))
        self.wait(.5)

        t = r"\(10^2\times\dfrac{1}{10^2} = 100\times 0,01 = 1 = 10^0\)"
        txt2 = Tex(t)
        self.play(Write(txt2.scale(0.75).next_to(txt1, DOWN)))
        self.wait(.5)
        
        t = r"\(10^3\times\dfrac{1}{10^3} = 1000\times 0,001 = 1 = 10^0\)"
        txt3 = Tex(t)
        self.play(Write(txt3.scale(0.75).next_to(txt2, DOWN)))
        self.wait(.5)

        
class Part2Scene2NegativePowers(Scene):
    def construct(self):
        msg = "Puissances négatives"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        t = r"Ainsi "
        t += r"\(\dfrac{1}{10^1} = 0,1 = 10^{-1}\)"
        txt1 = Tex(t)
        self.play(Write(txt1.scale(1).next_to(title_start, DOWN)))
        self.wait(2)

        t = r"Ainsi "
        t += r"\(\dfrac{1}{10^2} = 0,01 = 10^{-2}\)"
        txt2 = Tex(t)
        self.play(Write(txt2.scale(1).next_to(txt1, DOWN)))
        self.wait(2)

        t = r"Ainsi "
        t += r"\(\dfrac{1}{10^3} = 0,001 = 10^{-3}\)"
        txt3 = Tex(t)
        self.play(Write(txt3.scale(1).next_to(txt2, DOWN)))
        self.wait(2)
        
        t = "Avez-vous compris pourquoi ?"
        txt4 = Text(t)
        self.play(Write(txt4.scale(1).next_to(txt3, 2 * DOWN)))
        self.wait(2)


            
class Part2Scene3MovingNumber(Scene):
    def construct(self):
        msg = "Sont-ce les nombres ou la virgule qui bougent ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        phrase = []
        for i in range(1, 9):
            p = r"\(1\div " + f"{10**i}" + r"= 0,"
            q = (i-1) * "0"
            p += q
            p += r"1\quad 1,0" + q + r"\times " 
            p += f"{10**i}" + r"= 10"
            p += q
            p += r"\)"
            phrase += [p]

        powers = [Tex(p) for p in phrase]
        targets = targets_to_write(
            powers,
            title_start,
            size=1.5
        )
        for t in targets:
            self.play(Write(t.scale(0.75)))
            self.wait(2)



class Part2Scene4NegativePowers(Scene):
    def construct(self):
        msg = "Puissances de 10 négatives"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        phrase = []
        for i in range(1, 5):
            p = r"Dans 0,"
            q = (i-1) * "0"
            p += q
            p += f"1 il y a {i} zéro"
            q = "s" if i > 1 else ""
            p += q
            p += " à gauche du 1 donc on écrit "
            p += r"\(10^{"
            p += f"-{i}"
            p += r"} = 0,\)"
            q = (i-1) * "0"
            p += q
            p += "1"
            phrase += [p]

        powers = [Tex(p) for p in phrase]
        targets = targets_to_write(
            powers,
            title_start,
            size=2.5
        )
        for t in targets:
            self.play(Write(t.scale(0.9)))
            self.wait(2)


class Part2Scene5Differences(Scene):
    def construct(self):
        msg = "Connaissez-vous la magie de 2024 ?"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        A = MathTex(
            r"2024,000 =",
            r"0\times 10^{-3}",
            r" + ",
            r"0\times 10^{-2}",
            r" + ",
            r"0\times 10^{-1}",
            r" + ",
            r"4\times 10^0",
            r" + ",
            r"2\times 10^1",
            r" + ",
            r"0\times 10^2",
            r" + ",
            r"2\times 10^3"
        )
        self.play(Write(A.scale(0.75).next_to(title_start, 2 * DOWN)))
        self.wait(4)

        A2 = MathTex(
            r"202,400 =",
            r"0\times 10^{-3}",
            r" + ",
            r"0\times 10^{-2}",
            r" + ",
            r"4\times 10^{-1}",
            r" + ",
            r"2\times 10^0",
            r" + ",
            r"0\times 10^1",
            r" + ",
            r"2\times 10^2"
        )
        self.play(Write(A2.scale(0.75).next_to(A, 2 * DOWN)))
        self.wait(4)


        A3 = MathTex(
            r"20,240 =",
            r"0\times 10^{-3}",
            r" + ",
            r"4\times 10^{-2}",
            r" + ",
            r"2\times 10^{-1}",
            r" + ",
            r"0\times 10^0",
            r" + ",
            r"2\times 10^1"
        )
        self.play(Write(A3.scale(0.75).next_to(A2, 2 * DOWN)))
        self.wait(4)

        A4 = MathTex(
            r"2,024 =",
            r"4\times 10^{-3}",
            r" + ",
            r"2\times 10^{-2}",
            r" + ",
            r"0\times 10^{-1}",
            r" + ",
            r"2\times 10^0"
        )
        self.play(Write(A4.scale(0.75).next_to(A3, 2 * DOWN)))
        self.wait(4)
            

        D1 = MathTex(
            r"20,240 - ",
            r"2,024 = ",
            r"18,216"
        )
        self.play(Write(D1.scale(0.75).next_to(A4, 2 * DOWN)))
        self.wait(4)

        D2 = MathTex(
            r"202,400 - ",
            r"20,240 = ",
            r"182,160"
        )
        self.play(Write(D2.scale(0.75).next_to(D1, 2 * DOWN)))
        self.wait(4)

        D3 = MathTex(
            r"2024,000 - ",
            r"202,400 = ",
            r"1821,600"
        )
        self.play(Write(D3.scale(0.75).next_to(D2, 2 * DOWN)))
        self.wait(4)



###################################################
##########            PART 3             ##########
##################################################
        
class Part3Scene1Iteration(Scene):
    def construct(self):
        msg = "Ordinal ou cardinal ? Les 2 mon général !"
        title_start = Title(f"{msg}")
        self.add(title_start.scale(1))
        self.wait(2)

        youtube_long = ImageMobject(
            "/Users/dn/Documents/pics/png/youtube_logo.png",
        ).scale(0.2)
        self.play(FadeIn(youtube_long.to_edge(2.5 * UP)))

        numbers = list(range(19))
        numbersMaths = [MathTex(str(d) + ", ") for d in numbers]
        numbersMaths += [MathTex(r"\dots")]

        for i, d in enumerate(numbersMaths):
            if i == 0: ref, pos = title_start, 3 * DOWN + 1.95 * LEFT
            else: ref, pos = numbersMaths[i - 1], RIGHT
            self.play(
                Write(
                    d.next_to(ref, pos),
                    run_time=0.5
                )
            )
            self.wait(0.125)

        self.play(
            youtube_long.animate.shift(5.75 * LEFT + 0.5 * UP).scale(2)
        )
        self.wait()

        
        # digits = list(range(10))
        # for i in range(10):
        #     digits += [i + ]
        # digitsMaths = [MathTex(str(d) + "=") for d in digits]
        # for i, d in enumerate(digitsMaths):
        #     if i == 0: ref, pos = numbersMaths, 2 * DL
        #     else: ref, pos = digitsMaths[i - 1], DOWN
        #     self.play(
        #         Write(
        #             d.next_to(ref, pos),
        #             run_time=0.5
        #         )
        #     )
        #     self.wait(0.125)

        digits = [
            r"0",
            r"1 = 0 + 1",
            r"2 = 1 + 1 = 1 + 1",
            r"3 = 2 + 1 = 1 + 1 + 1",
            r"4 = 3 + 1 = 1 + 1 + 1 + 1",
            r"5 = 4 + 1 = 1 + 1 + 1 + 1 + 1",
            r"6 = 5 + 1 = 1 + 1 + 1 + 1 + 1 + 1",
            r"7 = 6 + 1 = 1 + 1 + 1 + 1 + 1 + 1 + 1",
            r"8 = 7 + 1 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1",
            r"9 = 8 + 1 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1",
        ]
        digitsMaths = [MathTex(d) for d in digits]
        for i, d in enumerate(digitsMaths):
            if i == 0:
                self.play(
                    ReplacementTransform(
                        numbersMaths[i],
                        d.next_to(title_start, 2 * DOWN)
                    )
                )
            else:
                self.play(
                    ReplacementTransform(
                        numbersMaths[i],
                        d.next_to(digitsMaths[i-1], DOWN)
                    )
                )
            self.wait()
        nd = len(digitsMaths)
        nm = len(numbersMaths)
        self.play(
            *[FadeOut(numbersMaths[i]) for i in range(nd - 1, nm)]
        )
        self.wait()
        self.play(*[FadeOut(d) for d in digitsMaths])
        self.wait()
        
        noms = [
            "zéro", "un", "deux", "trois", "quatre",
            "cinq", "six", "sept", "huit", "neuf",
            "dix", "onze", "douze", "treize", "quatorze",
            "quinze", "seize", "dix-sept", "dix-huit", "etc"
        ]
        noms_txt = [Text(nom) for nom in noms]
        for i, n in enumerate(noms_txt):
            if i == 0: ref, pos = youtube_long, DOWN
            elif i in {5, 10, 15}: ref, pos = noms_txt[5 * (i // 5 - 1)], DOWN
            else: ref, pos = noms_txt[i - 1], RIGHT
            self.play(
                Write(
                    n.next_to(ref, pos),
                    run_time=1
                )
            )
            self.wait(0.125)


        self.play(*[FadeOut(n) for n in noms_txt])
        self.wait()

        names = [
            "zero", "one", "two", "three",
            "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven",
            "twelve", "thirteen", "fourteen", "etc"
        ]
        names_txt = [Text(name) for name in names]
        for i, n in enumerate(names_txt):
            if i == 0: ref, pos = youtube_long, DOWN
            elif i in {4, 8, 12}: ref, pos = names_txt[4 * (i // 4 - 1)], DOWN
            else: ref, pos = names_txt[i - 1], RIGHT
            self.play(
                Write(
                    n.next_to(ref, pos),
                    run_time=1
                )
            )
            self.wait(0.125)

            
            
