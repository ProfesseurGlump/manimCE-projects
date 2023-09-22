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

class NormalDistribution(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Loi normale"
        title = Title(f"{msg} avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        ax = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-0.1, 0.5]
        )
        
        bell_curve = ax.plot(
            lambda x: e**(-0.5 * x**2)/((2 * pi)**0.5), color=GREEN
            )
        
        self.play(Create(ax, run_time=2), Create(bell_curve, run_time=5))
        normal_density = "f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-\dfrac{x^2}{2}}"
        gaussian = MathTex(normal_density)
        label = ax.get_graph_label(
            bell_curve,
            gaussian,
            x_val=0,
            direction=2*DOWN
        )
        self.play(Create(label.next_to(ax, DOWN)))
                  
        disp_bell_curv_area(
            self,
            ax,
            bell_curve,
            x_interval=[-2.5, 0],
            qx=0,
            px=0.5,
            dir=1
        )
        self.wait(3)
        disp_bell_curv_area(
            self,
            ax,
            bell_curve,
            x_interval=[0, 2.5],
            qx=0,
            px=0.5,
            dir=-1
        )
        self.wait(3)

        disp_bell_curv_area(
            self,
            ax,
            bell_curve,
            x_interval=[-2.5, 1],
            qx=1,
            px=0.84,
            dir=1
        )
        self.wait(3)

        disp_bell_curv_area(
            self,
            ax,
            bell_curve,
            x_interval=[1, 2.5],
            qx=1,
            px=0.84,
            dir=-1
        )
        self.wait(3)

        disp_bell_curv_area(
            self,
            ax,
            bell_curve,
            x_interval=[-1, 1],
            qx=1,
            px=0.84,
            dir=0
        )
        self.wait(3)
        
        disp_sub(self, lang='fr')


class YouTubeShortSetup(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
            
    def construct(self):
        msg = "Comment coder"
        title = Title(f"{msg} avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "/Users/dn/Documents/pics/svg/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))
        title2 = Title("Pour le format YouTube Shorts")
        self.play(ReplacementTransform(title, title2), run_time=2)
        
        code = '''from manim import *
import manim

SCALE_FACTOR = 0.5
# flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height
config.frame_height /= SCALE_FACTOR
config.frame_width = config.frame_height
config.frame_width *= 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(Write(rendered_code.scale(0.75)), run_time=5)
        self.wait(2)

        title3 = Title("Pour que tu puisses t'abonner")
        self.play(ReplacementTransform(title2, title3), run_time=2)
        
        code2 = '''def disp_sub(self, lang):
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
'''
        rendered_code2 = Code(code=code2, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(
            ReplacementTransform(
                rendered_code.scale(0.75),
                rendered_code2.scale(0.75)
            ),
            run_time=5)
        self.wait(2)
                  

        title4 = Title("Pour afficher des photos")
        self.play(ReplacementTransform(title3, title4), run_time=2)
        
        code3 = '''def disp_full_part_full(
        self, full, part,
        images, lang, full_scale=1
        ):
    self.play(
        Write(
        full.scale(full_scale),
        run_time = 5
        )
        )
    self.wait(5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(3)
        self.remove(pic)
        
    self.play(
        Write(part.scale(full_scale),
        run_time = 3
        )
        )
    self.wait(3)
        
    self.play(
        ReplacementTransform(part, full),
        run_time=3
        )
    self.wait(3)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)
'''

        rendered_code3 = Code(code=code3, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(
            ReplacementTransform(
                rendered_code2.scale(0.75),
                rendered_code3.scale(0.75)
            ),
            run_time=5)
        self.wait(2)

        title5 = Title("Pour afficher la courbe de Gauss")
        self.play(ReplacementTransform(title4, title5), run_time=2)
        
        code4 = '''from math import e, pi
def disp_bell_curv_area(
        self, axe, curve,
        x_interval, qx, px, dir
        ):
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
    self.play(FadeOut(prob), FadeOut(area))'''


        rendered_code4 = Code(code=code4, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(
            ReplacementTransform(
                rendered_code3.scale(0.75),
                rendered_code4.scale(0.75)
            ),
            run_time=5)
        self.wait(2)
        self.play(FadeOut(rendered_code4.scale(0.75)))
        self.wait(2)
        disp_sub(self, lang='fr')
