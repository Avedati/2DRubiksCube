#!/usr/bin/env python

""" main.py: A 2D Rubik's Cube written in Python as a first program. """

__author__  = "Abhinav Vedati"
__version__ = "0.0.1"

from turtle import *
from random import *
import time, os
wn = Screen()
wn.setup(1000, 1000)
wn.bgcolor("black")
#set lists
frontindex = ["white","white","white",
              "white","white","white",
              "white","white","white",
              "placeholder1","placeholder11","placeholder111"
              "1","11","111","1111"]
backindex = ["yellow","yellow","yellow",
             "yellow","yellow","yellow",
             "yellow","yellow","yellow",
             "placeholder2","placeholder21","placeholder211",
             "2","21","211","2111"]
leftindex = ["blue","blue","blue",
             "blue","blue","blue",
             "blue","blue","blue",
             "placeholder3","placeholder31","placeholder311",
             "3","31","311","3111"]
rightindex = ["green","green","green",
              "green","green","green",
              "green","green","green",
              "placeholder4","placeholder41","placholder411",
              "4","41","411","4111"]
topindex = ["red","red","red",
            "red","red","red",
            "red","red","red",
            "placeholder5","placeholder51","placeholder511",
            "5","51","511","5111"]
downindex = ["orange","orange","orange",
             "orange","orange","orange",
             "orange","orange","orange",
             "placeholder6","placeholder61","placeholder611",
             "6","61","611","6111"]
#define functions
"""
  top()
  
  This function sets up the 9 turtles representing the top face of the Rubik's Cube.
"""
def top():
  t1 = Turtle()
  t2 = Turtle()
  t3 = Turtle()
  t4 = Turtle()
  t5 = Turtle()
  t6 = Turtle()
  t7 = Turtle()
  t8 = Turtle()
  t9 = Turtle()
  t1.speed(0)
  t2.speed(0)
  t3.speed(0)
  t4.speed(0)
  t5.speed(0)
  t6.speed(0)
  t7.speed(0)
  t8.speed(0)
  t9.speed(0)
  t1.penup()
  t2.penup()
  t3.penup()
  t4.penup()
  t5.penup()
  t6.penup()
  t7.penup()
  t8.penup()
  t9.penup()
  t1.shape("square")
  t2.shape("square")
  t3.shape("square")
  t4.shape("square")
  t5.shape("square")
  t6.shape("square")
  t7.shape("square")
  t8.shape("square")
  t9.shape("square")
  t1.color(topindex[0])
  t2.color(topindex[1])
  t3.color(topindex[2])
  t4.color(topindex[3])
  t5.color(topindex[4])
  t6.color(topindex[5])
  t7.color(topindex[6])
  t8.color(topindex[7])
  t9.color(topindex[8])
  t1.goto(-27, 108)
  t2.goto(0, 108)
  t3.goto(27, 108)
  t4.goto(-27, 81)
  t5.goto(0, 81)
  t6.goto(27, 81)
  t7.goto(-27, 54)
  t8.goto(0, 54)
  t9.goto(27, 54)
 
"""
  down()
  
  This function sets up the 9 turtles representing the bottom face of the Rubik's Cube.
"""
def down():
  d1 = Turtle()
  d2 = Turtle()
  d3 = Turtle()
  d4 = Turtle()
  d5 = Turtle()
  d6 = Turtle()
  d7 = Turtle()
  d8 = Turtle()
  d9 = Turtle()
  d1.speed(0)
  d2.speed(0)
  d3.speed(0)
  d4.speed(0)
  d5.speed(0)
  d6.speed(0)
  d7.speed(0)
  d8.speed(0)
  d9.speed(0)
  d1.penup()
  d2.penup()
  d3.penup()
  d4.penup()
  d5.penup()
  d6.penup()
  d7.penup()
  d8.penup()
  d9.penup()
  d1.shape("square")
  d2.shape("square")
  d3.shape("square")
  d4.shape("square")
  d5.shape("square")
  d6.shape("square")
  d7.shape("square")
  d8.shape("square")
  d9.shape("square")
  d1.color(downindex[0])
  d2.color(downindex[1])
  d3.color(downindex[2])
  d4.color(downindex[3])
  d5.color(downindex[4])
  d6.color(downindex[5])
  d7.color(downindex[6])
  d8.color(downindex[7])
  d9.color(downindex[8])
  d1.goto(-27, -54)
  d2.goto(0, -54)
  d3.goto(27, -54)
  d4.goto(-27, -81)
  d5.goto(0, -81)
  d6.goto(27, -81)
  d7.goto(-27, -108)
  d8.goto(0, -108)
  d9.goto(27, -108)
  

