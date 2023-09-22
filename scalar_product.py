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
    

class CercleViaProduitScalaire(Scene):
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
        
        line1 = MathTex(
            "\\overrightarrow{MA}", ".", "\\overrightarrow{MB} = 0"
        )
        line2 = MathTex(
            "\\left(\\overrightarrow{MI}",
            "+",
            "\\overrightarrow{IA}\\right)",
            ".",
            "\\left(\\overrightarrow{MI}",
            "+",
            "\\overrightarrow{IB}\\right)",
            "= 0"
        )
        line3 = MathTex(
            "MI^2",
            "+",
            "\\overrightarrow{MI}",
            "\\left(",
            "\\overrightarrow{IB}",
            "+",
            "\\overrightarrow{IA}",
            "\\right)",
            "+",
            "\\overrightarrow{IA}",
            ".",
            "\\overrightarrow{IB}",
            "=",
            "0"
        )
        line4 = MathTex(
            "\\overrightarrow{IB}",
            "+",
            "\\overrightarrow{IA}",
            "=",
            "\\dfrac{1}{2}",
            "\\overrightarrow{AB}",
            "+",
            "\\dfrac{1}{2}",
            "\\overrightarrow{BA}",
            "=",
            "0"
        )
        line5 = MathTex(
            "\\overrightarrow{IA}",
            ".",
            "\\overrightarrow{IB}",
            "=",
            "-",
            "\\dfrac{1}{4}",
            "AB^2"
        )
        lines = [line1, line2, line3, line4, line5]
        scales = [1, 1, 1, 1, 1]

        write_lines(self, liste=lines, scales=scales)
        self.wait()

        for i in range(len(lines)-1, 0, -1): self.play(Unwrite(lines[i]))
        line2 = MathTex(
            "MI^2",
            "=",
            "\\dfrac{1}{4}",
            "AB^2"
        )
        line3 = Text("Cercle de diamètre AB")
        line4 = MathTex(
            "I",
            "\\left(",
            "\\dfrac{x_A+x_B}{2}",
            ";",
            "\\dfrac{y_A+y_B}{2}",
            "\\right)"
        )
        line5 = MathTex(
            "\\left(",
            "x",
            "-",
            "\\dfrac{x_A+x_B}{2}",
            "\\right)",
            "^2",
            "+",
            "\\left(",
            "y",
            "-",
            "\\dfrac{y_A+y_B}{2}",
            "\\right)",
            "^2",
            "=",
            "\\dfrac{1}{4}",
            "\\left(",
            "(x_B - x_A)^2",
            "+",
            "(y_B - y_A)^2",
            "\\right)"
        )
        line6 = Text("Cercle de centre I milieu de [AB]")
        lines = [line1, line2, line3, line4, line5, line6]
        scales = [0.75, 0.75, 1, 1, 0.5, 0.85]
        write_lines(self, liste=lines, scales=scales)
        self.wait()
        call_to_action(self)


class Vectors(VectorScene):
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

        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([2,0], color = YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vector)

        vector2 = self.add_vector([0, 2])
        self.write_vector_coordinates(vector = vector2)

        vector3 = self.add_vector([-2, 2])
        self.write_vector_coordinates(vector = vector3)

        




        

