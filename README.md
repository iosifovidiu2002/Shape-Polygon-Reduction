# Shape-Polygon-Reduction
Using the Douglas–Peucker algorithm for curve decimation to reduce shapes drawn Paint-like to a minimum edge polygon.

## Algoritghm use case
Let's have a look at one use case for this algorithm.

Here we have a Paint-like hand drawn shape of a field from a satellite image from Google Maps.

![image](https://user-images.githubusercontent.com/72406655/194962514-32ea0a89-730b-435c-aead-754835f09cb3.png)

After the algorithm is applied, the set of points that defines the drawing is reduced to a much smaller ordered set representing the reduced polygon shape.

![image](https://user-images.githubusercontent.com/72406655/194962811-6e6fcba9-8fdb-413e-96ff-098f667bdc1e.png)

## Epsilon Parameter
```python
douglas_peucker(points, epsilon)
```
The epsilon parameter is linked to the smoothness of the resulting shape in the curve decimation context, in our use case the parameter dictates the amount of edges the final polygon will have.
