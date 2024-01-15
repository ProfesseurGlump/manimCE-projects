from manim import *
import manim
from decimal import *

def res_a_op_b(a, op, b):
    a_op_b = []
    for i in range(len(a)):
        if op[i] == "+":
            a_op_b += [Decimal(a[i] + b[i])]
        elif op[i] == "-":
            a_op_b += [Decimal(a[i] - b[i])]
        elif op[i] == r"\times":
            a_op_b += [Decimal(a[i] * b[i])]
        elif op[i] == r"\div":
            a_op_b += [Decimal(a[i] / b[i])]
    return a_op_b

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
            r"2\times 3", # 2
            r"- 4 + ",
            r"5\times 6", # 4
            r")\div 11"
        )
        self.play(Write(A.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesA = [SurroundingRectangle(A[i]) for i in [2, 4]]
        self.play(*[Create(box) for box in boxesA])
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
        boxesA1 = [SurroundingRectangle(A1[i]) for i in [2, 4]]
        self.play(
            *[
                ReplacementTransform(
                    boxesA[i],
                    boxesA1[i]
                ) for i in range(len(boxesA))
            ]
        )
        self.wait()

        ext_boxA1 = SurroundingRectangle(A1[1:3])
        self.play(
            ReplacementTransform(boxesA1[0], ext_boxA1),
        )
        self.wait()
        self.play(*[FadeOut(box) for box in boxesA1])
        
        A2 = MathTex(
            r"A = (",
            r"7 ",
            r"- 4",
            r"+ 30",
            r")\div 11",
        )
        self.play(
            Write(A2.next_to(A1, DOWN)),
        )
        self.wait()
        boxA21 = SurroundingRectangle(A2[1])
        self.play(
            ReplacementTransform(ext_boxA1, boxA21)
        )
        self.wait()

        ext_boxA2 = SurroundingRectangle(A2[1:3])
        self.play(
            ReplacementTransform(boxA21, ext_boxA2)
        )
        self.wait()
        
        A3 = MathTex(
            r"A = (",
            r"3",
            r"+ 30",
            r")\div 11",
        )
    
        self.play(
            Write(A3.next_to(A2, DOWN))
        )
        self.wait()
        
        boxA31 = SurroundingRectangle(A3[1])
        self.play(ReplacementTransform(ext_boxA2, boxA31))
        self.wait()
        ext_boxA3 = SurroundingRectangle(A3[1:3])
        self.play(ReplacementTransform(boxA31, ext_boxA3))
        self.wait()
        
        A4 = MathTex(
            r"A =",
            r"33",
            r"\div 11"
        )
        
        self.play(
            Write(A4.next_to(A3, DOWN))
        )
        self.wait()
        
        boxA41 = SurroundingRectangle(A4[1])
        self.play(ReplacementTransform(ext_boxA3, boxA41))
        self.wait()

        ext_boxA4 = SurroundingRectangle(A4[1:3])
        self.play(ReplacementTransform(boxA41, ext_boxA4))
        self.wait()
        
        A5 = MathTex(
            r"A =",
            r"3", # 1
        )
        
        self.play(
            Write(A5.next_to(A4, DOWN))
        )
        self.wait()

        boxA51 = SurroundingRectangle(A5[1])
        self.play(
            ReplacementTransform(ext_boxA4, boxA51)
        )
        self.wait()

        boxA5 = SurroundingRectangle(A5)
        self.play(
            ReplacementTransform(boxA51, boxA5)
        )
        self.wait()
        self.play(FadeOut(boxA51))


class exerciceB(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        B = MathTex(
            r"B =",
            r"(9 - ",
            r"4\times 2", # 2
            r" + ",
            r"7\times 3", # 4
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
            r"4\times 2", # 2
            r"+ ",
            r"7\times 3 ", # 4
            r")",
            r"\div 11"
        )
        self.play(Write(B.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesB = [SurroundingRectangle(B[i]) for i in [2, 4]]
        self.play(*[Create(box) for box in boxesB])
        self.wait()
        
        B1 = MathTex(
            r"B = (",
            r"9 - ",
            r"8", # 2
            r" + ",
            r"21", # 4
            r")",
            r"\div 11",
        )
        
        self.play(Write(B1.next_to(B, DOWN)))
        self.wait()
        boxesB1 = [SurroundingRectangle(B1[i]) for i in [2, 4]]
        self.play(
            *[
                ReplacementTransform(
                    boxesB[i],
                    boxesB1[i]
                ) for i in range(len(boxesB))
            ]
        )
        self.wait()

        ext_boxB1 = SurroundingRectangle(B1[1:3])
        self.play(ReplacementTransform(boxesB1[0], ext_boxB1))
        self.wait()
        self.play(*[FadeOut(box) for box in boxesB1])
        
        B2 = MathTex(
            r"B = (",
            r"1 ", # 1
            r"+ ",
            r"21", # 3
            r")",
            r"\div 11",
        )
        
        self.play(
            Write(B2.next_to(B1, DOWN)),
        )
        self.wait()
                  
        boxB21 = SurroundingRectangle(B2[1])
        self.play(
            ReplacementTransform(ext_boxB1, boxB21)
        )
        self.wait()

        ext_boxB2 = SurroundingRectangle(B2[1:4])
        self.play(ReplacementTransform(boxB21, ext_boxB2))
        self.wait()
        self.play(FadeOut(boxB21))
    
                  
        B3 = MathTex(
            r"B = ",
            r"22",
            r"\div 11",
        )
        
        self.play(
            Write(B3.next_to(B2, DOWN))
        )
        self.wait()
                  
        boxB31 = SurroundingRectangle(B3[1])
        self.play(ReplacementTransform(ext_boxB2, boxB31))
        self.wait()

        ext_boxB3 = SurroundingRectangle(B3[1:3])
        self.play(ReplacementTransform(boxB31, ext_boxB3))
        self.wait()
        self.play(FadeOut(boxB31))
                  
        B4 = MathTex(
            r"B =",
            r"2",
        )
        self.play(
            Write(B4.next_to(B3, DOWN))
        )
        self.wait()
                  
        boxB41 = SurroundingRectangle(B4[1])
        self.play(ReplacementTransform(ext_boxB3, boxB41))
        self.wait()
        self.play(FadeOut(ext_boxB3))

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
            r")\times (",
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
            r")\times (",
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

        ext_boxD1 = SurroundingRectangle(D1[3:5])
        self.play(ReplacementTransform(boxesD1[1], ext_boxD1))
        self.play(*[FadeOut(b) for b in boxesD1])
        
        D2 = MathTex(
            r"D = (",
            r"3 - ",
            r"3\times ",
            r"1", # 3
            r")\times 23",
        )
        
        self.play(
            Write(D2.next_to(D1, DOWN)),
        )
        self.wait()
        
        
        boxD23 = SurroundingRectangle(D2[3])
        self.play(
            ReplacementTransform(
                ext_boxD1,
                boxD23
            ) 
        )
        self.wait()
        self.play(FadeOut(ext_boxD1))

        ext_boxD2 = SurroundingRectangle(D2[2:4])
        self.play(ReplacementTransform(boxD23, ext_boxD2))
        self.wait()
        self.play(FadeOut(boxD23))
        
        D3 = MathTex(
            r"D = (",
            r"3 - ",
            r"3", # 2
            r")\times 23",
        )
        self.play(
            Write(D3.next_to(D2, DOWN))
        )
        self.wait()
        
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

        ext_boxD4 = SurroundingRectangle(D4[1:])
        self.play(ReplacementTransform(boxD41, ext_boxD4))
        self.wait()
        self.play(FadeOut(boxD41))

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
            ReplacementTransform(ext_boxD4, boxD51),
        )
        self.wait()
        self.play(FadeOut(ext_boxD4))
        
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


class exerciceH(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        H = MathTex(
            r"H = [(",
            r"0,17 + 3,24", # 1 
            r") + (", 
            r"0,09 + 0,5", # 3
            r")]\times (", 
            r"0,01\times 25", # 5
            r") - [(",
            r"8\times 0,125", # 7
            r") + (",
            r"0,125 + 1,375", # 9
            r")]\times (",
            r"3,749 - 3,549", # 11
            r")"
        ).scale(0.55)
        self.play(Write(H.next_to(title_start, 2 * DOWN)))
        self.wait()

        H1 = MathTex(
            r"H = ",
            r"\,?"
        )
        
        self.play(Write(H1.next_to(H, DOWN)))
        self.wait()
        
        
class solutionH(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        H = MathTex(
            r"H = [(",
            r"0,17 + 3,24", # 1 
            r") + (", 
            r"0,09 + 0,5", # 3
            r")]\times (", 
            r"0,01\times 25", # 5
            r") - [(",
            r"8\times 0,125", # 7
            r") + (",
            r"0,125 + 1,375", # 9
            r")]\times (",
            r"3,749 - 3,549", # 11
            r")"
        ).scale(0.55)
        self.play(Write(H.next_to(title_start, 2 * DOWN)))
        self.wait()
        boxesH = [
            SurroundingRectangle(H[i]) for i in range(1, 12, 2)
        ]
        self.play(*[Create(box) for box in boxesH])
        self.wait()
        
        H1 = MathTex(
            r"H = [(",
            r"3,41", # 1 
            r"+ ", 
            r"0,59", # 3
            r")\times ", 
            r"0,25", # 5
            r"] - [(",
            r"1", # 7
            r"+ ",
            r"1,5", # 9
            r")\times ",
            r"0,2", # 11
            r"]"
        )
        
        self.play(Write(H1.next_to(H, DOWN)))
        self.wait()
        boxesH1 = [
            SurroundingRectangle(H1[i]) for i in range(1, 12, 2)
        ]
        self.play(
            *[
                ReplacementTransform(
                    boxesH[i], boxesH1[i]
                ) for i in range(len(boxesH))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesH])

        ext_boxesH1 = [
            SurroundingRectangle(H1[1:4]),
            SurroundingRectangle(H1[7:10])
        ]
        
        self.play(
            *[
                ReplacementTransform(
                    boxesH1[i],
                    ext_boxesH1[0]
                ) for i in [0, 1]
            ],
            *[
                ReplacementTransform(
                    boxesH1[i],
                    ext_boxesH1[1]
                ) for i in [3, 4]
            ],
            *[FadeOut(boxesH1[i]) for i in [2, 5]]
        )
        self.wait()
        
        H2 = MathTex(
            r"H = (",
            r"4", # 1 
            r"\times ", 
            r"0,25", # 3
            r") - (",
            r"2,5", # 5
            r"\times ",
            r"0,2", # 7
            r")"
        )
        
        self.play(
            Write(H2.next_to(H1, DOWN)),
        )
        self.wait()

        
        boxesH215 = [
            SurroundingRectangle(H2[1]),
            SurroundingRectangle(H2[5])
            ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesH1[i],
                    boxesH215[i]
                ) for i in range(len(boxesH215))
            ]
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesH1])

        ext_boxesH2 = [
            SurroundingRectangle(H2[1:4]),
            SurroundingRectangle(H2[5:8])
        ]
            
        self.play(
            *[
                ReplacementTransform(
                    boxesH215[i],
                    ext_boxesH2[i]
                ) for i in range(len(boxesH215))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesH215])
        
        H3 = MathTex(
            r"H = ",
            r"1", # 1 
            r" - ",
            r"0,5", # 3
        )

        self.play(
            Write(H3.next_to(H2, DOWN))
        )
        self.wait()
        
        boxesH313 = [
            SurroundingRectangle(H3[1]),
            SurroundingRectangle(H3[3])
        ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesH2[i],
                    boxesH313[i]
                ) for i in range(len(boxesH313))
            ],
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesH2])

        ext_boxH3 = SurroundingRectangle(H3[1:4])
        self.play(
            *[
                ReplacementTransform(
                    b,
                    ext_boxH3
                ) for b in boxesH313
            ]
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesH313])
        
        H4 = MathTex(
            r"H = ",
            r"0,5", # 1
        )

        self.play(
            Write(H4.next_to(H3, DOWN))
        )
        self.wait()             
        
        boxH41 = SurroundingRectangle(H4[1])
        
        self.play(
            ReplacementTransform(ext_boxH3, boxH41),
        )
        self.wait()
        self.play(FadeOut(ext_boxH3))

        boxH4 = SurroundingRectangle(H4)
        self.play(ReplacementTransform(boxH41, boxH4))
        self.wait()
        self.play(FadeOut(boxH41))
        
        
        
        
