from manim import *
import manim
from math import e, pi


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
    svg_path = "/Users/dn/Documents/pics/svg/subscribe.svg"
    jpg_png_path = "/Users/dn/Documents/pics/png/sabonner.png"
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        sub_pic = SVGMobject(svg_path)
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        sub_pic = ImageMobject(jpg_png_path)
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(3)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.wait()

    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(3)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 3))
    self.wait(3)
        
    self.play(ReplacementTransform(part, full), run_time=3)
    self.wait(3)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)

    
def disp_bell_curv_area(self, axe, curve, x_interval, qx, px, dir):
    area = axe.get_area(curve, x_range=x_interval)
    self.play(FadeIn(area))
    
    if dir == 1:
        msg = f"\Phi({qx}) = "
        msg += "\mathbb{P}(X \leqslant "
        msg += f"{qx}) = {px}"
    elif dir == 0:
        msg = "\mathbb{P}("
        msg += f"{-qx} \leqslant X "
        msg += f"\leqslant {qx}) = "
        msg += f"2\Phi({qx}) - 1 = "
        msg += f"{2*px}-1"
    elif dir == -1:
        msg = "\mathbb{P}(X \geqslant "
        msg += f"{qx}) = 1 - \Phi({qx}) = 1 - {px}"
        
    prob = MathTex(msg)
    self.play(Create(prob.scale(0.75)))
    self.wait(3)
    self.play(FadeOut(prob), FadeOut(area))

class Racine(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()

        example1 = MathTex(
            r"u_k = \sqrt{k}\\",
            r"u_{k+1} - u_{k} = \sqrt{k+1} - \sqrt{k}\\",
            r"u_{k+1} - u_{k} = \dfrac{(\sqrt{k+1} - \sqrt{k})(\sqrt{k+1} + \sqrt{k})}{\sqrt{k+1} + \sqrt{k}}\\",
            r"u_{k+1} - u_{k} = \dfrac{k+1 - k}{\sqrt{k+1} + \sqrt{k}}\\",
            r"u_{k+1} - u_{k} = \dfrac{1}{\sqrt{k+1} + \sqrt{k}}\\",
            r"S_n = \sum_{k = 0}^n\dfrac{1}{\sqrt{k+1} + \sqrt{k}} = \sqrt{n + 1}\\"
        )
        title_ex1 = Title("Exemple 1")
        self.play(ReplacementTransform(title, title_ex1))

        for i in range(len(example1)):
            if i == 2:
                self.play(
                    Write(
                        example1[i].scale(0.75).shift(0.6*LEFT)
                    )
                )
            else:
                self.play(
                    Write(example1[i].shift(0.6*LEFT)
                          )
                )
            self.wait(3)    

        self.play(FadeOut(example1))
        self.wait()

        disp_sub(self, lang='fr')


class Geom(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        title_ex2 = Title("Exemple 2")
        self.play(ReplacementTransform(title, title_ex2))

        example2 = MathTex(
            r"u_k = q^{k}\\",
            r"u_{k+1} - u_{k} = q^{k+1} - q^{k}\\",
            r"u_{k+1} - u_{k} = (q - 1)q^{k}\\",
            r"S_n = \sum_{k = 0}^n(q - 1)q^{k}\\",
            r"S_n = (q-1)\sum_{k = 0}^nq^{k} = q^{n+1} - 1\\",
            r"q \neq 1 \Rightarrow",
            r"\sum_{k = 0}^nq^{k} = \dfrac{q^{n+1} - 1}{q - 1}\\"
        )
            
            
        for i in range(len(example2)):
            self.play(Write(example2[i].shift(0.6*LEFT)))
            self.wait(3)    

        self.play(FadeOut(example2))
        self.wait()
        disp_sub(self, lang='fr')


class NpremEntiers(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        title_ex3 = Title("Exemple 3")
        self.play(ReplacementTransform(title, title_ex3))

        example3 = MathTex(
            r"u_k = k^{2}\\",
            r"u_{k+1} - u_{k} = (k+1)^{2} - k^{2}\\",
            r"u_{k+1} - u_{k} = 2k + 1\\",
            r"S_n = \sum_{k = 0}^n(2k + 1)\\",
            r"S_n = 2\sum_{k = 0}^nk + (n + 1)\\",
            r"S_n = (n + 1)^2\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{(n + 1)^2 - (n + 1)}{2}\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{n^{2} + n}{2}\\",
            r"\Rightarrow \sum_{k = 0}^nk = \dfrac{n(n + 1)}{2}\\",
        )
            
            
        for i in range(len(example3)):
            self.play(Write(example3[i].shift(0.6*LEFT+DOWN)))
            self.wait()    

        self.wait(3)
        self.play(FadeOut(example3))
        self.wait()
        disp_sub(self, lang='fr')
        

class NpremSquare(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Connaissez-vous la simplification diagonale ?")
        self.add(title.scale(0.85))
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        initial_sum = MathTex(
            "S_n = \sum_{k = 0}^n(u_{k+1} - u_{k}) = u_{n+1} - u_{0}"
        )
        self.play(Write(initial_sum.shift(5*UP+0.5*LEFT)))
        self.wait()
            
        title_ex4 = Title("Exemple 4")
        self.play(ReplacementTransform(title, title_ex4))

        example4 = MathTex(
            r"u_k = k^{3}\\",
            r"u_{k+1} - u_{k} = (k+1)^{3} - k^{3}\\",
            r"u_{k+1} - u_{k} = 3k^2 + 3k + 1\\",
            r"S_n = \sum_{k = 0}^n(3k^2 + 3k + 1)\\",
            r"S_n = 3\sum_{k = 0}^nk^2 + 3\sum_{k = 0}^nk + (n + 1)\\",
            r"S_n = (n + 1)^3\\",
            r"\sum_{k = 0}^nk = \dfrac{n(n+1)}{2}\\",
            r"\sum_{k = 0}^nk^2 = \dfrac{2(n + 1)^3 - 3n(n+1) - 2(n + 1)}{6}\\",
            r"\sum_{k = 0}^nk^2 = \dfrac{n(n + 1)(2n + 1)}{6}\\",
        )
            
            
        for i in range(len(example4)):
            if i == len(example4) - 2:
                self.play(
                    Write(
                        example4[i].scale(0.8).shift(0.6*LEFT+DOWN)
                    )
                )
            elif i == len(example4) - 1:
                self.play(
                    Write(
                        example4[i].shift(0.6*LEFT+DOWN)
                    )
                )
                result = SurroundingRectangle(example4[i])
                self.play(Write(result))
                self.wait(2)
            else:
                self.play(
                    Write(
                        example4[i].shift(0.6*LEFT+DOWN)
                    )
                )
            self.wait()    

        self.wait(4)
        self.play(FadeOut(example4))
        self.play(Unwrite(result))
        self.wait()
        
        disp_sub(self, lang='fr')
        
        