"""
  left()
  
  This function sets up the 9 turtles representing the left face of the Rubik's Cube.
"""
def left():
  l1 = Turtle()
  l2 = Turtle()
  l3 = Turtle()
  l4 = Turtle()
  l5 = Turtle()
  l6 = Turtle()
  l7 = Turtle()
  l8 = Turtle()
  l9 = Turtle()
  l1.speed(0)
  l2.speed(0)
  l3.speed(0)
  l4.speed(0)
  l5.speed(0)
  l6.speed(0)
  l7.speed(0)
  l8.speed(0)
  l9.speed(0)
  l1.penup()
  l2.penup()
  l3.penup()
  l4.penup()
  l5.penup()
  l6.penup()
  l7.penup()
  l8.penup()
  l9.penup()
  l1.shape("square")
  l2.shape("square")
  l3.shape("square")
  l4.shape("square")
  l5.shape("square")
  l6.shape("square")
  l7.shape("square")
  l8.shape("square")
  l9.shape("square")
  l1.color(leftindex[0])
  l2.color(leftindex[1])
  l3.color(leftindex[2])
  l4.color(leftindex[3])
  l5.color(leftindex[4])
  l6.color(leftindex[5])
  l7.color(leftindex[6])
  l8.color(leftindex[7])
  l9.color(leftindex[8])
  l1.goto(-108, 27)
  l2.goto(-81, 27)
  l3.goto(-54, 27)
  l4.goto(-108, 0)
  l5.goto(-81, 0)
  l6.goto(-54, 0)
  l7.goto(-108, -27)
  l8.goto(-81, -27)
  l9.goto(-54, -27)

"""
  right()
  
  This function sets up the 9 turtles representing the right face of the Rubik's Cube.
"""
def right():
  r1 = Turtle()
  r2 = Turtle()
  r3 = Turtle()
  r4 = Turtle()
  r5 = Turtle()
  r6 = Turtle()
  r7 = Turtle()
  r8 = Turtle()
  r9 = Turtle()
  r1.speed(0)
  r2.speed(0)
  r3.speed(0)
  r4.speed(0)
  r5.speed(0)
  r6.speed(0)
  r7.speed(0)
  r8.speed(0)
  r9.speed(0)
  r1.penup()
  r2.penup()
  r3.penup()
  r4.penup()
  r5.penup()
  r6.penup()
  r7.penup()
  r8.penup()
  r9.penup()
  r1.shape("square")
  r2.shape("square")
  r3.shape("square")
  r4.shape("square")
  r5.shape("square")
  r6.shape("square")
  r7.shape("square")
  r8.shape("square")
  r9.shape("square")
  r1.color(rightindex[0])
  r2.color(rightindex[1])
  r3.color(rightindex[2])
  r4.color(rightindex[3])
  r5.color(rightindex[4])
  r6.color(rightindex[5])
  r7.color(rightindex[6])
  r8.color(rightindex[7])
  r9.color(rightindex[8])
  r1.goto(54, 27)
  r2.goto(81, 27)
  r3.goto(108, 27)
  r4.goto(54, 0)
  r5.goto(81, 0)
  r6.goto(108, 0)
  r7.goto(54, -27)
  r8.goto(81, -27)
  r9.goto(108, -27)

