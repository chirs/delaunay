# Computational Geometry algorithms in Python

The initial goal was to be able to draw a voronoi diagram by hand.

The goal developed after that was to have a clear set of geometry primitives for doing computational geometry.

Clarity heavily prioritized over performance.


## Algorithms


### Delaunay triangulation

A Delaunay triangulation for a set P of points in a plane is a triangulation DT(P) such that no point in P is inside the circumcircle of any triangle in DT(P).

Delaunay triangulations maximize the minimum angle of all the angles of the triangles in the triangulation; they tend to avoid sliver triangles.

There are many different ways to do a Delaunay triangulation, we started by using [S-hull](http://www.s-hull.org/paper/s_hull.pdf), but that paper is not very well written.

Considering other approaches.
* http://www.qhull.org/html/index.htm
* http://www.cs.mcgill.ca/~fukuda/soft/polyfaq/polyfaq.html


### Convex Hull

The convex hull of a set X of points in the Euclidean plane is the smallest convex set that contains X.

* Graham Scan - avoid all right-handed turns by managing big stack that represents the graph.


## Testing

Run the tests

```PYTHONPATH=src pytest tests```


## To-do

A. Finish delaunay triangle algorithm.

1. Are all the lines being drawn for the initial triangulation?
2. Return all pairs of triangles
3. Strategy for edge-swapping.

B. Finish convex hull algorithm.


C. Basic testing and documentation

D. What next?


