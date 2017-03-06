* There will be 11 datasets to test contestant's program on.
* Number of different cities in datasets are going to be:
    1. 5
    2. 15
    3. 20
    4. 30
    5. 40
    6. 50
    7. 60
    8. 70
    9. 100
    10. 200
    11. 300
* Competitor's program will be run on each dataset and for each dataset
competitor will earn points.
    * If competitor's program gives wrong output, competitor will get 0 points.
    * If competitor's program gives valid output, competitor will get P points, which will be computed as follows.
        * If competitor's program's output gives price which is equal to best one or is better than best one then P=log_2(size of particular dataset)
        * If competitor's program's output is worse than best one then P=[(b/y)^2]*log_2(size of particular dataset) where b is best price amongst all competitors and y is your price.
* Total points for given solution will be sum of points earned in each dataset
* If somebody gives better solution than best one, everybody's points are going to
be recomputed based on how good is their solution relatively to the new best one.
