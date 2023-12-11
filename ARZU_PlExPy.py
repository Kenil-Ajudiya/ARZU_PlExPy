# A Research-grade Zero-effort and User-friendly Plotting Experience using Python (ARZU_PlExPy)

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
plt.rc('font', family='serif')

def help(*args):
    for arg in args:
        if arg == 'line_plot':
            print("***** A Research-grade Zero-effort and User-friendly Plotting Experience using Python (ARZU_PlExPy) *****\n"
                  "line_plot: A function for plotting 1-dimensional data curves in a single plot.\n"
                  "USAGE: line_plot(y=[], x=[], labels=[], colors=[], title='Title', xlabel='X Label', ylabel='Y Label', y_lim=[], x_lim=[], axis='both', direction='in', major_length=8, major_width=1, minor_length=4, minor_width=1, path='', dpi=128)\n"
                  "OPTIONS:     y=[y[i]] for integer i from 0 to, say, n. This will plot n curves of y in a single plot.\n"
                  "             x=[x[i]] for integer i from 0 to, say, m. Note that either m=n (1 x for each y) or m=1 (1 x for all y) or m=0 (x unspecified).\n"
                  "             labels=[label[i]] for integer i from 0 to, say, l. Note that either l=n (1 label for each y, legends will be plotted) or l=0 (no labels specified, no legends will be plotted).\n"
                  "             colors=[color[i]] for integer i from 0 to, say, c. Note that either c=n (user specified colors will be used, check for compatibility with matplotlib) or c=0 (matplotlib default colors will be used).\n"
                  "             y_lim and x_lim should be in the format [lower_limit, upper_limit]"
                  "             axis='x', 'y' or 'both'. See matplotlib.axes.Axes.tick_params\n"
                  "             direction='in', 'out' or 'inout'. See matplotlib.axes.Axes.tick_params\n"
                  "             major_length, major_width, minor_length and minor_width are same as length and width of matplotlib.axes.Axes.tick_params, but applied to major and minor ticks separately.\n"
                  "             If path (including filename and extension, e.g. ./plots/file_name.png) is specified, the figure will be saved to the specified directory with the specified filename, extension and DPI.\n")
            return

        elif arg == 'sub_plots':
            print("sub_plots will be added soon. Till then, hold tight!")
            return

        elif arg == 'color_plot':
            print("color_plot will be added soon. Till then, hold tight!")
            return

        elif arg == 'contour_plot':
            print("contour_plot will be added soon. Till then, hold tight!")
            return


    print("***** A Research-grade Zero-effort and User-friendly Plotting Experience using Python (ARZU_PlExPy) *****\n"
        "The following plotting functions are currently available:\n"
        "['func_name'] = ['line_plot']\n"
        "Type help('func_name') to display the help for 'func_name'."
        "Functions like 'sub_plots', 'color_plot', 'contour_plot', etc. will be added soon. Till then, hold tight!")
    return


def line_plot(y=[], x=[], labels=[], colors=[], title='Title', xlabel='X Label', ylabel='Y Label', y_lim=[], x_lim=[], axis='both', direction='in', major_length=8, major_width=1, minor_length=4, minor_width=1, path='', dpi=128):
    fig = plt.figure(figsize=(20, 11.25))
    ax = fig.gca()
    m = len(x)
    n = len(y)
    l = len(labels)
    c = len(colors)

    if m != n and m != 1 and m != 0:
        print("Invalid X data. len(x) can either be zero or one or equal to len(y).")
        return

    if c != n and c != 0:
        print("Invalid colors specification. len(colors) should be either zero - use default colors, or equal to len(y) - one color for each y[i].")
        return

    if l != n and l != 0:
        print("Invalid labels specification. len(labels) should be either zero or equal to len(y) - one label for each y[i].")
        return
    
    if l == n:
        if c == n:
            if n > 0:           # one or more curves in the same plot
                if m == n:                  # one x[i] for each y[i]
                    for i in range(n):
                        plt.plot(x[i], y[i], colors[i], label=labels[i])
                elif m == 1 and n != 1:     # same x values for all y[i]
                    for i in range(n):
                        plt.plot(x[0], y[i], colors[i], label=labels[i])
                else:                       # x values not specified 
                    for i in range(n):
                        plt.plot(y[i], colors[i], label=labels[i])

            else:               # empty figure
                plt.plot()

        else: # c == 0
            if n > 0:           # one or more curves in the same plot
                if m == n:                  # one x[i] for each y[i]
                    for i in range(n):
                        plt.plot(x[i], y[i], label=labels[i])
                elif m == 1 and n != 1:     # same x values for all y[i]
                    for i in range(n):
                        plt.plot(x[0], y[i], label=labels[i])
                else:                       # x values not specified
                    for i in range(n):
                        plt.plot(y[i], label=labels[i])

            else:               # empty figure
                plt.plot()
        plt.legend(fontsize=16)

    else: # l == 0
        if c == n:
            if n > 0:           # one or more curves in the same plot
                if m == n:                  # one x[i] for each y[i]
                    for i in range(n):
                        plt.plot(x[i], y[i], colors[i])
                elif m == 1 and n != 1:     # same x values for all y[i]
                    for i in range(n):
                        plt.plot(x[0], y[i], colors[i])
                else:                       # x values not specified
                    for i in range(n):
                        plt.plot(y[i], colors[i])

            else:               # empty figure
                plt.plot()

        else:  # c == 0
            if n > 0:           # one or more curves in the same plot
                if m == n:                  # one x[i] for each y[i]
                    for i in range(n):
                        plt.plot(x[i], y[i])
                elif m == 1 and n != 1:     # same x values for all y[i]
                    for i in range(n):
                        plt.plot(x[0], y[i])
                else:                       # x values not specified
                    for i in range(n):
                        plt.plot(y[i])

            else:               # empty figure
                plt.plot()

    plt.title(title, fontsize=18)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    if y_lim != []:
        plt.ylim(y_lim[0], y_lim[1])
    if x_lim != []:
        plt.xlim(x_lim[0], x_lim[1])
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis=axis, direction=direction, which='minor', length=minor_length, width=minor_width, right='on', top='on')
    ax.tick_params(axis=axis, direction=direction, which='major', length=major_length, width=major_width, labelsize=16, pad=10, right='on', top='on');
    if path != '':
        plt.savefig(path, dpi=dpi, facecolor='white');

def sub_plots():
    print("sub_plots will be added soon. Till then, hold tight!")
    return

def color_plot():
    print("color_plot will be added soon. Till then, hold tight!")
    return

def contour_plot():
    print("contour_plot will be added soon. Till then, hold tight!")
    return
