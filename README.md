## Learning some basic game physics stuff.
*Later i want to use genetic algorithm  combined to a neural network to train an AI on my physics based game, but first i need to create one in order to understand all the math and physics stuff.*
Im using:
>Processing

>Python

>Some very special help from [Sentdex](https://github.com/Sentdex) python tutorials.

*-Later-*

>TensorFlow

*Game Steps:*
- [x] Physics engine & basic collision(Rect-Circle)
- [x] Self-generated levels 
- [ ] Adding the GenetiAlgorithm 
- [ ] Create the neuralnetwork 

![cattura](https://cloud.githubusercontent.com/assets/22122998/25442732/1aa7a52a-2aa6-11e7-9d36-a20247ac0232.PNG)
[Collision point detector](https://yal.cc/rectangle-circle-intersection-test/)
```
DeltaX = CircleX - Max(RectX, Min(CircleX, RectX + RectWidth));
DeltaY = CircleY - Max(RectY, Min(CircleY, RectY + RectHeight));
return (DeltaX * DeltaX + DeltaY * DeltaY) < (CircleRadius * CircleRadius);
```
