from manim import *

class MyGraph(Scene):
    def construct(self):
        # create axes
        x_min = -5
        x_max = 5
        y_min = -3
        y_max = 3
        x_axis = NumberLine(x_range=[x_min, x_max], length=8, include_ticks=True, include_numbers=True)
        y_axis = NumberLine(x_range=[y_min, y_max], length=6, include_ticks=True, include_numbers=True)
        x_axis.add_numbers()
        y_axis.add_numbers()
        axes = VGroup(x_axis, y_axis).arrange(RIGHT)

        # create function and graph
        func = lambda x: 0.5 * x**3 - x
        graph = FunctionGraph(func, x_range=(-2, 2), color=BLUE)

        # create a dot to track the function
        dot = Dot().move_to(graph.points[1], UP)

        # create labels for the function and the dot
        label = MathTex("y = 0.5x^3 - x").to_edge(UP)
        dot_label = MathTex("x = 1, y = -0.5").next_to(dot, RIGHT)

        # add everything to the scene
        self.play(Create(axes), Create(graph), Create(dot))
        self.play(Create(label))
        self.wait()
        self.play(MoveAlongPath(dot, graph), Write(dot_label))
        self.wait()

if __name__ == "__main__":
    MyGraph().render()
