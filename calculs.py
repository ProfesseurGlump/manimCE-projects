from manim import *
import manim


class exerciceA(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
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

        A1 = MathTex(
            r"A = ",
            r"\,?"
        )
        
        self.play(Write(A1.next_to(A, DOWN)))
        self.wait()
        
        
class solutionA(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
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


class exerciceB(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        B = MathTex(
            r"B =",
            r"(9 - ",
            r"4\times 2",
            r" + ",
            r"7\times 3",
            r")\div 11"
        )
        self.play(Write(B.next_to(title_start, 2 * DOWN)))
        self.wait()

        B1 = MathTex(
            r"B = ",
            r"\,?"
        )
        
        self.play(Write(B1.next_to(B, DOWN)))
        self.wait()
        
        
class solutionB(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        B = MathTex(
            r"B = (",
            r"9 - ",
            r"4\times 2",
            r"+ ",
            r"7\times 3 ",
            r")",
            r"\div 11"
        )
        self.play(Write(B.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxB02 = SurroundingRectangle(B[2])
        boxB04 = SurroundingRectangle(B[4])
        self.play(*[Create(box) for box in [boxB02, boxB04]])
        self.wait()
        
        B1 = MathTex(
            r"B = (",
            r"9 - ",
            r"8",
            r" + ",
            r"21",
            r")",
            r"\div 11",
        )
        
        self.play(Write(B1.next_to(B, DOWN)))
        self.wait()
        boxB12 = SurroundingRectangle(B1[2])
        boxB14 = SurroundingRectangle(B1[4])
        self.play(
            ReplacementTransform(boxB02, boxB12),
            ReplacementTransform(boxB04, boxB14),
        )
        self.wait()
        
        B2 = MathTex(
            r"B = (",
            r"1 ",
            r"+ ",
            r"21",
            r")",
            r"\div 11",
        )
        boxB112 = SurroundingRectangle(B1[1:3])
        self.play(
            ReplacementTransform(boxB12, boxB112),
            Write(B2.next_to(B1, DOWN)),
            *[FadeOut(box) for box in [boxB14, boxB04]],
        )
        self.wait()
        boxB21 = SurroundingRectangle(B2[1])
        self.play(
            ReplacementTransform(boxB112, boxB21)
        )
        self.wait()

        B3 = MathTex(
            r"B = ",
            r"22",
            r"\div 11",
        )
        boxB212 = SurroundingRectangle(B2[1:4])
        self.play(
            ReplacementTransform(boxB21, boxB212),
            Write(B3.next_to(B2, DOWN))
        )
        self.wait()
        boxB31 = SurroundingRectangle(B3[1])
        self.play(ReplacementTransform(boxB212, boxB31))
        self.wait()

        B4 = MathTex(
            r"B =",
            r"2",
        )
        boxB312 = SurroundingRectangle(B3[1:3])
        self.play(
            ReplacementTransform(boxB31, boxB312),
            Write(B4.next_to(B3, DOWN))
        )
        self.wait()
        boxB41 = SurroundingRectangle(B4[1])
        self.play(ReplacementTransform(boxB312, boxB41))
        self.wait()

        boxB4 = SurroundingRectangle(B4)
        self.play(
            ReplacementTransform(boxB41, boxB4)
        )
        self.wait()
        


class exerciceC(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        C = MathTex(
            r"C = 2\times [(",
            r"19 - 8",
            r")\times 4 - (",
            r"5 + 1",
            r")\times ",
            r"3 + 4",
            r")]"
        )
        self.play(Write(C.next_to(title_start, 2 * DOWN)))
        self.wait()

        C1 = MathTex(
            r"C = ",
            r"\,?"
        )
        
        self.play(Write(C1.next_to(C, DOWN)))
        self.wait()
        
        
class solutionC(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        C = MathTex(
            r"C = 2\times [(",
            r"19 - 8", # 1
            r")\times 4 - (",
            r"5 + 1", # 3
            r")\times ",
            r"3 + 4", # 5
            r")]"
        )
        self.play(Write(C.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesC = [SurroundingRectangle(C[i]) for i in [1, 3, 5]]
        self.play(*[Create(box) for box in boxesC])
        self.wait()
        
        C1 = MathTex(
            r"C = 2\times[",
            r"11", # 1
            r"\times 4",
            r"-",
            r"6", # 4
            r"\times ",
            r"7", # 6
            r"]",
        )
        
        self.play(Write(C1.next_to(C, DOWN)))
        self.wait()
        boxesC1 = [SurroundingRectangle(C1[i]) for i in [1, 4, 6]]
        self.play(
            *[
                ReplacementTransform(
                    boxesC[i], boxesC1[i]
                ) for i in range(3)
            ],
        )
        self.wait()
        self.play(*[FadeOut(boxesC[i]) for i in range(3)])
        
        C2 = MathTex(
            r"C = 2\times (",
            r"44 ", # 1
            r"- ",
            r"42", # 3
            r")",
        )
        boxC112 = SurroundingRectangle(C1[1:3])
        boxC114 = SurroundingRectangle(C1[4:7])
        ext_boxesC1 = [boxC112, boxC114]
        self.play(
            ReplacementTransform(boxesC1[0], ext_boxesC1[0]),
            *[
                ReplacementTransform(
                    boxesC1[i],
                    ext_boxesC1[-1]
                ) for i in range(1, 3)
            ],
            Write(C2.next_to(C1, DOWN)),
        )
        self.wait()
        self.play(*[FadeOut(boxesC1[i]) for i in range(3)])
        
        boxesC2 = [SurroundingRectangle(C2[i]) for i in [1, 3]]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesC1[i],
                    boxesC2[i]
                ) for i in range(2)
            ],
        )
        self.wait()
        self.play(*[FadeOut(ext_boxesC1[i]) for i in range(2)])

        ext_boxC2 = SurroundingRectangle(C2[1:4])
        C3 = MathTex(
            r"C = ",
            r"2", 
            r"\times", 
            r"2" # 3
        )
        self.play(
            *[
                ReplacementTransform(
                    b,
                    ext_boxC2
                ) for b in boxesC2
            ],
            Write(C3.next_to(C2, DOWN))
        )

        self.wait()
        self.play(*[FadeOut(b) for b in boxesC2])
        
        boxC33 = SurroundingRectangle(C3[3])
        self.play(
            ReplacementTransform(ext_boxC2, boxC33),
        )
        self.wait()
        self.play(FadeOut(ext_boxC2))

        ext_boxC3 = SurroundingRectangle(C3[1:4])
        self.play(
            ReplacementTransform(boxC33, ext_boxC3),
        )
        self.wait()
        self.play(FadeOut(boxC33))
        
        C4 = MathTex(
            r"C = ",
            r"4",
        )

        self.play(
            Write(C4.next_to(C3, DOWN))
        )
        self.wait()
        
        boxC41 = SurroundingRectangle(C4[1])
        
        self.play(
            ReplacementTransform(ext_boxC3, boxC41),
        )
        self.wait()
        self.play(FadeOut(ext_boxC3))
        
        boxC4 = SurroundingRectangle(C4)
        self.play(
            ReplacementTransform(boxC41, boxC4)
        )
        self.wait()


class exerciceD(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        D = MathTex(
            r"D = \{(",
            r"1 + 2", # 1
            r") - 3\times [6\div (",
            r"3 + 3", # 3
            r")]\}\times ",
            r"23",
        )
        self.play(Write(D.next_to(title_start, 2 * DOWN)))
        self.wait()

        D1 = MathTex(
            r"D = ",
            r"\,?"
        )
        
        self.play(Write(D1.next_to(D, DOWN)))
        self.wait()
        
        
class solutionD(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        D = MathTex(
            r"D = \{(",
            r"1 + 2", # 1
            r") - 3\times [6\div (",
            r"3 + 3", # 3
            r")]\}\times ",
            r"23",
        )
        self.play(Write(D.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesD = [SurroundingRectangle(D[i]) for i in [1, 3]]
        self.play(*[Create(box) for box in boxesD])
        self.wait()
        
        D1 = MathTex(
            r"D = [",
            r"3", # 1
            r"- 3\times (",
            r"6\div ",
            r"6", # 4
            r")]\times ",
            r"23",
        )
        
        self.play(Write(D1.next_to(D, DOWN)))
        self.wait()
        boxesD1 = [SurroundingRectangle(D1[i]) for i in [1, 4]]
        self.play(
            *[
                ReplacementTransform(
                    boxesD[i], boxesD1[i]
                ) for i in range(2)
            ],
        )
        self.wait()
        self.play(*[FadeOut(boxesD[i]) for i in range(2)])
        
        D2 = MathTex(
            r"D = (",
            r"3 - ",
            r"3\times ",
            r"1", # 3
            r")\times 23",
        )
        boxD134 = SurroundingRectangle(D1[3:5])
        self.play(
            FadeOut(boxesD1[0]),
            ReplacementTransform(boxesD1[-1], boxD134),
            Write(D2.next_to(D1, DOWN)),
        )
        self.wait()
        self.play(FadeOut(boxesD1[-1]))
        
        boxD23 = SurroundingRectangle(D2[3])
        self.play(
            ReplacementTransform(
                boxD134,
                boxD23
            ) 
        )
        self.wait()
        self.play(FadeOut(boxD134))

        ext_boxD2 = SurroundingRectangle(D2[2:4])
        D3 = MathTex(
            r"D = (",
            r"3 - ",
            r"3", # 2
            r")\times 23",
        )
        self.play(
            ReplacementTransform(boxD23, ext_boxD2),
            Write(D3.next_to(D2, DOWN))
        )
        self.wait()
        self.play(FadeOut(boxD23))
        
        boxD32 = SurroundingRectangle(D3[2])
        self.play(
            ReplacementTransform(ext_boxD2, boxD32),
        )
        self.wait()
        self.play(FadeOut(ext_boxD2))

        ext_boxD3 = SurroundingRectangle(D3[1:3])
        self.play(
            ReplacementTransform(boxD32, ext_boxD3),
        )
        self.wait()
        self.play(FadeOut(boxD32))
        
        D4 = MathTex(
            r"D = ",
            r"0", # 1
            r"\times 23"
        )

        self.play(
            Write(D4.next_to(D3, DOWN))
        )
        self.wait()             
        
        boxD41 = SurroundingRectangle(D4[1])
        
        self.play(
            ReplacementTransform(ext_boxD3, boxD41),
        )
        self.wait()
        self.play(FadeOut(ext_boxD3))

        D5 = MathTex(
            r"D = ",
            r"0", # 1
        )

        self.play(
            Write(D5.next_to(D4, DOWN))
        )
        self.wait()
        
        boxD51 = SurroundingRectangle(D5[1])
        
        self.play(
            ReplacementTransform(boxD41, boxD51),
        )
        self.wait()
        self.play(FadeOut(boxD41))
        
        boxD5 = SurroundingRectangle(D5)
        self.play(
            ReplacementTransform(boxD51, boxD5)
        )
        self.wait()
        self.play(FadeOut(boxD51))
        


class exerciceE(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        E = MathTex(
            r"E = \{[",
            r"1 + (", 
            r"1 + 2", # 2
            r")] + [",
            r"2 + 3", # 4
            r"]\}\times 4 - ",
            r"2\times 2", # 6
            r"-",
            r"3\times 3"
        )
        self.play(Write(E.next_to(title_start, 2 * DOWN)))
        self.wait()

        E1 = MathTex(
            r"E = ",
            r"\,?"
        )
        
        self.play(Write(E1.next_to(E, DOWN)))
        self.wait()
        
        
class solutionE(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        E = MathTex(
            r"E = \{[",
            r"1 + (", 
            r"1 + 2", # 2
            r")] + [",
            r"2 + 3", # 4
            r"]\}\times 4 - ",
            r"2\times 2", # 6
            r"-",
            r"3\times 3" # 8
        )
        self.play(Write(E.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesE = [
            SurroundingRectangle(E[i]) for i in range(2, 9, 2)
        ]
        self.play(*[Create(box) for box in boxesE])
        self.wait()
        
        E1 = MathTex(
            r"E = [(",
            r"1 + ", 
            r"3", # 2
            r") + ",
            r"5", # 4
            r"]\times 4 - ",
            r"4", # 6
            r"-",
            r"9" # 8
        )
        
        self.play(Write(E1.next_to(E, DOWN)))
        self.wait()
        boxesE1 = [
            SurroundingRectangle(E1[i]) for i in range(2, 9, 2)
        ]
        self.play(
            *[
                ReplacementTransform(
                    boxesE[i], boxesE1[i]
                ) for i in range(len(boxesE))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesE])

        ext_boxE1 = SurroundingRectangle(E1[1:3])
        self.play(ReplacementTransform(boxesE1[0], ext_boxE1))
        self.wait()
        
        E2 = MathTex(
            r"E = (",
            r"4", # 1
            r"+ 5", 
            r")\times 4 - ",
            r"4", 
            r"- 9"
        )
        
        self.play(
            Write(E2.next_to(E1, DOWN)),
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesE1])
        
        boxE21 = SurroundingRectangle(E2[1])
        self.play(
            ReplacementTransform(
                ext_boxE1,
                boxE21
            ) 
        )
        self.wait()
        self.play(FadeOut(ext_boxE1))

        ext_boxE2 = SurroundingRectangle(E2[1:3])
        self.play(ReplacementTransform(boxE21, ext_boxE2))
        self.wait()
        
        E3 = MathTex(
            r"E = ",
            r"9", # 1
            r"\times 4 ",
            r"- 4 - 9"
        )

        self.play(
            Write(E3.next_to(E2, DOWN))
        )
        self.wait()
        self.play(FadeOut(boxE21))
        
        boxE31 = SurroundingRectangle(E3[1])
        self.play(
            ReplacementTransform(ext_boxE2, boxE31),
        )
        self.wait()
        self.play(FadeOut(ext_boxE2))

        ext_boxE3 = SurroundingRectangle(E3[1:3])
        self.play(
            ReplacementTransform(boxE31, ext_boxE3),
        )
        self.wait()
        self.play(FadeOut(boxE31))
        
        E4 = MathTex(
            r"E = ",
            r"36", # 1
            r"- 4 ",
            r"- 9"
        )

        self.play(
            Write(E4.next_to(E3, DOWN))
        )
        self.wait()             
        
        boxE41 = SurroundingRectangle(E4[1])
        
        self.play(
            ReplacementTransform(ext_boxE3, boxE41),
        )
        self.wait()
        self.play(FadeOut(ext_boxE3))

        ext_boxE4 = SurroundingRectangle(E4[1:3])
        self.play(ReplacementTransform(boxE41, ext_boxE4))
        self.wait()
        
        E5 = MathTex(
            r"E = ",
            r"32", # 1
            r"- 9 ",
        )

        self.play(
            Write(E5.next_to(E4, DOWN))
        )
        self.wait()
        
        boxE51 = SurroundingRectangle(E5[1])
        
        self.play(
            ReplacementTransform(ext_boxE4, boxE51),
        )
        self.wait()
        self.play(FadeOut(ext_boxE4))

        ext_boxE5 = SurroundingRectangle(E5[1:3])
        self.play(ReplacementTransform(boxE51, ext_boxE5))
        self.wait()
        
        
        E6 = MathTex(
            r"E = ",
            r"23", # 1
        )

        self.play(
            Write(E6.next_to(E5, DOWN))
        )
        self.wait()
        
        boxE61 = SurroundingRectangle(E6[1])
        
        self.play(
            ReplacementTransform(ext_boxE5, boxE61),
        )
        self.wait()
        self.play(FadeOut(ext_boxE5))

        boxE6 = SurroundingRectangle(E6)
        self.play(
            ReplacementTransform(boxE61, boxE6),
        )
        self.wait()
        self.play(FadeOut(boxE61))
        


class exerciceF(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        F = MathTex(
            r"F = [(",
            r"17 + 3", # 1 
            r") + (", 
            r"4\times 5", # 3
            r")]\times (", 
            r"0,5\times 0,5", # 5
            r") - [(",
            r"8\times 5", # 7
            r") + (",
            r"2,5 + 7,5", # 9
            r")]\times (",
            r"0,75 - 0,55", # 11
            r")"
        ).scale(0.8)
        self.play(Write(F.next_to(title_start, 2 * DOWN)))
        self.wait()

        F1 = MathTex(
            r"F = ",
            r"\,?"
        )
        
        self.play(Write(F1.next_to(F, DOWN)))
        self.wait()
        
        
class solutionF(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        F = MathTex(
            r"F = [(",
            r"17 + 3", # 1 
            r") + (", 
            r"4\times 5", # 3
            r")]\times (", 
            r"0,5\times 0,5", # 5
            r") - [(",
            r"8\times 5", # 7
            r") + (",
            r"2,5 + 7,5", # 9
            r")]\times (",
            r"0,75 - 0,55", # 11
            r")"
        ).scale(0.8)
        self.play(Write(F.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesF = [
            SurroundingRectangle(F[i]) for i in range(1, 12, 2)
        ]
        self.play(*[Create(box) for box in boxesF])
        self.wait()
        
        F1 = MathTex(
            r"F = [(",
            r"20", # 1 
            r"+ ", 
            r"20", # 3
            r")\times ", 
            r"0,25", # 5
            r"] - [(",
            r"40", # 7
            r"+ ",
            r"10", # 9
            r")\times ",
            r"0,2", # 11
            r"]"
        )
        
        self.play(Write(F1.next_to(F, DOWN)))
        self.wait()
        boxesF1 = [
            SurroundingRectangle(F1[i]) for i in range(1, 12, 2)
        ]
        self.play(
            *[
                ReplacementTransform(
                    boxesF[i], boxesF1[i]
                ) for i in range(len(boxesF))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesF])

        ext_boxesF1 = [
            SurroundingRectangle(F1[1:4]),
            SurroundingRectangle(F1[7:10])
        ]
        
        self.play(
            *[
                ReplacementTransform(
                    boxesF1[i],
                    ext_boxesF1[0]
                ) for i in [0, 1]
            ],
            *[
                ReplacementTransform(
                    boxesF1[i],
                    ext_boxesF1[1]
                ) for i in [3, 4]
            ],
            *[FadeOut(boxesF1[i]) for i in [2, 5]]
        )
        self.wait()
        
        F2 = MathTex(
            r"F = (",
            r"40", # 1 
            r"\times ", 
            r"0,25", # 3
            r") - (",
            r"50", # 5
            r"\times ",
            r"0,2", # 7
            r")"
        )
        
        self.play(
            Write(F2.next_to(F1, DOWN)),
        )
        self.wait()

        
        boxesF215 = [
            SurroundingRectangle(F2[1]),
            SurroundingRectangle(F2[5])
            ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesF1[i],
                    boxesF215[i]
                ) for i in range(len(boxesF215))
            ]
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesF1])

        ext_boxesF2 = [
            SurroundingRectangle(F2[1:4]),
            SurroundingRectangle(F2[5:8])
        ]
            
        self.play(
            *[
                ReplacementTransform(
                    boxesF215[i],
                    ext_boxesF2[i]
                ) for i in range(len(boxesF215))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesF215])
        
        F3 = MathTex(
            r"F = ",
            r"10", # 1 
            r" - ",
            r"10", # 3
        )

        self.play(
            Write(F3.next_to(F2, DOWN))
        )
        self.wait()
        
        boxesF313 = [
            SurroundingRectangle(F3[1]),
            SurroundingRectangle(F3[3])
        ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesF2[i],
                    boxesF313[i]
                ) for i in range(len(boxesF313))
            ],
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesF2])

        ext_boxF3 = SurroundingRectangle(F3[1:4])
        self.play(
            *[
                ReplacementTransform(
                    b,
                    ext_boxF3
                ) for b in boxesF313
            ]
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesF313])
        
        F4 = MathTex(
            r"F = ",
            r"0", # 1
        )

        self.play(
            Write(F4.next_to(F3, DOWN))
        )
        self.wait()             
        
        boxF41 = SurroundingRectangle(F4[1])
        
        self.play(
            ReplacementTransform(ext_boxF3, boxF41),
        )
        self.wait()
        self.play(FadeOut(ext_boxF3))

        boxF4 = SurroundingRectangle(F4)
        self.play(ReplacementTransform(boxF41, boxF4))
        self.wait()
        self.play(FadeOut(boxF41))
        
        
        
class exerciceG(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        G = MathTex(
            r"G =",
            r"7\times [(8 + ",
            r"9\times 10", # 2
            r"- 11 + ",
            r"12\times 13", # 4
            r")\div 9]"
        )
        self.play(Write(G.next_to(title_start, 2 * DOWN)))
        self.wait()

        G1 = MathTex(
            r"G = ",
            r"\,?"
        )
        
        self.play(Write(G1.next_to(G, DOWN)))
        self.wait()
        
        
class solutionG(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        G = MathTex(
            r"G =",
            r"7\times [(8 + ",
            r"9\times 10", # 2
            r"- 11 + ",
            r"12\times 13", # 4
            r")\div 9]"
        )
        self.play(Write(G.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesG = [
            SurroundingRectangle(G[2]),
            SurroundingRectangle(G[4])
        ]
        self.play(*[Create(box) for box in boxesG])
        self.wait()
        
        G1 = MathTex(
            r"G =",
            r"7\times [(",
            r"8 + ", 
            r"90", # 3
            r"- 11 + ",
            r"156", # 5
            r")\div 9]"
        )
        
        self.play(Write(G1.next_to(G, DOWN)))
        self.wait()
        
        boxesG1 = [SurroundingRectangle(G1[i]) for i in [3, 5]]
        self.play(
            *[
                ReplacementTransform(
                    boxesG[i],
                    boxesG1[i]
                ) for i in range(len(boxesG))
            ]
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesG])

        ext_boxG1 = SurroundingRectangle(G1[2:4])
        self.play(
            ReplacementTransform(boxesG1[0], ext_boxG1)
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesG1])
        
        G2 = MathTex(
            r"G =",
            r"7\times [(",
            r"98", # 2
            r"- 11",
            r"+ 156)\div 9]"
        )
        self.play(
            Write(G2.next_to(G1, DOWN)),
        )
        self.wait()
        
        boxG22 = SurroundingRectangle(G2[2])
        self.play(
            ReplacementTransform(ext_boxG1, boxG22)
        )
        self.wait()
        self.play(FadeOut(ext_boxG1))

        ext_boxG2 = SurroundingRectangle(G2[2:4])
        self.play(ReplacementTransform(boxG22, ext_boxG2))
        self.wait()
        
        G3 = MathTex(
            r"G =",
            r"7\times [(",
            r"87", # 2
            r"+ 156",
            r")\div 9]"
        )

        self.play(
            Write(G3.next_to(G2, DOWN))
        )
        self.wait()
        
        boxG32 = SurroundingRectangle(G3[2])
        self.play(ReplacementTransform(ext_boxG2, boxG32))
        self.wait()
        self.play(FadeOut(ext_boxG2))

        ext_boxG3 = SurroundingRectangle(G3[2:4])
        self.play(ReplacementTransform(boxG32, ext_boxG3))
        self.wait()
        self.play(FadeOut(boxG32))
        
        G4 = MathTex(
            r"G =",
            r"7\times (",
            r"243", # 2
            r"\div 9",
            r")"
        )
        
        self.play(
            Write(G4.next_to(G3, DOWN))
        )
        self.wait()
        
        boxG42 = SurroundingRectangle(G4[2])
        self.play(ReplacementTransform(ext_boxG3, boxG42))
        self.wait()
        self.play(FadeOut(ext_boxG3))

        ext_boxG4 = SurroundingRectangle(G4[2:4])
        self.play(ReplacementTransform(boxG42, ext_boxG4))
        self.wait()
        self.play(FadeOut(boxG42))
        
        G5 = MathTex(
            r"G =",
            r"7\times ",
            r"27", # 2
        )

        self.play(
            Write(G5.next_to(G4, DOWN))
        )
        self.wait()

        boxG52 = SurroundingRectangle(G5[2])
        self.play(
            ReplacementTransform(ext_boxG4, boxG52)
        )
        self.wait()
        self.play(FadeOut(ext_boxG4))

        ext_boxG5 = SurroundingRectangle(G5[1:])
        self.play(ReplacementTransform(boxG52, ext_boxG5))
        self.wait()
        self.play(FadeOut(boxG52))

        
        G6 = MathTex(
            r"G =",
            r"189", # 1
        )

        self.play(
            Write(G6.next_to(G5, DOWN))
        )
        self.wait()

        boxG61 = SurroundingRectangle(G6[1])
        self.play(ReplacementTransform(ext_boxG5, boxG61))
        self.wait()
        self.play(FadeOut(ext_boxG5))

        boxG6 = SurroundingRectangle(G6)
        self.play(ReplacementTransform(boxG61, boxG6))
        self.wait()
        self.play(FadeOut(boxG61))
