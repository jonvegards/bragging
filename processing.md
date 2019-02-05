# Notes from learning Processing with "Getting Started with Processing"

## Keyboard bindings

| `cmd -` | comment out line |


## Drawing

| Command                               | Description                                                                               |
|---------------------------------------|-------------------------------------------------------------------------------------------|
| `size(X, Y)`                          | Generate window of size `(X,Y)`                                                           |
| `point(X,Y`                           | Color one pixel at `(X,Y)`                                                                |
| `line(x1,y1,x2,y2)`                   |                                                                                           |
| `triangle(x1,y1,x2,y2,x3,y3)`         |                                                                                           |
| `quad(...)`                           | Square with freely defined corners                                                        |
| `rect(x, y, width, height)`           |                                                                                           |
| `ellipse(x,y,w,h)`                    | Ellipse with center `x,y` and height and width `h, w`                                     |
| `arc(x,y,width, height, start, stop)` | Circle with a cake piece removed at angles `start,stop`                                   |
| `PI, HALF_PI, ...`                    | The constant for pi.                                                                      |
| `strokeWeight(X)`                     | Thickness of line drawn.                                                                  |
| `strokeCap(arg)`                      | Line endings: `SQUARE`, `PROJECT`, `ROUND`.                                               |
| `strokeJoin(arg)`                     | Joining of lines, *e.g.* in squares: `ROUND`, `BEVEL`, `MITER`.                           |
| `ellipseMode(CORNER)`                 | Run bef. `ellipse()` -> `x,y` upper left corner of the square the circle is drwan within. |
| `ellipseMode(RADIUS)`                 | Last two args. treated as radial width and height.                                        |
| `fill(), background(), stroke()`      | Set the colors of the objects drawn.                                                      |
| `noStroke()`                          | No stroke around figures.                                                                 |
| `beginShape()`                        | Tells Processing that the following cmds will form a figure/shape.                        |
| `vertex()`                            | Define pair of coordinates for a shape.                                                   |
| `endShape()`                          | End the shape. Pass `CLOSE` if you want to connect the two last vertices.                 |
|                                       |                                                                                           |

## Basic features of processing-language
Some variables are global:

| `width`, `height` | Defined by `size()` and is the h and w of the window. |
|                   |                                                       |

- Variables must be defined as in `C++`, *e.g.* `int a = 2`.
- Increment variable `a` with `a++;` or, *e.g.*, `a += 3`.
- For-loops: `for (int i = 20; i < 400; i += 60) { do sth; }`
