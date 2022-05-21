import time
import matplotlib.pyplot as plt

from backtrack import knight_tour


def plot():
    chessboard = [i+1 for i in range(8)]
    time_difference = []
    for i in range(8):
        initialization = knight_tour(N=i+1)
        start_time = time.time()
        initialization.start_tour()
        end_time = time.time()
        time_difference.append((end_time-start_time))
    plt.figure("Knight's Tour")
    plt.title(
        "Time taken for solutions of Knight's tour problem")
    plt.xlabel("Size of Chessboard")
    plt.ylabel("Time(seconds)")
    plt.plot(chessboard, time_difference, 'x', label="time")
    plt.legend()


if __name__ == '__main__':
    plot()
    plt.show()
