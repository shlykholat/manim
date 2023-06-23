from manim import *

class MyScene(Scene):
    def construct(self):
        # create a circle
        circle = Circle(radius=1, color=BLUE)

        # animate the circle to grow in size
        self.play(Create(circle))
        self.play(circle.animate.scale(2))

        # wait for a few seconds
        self.wait(2)

        # animate the circle to shrink in size and fade away
        self.play(circle.animate.scale(0.5).fade(1))

if __name__ == "__main__":
    # render the scene as a video
    MyScene().render()
