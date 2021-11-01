# Sent to me by Max:
# Over 10000 instances, compute the average number of streaks of length 6 or more in 100 coin flips.

import random
import math


def flip(n):
    """
    Flip a coin n times and count the number of streaks
    """
    last_value = None
    current_streak = 0
    streak_count = 0
    for _ in range(n):
        # values = {HEADS: 0, TAILS: 1}
        value = math.floor(random.random() + 0.5)
        if value == last_value:
            current_streak += 1
        else:
            if current_streak >= 6:
                streak_count += 1
            current_streak = 1
        last_value = value
    if current_streak >= 6:
        streak_count += 1

    return streak_count


def average_sampling(m, n):
    """
    Average the results of flip(n) over m instances
    """
    sum = 0
    for _ in range(m):
        sum += flip(n)

    return sum/m


print(average_sampling(10000, 100))

# It looks like we're getting roughly 1.5 as our answser
