from manim import *
import manim

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


def call_to_action(self):
    sub_svg = SVGMobject("~/Documents/svg-pics/subscribe.svg")
    self.play(GrowFromCenter(sub_svg.scale(0.85).to_edge(4.5*UP)))
    final_text = Text("Abonnez-vous").scale(2).to_edge(4.5*DOWN)
    self.play(Write(final_text))
    self.wait()

def write_lines(self, liste, scales):
    top_line = 8.5
    for i in range(len(liste)):
        if i == 0:
            self.play(
                Write(
                    liste[i].scale(scales[0]).to_edge(top_line * UP + LEFT)
                )
            )
        else:
            mult_up = (top_line + i*3)
            self.play(
                Write(liste[i].scale(scales[i]).to_edge(
                    mult_up  * UP + LEFT
                )
                      )
            )
        self.wait(1)
    

class Tribu(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title(f"YouTube Shorts avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "~/Documents/svg-pics/Youtube_shorts.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))
        line0 = Text(
            "Soit E un ensemble quelconque. Une tribu (ou"
        )
        line1 = MathTex("\\sigma")
        line2 = Text(
            "- algèbre) sur E est une famille"
        )
        line3 = MathTex("\\mathcal{A}")
        line4 = Text("de parties de E telle que : ")
        line5 = MathTex(
            "1) E\\in\\mathcal{A}",
            "2) A\\in\\mathcal{A}\\Rightarrow A^c\\in\\mathcal{A}",
            "3) \\forall n\\in\\mathbb{N}, A_n\\in\\mathcal{A}",
            "\\Rightarrow \\bicup_{n\\in\\mathbb{N}A_n}\\in\\mathcal{A}"
        )
        line6 = Text("Les éléments de ")
        line7 = MathTex("\\mathcal{A}")
        line8 = Text(
            "sont appelés parties mesurables. On dit que (E, "
        )
        line9 = MathTex("\\mathcal{A})")
        line10 = Text("est un espace mesurable.")
    
        lines = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
        scales = [1,        1,     1,     1,     1,     1,     1,     1,     1,     1,      1]

        write_lines(self, liste=lines, scales=scales)
        self.wait()
