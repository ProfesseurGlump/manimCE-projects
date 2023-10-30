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
    self.wait(1)
    self.play(FadeOut(sub))
    self.add(sub_pic.scale(sub_scale))
    self.wait(1)

    
def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 2.5))
    self.wait(1)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(1)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 1.5))
    self.wait(1)
        
    self.play(ReplacementTransform(part, full), run_time=1.5)
    self.wait(1) 
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
                "z_{" + f"{k}" + "}" + exp1 + f"{k}" + exp2 + f"{n}" + "}" for k in range(n)
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
                self.wait(1)
                self.play(*[Write(l) for l in labs])
            elif action == -1:
                self.play(*[Unwrite(d) for d in dots])
                self.wait(1)
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
            self.play(
                *[
                    ReplacementTransform(
                        old_labs[i],
                        new_labs[i]
                    ) for i in range(len(new_labs))
                ]
            )
            self.wait(time)
                      

        def disp_dots_and_labs(re_z, j_im_z):
            n = len(re_z)
            size = 360 // n
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
        old_eq, new_msg, time = title, "$z^{12} = 1$ ", 1
        new_eq = equation_title(old_eq, new_msg, time)


        # STEP 2: get cartesian coordinates
        re_z = [
            1, 0.86603, 0.5, 0, -0.5, -0.86603,
            -1, -0.86603, -0.5, 0, 0.5, 0.86603
        ]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        
        j_im_z = [
            0j, 0.5j, 0.86603j, 1j, 0.86603j, 0.5j,
            0j, -0.5j, -0.86603j, -1j, -0.86603j, -0.5j 
        ]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(re_z))]
        
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(1.5) 

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{i\\pi}{6}}}"
        s_msg2 = "z_2 = e^{\\frac{i\\pi}{3}}}"
        s_msg3 = "z_3 = i"
        s_msg4 = "z_4 = e^{\\frac{2i\\pi}{3}}}"
        s_msg5 = "z_5 = e^{\\frac{5i\\pi}{6}}}"
        s_msg6 = "z_6 = -1"
        s_msg7 = "z_7 = e^{\\frac{-5i\\pi}{6}}}"
        s_msg8 = "z_8 = e^{\\frac{-2i\\pi}{3}}}"
        s_msg9 = "z_9 = e^{\\frac{-2i\\pi}{3}}}"
        s_msg10 = "z_{10} = e^{\\frac{-i\\pi}{3}}}"
        s_msg11 = "z_{11} = e^{\\frac{-i\\pi}{6}}}"
        s_msg_s = [
            s_msg0, s_msg1, s_msg2, s_msg3, s_msg4, s_msg5,
            s_msg6, s_msg7, s_msg8, s_msg9, s_msg10, s_msg11
        ] 

        # STEP 10: turn simplified messages into labels
        size = 360 // n
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=1)

        # STEP 11: unwrite
        action = -1
        write_dots_labs(dots, s_labs, action)
        self.wait(1)
        self.play(Unwrite(poly_n_gon))
        self.wait(1)

        # STEP 1: define title 
        old_eq, new_msg, time = new_eq, "$z^{13} = 1$ ", 1
        new_eq = equation_title(old_eq, new_msg, time)


        # STEP 2: get cartesian coordinates
        re_z = [
            1, 0.88546, 0.56806, 0.12054, -0.3546, -0.74851,
            -0.970904,
            -0.97094, -0.74851, -0.3546, 0.12054, 0.56806, 0.88546
        ]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        j_im_z = [
            0j, 0.46472j, 0.82298j, 0.99271j, 0.93502j, 0.66312j,
            0.23932j,
            -0.23932j, -0.66312j, -0.93502j, -0.9927j, -0.82298j, -0.46472j
        ]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(re_z))]
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(1.5) 

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{2i\\pi}{13}}}"
        s_msg2 = "z_2 = e^{\\frac{4i\\pi}{13}}}"
        s_msg3 = "z_3 = e^{\\frac{6i\\pi}{13}}}"
        s_msg4 = "z_4 = e^{\\frac{8i\\pi}{13}}}"
        s_msg5 = "z_5 = e^{\\frac{10i\\pi}{13}}}"
        s_msg6 = "z_6 = e^{\\frac{12i\\pi}{13}}}"
        s_msg7 = "z_7 = e^{\\frac{-12i\\pi}{13}}}"
        s_msg8 = "z_8 = e^{\\frac{-10i\\pi}{13}}}"
        s_msg9 = "z_9 = e^{\\frac{-8i\\pi}{13}}}"
        s_msg10 = "z_{10} = e^{\\frac{-6i\\pi}{13}}}"
        s_msg11 = "z_{11} = e^{\\frac{-4i\\pi}{13}}}"
        s_msg12 = "z_{12} = e^{\\frac{-2i\\pi}{13}}}"
        s_msg_s = [
            s_msg0, s_msg1, s_msg2, s_msg3, s_msg4, s_msg5,
            s_msg6,
            s_msg7, s_msg8, s_msg9, s_msg10, s_msg11, s_msg12
        ] 

        # STEP 10: turn simplified messages into labels
        size = 360 // n
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=1)

        # STEP 11: unwrite
        action = -1
        write_dots_labs(dots, s_labs, action)
        self.wait(1)
        self.play(Unwrite(poly_n_gon))
        self.wait(1)

        # STEP 1: define title 
        old_eq, new_msg, time = new_eq, "$z^{14} = 1$ ", 1
        new_eq = equation_title(old_eq, new_msg, time)


        # STEP 2: get cartesian coordinates
        re_z = [
            1, 0.90097, 0.62349, 0.22252, -0.22252, -0.62349, -0.90097,
            -1, -0.90097, -0.62349, -0.22252, 0.22252, 0.62349, 0.90097
        ]
        scale_fact = 2.5
        re_z = [scale_fact * re_z[i] for i in range(len(re_z))]
        j_im_z = [
            0j, 0.43388j, 0.78183j, 0.97493j, 0.97493j, 0.78183j, 0.43388j,
            0j, -0.43388j, -0.78183j, -0.97493j, -0.97493j, -0.78183j, -0.43388j
        ]
        j_im_z = [scale_fact * j_im_z[i] for i in range(len(re_z))]
        n = len(re_z)

        # STEP 3 TO 7
        z_k, dots, labs = disp_dots_and_labs(re_z, j_im_z)

        # STEP 8: create the regular n-polygon
        poly_n_gon = get_regular_polygon(n_gon=n)
        self.play(Write(poly_n_gon.scale(scale_fact)))
        self.wait(1.5) 

        # STEP 9: create simplified messages
        s_msg0 = "z_0 = 1"
        s_msg1 = "z_1 = e^{\\frac{i\\pi}{7}}}"
        s_msg2 = "z_2 = e^{\\frac{2i\\pi}{7}}}"
        s_msg3 = "z_3 = e^{\\frac{3i\\pi}{7}}}"
        s_msg4 = "z_4 = e^{\\frac{4i\\pi}{7}}}"
        s_msg5 = "z_5 = e^{\\frac{5i\\pi}{7}}}"
        s_msg6 = "z_6 = e^{\\frac{6i\\pi}{7}}}"
        s_msg7 = "z_7 = -1"
        s_msg8 = "z_8 = e^{\\frac{-6i\\pi}{7}}}"
        s_msg9 = "z_9 = e^{\\frac{-5i\\pi}{7}}}"
        s_msg10 = "z_{10} = e^{\\frac{-4i\\pi}{7}}}"
        s_msg11 = "z_{11} = e^{\\frac{-3i\\pi}{7}}}"
        s_msg12 = "z_{12} = e^{\\frac{-2i\\pi}{7}}}"
        s_msg13 = "z_{13} = e^{\\frac{-i\\pi}{7}}}"
        s_msg_s = [
            s_msg0, s_msg1, s_msg2, s_msg3, s_msg4, s_msg5, s_msg6,
            s_msg7, s_msg8, s_msg9, s_msg10, s_msg11, s_msg12, s_msg13
        ] 

        # STEP 10: turn simplified messages into labels
        size = 360 // n
        s_labs = get_labs(n, re_z, s_msg_s, dots, size)
        simplify_labs(old_labs=labs, new_labs=s_labs, time=1)

        # STEP 11: unwrite
        action = -1
        write_dots_labs(dots, s_labs, action)
        self.wait(1)
        self.play(Unwrite(poly_n_gon))
        self.wait(1)
        
        disp_sub(self, lang='fr')

        
