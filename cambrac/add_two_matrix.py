import cProfile
import io
import json
import pstats
import os
import matplotlib.pyplot as plt


def add_by(length, is_row=False):
    A = [[1 for i in range(length)] for j in range(length)]
    B = [[2 for i in range(length)] for j in range(length)]

    C = [[0 for i in range(length)] for j in range(length)]

    if is_row:
        for j in range(length):
            for i in range(length):
                C[i][j] = A[i][j] + B[i][j]
    else:
        for i in range(length):
            for j in range(length):
                C[i][j] = A[i][j] + B[i][j]


def add_by_row(length):
    add_by(length, True)


def add_by_col(length):
    add_by(length, False)


def simulate(Range=100, steps=1):
    rows = []
    cols = []

    test_prefix = "Until" + str(Range) + "Step" + str(steps) + "/"
    path = "./results/" + test_prefix

    try:
        os.mkdir(path)
    except OSError:
        pass
    else:
        pass

    for i in range(1, Range, steps):
        pr = cProfile.Profile()
        pr.enable()
        add_by_row(i)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s)
        ps.print_stats()
        result = s.getvalue().strip()
        result = result.partition('\n')[0]
        result = result.split()[4]
        rows.append(float(result))

    with open(path + 'rows.txt', 'w+') as f:
        f.write(str(rows))

    for i in range(1, Range, steps):
        pr = cProfile.Profile()
        pr.enable()
        add_by_col(i)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s)
        ps.print_stats()
        result = s.getvalue().strip()
        result = result.partition('\n')[0]
        result = result.split()[4]
        cols.append(float(result))

    with open(path + 'cols.txt', 'w+') as f:
        f.write(str(cols))


def make_plt(Range=100, steps=1, is_fresh=True):
    if is_fresh:
        simulate(Range, steps)

    test_prefix = "Until" + str(Range) + "Step" + str(steps) + "/"
    path = "./results/" + test_prefix

    myrows = json.load(open(path + 'rows.txt'))
    mycols = json.load(open(path + 'cols.txt'))

    fig, ax = plt.subplots()

    line1, = ax.plot(myrows, label="Rows", linewidth=1, linestyle='-')
    line2, = ax.plot(mycols, label="Cols", linewidth=1, linestyle='-')

    first_legend = ax.legend(handles=[line1], loc='upper right')
    ax.add_artist(first_legend)
    ax.legend(handles=[line2], loc='lower right')
    fig = plt.gcf()
    fig.canvas.set_window_title('Compare Add Two Matrix by Row & Col')
    plt.title("Result")
    plt.savefig(path + 'plot.png', dpi=300, bbox_inches='tight')
    print("Image has been saved as " + path + 'plot.png')

def main():
    Range = 500
    Steps = 10
    make_plt(Range, Steps)


if __name__ == "__main__":
    main()