"""
  back()
  
  This function sets up the 9 turtles representing the back face of the Rubik's Cube.
"""
def back():
  b1 = Turtle()
  b2 = Turtle()
  b3 = Turtle()
  b4 = Turtle()
  b5 = Turtle()
  b6 = Turtle()
  b7 = Turtle()
  b8 = Turtle()
  b9 = Turtle()
  b1.speed(0)
  b2.speed(0)
  b3.speed(0)
  b4.speed(0)
  b5.speed(0)
  b6.speed(0)
  b7.speed(0)
  b8.speed(0)
  b9.speed(0)
  b1.penup()
  b2.penup()
  b3.penup()
  b4.penup()
  b5.penup()
  b6.penup()
  b7.penup()
  b8.penup()
  b9.penup()
  b1.shape("square")
  b2.shape("square")
  b3.shape("square")
  b4.shape("square")
  b5.shape("square")
  b6.shape("square")
  b7.shape("square")
  b8.shape("square")
  b9.shape("square")
  b1.color(backindex[8])
  b2.color(backindex[7])
  b3.color(backindex[6])
  b4.color(backindex[5])
  b5.color(backindex[4])
  b6.color(backindex[3])
  b7.color(backindex[2])
  b8.color(backindex[1])
  b9.color(backindex[0])
  b1.goto(-27, 189)
  b2.goto(0, 189)
  b3.goto(27, 189)
  b4.goto(-27, 162)
  b5.goto(0, 162)
  b6.goto(27, 162)
  b7.goto(-27, 135)
  b8.goto(0, 135)
  b9.goto(27, 135)

"""
  front()
  
  This function sets up the 9 turtles representing the front face of the Rubik's Cube.
"""
def front():
  f1 = Turtle()
  f2 = Turtle()
  f3 = Turtle()
  f4 = Turtle()
  f5 = Turtle()
  f6 = Turtle()
  f7 = Turtle()
  f8 = Turtle()
  f9 = Turtle()
  f1.speed(0)
  f2.speed(0)
  f3.speed(0)
  f4.speed(0)
  f5.speed(0)
  f6.speed(0)
  f7.speed(0)
  f8.speed(0)
  f9.speed(0)
  f1.penup()
  f2.penup()
  f3.penup()
  f4.penup()
  f5.penup()
  f6.penup()
  f7.penup()
  f8.penup()
  f9.penup()
  f1.shape("square")
  f2.shape("square")
  f3.shape("square")
  f4.shape("square")
  f5.shape("square")
  f6.shape("square")
  f7.shape("square")
  f8.shape("square")
  f9.shape("square")
  f1.color(frontindex[0])
  f2.color(frontindex[1])
  f3.color(frontindex[2])
  f4.color(frontindex[3])
  f5.color(frontindex[4])
  f6.color(frontindex[5])
  f7.color(frontindex[6])
  f8.color(frontindex[7])
  f9.color(frontindex[8])
  f1.goto(-27, 27)
  f2.goto(0, 27)
  f3.goto(27, 27)
  f4.goto(-27, 0)
  f5.goto(0, 0)
  f6.goto(27, 0)
  f7.goto(-27, -27)
  f8.goto(0, -27)
  f9.goto(27, -27)
  
