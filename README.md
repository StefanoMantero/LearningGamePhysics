## Learning some basic game physics stuff.
*Later i want to use genetic algorithm  combined to a neural network to train an AI on my physics based game, but first i need to create one in order to understand all the math and physics stuff.*
Im using:
>Processing

>Python

>Some very special help from [Sentdex](https://github.com/Sentdex) youtube channel.

*-Later-*

>TensorFlow

*Game Steps:*
- [x] Physics engine & basic collision(Rect-Circle)
- [ ] Angle and rotation
- [x] Self-generated levels 
- [ ] Adding the GenetiAlgorithm 
- [ ] Create the neuralnetwork 

[Collision point detector](https://yal.cc/rectangle-circle-intersection-test/)
```
DeltaX = CircleX - Max(RectX, Min(CircleX, RectX + RectWidth));
DeltaY = CircleY - Max(RectY, Min(CircleY, RectY + RectHeight));
return (DeltaX * DeltaX + DeltaY * DeltaY) < (CircleRadius * CircleRadius);
```
