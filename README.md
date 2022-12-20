# Smartphone-Recognition
This is a program to recognize a smartphone from an image. There are many ways and technologies to recognize in Machine Learning or Deep Learning field.
However, in this program, I applied a **theoretical method** in digital image processing, using Python and OpenCV library.

# Steps
1. Preprocessing:

    Each image has its own size, so I firstly resize it to a fixed size (600x400). 
    
    The input image is a color image, to procees, I converted  into a grayscale image. Here, I used the average method, 
    which each pair of pixels (x,y) has a value of $\dfrac{r+g+b}{3}$.
    
2. Edge detection:

    Edge detection is use for detect edges of a smartphone. I used the Roberts Cross Gradient to hightlight fine details. 
    
    The math background of Robert Corss Gradient is *the first derivative* of function $f(x,y)$
    
    Gradient of $f(x,y)$: 
    
      $ grad(f) = \begin{bmatrix} G_x \\\  G_y \end{bmatrix} $
    
      $ =\begin{bmatrix} \dfrac{\partial f(x,y)}{\partial x} = f(x+1,y) - f(x,y) \\\ \dfrac{\partial f(x,y)}{\partial y} = f(x,y+1) - f(x,y)  \end{bmatrix}$

    The magnitude of the vector is the rate of change of the value at (x,y) along the gradient direction.
    
     $$\nabla f(x,y) = mag(\nabla f) = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$$

3. Finding contours and draw it on the image:

  Find the contours with sides of 4 and the area meets the conditional range. Then, draw it.


# Note:
- The program recognizes the smartphone by theoretical method so the accuracy is not really high. It is affected by brightness, other objects that may change the smartphone shape, etc.

# Demo:
![image](https://user-images.githubusercontent.com/106876168/208651247-33889a0d-b189-47e3-9523-7e52eace9b7d.png)