"""
  f()
  
  This function performs a front clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def f():
  in1 = []
  in1.append(topindex[6])
  in1.append(topindex[7])
  in1.append(topindex[8])
  in1.append(rightindex[0])
  in1.append(rightindex[3])
  in1.append(rightindex[6])
  in1.append(downindex[0])
  in1.append(downindex[1])
  in1.append(downindex[2])
  in1.append(leftindex[2])
  in1.append(leftindex[5])
  in1.append(leftindex[8])
  u = -2
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del rightindex[u]
    del downindex[0]
    del leftindex[v]
    del topindex[6]
  rightindex.insert(0, in1[2])
  rightindex.insert(3, in1[1])
  rightindex.insert(6, in1[0])
  downindex.insert(0, in1[5])
  downindex.insert(1, in1[4])
  downindex.insert(2, in1[3])
  leftindex.insert(2, in1[8])
  leftindex.insert(5, in1[7])
  leftindex.insert(8, in1[6])
  topindex.insert(6, in1[11])
  topindex.insert(7, in1[10])
  topindex.insert(8, in1[9])
  fu0 = frontindex[0]
  fu1 = frontindex[1]
  fu2 = frontindex[2]
  fu3 = frontindex[3]
  fu4 = frontindex[4]
  fu5 = frontindex[5]
  fu6 = frontindex[6]
  fu7 = frontindex[7]
  fu8 = frontindex[8]
  frontindex[0] = fu6
  frontindex[1] = fu3
  frontindex[2] = fu0
  frontindex[3] = fu7
  frontindex[5] = fu1
  frontindex[6] = fu8
  frontindex[7] = fu5
  frontindex[8] = fu2

"""
  F()
  
  This function performs a front counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def F():
  in2 = []
  in2.append(topindex[6])
  in2.append(topindex[7])
  in2.append(topindex[8])
  in2.append(rightindex[0])
  in2.append(rightindex[3])
  in2.append(rightindex[6])
  in2.append(downindex[0])
  in2.append(downindex[1])
  in2.append(downindex[2])
  in2.append(leftindex[2])
  in2.append(leftindex[5])
  in2.append(leftindex[8])
  u = -2
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del rightindex[u]
    del downindex[0]
    del leftindex[v]
    del topindex[6]
  leftindex.insert(2, in2[2])
  leftindex.insert(5, in2[1])
  leftindex.insert(8, in2[0])
  topindex.insert(6, in2[5])
  topindex.insert(7, in2[4])
  topindex.insert(8, in2[3])
  rightindex.insert(0, in2[8])
  rightindex.insert(3, in2[7])
  rightindex.insert(6, in2[6])
  downindex.insert(0, in2[11])
  downindex.insert(1, in2[10])
  downindex.insert(2, in2[9])
  fv0 = frontindex[0]
  fv1 = frontindex[1]
  fv2 = frontindex[2]
  fv3 = frontindex[3]
  fv4 = frontindex[4]
  fv5 = frontindex[5]
  fv6 = frontindex[6]
  fv7 = frontindex[7]
  fv8 = frontindex[8]
  frontindex[0] = fv2
  frontindex[1] = fv5
  frontindex[2] = fv8
  frontindex[3] = fv1
  frontindex[5] = fv7
  frontindex[6] = fv0
  frontindex[7] = fv3
  frontindex[8] = fv6

"""
  b()
  
  This function performs a back clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def b():
  in3 = []
  in3.append(topindex[0])
  in3.append(topindex[1])
  in3.append(topindex[2])
  in3.append(rightindex[2])
  in3.append(rightindex[5])
  in3.append(rightindex[8])
  in3.append(downindex[6])
  in3.append(downindex[7])
  in3.append(downindex[8])
  in3.append(leftindex[0])
  in3.append(leftindex[3])
  in3.append(leftindex[6])
  u = -2
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del rightindex[v]
    del downindex[6]
    del leftindex[u]
    del topindex[0]
  leftindex.insert(0, in3[0])
  leftindex.insert(3, in3[1])
  leftindex.insert(6, in3[2])
  topindex.insert(0, in3[3])
  topindex.insert(1, in3[4])
  topindex.insert(2, in3[5])
  rightindex.insert(2, in3[6])
  rightindex.insert(5, in3[7])
  rightindex.insert(8, in3[8])
  downindex.insert(6, in3[9])
  downindex.insert(7, in3[10])
  downindex.insert(8, in3[11])
  bv0 = backindex[0]
  bv1 = backindex[1]
  bv2 = backindex[2]
  bv3 = backindex[3]
  bv4 = backindex[4]
  bv5 = backindex[5]
  bv6 = backindex[6]
  bv7 = backindex[7]
  bv8 = backindex[8]
  backindex[0] = bv2
  backindex[1] = bv5
  backindex[2] = bv8
  backindex[3] = bv1
  backindex[5] = bv7
  backindex[6] = bv0
  backindex[7] = bv3
  backindex[8] = bv6

"""
  B()
  
  This function performs a back counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def B():
  in4 = []
  in4.append(topindex[0])
  in4.append(topindex[1])
  in4.append(topindex[2])
  in4.append(rightindex[2])
  in4.append(rightindex[5])
  in4.append(rightindex[8])
  in4.append(downindex[6])
  in4.append(downindex[7])
  in4.append(downindex[8])
  in4.append(leftindex[0])
  in4.append(leftindex[3])
  in4.append(leftindex[6])
  u = -2
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del rightindex[v]
    del downindex[6]
    del leftindex[u]
    del topindex[0]
  rightindex.insert(2, in4[0])
  rightindex.insert(5, in4[1])
  rightindex.insert(8, in4[2])
  downindex.insert(6, in4[3])
  downindex.insert(7, in4[4])
  downindex.insert(8, in4[5])
  leftindex.insert(0, in4[6])
  leftindex.insert(3, in4[7])
  leftindex.insert(6, in4[8])
  topindex.insert(0, in4[9])
  topindex.insert(1, in4[10])
  topindex.insert(2, in4[11])
  bu0 = backindex[0]
  bu1 = backindex[1]
  bu2 = backindex[2]
  bu3 = backindex[3]
  bu4 = backindex[4]
  bu5 = backindex[5]
  bu6 = backindex[6]
  bu7 = backindex[7]
  bu8 = backindex[8]
  backindex[0] = bu6
  backindex[1] = bu3
  backindex[2] = bu0
  backindex[3] = bu7
  backindex[5] = bu1
  backindex[6] = bu8
  backindex[7] = bu5
  backindex[8] = bu2

