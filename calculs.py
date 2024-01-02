from manim import *
import manim

class A(Scene):
    def construct(self):
        msg = "Calculs avec "
        title_start = Title(f"{msg} Manim {manim.__version__}")
        self.add(title_start)
        self.wait()
        A = MathTex(
            r"A =",
            r"(1 + ",
            r"2\times 3",
            r"- 4 + ",
            r"5\times 6",
            r")\div 11"
        )
        self.play(Write(A.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxA02 = SurroundingRectangle(A[2])
        boxA04 = SurroundingRectangle(A[4])
        self.play(*[Create(box) for box in [boxA02, boxA04]])
        self.wait()
        
        A1 = MathTex(
            r"A = (",
            r"1 + ",
            r"6",
            r" - 4 + ",
            r"30",
            r")\div 11",
        )
        
        self.play(Write(A1.next_to(A, DOWN)))
        self.wait()
        boxA12 = SurroundingRectangle(A1[2])
        boxA14 = SurroundingRectangle(A1[4])
        self.play(
            ReplacementTransform(boxA02, boxA12),
            ReplacementTransform(boxA04, boxA14),
        )
        self.wait()
        
        A2 = MathTex(
            r"A = (",
            r"7 ",
            r"- 4",
            r"+ 30",
            r")\div 11",
        )
        boxA112 = SurroundingRectangle(A1[1:3])
        self.play(
            ReplacementTransform(boxA12, boxA112),
            Write(A2.next_to(A1, DOWN)),
            *[FadeOut(box) for box in [boxA14, boxA04]],
        )
        self.wait()
        boxA21 = SurroundingRectangle(A2[1])
        self.play(
            ReplacementTransform(boxA112, boxA21)
        )
        self.wait()

        A3 = MathTex(
            r"A = (",
            r"3",
            r"+ 30",
            r")\div 11",
        )
        boxA212 = SurroundingRectangle(A2[1:3])
        self.play(
            ReplacementTransform(boxA21, boxA212),
            Write(A3.next_to(A2, DOWN))
        )
        self.wait()
        boxA31 = SurroundingRectangle(A3[1])
        self.play(ReplacementTransform(boxA212, boxA31))
        self.wait()

        A4 = MathTex(
            r"A =",
            r"33",
            r"\div 11"
        )
        boxA312 = SurroundingRectangle(A3[1:3])
        self.play(
            ReplacementTransform(boxA31, boxA312),
            Write(A4.next_to(A3, DOWN))
        )
        self.wait()
        boxA41 = SurroundingRectangle(A4[1])
        self.play(ReplacementTransform(boxA312, boxA41))
        self.wait()

        A5 = MathTex(
            r"A =",
            r"3",
        )
        boxA412 = SurroundingRectangle(A4[1:3])
        self.play(
            ReplacementTransform(boxA41, boxA412),
            Write(A5.next_to(A4, DOWN))
        )
        self.wait()

        boxA5 = SurroundingRectangle(A5)
        self.play(
            ReplacementTransform(boxA412, boxA5)
        )
        self.wait()
