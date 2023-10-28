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
    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
        svg_loc = "/Users/dn/Documents/pics/svg/subscribe.svg"
        sub_pic = SVGMobject(svg_loc)
        sub_scale = 0.85
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
        png_loc = "/Users/dn/Documents/pics/png/sabonner.png"
        sub_pic = ImageMobject(png_loc)
        sub_scale = 0.45
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"

    sub = Paragraph(written, phon, line_spacing=0.5)
    self.play(GrowFromCenter(sub))
    self.wait(0.25)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.wait(0.25)

    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(0.25)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(0.25)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 3))
    self.wait(0.25)
        
    self.play(ReplacementTransform(part, full), run_time=3)
    self.wait(0.25) 
    self.play(FadeOut(full))
    
    disp_sub(self, lang)

    

class UnitRoots(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        msg = "Racines de l'unité "
        title = Title(f"{msg} avec Manim {manim.__version__}")
        self.add(title)
        
        svg_loc = "/Users/dn/Documents/pics/svg/Youtube_shorts.svg"
        youtube_shorts = SVGMobject(
            svg_loc,
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))

        #plane = ComplexPlane().add_coordinates()
        plane = ComplexPlane()
        self.play(Write(plane))

        def equation_title(old_eq, new_msg, time):
            msg = new_msg
            new_eq = Title(f"{msg}")
            self.play(ReplacementTransform(old_eq, new_eq))
            self.wait(time)
            return new_eq

        def get_msg_s(n):
            exp1 = "= e^{\\frac{2\\times {"
            exp2 = "}\\times i\\pi}{"
            msg_s = [
                f"z_{k}" + exp1 + f"{k}" + exp2 + f"{n}" + "}" for k in range(n)
            ]
            return msg_s

        def get_labs(n, re_z, msg_s, dots, size):
            labs = list(range(n))
            #print("len(labs) =", len(labs))
            for k in range(n):
                if k < n // 2 and re_z[k] > 0:
                    labs[k] = MathTex(
                        msg_s[k],
                        font_size=size
                    ).next_to(dots[k], UR, 0.1)
                elif k < n // 2 and re_z[k] <= 0:
                    labs[k] = MathTex(
                        msg_s[k],
                        font_size=size
                    ).next_to(dots[k], UL, 0.1)
                elif k >= n // 2 and re_z[k] <= 0:
                    labs[k] = MathTex(
                        msg_s[k],
                        font_size=size
                    ).next_to(dots[k], DL, 0.1)
                elif k >= n // 2 and re_z[k] > 0:
                    labs[k] = MathTex(
                        msg_s[k],
                        font_size=size
                    ).next_to(dots[k], DR, 0.1)
                #print("Inside get_labs(n, re_z, msg_s, dots)", k, labs[k])
            return labs

        def write_dots_labs(dots, labs, action):
            if action == 1:
                self.play(*[Write(d) for d in dots])
                self.wait(0.25)
                self.play(*[Write(l) for l in labs])
            elif action == -1:
                self.play(*[Unwrite(d) for d in dots])
                self.wait(0.25)
                self.play(*[Unwrite(l) for l in labs])

        def get_regular_polygon(n_gon):
            angle = (360 / n_gon) * DEGREES
            poly_n_gon = RegularPolygon(
                n = n_gon,
                start_angle = angle,
                color = RED
            )
            return poly_n_gon

        def simplify_labs(old_labs, new_labs, time):
            for i in range(len(new_labs)):
                self.play(
                    ReplacementTransform(
                        old_labs[i],
                        new_labs[i]
                    )
                )
                self.wait(time)

        def disp_dots_and_labs(re_z, j_im_z):
            n = len(re_z)
            size = 200 // n
            # STEP 3: build the complex number list
            z_k = [re_z[i] + j_im_z[i] for i in range(n)]

            # STEP 4: get the messages
            msg_s = get_msg_s(n)

            # STEP 5: create the dots
            dots = [
                Dot(
                    plane.n2p(z_k[k]),
                    color=YELLOW) for k in range(n)
            ]

            # STEP 6: make labels related to dots
            labs = get_labs(n, re_z, msg_s, dots, size)

            # STEP 7: write dots and labels
            action = 1
            write_dots_labs(dots, labs, action)
            
            return z_k, dots, labs
            
        
        # STEP 1: define title 
        old_eq, new_msg, time = title, "$z^{6} = 1$ ", 0.5
        new_eq = equation_title(old_eq, new_msg, time)

        # STEP 2: get cartesian coordinates
        re_z = [1, 0.5, -0.5, -1, -0.5, 0.5]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        j_im_z = [0j, 0.87j, 0.87j, 0j, -0.87j, -0.87j]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(j_im_z))]
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(0.5)

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{i\\pi}{3}}}"
        s_msg2 = "z_2 = e^{\\frac{2i\\pi}{3}}}"
        s_msg3 = "z_3 = -1"
        s_msg4 = "z_4 = e^{\\frac{-2i\\pi}{3}}}"
        s_msg5 = "z_5 = e^{\\frac{-i\\pi}{3}}}"
        s_msg_s = [s_msg0, s_msg1, s_msg2, s_msg3, s_msg4, s_msg5] 

        # STEP 10: turn simplified messages into labels
        size = 40
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=0.25)

        # STEP 11: unwrite
        write_dots_labs(dots, s_labs, action=-1)
        self.wait(0.15)
        self.play(Unwrite(poly_n_gon))
        self.wait(0.15)        

        ############################################################
        
        # STEP 1: define title 
        old_eq, new_msg, time = new_eq, "$z^{7} = 1$ ", 0.5
        new_eq = equation_title(old_eq, new_msg, time)

        # STEP 2: get cartesian coordinates
        re_z = [1, 0.6235, -0.2225, -0.901, -0.901, -0.2225, 0.6235]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        j_im_z = [
            0j, 0.7818j, 0.9749j, 0.4339j, -0.4339j, -0.9749j, -0.7818j
        ]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(j_im_z))]
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(0.5) 

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{2i\\pi}{7}}}"
        s_msg2 = "z_2 = e^{\\frac{4i\\pi}{7}}}"
        s_msg3 = "z_3 = e^{\\frac{6i\\pi}{7}}}"
        s_msg4 = "z_4 = e^{\\frac{-6i\\pi}{7}}}"
        s_msg5 = "z_5 = e^{\\frac{-4i\\pi}{7}}}"
        s_msg6 = "z_6 = e^{\\frac{-2i\\pi}{7}}}"
        s_msg_s = [
            s_msg0, s_msg1, s_msg2, s_msg3, s_msg4, s_msg5, s_msg6
        ] 

        # STEP 10: turn simplified messages into labels
        size = 40
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=0.25)

        # STEP 11: unwrite
        action = -1
        write_dots_labs(dots, s_labs, action)
        self.wait(0.15)
        self.play(Unwrite(poly_n_gon))
        self.wait(0.15)

        ############################################################
        
        # STEP 1: define title 
        old_eq, new_msg, time = new_eq, "$z^{8} = 1$ ", 0.5
        new_eq = equation_title(old_eq, new_msg, time)

        # STEP 2: get cartesian coordinates
        re_z = [1, 0.7071, 0, -0.7071, -1, -0.7071, 0, 0.7071]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        j_im_z = [0j, 0.7071j, 1j, 0.7071j, 0j, -0.7071j, -1j, -0.7071j]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(re_z))]
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(0.5) 

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{i\\pi}{4}}}"
        s_msg2 = "z_2 = i"
        s_msg3 = "z_3 = e^{\\frac{3i\\pi}{4}}}"
        s_msg4 = "z_4 = -1"
        s_msg5 = "z_5 = e^{\\frac{-3i\\pi}{4}}}"
        s_msg6 = "z_6 = -i"
        s_msg7 = "z_7 = e^{\\frac{-i\\pi}{4}}}"
        s_msg_s = [
            s_msg0, s_msg1, s_msg2, s_msg3,
            s_msg4, s_msg5, s_msg6, s_msg7
        ] 

        # STEP 10: turn simplified messages into labels
        size = 40
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=0.25)

        # STEP 11: unwrite
        action = -1
        write_dots_labs(dots, s_labs, action)
        self.wait(0.15)
        self.play(Unwrite(poly_n_gon))
        self.wait(0.15)
        
        disp_sub(self, lang='fr')

        