"""
  l()
  
  This function performs a left clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def l():
  in5 = []
  in5.append(topindex[0])
  in5.append(topindex[3])
  in5.append(topindex[6])
  in5.append(frontindex[0])
  in5.append(frontindex[3])
  in5.append(frontindex[6])
  in5.append(downindex[0])
  in5.append(downindex[3])
  in5.append(downindex[6])
  in5.append(backindex[2])
  in5.append(backindex[5])
  in5.append(backindex[8])
  u = -2
  v = -2
  for x in range (0, 3):
    u += 2
    v += 2
    del backindex[v]
    del downindex[u]
    del frontindex[u]
    del topindex[u]
  frontindex.insert(0, in5[0])
  frontindex.insert(3, in5[1])
  frontindex.insert(6, in5[2])
  downindex.insert(0, in5[3])
  downindex.insert(3, in5[4])
  downindex.insert(6, in5[5])
  backindex.insert(2, in5[6])
  backindex.insert(5, in5[7])
  backindex.insert(8, in5[8])
  topindex.insert(0, in5[9])
  topindex.insert(3, in5[10])
  topindex.insert(6, in5[11])
  lu0 = leftindex[0]
  lu1 = leftindex[1]
  lu2 = leftindex[2]
  lu3 = leftindex[3]
  lu4 = leftindex[4]
  lu5 = leftindex[5]
  lu6 = leftindex[6]
  lu7 = leftindex[7]
  lu8 = leftindex[8]
  leftindex[0] = lu6
  leftindex[1] = lu3
  leftindex[2] = lu0
  leftindex[3] = lu7
  leftindex[5] = lu1
  leftindex[6] = lu8
  leftindex[7] = lu5
  leftindex[8] = lu2

"""
  L()
  
  This function performs a left counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def L():
  in6 = []
  in6.append(topindex[0])
  in6.append(topindex[3])
  in6.append(topindex[6])
  in6.append(frontindex[0])
  in6.append(frontindex[3])
  in6.append(frontindex[6])
  in6.append(downindex[0])
  in6.append(downindex[3])
  in6.append(downindex[6])
  in6.append(backindex[2])
  in6.append(backindex[5])
  in6.append(backindex[8])
  u = -2
  v = -2
  for x in range (0, 3):
    u += 2
    v += 2
    del backindex[v]
    del downindex[u]
    del frontindex[u]
    del topindex[u]
  backindex.insert(2, in6[0])
  backindex.insert(5, in6[1])
  backindex.insert(8, in6[2])
  topindex.insert(0, in6[3])
  topindex.insert(3, in6[4])
  topindex.insert(6, in6[5])
  frontindex.insert(0, in6[6])
  frontindex.insert(3, in6[7])
  frontindex.insert(6, in6[8])
  downindex.insert(0, in6[9])
  downindex.insert(3, in6[10])
  downindex.insert(6, in6[11])
  lv0 = leftindex[0]
  lv1 = leftindex[1]
  lv2 = leftindex[2]
  lv3 = leftindex[3]
  lv4 = leftindex[4]
  lv5 = leftindex[5]
  lv6 = leftindex[6]
  lv7 = leftindex[7]
  lv8 = leftindex[8]
  leftindex[0] = lv2
  leftindex[1] = lv5
  leftindex[2] = lv8
  leftindex[3] = lv1
  leftindex[5] = lv7
  leftindex[6] = lv0
  leftindex[7] = lv3
  leftindex[8] = lv6

