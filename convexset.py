from manim import *
import numpy as np

# class TriangleAsConvexSet(Scene):
#     def construct(self):
#         # Définition du centre et du rayon du cercle
#         center = np.array([0, 0, 0])
#         radius = 3

#         # Création de l'objet graphique représentant le cercle
#         circle = Circle(radius=radius)
#         circle.set_color(BLUE)
#         self.add(circle)

#         # Création des objets graphiques représentant les points
#         point_A = Dot(center + radius*np.array([1, 0, 0]))
#         point_A.set_color(WHITE)
#         point_B = Dot(center + radius*np.array([-0.5, np.sqrt(3)/2, 0]))
#         point_B.set_color(WHITE)
#         point_C = Dot(center + radius*np.array([-0.5, -np.sqrt(3)/2, 0]))
#         point_C.set_color(WHITE)

#         # Création des objets graphiques représentant les segments de droite
#         segment_AB = Line(point_A.get_center(), point_B.get_center())
#         segment_AB.set_color(WHITE)
#         segment_BC = Line(point_B.get_center(), point_C.get_center())
#         segment_BC.set_color(WHITE)
#         segment_CA = Line(point_C.get_center(), point_A.get_center())
#         segment_CA.set_color(WHITE)

#         # Création des objets graphiques représentant les rayons
#         ray_A = Line(center, point_A.get_center())
#         ray_A.set_color(RED)
#         ray_B = Line(center, point_B.get_center())
#         ray_B.set_color(RED)
#         ray_C = Line(center, point_C.get_center())
#         ray_C.set_color(RED)

#         # Ajout des objets graphiques à la scène
#         self.play(
#             Create(point_A),
#             run_time=2
#         )
#         self.play(
#             Create(point_B),
#             run_time=2
#         )
#         self.play(
#             Create(point_C),
#             run_time=2
#         )
#         self.play(
#             Create(segment_AB),
#             run_time=2
#         )
#         self.play(
#             Create(segment_BC),
#             run_time=2
#         )
#         self.play(
#             Create(segment_CA),
#             run_time=2
#         )
#         self.play(
#             Create(ray_A),
#             run_time=2
#         )
#         self.play(
#             Create(ray_B),
#              run_time=2
#         )
#         self.play(
#             Create(ray_C),
#             run_time=2
#         )


# class SquareAsConvexSet(Scene):
#     def construct(self):
#         # Définition du centre et du rayon du cercle
#         center = np.array([0, 0, 0])
#         radius = 3

#         # Création de l'objet graphique représentant le cercle
#         circle = Circle(radius=radius)
#         circle.set_color(BLUE)
#         self.add(circle)

#         # Création des objets graphiques représentant les points
#         point_A = Dot(center + radius*np.array([1, 0, 0]))
#         point_A.set_color(WHITE)

#         point_B = Dot(center + radius*np.array([0, 1, 0]))
#         point_B.set_color(WHITE)

#         point_C = Dot(center + radius*np.array([-1, 0, 0]))
#         point_C.set_color(WHITE)

#         point_D = Dot(center + radius*np.array([0, -1, 0]))
#         point_D.set_color(WHITE)


#         # Création des objets graphiques représentant les segments de droite
#         segment_AB = Line(point_A.get_center(), point_B.get_center())
#         segment_AB.set_color(WHITE)
#         segment_BC = Line(point_B.get_center(), point_C.get_center())
#         segment_BC.set_color(WHITE)
#         segment_CD = Line(point_C.get_center(), point_D.get_center())
#         segment_CD.set_color(WHITE)
#         segment_DA = Line(point_D.get_center(), point_A.get_center())
#         segment_DA.set_color(WHITE)

#         # Création des objets graphiques représentant les rayons
#         ray_A = Line(center, point_A.get_center())
#         ray_A.set_color(RED)
#         ray_B = Line(center, point_B.get_center())
#         ray_B.set_color(RED)
#         ray_C = Line(center, point_C.get_center())
#         ray_C.set_color(RED)
#         ray_D = Line(center, point_D.get_center())
#         ray_D.set_color(RED)
        
#         # Ajout des objets graphiques à la scène
#         self.play(
#             Create(point_A),
#             run_time=2
#         )
#         self.play(
#             Create(point_B),
#             run_time=2
#         )
#         self.play(
#             Create(point_C),
#             run_time=2
#         )
#         self.play(
#             Create(point_D),
#             run_time=2
#         )
#         self.play(
#             Create(segment_AB),
#             run_time=2
#         )
#         self.play(
#             Create(segment_BC),
#             run_time=2
#         )
#         self.play(
#             Create(segment_CD),
#             run_time=2
#         )
#         self.play(
#             Create(segment_DA),
#             run_time=2
#         )
#         self.play(
#             Create(ray_A),
#             run_time=2
#         )
#         self.play(
#             Create(ray_B),
#              run_time=2
#         )
#         self.play(
#             Create(ray_C),
#             run_time=2
#         )
#         self.play(
#             Create(ray_D),
#             run_time=2
#         )


