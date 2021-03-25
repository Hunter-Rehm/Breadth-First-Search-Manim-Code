#!/usr/bin/env python
import numpy as np
from manimlib.imports import *
from random import randrange
# To watch one of these scenes, run the following:
#cd Python; python3 -m venv ManimEnv; cd ManimEnv; source bin/activate; cd manim; python3 manim.py IntroductionToGraphTheoryAdjacencyandIncidenceMatrix.py AdandIncMatrix -p
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)
def set_background(self):
    background = Rectangle(
    width = FRAME_WIDTH,
    height = FRAME_HEIGHT,
    stroke_width = 0,
    fill_color = BLACK)
    self.add(background)



class BFS(GraphScene):
    CONFIG = {
    "x_min" : -10,
    "x_max" : 10,
    "y_min" : -1.5,
    "y_max" : 1.5,
    "graph_origin" : ORIGIN ,
    "function_color" : WHITE ,
    "axes_color" : WHITE,
    "x_labeled_nums" :range(-10,12,2),
     
    }

    def construct(self):



        #Open up with video introduction
        #### "Hello, my name is Hunter and today I will be introducing how to do a breadth first search through a graph. "

        #Put up the three sections we will go through with their times
        #### " We will start by going through an example, then I will give the algorithm in the abstract, and lastly I will present some psuedocode demonstrating the algorithm with the complexity."

        #Write the word 'example' then show a graph with labelled vertices.
        #### "Consider this graph with the following vertex labeling."
        Example = TextMobject("Breadth First Search").scale(2.5)
        self.wait()
        self.play(Write(Example))
        self.wait()
        self.play(FadeOut(Example))
        self.wait()
        v11 = Dot([-2,2,0], radius = .2)
        v12 = Dot([0,2,0], radius = .2)
        v13 = Dot([2,2,0], radius = .2)
        v21 = Dot([-2,0,0], radius = .2)
        v22 = Dot([0,0,0], radius = .2)
        v23 = Dot([2,0,0], radius = .2)
        v31 = Dot([-2,-2,0], radius = .2)
        v32 = Dot([0,-2,0], radius = .2)
        v33 = Dot([2,-2,0], radius = .2)

        v11label = TextMobject("1",color = BLACK).move_to(v11.get_center()).scale(.75)
        v12label = TextMobject("2",color = BLACK).move_to(v12.get_center()).scale(.75)
        v13label = TextMobject("3",color = BLACK).move_to(v13.get_center()).scale(.75)
        v21label = TextMobject("4",color = BLACK).move_to(v21.get_center()).scale(.75)
        v22label = TextMobject("5",color = BLACK).move_to(v22.get_center()).scale(.75)
        v23label = TextMobject("6",color = BLACK).move_to(v23.get_center()).scale(.75)
        v31label = TextMobject("7",color = BLACK).move_to(v31.get_center()).scale(.75)
        v32label = TextMobject("8",color = BLACK).move_to(v32.get_center()).scale(.75)
        v33label = TextMobject("9",color = BLACK).move_to(v33.get_center()).scale(.75)

        e11_12 = Line(v11.get_center(), v12.get_center())
        e12_13 = Line(v12.get_center(), v13.get_center())
        e21_22 = Line(v21.get_center(), v22.get_center())
        e22_23 = Line(v22.get_center(), v23.get_center())
        e31_32 = Line(v31.get_center(), v32.get_center())
        e32_33 = Line(v32.get_center(), v33.get_center())
        e11_21 = Line(v11.get_center(), v21.get_center())
        e12_22 = Line(v12.get_center(), v22.get_center())
        e13_23 = Line(v13.get_center(), v23.get_center())
        e21_31 = Line(v21.get_center(), v31.get_center())
        e22_32 = Line(v22.get_center(), v32.get_center())
        e23_33 = Line(v23.get_center(), v33.get_center())

        vertices = VGroup(v11,v12,v13,v21,v22,v23,v31,v32,v33)
        edges = VGroup(e11_12,e12_13,e21_22,e22_23,e31_32,e32_33,e11_21,e12_22,e13_23,e21_31,e22_32,e23_33)
        vertexlabels = VGroup(v11label, v12label, v13label, v21label, v22label, v23label, v31label, v32label, v33label)
        graph = VGroup(edges, vertices, vertexlabels).scale(1.5)
        self.play(FadeIn(graph))

        self.wait()
        #Move graph to the left and create a queue, and add the vertex v_1 to the queue "
        #### "We start by selecting a random vertex from our graph and putting that vertex in the queue. Since the one that I selected (at random) was not, then..."
        queue = VGroup(Rectangle(height=6, width=1.5),
                Line([-.75,3 - 6/9,0], [.75,3-6/9,0]),
                Line([-.75,3 - 2*6/9,0], [.75,3-2*6/9,0]),
                Line([-.75,3 - 3*6/9,0], [.75,3-3*6/9,0]),
                Line([-.75,3 - 4*6/9,0], [.75,3-4*6/9,0]),
                Line([-.75,3 - 5*6/9,0], [.75,3-5*6/9,0]),
                Line([-.75,3 - 6*6/9,0], [.75,3-6*6/9,0]),
                Line([-.75,3 - 7*6/9,0], [.75,3-7*6/9,0]),
                Line([-.75,3 - 8*6/9,0], [.75,3-8*6/9,0])
                ).move_to([3,0,0])
        queueword = TextMobject("Queue (visited)").move_to([3,3+ 3/9,0])

        queue1 = TextMobject("1", color = WHITE).move_to([3,3 - 8*6/9-.3,0])
        queue4 = TextMobject("4", color = WHITE).move_to([3,3 - 7*6/9-.3,0])
        queue2 = TextMobject("2", color = WHITE).move_to([3,3 - 6*6/9-.3,0])
        queue5 = TextMobject("5", color = WHITE).move_to([3,3 - 5*6/9-.3,0])
        queue7 = TextMobject("7", color = WHITE).move_to([3,3 - 4*6/9-.3,0])
        queue3 = TextMobject("3", color = WHITE).move_to([3,3 - 3*6/9-.3,0])
        queue8 = TextMobject("8", color = WHITE).move_to([3,3 - 2*6/9-.3,0])
        queue6 = TextMobject("6", color = WHITE).move_to([3,3 - 1*6/9-.3,0])
        queue9 = TextMobject("9", color = WHITE).move_to([3,3 - 0*6/9-.3,0])
        self.wait()
        start = TextMobject("Start").move_to([-5.3+3,2.5,0])
        goal = TextMobject("Goal").move_to([-.7+3,-2.5,0])
        self.play(FadeToColor(v33, GREEN),FadeToColor(v11, BLUE), Write(start), Write(goal))
        self.wait()

        self.play(ApplyMethod(goal.shift,3*LEFT),ApplyMethod(start.shift,3*LEFT),ApplyMethod(vertices.shift,3*LEFT),ApplyMethod(edges.shift,3*LEFT),ApplyMethod(vertexlabels.shift,3*LEFT))
        self.wait()
        self.play(FadeIn(queue), FadeIn(queueword))
        self.wait()
        self.play(Write(queue1))
        self.wait()
        #highlight the neighbors of v_1, and put them on the queue, do this for all neightbors.
        #### "We look at the neighbors of v_1 and put those on our queue. and so on"
        arrow1 = Arrow(np.array([5, -2.7, 0]), np.array([4, -2.7, 0]), buff=0)
        self.play(FadeToColor(v21,BLUE), FadeToColor(v12, BLUE), Write(arrow1))
        self.wait()
        self.play(Write(queue4), Write(queue2))
        self.wait()

        arrow2 = Arrow(np.array([5, -2.7 + 1*6/9, 0]), np.array([4, -2.7+1*6/9, 0]), buff=0)
        self.play(FadeOut(arrow1), Write(arrow2))
        self.wait()
        self.play(FadeToColor(v31,BLUE), FadeToColor(v22, BLUE))
        self.wait()
        self.play(Write(queue7), Write(queue5))
        self.wait()

        arrow3 = Arrow(np.array([5, -2.7 + 2*6/9, 0]), np.array([4, -2.7+2*6/9, 0]), buff=0)
        self.play(FadeOut(arrow2), FadeIn(arrow3))
        self.wait()
        self.play(FadeToColor(v13, BLUE))
        self.wait()
        self.play(FadeIn(queue3))
        self.wait()
        arrow4 = Arrow(np.array([5, -2.7 + 3*6/9, 0]), np.array([4, -2.7+3*6/9, 0]), buff=0)

        self.play(FadeToColor(v32,BLUE), FadeToColor(v23, BLUE), FadeIn(arrow4), FadeOut(arrow3))
        self.wait()
        self.play(FadeIn(queue6), FadeIn(queue8))
        self.wait()
        arrow5 = Arrow(np.array([5, -2.7 + 4*6/9, 0]), np.array([4, -2.7+4*6/9, 0]), buff=0)
        arrow6 = Arrow(np.array([5, -2.7 + 5*6/9, 0]), np.array([4, -2.7+5*6/9, 0]), buff=0)
        self.play(FadeOut(arrow4), FadeIn(arrow5))
        self.wait()
        self.play(FadeOut(arrow5), FadeIn(arrow6))
        self.wait()
        arrow7 = Arrow(np.array([5, -2.7 + 6*6/9, 0]), np.array([4, -2.7+6*6/9, 0]), buff=0)

        self.play(FadeToColor(v33, BLUE), FadeOut(arrow6), FadeIn(arrow7))
        self.wait()
        self.play(FadeIn(queue9))
        self.wait()
        arrow8 = Arrow(np.array([5, -2.7 + 7*6/9, 0]), np.array([4, -2.7+7*6/9, 0]), buff=0)
        arrow9 = Arrow(np.array([5, -2.7 + 8*6/9, 0]), np.array([4, -2.7+8*6/9, 0]), buff=0)
        self.play(FadeIn(arrow8), FadeOut(arrow7))
        self.wait()
        self.play(FadeIn(arrow9), FadeOut(arrow8))
        self.wait()
        yay = TextMobject("Yay!").move_to([1.5, -2.7 + 8*6/9, 0])
        self.play(Write(yay))
        self.play(FadeOut(arrow9))
        self.wait()

        #make all nodes white
        self.play(FadeToColor(v11, WHITE),FadeToColor(v12, WHITE),FadeToColor(v13, WHITE),FadeToColor(v21, WHITE),FadeToColor(v22, WHITE),FadeToColor(v23, WHITE),FadeToColor(v31, WHITE),FadeToColor(v32, WHITE),FadeToColor(v33, WHITE))

        #highlight levels
        level1line = Line([3.75,3-8*6/9,0],[3.75,3-9*6/9,0])
        bracket1 = Brace(mobject = level1line,direction = RIGHT)

        level2line = Line([3.75,3-8*6/9,0],[3.75,3-6*6/9,0])
        bracket2 = Brace(mobject = level2line,direction = RIGHT)

        level3line = Line([3.75,3-6*6/9,0],[3.75,3-3*6/9,0])
        bracket3 = Brace(mobject = level3line,direction = RIGHT)

        level4line = Line([3.75,3-1*6/9,0],[3.75,3-3*6/9,0])
        bracket4 = Brace(mobject = level4line,direction = RIGHT)

        level5line = Line([3.75,3-1*6/9,0],[3.75,3-0*6/9,0])
        bracket5 = Brace(mobject = level5line,direction = RIGHT)

        level1 = Ellipse(color = RED, width = 2, height = 1).rotate(math.pi/4)
        level1.move_to(v11.get_center())

        level2 = Ellipse(color = RED, width = 6, height = 1.5).rotate(math.pi/4)
        level2.move_to([-4.55,1.45,0])

        level3 = Ellipse(color = RED, width = 10, height = 2).rotate(math.pi/4)
        level3.move_to(v22.get_center())

        level4 = Ellipse(color = RED, width = 6, height = 1.5).rotate(math.pi/4)
        level4.move_to([-1.5,-1.5,0])

        level5 = Ellipse(color = RED, width = 2, height = 1).rotate(math.pi/4)
        level5.move_to(v33.get_center())
        self.wait()
        self.play(FadeIn(bracket1),FadeToColor(v11, BLUE), FadeToColor(queue1, BLUE),FadeIn(level1, run_time = 2))
        self.wait()
        self.play(FadeIn(bracket2), FadeToColor(v11, WHITE),FadeToColor(v21,BLUE), FadeToColor(v12,BLUE), FadeToColor(queue2, BLUE), FadeToColor(queue4, BLUE), FadeToColor(queue1, WHITE),FadeOut(bracket1))
        self.wait()
        self.play(FadeOut(level1, run_time = 2),FadeIn(level2, run_time = 2))
        self.wait()
        self.play(FadeIn(bracket3),FadeToColor(v21,WHITE), FadeToColor(v12,WHITE), FadeToColor(v31,BLUE), FadeToColor(v22, BLUE), FadeToColor(v13, BLUE),FadeToColor(queue7, BLUE), FadeToColor(queue5, BLUE),FadeToColor(queue3, BLUE), FadeToColor(queue2, WHITE), FadeToColor(queue4, WHITE),  FadeOut(bracket2))  
        self.wait()      
        self.play(FadeIn(level3, run_time = 2), FadeOut(level2, run_time = 2))
        self.wait()
        self.play(FadeIn(bracket4), FadeIn(level4, run_time = 2), FadeToColor(v31,WHITE), FadeToColor(v22, WHITE), FadeToColor(v13, WHITE),FadeToColor(v32, BLUE), FadeToColor(v23, BLUE), FadeToColor(queue8, BLUE), FadeToColor(queue6, BLUE), FadeToColor(queue7, WHITE), FadeToColor(queue5, WHITE),FadeToColor(queue3, WHITE), FadeOut(level3, run_time = 2), FadeOut(bracket3))
        self.wait()
        self.play(FadeIn(bracket5), FadeIn(level5, run_time = 2), FadeToColor(v32, WHITE), FadeToColor(v23, WHITE),FadeToColor(v33, BLUE),FadeToColor(queue9, BLUE), FadeToColor(queue8, WHITE), FadeToColor(queue6, WHITE), FadeOut(level4, run_time = 2), FadeOut(bracket4))
        self.wait()
        self.play(FadeOut(bracket5), FadeToColor(v33, WHITE),FadeToColor(queue9, WHITE), FadeOut(level5, run_time = 2))
        self.wait()
        self.play(FadeToColor(v11,BLUE, run_time = .4))
        self.play(FadeToColor(v12,BLUE, run_time = .4),FadeToColor(v21,BLUE, run_time = .4))
        self.play(FadeToColor(v13,BLUE, run_time = .4),FadeToColor(v22,BLUE, run_time = .4), FadeToColor(v31,BLUE, run_time = .4))
        self.play(FadeToColor(v32,BLUE, run_time = .4),FadeToColor(v23,BLUE, run_time = .4))
        self.play(FadeToColor(v33,BLUE, run_time = .4))

        self.play(FadeToColor(v11,WHITE, run_time = .4))
        self.play(FadeToColor(v12,WHITE, run_time = .4),FadeToColor(v21,WHITE, run_time = .4))
        self.play(FadeToColor(v13,WHITE, run_time = .4),FadeToColor(v22,WHITE, run_time = .4), FadeToColor(v31,WHITE, run_time = .4))
        self.play(FadeToColor(v32,WHITE, run_time = .4),FadeToColor(v23,WHITE, run_time = .4))
        self.play(FadeToColor(v33,WHITE, run_time = .4))

        self.play(FadeToColor(e11_21, RED, run_time = .4), FadeToColor(e11_12, RED, run_time = .4))
        self.play(FadeToColor(e21_31, RED, run_time = .4),FadeToColor(e21_22, RED, run_time = .4),FadeToColor(e12_22, RED, run_time = .4), FadeToColor(e12_13,RED, run_time = .4))
        self.play(FadeToColor(e31_32, RED, run_time = .4),FadeToColor(e22_32, RED, run_time = .4),FadeToColor(e22_23, RED, run_time = .4), FadeToColor(e13_23,RED, run_time = .4))
        self.play(FadeToColor(e32_33, RED, run_time = .4), FadeToColor(e23_33, RED, run_time = .4))
        
        self.play(FadeToColor(e11_21, WHITE, run_time = .4), FadeToColor(e11_12, WHITE, run_time = .4))
        self.play(FadeToColor(e21_31, WHITE, run_time = .4),FadeToColor(e21_22, WHITE, run_time = .4),FadeToColor(e12_22, WHITE, run_time = .4), FadeToColor(e12_13,WHITE, run_time = .4))
        self.play(FadeToColor(e31_32, WHITE, run_time = .4),FadeToColor(e22_32, WHITE, run_time = .4),FadeToColor(e22_23, WHITE, run_time = .4), FadeToColor(e13_23,WHITE, run_time = .4))
        self.play(FadeToColor(e32_33, WHITE, run_time = .4), FadeToColor(e23_33, WHITE, run_time = .4))
        
        square = Rectangle(
            width = FRAME_WIDTH,
            height = FRAME_HEIGHT ,
            fill_color = BLACK,
            fill_opacity = 1,
            stroke_width = 0)
        self.play(FadeIn(square))
        self.bring_to_front(square)
        self.wait()

        comp = TextMobject("O(n + m) where n = |V| and m = |E|").scale(1.5)
        self.play(Write(comp, run_time = 4))
        self.wait()
        self.play(FadeOut(comp))

        function = Text("def BFS(G):").move_to([-2,2.9,0])
        function[0:3].set_color(BLUE)
        function[4:7].set_color(GREEN)
        function[8].set_color(ORANGE)


        queue = Text("let Q be a queue").move_to([-.5,2.5-0.3,0])
        queue[4:5].set_color(ORANGE)
        root = Text("choose a root vertex").move_to([0,2-0.3,0])
        root[9:13].set_color(ORANGE)
        put = Text("put root vertex in Q").move_to([0,1.5-0.3,0])
        put[4:8].set_color(ORANGE)
        put[-1].set_color(ORANGE)

        whileloop = Text("while Q is not empty:").move_to([0,1-0.3-0.3,0])
        whileloop[0:5].set_color(RED)
        whileloop[11:14].set_color(RED)
        whileloop[6].set_color(ORANGE)

        dequeue = Text("u = Q.dequeue()").move_to([.8,.5-0.3-0.3,0])
        dequeue[4:5].set_color(ORANGE)
        dequeue[0:1].set_color(ORANGE)
        dequeue[6:13].set_color(BLUE)
        iffound = Text("if u is the goal:").move_to([0,0-0.3-0.3-0.3,0])
        iffound[3:4].set_color(ORANGE)
        iffound[0:2].set_color(RED)
        returnvertex = Text("return the vertex u").move_to([2.2,-0.5-0.3-0.3-0.3,0])
        returnvertex[18:].set_color(ORANGE)
        returnvertex[0:6].set_color(RED)
        forall = Text("for all edges (u,w) in G:").move_to([0,-1-0.3-0.3-0.3-0.3,0])
        forall[0:3].set_color(RED)
        forall[-2].set_color(ORANGE)
        forall[15:16].set_color(ORANGE)
        forall[17:18].set_color(ORANGE)
        notinQ = Text("if w has not been visited:").move_to([0,-1.5-0.3-0.3-0.3-0.3,0])
        notinQ[0:2].set_color(RED)
        notinQ[3:4].set_color(ORANGE)
        notinQ[9:12].set_color(RED)
        notinQ[18:25].set_color(ORANGE)

        then = Text("then label w as visited").move_to([3.8,-2-0.3-0.3-0.3-0.3,0])
        then[11:12].set_color(ORANGE)
        then[16:23].set_color(ORANGE)
        putonQ = Text("put w in Q").move_to([0,-2.5-0.3-0.3-0.3-0.3,0])
        putonQ[4:5].set_color(ORANGE)
        putonQ[9:].set_color(ORANGE)




        root.align_to(queue,LEFT)
        put.align_to(queue,LEFT)
        whileloop.align_to(queue,LEFT)
        iffound.align_to(dequeue,LEFT)
        forall.align_to(iffound,LEFT)
        notinQ.align_to(returnvertex,LEFT)
        putonQ.align_to(then,LEFT)

        lastreturn = Text("return goal not found").move_to([0,-3-0.3-0.3-0.3-0.3,0])
        lastreturn.align_to(whileloop,LEFT)
        lastreturn[:6].set_color(RED)

        code = VGroup(function,queue,root,put, whileloop, dequeue, iffound, returnvertex, forall, notinQ, then, putonQ, lastreturn)
        code.move_to([-.5,0,0])

        psuedocode = TextMobject("Pseudocode!").scale(3)
        psuedocode.set_color_by_gradient(RED, ORANGE, GREEN, BLUE)
        self.wait()
        self.play(Write(psuedocode))
        self.wait()
        self.play(FadeOut(psuedocode))
        self.wait()
        self.play(Write(function))
        self.wait()
        self.play(Write(queue))
        self.wait()
        self.play(Write(root))
        self.wait()
        self.play(Write(put))
        self.wait()
        self.play(Write(whileloop))
        self.wait()
        self.play(Write(dequeue))
        self.wait()
        self.play(Write(iffound))
        self.wait()
        self.play(Write(returnvertex))
        self.wait()
        self.play(Write(forall))
        self.wait()
        self.play(Write(notinQ))
        self.wait()
        self.play(Write(then))
        self.wait()
        self.play(Write(putonQ))
        self.wait()
        self.play(Write(lastreturn))
        self.wait()

        FadeOutAll(self)

        link = TextMobject("Example link below!", color = BLUE).scale(2)


        self.play(Write(link))

        self.wait()
        FadeOutAll(self)
        self.wait()
        thanks = TextMobject("Thank you!").scale(2)
        self.play(Write(thanks))
        self.wait()
        self.play(FadeOut(thanks))
        self.wait()


