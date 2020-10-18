# 2d-heat-transfer-conduction-simulation
Project developed for the discipline of Heat and Mass Transfer based on the transient simulation of a 2D surface with specific initial conditional parameters of temperature.
The discretization of the equations are done by the use of the finite element method(FEM).

This project is a simple model of the use of the FEM and my first try at it.
It is able to save the imagens present on each iteration on time on a file called "Imagens"(images in portuguese) and able to create a video at the end.
There is also a function used for analysing some specific calculation domains on the map, in which there is no need for the use of colormaps for informing temperature.
The funcions are well commented in portuguese in the code, so here i have the explanation in english.

simulacao:
Is the function responsible for making all the calculations.
There is also a way to uncomment some lines and make so every iteration is printed in the specified file cited earlier.

mostrar:
The function responsible for showing an image file at the end of the transient state.

analises:
This funciton is responsible for plotting the specific calculation domains analysis cited earlier.

simulacaoAnimada:
It works just like 'simulacao' but also generates a video using all the frames of the transient alaysis time iterations.
