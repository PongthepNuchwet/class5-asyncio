import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 1
# opponents = 24
move_pairs = 1
# move_pairs = 30

# วิธีการคำนวน ((my_compute_time + opponent_compute_time) * move_pairs * opponents) / 60 / 60
# ((5+55)*30*24) / 43200 sec / 720 minutes  = 12 hour

def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")