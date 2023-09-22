from manim import *
import numpy as np

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
    
        # Ajout des objets
        for point in points:
            self.add(point)
            self.wait(1)
        for segment in segments:
            self.add(segment)
            self.wait(1)
        for ray in rays:
            self.add(ray)
            self.wait(1)
    
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
