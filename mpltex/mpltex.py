"""
mpltex
======

"""

golden_ratio = (5**.5-1.0)/2.0

def pt_to_in(pt):
    return pt / 72.27


def pt_to_mm(pt):
    raise NotImplementedError


def get_rcParams(fig_width_pt = 232.0, scale = 1.0, dpi = 600):
    """TODO: write a description
    
    Parameters
    ----------
    fig_width_pt: float (232.0)
        Width of the figure in points. 
        Use LaTeX \showthe\linewidth to figure out what number to use.
            232.0 for two-column IEEEtran articles
            YYYY for MIT/WHOI thesis figures


    """
    fig_width = pt_to_in(fig_width_pt) # width in inches
    fig_height = fig_width * golden_ratio # height in inches
    fig_size =  [fig_width * scale, fig_height * scale]
    params = {  'axes.labelsize': 10,
                'text.fontsize': 8,
                'legend.fontsize': 8,
                'xtick.labelsize': 8,
                'ytick.labelsize': 8,
                'font.family': 'serif',
                'font.serif': 'Times',
                'text.usetex': True,
                'figure.figsize': fig_size,
                'figure.dpi': dpi}
    return params