class exerciceI(Scene):
    def construct(self):
        msg = "Exercice"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()

        a_1, a_3, a_5, a_7, a_9, a_11 = 0.17, 0.09, 0.01, 8, 0.125, 3.749
        op_1, op_3, op_5= "+", "+", r"\times"
        op_7, op_9, op_11 = r"\times", "+", "-"
        b_1, b_3, b_5, b_7, b_9, b_11 = 3.24, 0.5, 25, 0.124, 1.375, 3.549
        I = MathTex(
            r"I = [(",
            f"{a_1}{op_1}{b_1}", # 1 
            r") + (", 
            f"{a_3}{op_3}{b_3}", # 3
            r")]\times (", 
            f"{a_5}{op_5}{b_5}", # 5
            r") - [(",
            f"{a_7}{op_7}{b_7}", # 7
            r") + (",
            f"{a_9}{op_9}{b_9}", # 9
            r")]\times (",
            f"{a_11}{op_11}{b_11}", # 11
            r")"
        ).scale(0.55)
        self.play(Write(I.next_to(title_start, 2 * DOWN)))
        self.wait()

        I1 = MathTex(
            r"I = ",
            r"\,?"
        )
        
        self.play(Write(I1.next_to(I, DOWN)))
        self.wait()
        
        
class solutionI(Scene):
    def construct(self):
        msg = "Solution"
        title_start = Title(f"{msg}")
        self.add(title_start)
        self.wait()
        
        a_1, a_3, a_5, a_7, a_9, a_11 = 0.123, 1.62, 12, 3.125, 12.507, 3.519
        op_1, op_2, op_3, op_4, op_5= "+", "-", "-", r"\times", r"\div"
        op_6, op_7, op_8, op_9, op_10, op_11 = "-", "+", "+", "-", r"\times", "-"
        b_1, b_3, b_5, b_7, b_9, b_11 = 8.427, 0.07, 2, 4.375, 0.993, 1.769

        getcontext().prec = 3
        a = [a_1, a_3, a_5, a_7, a_9, a_11]
        a = [Decimal(a[i]) for i in range(len(a))]
        
        op = [op_1, op_3, op_5, op_7, op_9, op_11]
        
        b = [b_1, b_3, b_5, b_7, b_9, b_11]
        b = [Decimal(b[i]) for i in range(len(b))]
        I = MathTex(
            r"I = [(",
            f"{a_1}{op_1}{b_1}", # 1 
            f") {op_2} (", 
            f"{a_3}{op_3}{b_3}", # 3
            f")] {op_4} (", 
            f"{a_5}{op_5}{b_5}", # 5
            f") {op_6} [(",
            f"{a_7}{op_7}{b_7}", # 7
            f") {op_8} (",
            f"{a_9}{op_9}{b_9}", # 9
            f")] {op_10} (",
            f"{a_11}{op_11}{b_11}", # 11
            r")"
        ).scale(0.55)
        self.play(Write(I.next_to(title_start, 2 * DOWN)))
        self.wait()
        
        boxesI = [
            SurroundingRectangle(I[i]) for i in range(1, 12, 2)
        ]
        self.play(*[Create(box) for box in boxesI])
        self.wait()
        
        a_op_b = res_a_op_b(a, op, b)
        
        I1 = MathTex(
            r"I = [(",
            f"{a_op_b[0]}", # 1 
            f"{op_2}", 
            f"{a_op_b[1]}", # 3
            f") {op_4}", 
            f"{a_op_b[2]}", # 5
            f"] {op_6} [(",
            f"{a_op_b[3]}", # 7
            f"{op_8} ",
            f"{a_op_b[4]}", # 9
            f") {op_10}",
            f"{a_op_b[5]}", # 11
            r"]"
        )
        
        self.play(Write(I1.next_to(I, DOWN)))
        self.wait()

        a1 = [Decimal(a_op_b[i]) for i in range(len(a_op_b)) if i % 2 == 0]
        op1 = [op[i] for i in range(len(op)) if i % 2 == 1]
        b1 = [Decimal(a_op_b[i]) for i in range(len(a_op_b)) if i % 2 == 1]
        
        boxesI1 = [
            SurroundingRectangle(I1[i]) for i in range(1, 12, 2)
        ]
        self.play(
            *[
                ReplacementTransform(
                    boxesI[i], boxesI1[i]
                ) for i in range(len(boxesI))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesI])

        ext_boxesI1 = [
            SurroundingRectangle(I1[1:4]),
            SurroundingRectangle(I1[7:10])
        ]
        
        self.play(
            *[
                ReplacementTransform(
                    boxesI1[i],
                    ext_boxesI1[0]
                ) for i in [0, 1]
            ],
            *[
                ReplacementTransform(
                    boxesI1[i],
                    ext_boxesI1[1]
                ) for i in [3, 4]
            ], 
            *[FadeOut(boxesI1[i]) for i in [2, 5]]
        )
        self.wait()

        a_op_b2 = res_a_op_b(a1, op1, b1)
        
        I2 = MathTex(
            r"I = (",
            f"{a_op_b2[0]}", # 1 
            f"{op1[0]}", 
            f"{a_op_b2[1]}", # 3
            f") {op1[1]} (",
            f"{a_op_b2[2]}", # 5
            f"{op1[2]} ",
            f"{a_op_b2[-1]}", # 7
            r")"
        )
        
        self.play(
            Write(I2.next_to(I1, DOWN)),
        )
        self.wait()

        
        boxesI215 = [
            SurroundingRectangle(I2[1]),
            SurroundingRectangle(I2[5])
            ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesI1[i],
                    boxesI215[i]
                ) for i in range(len(boxesI215))
            ]
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesI1])

        ext_boxesI2 = [
            SurroundingRectangle(I2[1:4]),
            SurroundingRectangle(I2[5:8])
        ]
            
        self.play(
            *[
                ReplacementTransform(
                    boxesI215[i],
                    ext_boxesI2[i]
                ) for i in range(len(boxesI215))
            ],
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesI215])
        
        I3 = MathTex(
            r"I = ",
            r"1", # 1 
            r" - ",
            r"0,5", # 3
        )

        self.play(
            Write(I3.next_to(I2, DOWN))
        )
        self.wait()
        
        boxesI313 = [
            SurroundingRectangle(I3[1]),
            SurroundingRectangle(I3[3])
        ]
        self.play(
            *[
                ReplacementTransform(
                    ext_boxesI2[i],
                    boxesI313[i]
                ) for i in range(len(boxesI313))
            ],
        )
        self.wait()
        self.play(*[FadeOut(eb) for eb in ext_boxesI2])

        ext_boxI3 = SurroundingRectangle(I3[1:4])
        self.play(
            *[
                ReplacementTransform(
                    b,
                    ext_boxI3
                ) for b in boxesI313
            ]
        )
        self.wait()
        self.play(*[FadeOut(b) for b in boxesI313])
        
        I4 = MathTex(
            r"I = ",
            r"0,5", # 1
        )

        self.play(
            Write(I4.next_to(I3, DOWN))
        )
        self.wait()             
        
        boxI41 = SurroundingRectangle(I4[1])
        
        self.play(
            ReplacementTransform(ext_boxI3, boxI41),
        )
        self.wait()
        self.play(FadeOut(ext_boxI3))

        boxI4 = SurroundingRectangle(I4)
        self.play(ReplacementTransform(boxI41, boxI4))
        self.wait()
        self.play(FadeOut(boxI41))
        
        
        
        
