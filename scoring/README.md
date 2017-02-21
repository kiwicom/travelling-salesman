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
* Competitor's program will run on each dataset and for each dataset
competitor will earn points.
    * If competitor's program gives wrong output, competitor will be rewarded by 0 points.
    * If competitor's program gives valid output, competitor will be rewarded by P points.
    * If competitor's program's output gave price which is equal to best one or is better thanbest one then P=log_2(size of particular dataset)
    * If competitor's program's output is worse than best one then P=[(b/y)^2]*log_2(size of particular dataset) where b is best price amongst all competitors and y is your price.
* Total points for given solution will be sum of points earned in each dataset
* If somebody gives better solution that best one, everybody's point are going to
be recomputed based on how relative good is their to the new best one