# class PentagonAsConvexSet(Scene):
#     def construct(self):
#         # Définition du centre et du rayon du cercle
#         center = np.array([0, 0, 0])
#         radius = 3

#         # Création de l'objet graphique représentant le cercle
#         circle = Circle(radius=radius)
#         circle.set_color(BLUE)
#         self.add(circle)

#         # Création des objets graphiques représentant les points
#         point_A = Dot(np.array([(3*np.exp(2j*0*np.pi/5)).real, (3*np.exp(2j*0*np.pi/5)).imag, 0]))
#         point_B = Dot(np.array([(3*np.exp(2j*np.pi/5)).real, (3*np.exp(2j*np.pi/5)).imag, 0]))
#         point_C = Dot(np.array([(3*np.exp(4j*np.pi/5)).real, (3*np.exp(4j*np.pi/5)).imag, 0]))
#         point_D = Dot(np.array([(3*np.exp(6j*np.pi/5)).real, (3*np.exp(6j*np.pi/5)).imag, 0]))
#         point_E = Dot(np.array([(3*np.exp(8j*np.pi/5)).real, (3*np.exp(8j*np.pi/5)).imag, 0]))




#         # Création des objets graphiques représentant les segments de droite
#         segment_AB = Line(point_A.get_center(), point_B.get_center())
#         segment_AB.set_color(WHITE)
#         segment_BC = Line(point_B.get_center(), point_C.get_center())
#         segment_BC.set_color(WHITE)
#         segment_CD = Line(point_C.get_center(), point_D.get_center())
#         segment_CD.set_color(WHITE)
#         segment_DE = Line(point_D.get_center(), point_E.get_center())
#         segment_DE.set_color(WHITE)
#         segment_EA = Line(point_E.get_center(), point_A.get_center())
#         segment_EA.set_color(WHITE)

#         # Création des objets graphiques représentant les rayons
#         ray_A = Line(center, point_A.get_center())
#         ray_A.set_color(RED)
#         ray_B = Line(center, point_B.get_center())
#         ray_B.set_color(RED)
#         ray_C = Line(center, point_C.get_center())
#         ray_C.set_color(RED)
#         ray_D = Line(center, point_D.get_center())
#         ray_D.set_color(RED)
#         ray_E = Line(center, point_E.get_center())
#         ray_E.set_color(RED)
        
#         # Ajout des objets graphiques à la scène
#         self.play(
#             Create(point_A),
#             run_time=2
#         )
#         self.play(
#             Create(point_B),
#             run_time=2
#         )
#         self.play(
#             Create(point_C),
#             run_time=2
#         )
#         self.play(
#             Create(point_D),
#             run_time=2
#         )
#         self.play(
#             Create(point_E),
#             run_time=2
#         )
#         self.play(
#             Create(segment_AB),
#             run_time=2
#         )
#         self.play(
#             Create(segment_BC),
#             run_time=2
#         )
#         self.play(
#             Create(segment_CD),
#             run_time=2
#         )
#         self.play(
#             Create(segment_DE),
#             run_time=2
#         )
#         self.play(
#             Create(segment_EA),
#             run_time=2
#         )
#         self.play(
#             Create(ray_A),
#             run_time=2
#         )
#         self.play(
#             Create(ray_B),
#              run_time=2
#         )
#         self.play(
#             Create(ray_C),
#             run_time=2
#         )
#         self.play(
#             Create(ray_D),
#             run_time=2
#         )
#         self.play(
#             Create(ray_E),
#             run_time=2
#         )


# class HexagonAsConvexSet(Scene):
#     def construct(self):
#         # Définition du centre et du rayon du cercle
#         center = np.array([0, 0, 0])
#         radius = 3

#         # Création de l'objet graphique représentant le cercle
#         circle = Circle(radius=radius)
#         circle.set_color(BLUE)
#         self.add(circle)

#         # Création des objets graphiques représentant les points
#         point_A = Dot(np.array([(3*np.exp(2j*0*np.pi/6)).real, (3*np.exp(2j*0*np.pi/6)).imag, 0]))
#         point_B = Dot(np.array([(3*np.exp(2j*np.pi/6)).real, (3*np.exp(2j*np.pi/6)).imag, 0]))
#         point_C = Dot(np.array([(3*np.exp(4j*np.pi/6)).real, (3*np.exp(4j*np.pi/6)).imag, 0]))
#         point_D = Dot(np.array([(3*np.exp(6j*np.pi/6)).real, (3*np.exp(6j*np.pi/6)).imag, 0]))
#         point_E = Dot(np.array([(3*np.exp(8j*np.pi/6)).real, (3*np.exp(8j*np.pi/6)).imag, 0]))
#         point_F = Dot(np.array([(3*np.exp(10j*np.pi/6)).real, (3*np.exp(10j*np.pi/6)).imag, 0]))