def DrawCompleteGraph(n, scale = 1, color = False, people = False):
    vectors = []
    vertices = []
    Lines = []
    for i in range(n):
        vectors.append([scale*math.cos(i*2*math.pi/n),scale*math.sin(i*2*math.pi/n),0])
    if people:
        for i in range(n):
            v = AnimatedPerson()
            v.move_to(np.multiply([1.7,1.7,1.7],vectors[i]))
            v.rotate(3*math.pi/2)
            vertices.append(v)
    else:
        for i in range(n):
            v = Circle(radius = .2, color = WHITE).move_to(vectors[i])
            v.set_fill(WHITE, opacity=1)
            vertices.append(v)
    for i in range(n):
        for j in range(i+1,n):
            #coloring the outside cycle blue and inside red
            if color:
                if abs(j - i) == 1 or (j-i == n-1) and color:
                    Lines.append(Line(vectors[i],vectors[j], color = BLUE, stroke_width = 5))
                else:
                    Lines.append(Line(vectors[i],vectors[j], color = RED, stroke_width = 5))
            else:
                Lines.append(Line(vectors[i],vectors[j], stroke_width = 5))

    return vertices, Lines, vectors

def FadeOutAll(self):
        square = Rectangle(
        width = FRAME_WIDTH,
        height = FRAME_HEIGHT ,
        fill_color = BLACK,
        fill_opacity = 1,
        stroke_width = 0)
        self.play(FadeIn(square))
        self.bring_to_front(square)
        self.wait()