"""
  r()
  
  This function performs a right clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def r():
  in7 = []
  in7.append(topindex[2])
  in7.append(topindex[5])
  in7.append(topindex[8])
  in7.append(frontindex[2])
  in7.append(frontindex[5])
  in7.append(frontindex[8])
  in7.append(downindex[2])
  in7.append(downindex[5])
  in7.append(downindex[8])
  in7.append(backindex[0])
  in7.append(backindex[3])
  in7.append(backindex[6])
  u = 0
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del backindex[u]
    del downindex[v]
    del frontindex[v]
    del topindex[v]
  backindex.insert(0, in7[0])
  backindex.insert(3, in7[1])
  backindex.insert(6, in7[2])
  topindex.insert(2, in7[3])
  topindex.insert(5, in7[4])
  topindex.insert(8, in7[5])
  frontindex.insert(2, in7[6])
  frontindex.insert(5, in7[7])
  frontindex.insert(8, in7[8])
  downindex.insert(2, in7[9])
  downindex.insert(5, in7[10])
  downindex.insert(8, in7[11])
  ru0 = rightindex[0]
  ru1 = rightindex[1]
  ru2 = rightindex[2]
  ru3 = rightindex[3]
  ru4 = rightindex[4]
  ru5 = rightindex[5]
  ru6 = rightindex[6]
  ru7 = rightindex[7]
  ru8 = rightindex[8]
  rightindex[0] = ru6
  rightindex[1] = ru3
  rightindex[2] = ru0
  rightindex[3] = ru7
  rightindex[5] = ru1
  rightindex[6] = ru8
  rightindex[7] = ru5
  rightindex[8] = ru2

"""
  R()
  
  This function performs a right counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def R(): 
  in8 = []
  in8.append(topindex[2])
  in8.append(topindex[5])
  in8.append(topindex[8])
  in8.append(frontindex[2])
  in8.append(frontindex[5])
  in8.append(frontindex[8])
  in8.append(downindex[2])
  in8.append(downindex[5])
  in8.append(downindex[8])
  in8.append(backindex[0])
  in8.append(backindex[3])
  in8.append(backindex[6])
  u = 0
  v = 0
  for x in range (0, 3):
    u += 2
    v += 2
    del backindex[u]
    del downindex[v]
    del frontindex[v]
    del topindex[v]
  frontindex.insert(2, in8[0])
  frontindex.insert(5, in8[1])
  frontindex.insert(8, in8[2])
  downindex.insert(2, in8[3])
  downindex.insert(5, in8[4])
  downindex.insert(8, in8[5])
  backindex.insert(0, in8[6])
  backindex.insert(3, in8[7])
  backindex.insert(6, in8[8])
  topindex.insert(2, in8[9])
  topindex.insert(5, in8[10])
  topindex.insert(8, in8[11])
  rv0 = rightindex[0]
  rv1 = rightindex[1]
  rv2 = rightindex[2]
  rv3 = rightindex[3]
  rv4 = rightindex[4]
  rv5 = rightindex[5]
  rv6 = rightindex[6]
  rv7 = rightindex[7]
  rv8 = rightindex[8]
  rightindex[0] = rv2
  rightindex[1] = rv5
  rightindex[2] = rv8
  rightindex[3] = rv1
  rightindex[5] = rv7
  rightindex[6] = rv0
  rightindex[7] = rv3
  rightindex[8] = rv6

