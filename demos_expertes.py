from manim import *
import manim

class ZnMinusAn(Scene):
    def construct(self):
        msg = "Démonstration de maths expertes avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start)
        self.wait()
        text = MathTex(
            r"z^n - a^n =",
            r"a^n\left[\left(\frac{z}{a}\right)^n - 1\right]"
        )
        self.play(Write(text.next_to(title_start, 2 * DOWN)))
        self.wait(2)
        
        rappel1 = MathTex(
            r"S =",
            r"\sum_{k = 0}^{n - 1}q^k =",
            r"1 + q + q^2 + \dots + q^{n - 1}"
        )
        self.play(Write(rappel1.next_to(text, DOWN)))
        self.wait(4)

        rappel2 = MathTex(
            r"qS =",
            r"\sum_{k = 0}^{n - 1}q^{k + 1} =",
            r"\qquad q + q^2 + \dots + q^{n - 1} + q^n"
        )
        self.play(Write(rappel2.next_to(rappel1, DOWN)))
        self.wait(4)

        rappel3 = MathTex(
            r"qS - S =",
            r"q^n - 1",
        )
        self.play(Write(rappel3.next_to(rappel2, DOWN)))
        self.wait(4)

        rappel4 = MathTex(
            r"(q - 1)S =",
            r"q^n - 1",
        )
        self.play(
            ReplacementTransform(
                rappel3,
                rappel4.next_to(rappel2, DOWN)
            )
        )
        self.wait(4)

        rappel5 = MathTex(
            r"(q - 1)\sum_{k = 0}^{n - 1}q^k =",
            r"q^n - 1",
        )
        self.play(
            ReplacementTransform(
                rappel4,
                rappel5.next_to(rappel2, DOWN)
            )
        )
        self.wait(4)

        rappel6 = MathTex(
            r"q^n - 1 =",
            r"(q - 1)\sum_{k = 0}^{n - 1}q^k",
        )
        self.play(
            ReplacementTransform(
                rappel5,
                rappel6.next_to(rappel2, DOWN)
            )
        )
        self.wait(4)

        demo1_part2 = r"\left(\dfrac{z}{a} - 1\right)"
        demo1_part2 += r"\sum_{k = 0}^{n - 1}\left("
        demo1_part2 += r"\dfrac{z}{a}\right)^k"
        demo1 = MathTex(
            r"\left(\dfrac{z}{a}\right)^n - 1 =",
            demo1_part2
        )
        self.play(
            ReplacementTransform(
                rappel1,
                demo1.next_to(text, DOWN)
            )
        )
        self.wait(4)

        demo2_part2 = r"a^n\left(\dfrac{z}{a} - 1\right)"
        demo2_part2 += r"\sum_{k = 0}^{n - 1}"
        demo2_part2 += r"\left(\dfrac{z}{a}\right)^k"
        demo2 = MathTex(
            r"a^n\left[\left(\dfrac{z}{a}\right)^n - 1\right] =",
            demo2_part2
        )
        self.play(
            ReplacementTransform(
                rappel2,
                demo2.next_to(demo1, DOWN)
            )
        )
        self.wait(4)

        demo3_part2 = r"a^{n - 1}(z - a)"
        demo3_part2 += r"\sum_{k = 0}^{n - 1}"
        demo3_part2 += r"z^ka^{-k}"
        demo3 = MathTex(
            r"z^n - a^n =",
            demo3_part2
        )
        self.play(
            ReplacementTransform(
                rappel6,
                demo3.next_to(demo2, DOWN)
            )
        )
        self.wait(4)

        demo4_part2 = r"(z - a)"
        demo4_part2 += r"\sum_{k = 0}^{n - 1}"
        demo4_part2 += r"z^ka^{n-1-k}"
        demo4 = MathTex(
            r"z^n - a^n =",
            demo4_part2
        )
        self.play(
            *[FadeOut(demo2, demo3)],
            ReplacementTransform(
                demo1,
                demo4.next_to(text, DOWN)
            )
        )
        self.wait(4)
        
        self.play(
            FadeOut(text),
            Create(SurroundingRectangle(demo4))
        )
        self.wait(4)
        
