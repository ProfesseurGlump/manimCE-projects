from manim import *
import manim
import networkx as nx
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
    like_svg_path = "~/Documents/pics/svg/like.svg"
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    jpg_png_path = "~/Documents/pics/png/sabonner.png"
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        sub_pic = SVGMobject(sub_svg_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        sub_pic = ImageMobject(jpg_png_path)
        like_pic = SVGMobject(like_svg_path)
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(.5)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.add(like_pic.scale(sub_scale).next_to(sub_pic, LEFT))
    self.wait(0.1)



    
def put_sub_logo(self, svg_scale=0.25):
    sub_svg_path = "~/Documents/pics/svg/subscribe.svg"
    sub_pic = SVGMobject(sub_svg_path)
    self.play(
        FadeIn(
            sub_pic.scale(svg_scale).to_edge(2.5*UP)
        )
    )
    return sub_pic


    
def put_like_logo(self, sub_pic, svg_scale=0.25):
    like_svg_path = "~/Documents/pics/svg/like.svg"
    like_pic = SVGMobject(like_svg_path)
    self.play(
        FadeIn(
            like_pic.scale(svg_scale).next_to(sub_pic, LEFT)
        )
    )
    return like_pic


    
def put_youtube_short_logo(self, sub_pic, svg_scale=0.25):
    youtube_short_path = "~/Documents/pics/svg/Youtube_shorts.svg"
    youtube_shorts = SVGMobject(
        youtube_short_path,
        fill_opacity=1,
        fill_color=RED
    ).scale(svg_scale)
    self.play(
        FadeIn(
            youtube_shorts.next_to(sub_pic, RIGHT)
        )
    )
    return youtube_shorts


    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(2.5)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 2.5))
    self.wait(2.5)
        
    self.play(ReplacementTransform(part, full), run_time=2.5)
    self.wait(2.5)
    self.play(FadeOut(full))
    
    disp_sub(self, lang)


    


    
class LinearFreedom(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title_start = Title("Les vecteurs sont-ils libres ou PAS ?")
        self.add(title_start.scale(0.85))
        sub_pic = put_sub_logo(self)

        plane = NumberPlane()

        vect_1 = Vector([1, 0], color=YELLOW)
        vect_2 = Vector([3, 0], color=RED)
        label_1 = vect_1.coordinate_label(color=YELLOW)
        label_2 = vect_2.coordinate_label(color=RED)

        self.play(Create(plane))
        self.wait(0.5)
        self.play(
            Write(vect_1),
            Write(vect_2),
            Write(label_1),
            Write(label_2)
        )
        self.wait(2)
        # C-x C-t transpose line
        ent_A = [
            [1, 0],
            [3, 0]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=0, initial_scale_factor=1)
        self.add(A.next_to(plane, DOWN))
        self.play(Write(det_A.next_to(plane, DOWN)))
        self.wait(0.75)
        msg = "det = 0 \\iff \\mbox{vecteurs PAS libres}"
        msg = MathTex(msg).next_to(plane, DOWN)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))
        
        vect_3 = Vector([3, 1], color=GREEN)
        label_3 = vect_3.coordinate_label(color=GREEN)

        self.play(
            ReplacementTransform(vect_2, vect_3),
            ReplacementTransform(label_2, label_3),
        )
        self.wait(2)
        ent_A = [
            [1, 0],
            [3, 1]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=1, initial_scale_factor=1)
        self.add(A.next_to(plane, UP))
        self.play(Write(det_A.next_to(plane, UP)))
        self.wait(0.75)
        msg = "det \\neq 0 \\iff \\mbox{vecteurs libres}"
        msg = MathTex(msg).next_to(plane, UP)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))

        vect_4 = Vector([0, 2], color=GREEN)
        label_4 = vect_4.coordinate_label(color=GREEN)

        self.play(
            ReplacementTransform(vect_3, vect_4),
            ReplacementTransform(label_3, label_4),
        )
        self.wait(2)
        ent_A = [
            [1, 0],
            [0, 2]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=2, initial_scale_factor=1)
        self.add(A.next_to(plane, UP))
        self.play(Write(det_A.next_to(plane, UP)))
        self.wait(0.75)
        msg = "det \\neq 0 \\iff \\mbox{vecteurs libres}"
        msg = MathTex(msg).next_to(plane, UP)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))

        vect_5 = Vector([-1, 3], color=GREEN)
        label_5 = vect_5.coordinate_label(color=GREEN)

        self.play(
            ReplacementTransform(vect_4, vect_5),
            ReplacementTransform(label_4, label_5),
        )
        self.wait(2)
        ent_A = [
            [1, 0],
            [-1, 3]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=3, initial_scale_factor=1)
        self.add(A.next_to(plane, UP))
        self.play(Write(det_A.next_to(plane, UP)))
        self.wait(0.75)
        msg = "det \\neq 0 \\iff \\mbox{vecteurs libres}"
        msg = MathTex(msg).next_to(plane, UP)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))

        vect_6 = Vector([-2, 0], color=RED)
        label_6 = vect_6.coordinate_label(color=RED)

        self.play(
            ReplacementTransform(vect_5, vect_6),
            ReplacementTransform(label_5, label_6),
        )
        self.wait(2)
        ent_A = [
            [1, 0],
            [-2, 0]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=0, initial_scale_factor=1)
        self.add(A.next_to(plane, DOWN))
        self.play(Write(det_A.next_to(plane, DOWN)))
        self.wait(0.75)
        msg = "det = 0 \\iff \\mbox{vecteurs PAS libres}"
        msg = MathTex(msg).next_to(plane, DOWN)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))

        vect_7 = Vector([-2, -2], color=GREEN)
        label_7 = vect_7.coordinate_label(color=GREEN)

        self.play(
            ReplacementTransform(vect_6, vect_7),
            ReplacementTransform(label_6, label_7),
        )
        self.wait(2)
        ent_A = [
            [1, 0],
            [-2, -2]
        ]
        A = Matrix(ent_A)
        det_A = get_det_text(A, determinant=-2, initial_scale_factor=1)
        self.add(A.next_to(plane, UP))
        self.play(Write(det_A.next_to(plane, UP)))
        self.wait(0.75)
        msg = "det \\neq 0 \\iff \\mbox{vecteurs libres}"
        msg = MathTex(msg).next_to(plane, UP)
        self.play(
            FadeOut(det_A),
            ReplacementTransform(A, msg)
        )
        self.wait(0.75)
        self.play(FadeOut(msg))
        
        title_end = Title("Abonnez-vous parce que ça m'aide à vous aider")
        self.play(ReplacementTransform(title_start, title_end.scale(0.75)))
        disp_sub(self, lang='fr')

       