#         # Création des objets graphiques représentant les segments de droite
#         segment_AB = Line(point_A.get_center(), point_B.get_center())
#         segment_AB.set_color(WHITE)
#         segment_BC = Line(point_B.get_center(), point_C.get_center())
#         segment_BC.set_color(WHITE)
#         segment_CD = Line(point_C.get_center(), point_D.get_center())
#         segment_CD.set_color(WHITE)
#         segment_DE = Line(point_D.get_center(), point_E.get_center())
#         segment_DE.set_color(WHITE)
#         segment_EF = Line(point_E.get_center(), point_F.get_center())
#         segment_EF.set_color(WHITE)
#         segment_FA = Line(point_F.get_center(), point_A.get_center())
#         segment_FA.set_color(WHITE)

        
#         # Création des objets graphiques représentant les rayons
#         ray_A = Line(center, point_A.get_center())
#         ray_A.set_color(RED)
#         ray_B = Line(center, point_B.get_center())
#         ray_B.set_color(RED)
#         ray_C = Line(center, point_C.get_center())
#         ray_C.set_color(RED)
#         ray_D = Line(center, point_D.get_center())
#         ray_D.set_color(RED)
#         ray_E = Line(center, point_E.get_center())
#         ray_E.set_color(RED)
#         ray_F = Line(center, point_F.get_center())
#         ray_F.set_color(RED)
        
#         # Ajout des objets graphiques à la scène
#         self.play(
#             Create(point_A),
#             run_time=2
#         )
#         self.play(
#             Create(point_B),
#             run_time=2
#         )
#         self.play(
#             Create(point_C),
#             run_time=2
#         )
#         self.play(
#             Create(point_D),
#             run_time=2
#         )
#         self.play(
#             Create(point_E),
#             run_time=2
#         )
#         self.play(
#             Create(point_F),
#             run_time=2
#         )
#         self.play(
#             Create(segment_AB),
#             run_time=2
#         )
#         self.play(
#             Create(segment_BC),
#             run_time=2
#         )
#         self.play(
#             Create(segment_CD),
#             run_time=2
#         )
#         self.play(
#             Create(segment_DE),
#             run_time=2
#         )
#         self.play(
#             Create(segment_EF),
#             run_time=2
#         )
#         self.play(
#             Create(segment_FA),
#             run_time=2
#         )
#         self.play(
#             Create(ray_A),
#             run_time=2
#         )
#         self.play(
#             Create(ray_B),
#              run_time=2
#         )
#         self.play(
#             Create(ray_C),
#             run_time=2
#         )
#         self.play(
#             Create(ray_D),
#             run_time=2
#         )
#         self.play(
#             Create(ray_E),
#             run_time=2
#         )
#         self.play(
#             Create(ray_F),
#             run_time=2
#         )


class PolygonAsConvexSet(Scene):
    def construct(self, n):
        # Définition du centre et du rayon du cercle
        center = np.array([0, 0, 0])
        radius = 3

        # Création de l'objet graphique représentant le cercle
        circle = Circle(radius=radius)
        circle.set_color(BLUE)
        self.add(circle)

        # Création des objets graphiques représentant les points
        points = []
        for k in range(n):
            point = Dot(np.array([(3*np.exp(2j*k*np.pi/n)).real, (3*np.exp(2j*k*np.pi/n)).imag, 0]))
            points.append(point)

        # Création des objets graphiques représentant les segments de droite
        segments = []
        for k in range(n):
            segment = Line(points[k].get_center(), points[(k+1)%n].get_center())
            segment.set_color(WHITE)
            segments.append(segment)

        # Création des objets graphiques représentant les rayons
        rays = []
        for k in range(n):
            ray = Line(center, points[k].get_center())
            ray.set_color(RED)
            rays.append(ray)
        
        # Ajout des objets à la scène
        self.play(
            *[Create(point) for point in points],
            run_time=2
        )
        self.play(
            *[Create(segment) for segment in segments],
            run_time=2
        )
        self.play(
            *[Create(ray) for ray in rays],
            run_time=2
        )
        # Remplissage de l'intérieur du polygone
        interior = Polygon(*[point.get_center() for point in points])
        interior.set_fill(RED, 1)
        self.play(Create(interior), run_time=2)
        self.wait()


class TriangleAsConvexSet(PolygonAsConvexSet):
    def construct(self):
        super().construct(3)

class SquareAsConvexSet(PolygonAsConvexSet):
    def construct(self):
        super().construct(4)

class PentagonAsConvexSet(PolygonAsConvexSet):
    def construct(self):
        super().construct(5)

class HexagonAsConvexSet(PolygonAsConvexSet):
    def construct(self):
        super().construct(6)        
        
