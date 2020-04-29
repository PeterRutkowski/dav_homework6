from sys import argv
import bokeh
import webbrowser

def save_plotly(filename, fig):
    if len(argv) > 1:
        if argv[1] == '0':
            fig.show()
        else:
            fig.write_html('plots/plotly_%s.html'%(filename))
            print('plots/plotly_%s.html'%(filename))
    else:
        fig.write_html('plots/plotly_%s.html'%(filename))
        print('plots/plotly_%s.html'%(filename))

def save_bokeh(filename, plot):
    if len(argv) > 1:
        if argv[1] == '0':
            bokeh.plotting.show(plot)
        else:
            bokeh.io.saving.save(plot, 'plots/bokeh_%s.html'%(filename), title=filename)
            print('plots/bokeh_%s.html'%(filename))
    else:
        bokeh.io.saving.save(plot, 'plots/bokeh_%s.html'%(filename), title=filename)
        print('plots/bokeh_%s.html'%(filename))

def save_altair(filename, plot):
    if len(argv) > 1:
        if argv[1] == '0':
            plot.show()
        else:
            plot.save('plots/altair_%s.html'%(filename))
            print('plots/altair_%s.html'%(filename))
    else:
        plot.save('plots/altair_%s.html'%(filename))
        print('plots/altair_%s.html'%(filename))