"""
  t()
  
  This function performs a top clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def t():
  in9 = []
  in9.append(frontindex[0])
  in9.append(frontindex[1])
  in9.append(frontindex[2])
  in9.append(rightindex[0])
  in9.append(rightindex[1])
  in9.append(rightindex[2])
  in9.append(backindex[6])
  in9.append(backindex[7])
  in9.append(backindex[8])
  in9.append(leftindex[0])
  in9.append(leftindex[1])
  in9.append(leftindex[2])
  for x in range(0, 3):
    del leftindex[0]
    del rightindex[0]
    del frontindex[0]
    del backindex[0]
  leftindex.insert(0, in9[0])
  leftindex.insert(1, in9[1])
  leftindex.insert(2, in9[2])
  frontindex.insert(0, in9[3])
  frontindex.insert(1, in9[4])
  frontindex.insert(2, in9[5])
  rightindex.insert(0, in9[6])
  rightindex.insert(1, in9[7])
  rightindex.insert(2, in9[8])
  backindex.insert(6, in9[9])
  backindex.insert(7, in9[10])
  backindex.insert(8, in9[11])
  tu0 = topindex[0]
  tu1 = topindex[1]
  tu2 = topindex[2]
  tu3 = topindex[3]
  tu4 = topindex[4]
  tu5 = topindex[5]
  tu6 = topindex[6]
  tu7 = topindex[7]
  tu8 = topindex[8]
  topindex[0] = tu6
  topindex[1] = tu3
  topindex[2] = tu0
  topindex[3] = tu7
  topindex[5] = tu1
  topindex[6] = tu8
  topindex[7] = tu5
  topindex[8] = tu2

"""
  T()
  
  This function performs a top counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def T():
  in10 = []
  in10.append(frontindex[0])
  in10.append(frontindex[1])
  in10.append(frontindex[2])
  in10.append(rightindex[0])
  in10.append(rightindex[1])
  in10.append(rightindex[2])
  in10.append(backindex[6])
  in10.append(backindex[7])
  in10.append(backindex[8])
  in10.append(leftindex[0])
  in10.append(leftindex[1])
  in10.append(leftindex[2])
  for x in range(0, 3):
    del leftindex[0]
    del rightindex[0]
    del frontindex[0]
    del backindex[0]
  rightindex.insert(0, in10[0])
  rightindex.insert(1, in10[1])
  rightindex.insert(2, in10[2])
  backindex.insert(6, in10[3])
  backindex.insert(7, in10[4])
  backindex.insert(8, in10[5])
  leftindex.insert(0, in10[6])
  leftindex.insert(1, in10[7])
  leftindex.insert(2, in10[8])
  frontindex.insert(0, in10[9])
  frontindex.insert(1, in10[10])
  frontindex.insert(2, in10[11])
  tv0 = topindex[0]
  tv1 = topindex[1]
  tv2 = topindex[2]
  tv3 = topindex[3]
  tv4 = topindex[4]
  tv5 = topindex[5]
  tv6 = topindex[6]
  tv7 = topindex[7]
  tv8 = topindex[8]
  topindex[0] = tv2
  topindex[1] = tv5
  topindex[2] = tv8
  topindex[3] = tv1
  topindex[5] = tv7
  topindex[6] = tv0
  topindex[7] = tv3
  topindex[8] = tv6

  
"""
  d()
  
  This function performs a bottom clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def d():
  in11 = []
  in11.append(frontindex[6])
  in11.append(frontindex[7])
  in11.append(frontindex[8])
  in11.append(rightindex[6])
  in11.append(rightindex[7])
  in11.append(rightindex[8])
  in11.append(backindex[0])
  in11.append(backindex[1])
  in11.append(backindex[2])
  in11.append(leftindex[6])
  in11.append(leftindex[7])
  in11.append(leftindex[8])
  for x in range(0, 3):
    del leftindex[6]
    del rightindex[6]
    del frontindex[6]
    del backindex[6]
  rightindex.insert(6, in11[0])
  rightindex.insert(7, in11[1])
  rightindex.insert(8, in11[2])
  backindex.insert(0, in11[3])
  backindex.insert(1, in11[4])
  backindex.insert(2, in11[5])
  leftindex.insert(6, in11[6])
  leftindex.insert(7, in11[7])
  leftindex.insert(8, in11[8])
  frontindex.insert(6, in11[9])
  frontindex.insert(7, in11[10])
  frontindex.insert(8, in11[11])
  du0 = downindex[0]
  du1 = downindex[1]
  du2 = downindex[2]
  du3 = downindex[3]
  du4 = downindex[4]
  du5 = downindex[5]
  du6 = downindex[6]
  du7 = downindex[7]
  du8 = downindex[8]
  downindex[0] = du6
  downindex[1] = du3
  downindex[2] = du0
  downindex[3] = du7
  downindex[5] = du1
  downindex[6] = du8
  downindex[7] = du5
  downindex[8] = du2

"""
  D()
  
  This function performs a bottom counter-clockwise turn on the Rubik's Cube.
  It will change the colors of the appropriate turtles.
