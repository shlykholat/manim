from manim import *

class MyScene(Scene):
    def construct(self):
        # create shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Polygon(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0]),
            color=YELLOW
        )

        # add shapes to the scene
        self.add(circle, square, triangle)

        # animate shapes
        self.play(circle.animate.shift(UP).rotate(PI/4))
        self.play(square.animate.scale(2).set_color(GREEN))
        self.play(triangle.animate.rotate(-PI/2))

if __name__ == "__main__":
    MyScene().render()
