# Slots Simulator

The slot machine is comprised of 5 slots, each with 5 different possible items.

The scripts run the machine X number of times (defined by variable j), and displays some statistics: Wins, losses, and biggest loss streak.

## Winning condition

Wins are determined based on how many of the same item show up. If you get any 3, 4, or 5 repetitions, you win. The more repetitions, the higher the prize would be.

## Slots Versions

Both scripts generate the same results. The only difference is how the results are calculated. slots_v1.py uses a more 'manual' approach, whereas slots_v2.py puts the results into a dictionary where duplicate results are detected with a loop.