"""
def D():
  in12 = []
  in12.append(frontindex[6])
  in12.append(frontindex[7])
  in12.append(frontindex[8])
  in12.append(rightindex[6])
  in12.append(rightindex[7])
  in12.append(rightindex[8])
  in12.append(backindex[0])
  in12.append(backindex[1])
  in12.append(backindex[2])
  in12.append(leftindex[6])
  in12.append(leftindex[7])
  in12.append(leftindex[8])
  for x in range(0, 3):
    del leftindex[6]
    del rightindex[6]
    del frontindex[6]
    del backindex[6]
  leftindex.insert(6, in12[0])
  leftindex.insert(7, in12[1])
  leftindex.insert(8, in12[2])
  frontindex.insert(6, in12[3])
  frontindex.insert(7, in12[4])
  frontindex.insert(8, in12[5])
  rightindex.insert(6, in12[6])
  rightindex.insert(7, in12[7])
  rightindex.insert(8, in12[8])
  backindex.insert(0, in12[9])
  backindex.insert(1, in12[10])
  backindex.insert(2, in12[11])
  dv0 = downindex[0]
  dv1 = downindex[1]
  dv2 = downindex[2]
  dv3 = downindex[3]
  dv4 = downindex[4]
  dv5 = downindex[5]
  dv6 = downindex[6]
  dv7 = downindex[7]
  dv8 = downindex[8]
  downindex[0] = dv2
  downindex[1] = dv5
  downindex[2] = dv8
  downindex[3] = dv1
  downindex[5] = dv7
  downindex[6] = dv0
  downindex[7] = dv3
  downindex[8] = dv6

"""
  refresh()
  
  This function redraws every face of the Rubik's Cube.
"""
def refresh():
  front()
  back()
  down()
  top()
  left()
  right()
  
"""
  cubeconsole()
  
  This function is the user input function.
  If the user types in a side (F, for example), that side will be turned clockwise.
  However, if there is a ' after the side (F', for example), that side will be turned counterclockwise.
  Incorrect input will be discarded.
"""
def cubeconsole():
  os.system('clear')
  print "Type ? for help."
  newinput = raw_input().upper()
  if newinput == "F":
    f()
    refresh()
    cubeconsole()
  elif newinput == "F'":
    F()
    refresh()
    cubeconsole()
  elif newinput == "B":
    b()
    refresh()
    cubeconsole()
  elif newinput == "B'":
    B()
    refresh()
    cubeconsole()
  elif newinput == "L":
    l()
    refresh()
    cubeconsole()
  elif newinput == "L'":
    L()
    refresh()
    cubeconsole()
  elif newinput == "R":
    r()
    refresh()
    cubeconsole()
  elif newinput == "R'":
    R()
    refresh()
    cubeconsole()
  elif newinput == "U":
    t()
    refresh()
    cubeconsole()
  elif newinput == "U'":
    T()
    refresh()
    cubeconsole()
  elif newinput == "D":
    d()
    refresh()
    cubeconsole()
  elif newinput == "D'":
    D()
    refresh()
    cubeconsole()
  elif newinput == "Q":
    exit(0)
  else:
    print "Error: Invalid Syntax"
    time.sleep(1)
    print "Redirecting ... "
    time.sleep(1)
    cubeconsole()
refresh()
cubeconsole()
