import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from collections import Counter


def make_heatmap(df, outline, map_var, cbar_label, cmap = "Reds", norm_min = -1, norm_max = 1 , fontset = 'custom',
                 mathtext_rm = 'Bitstream Vera Sans', mathtext_it = 'Bitstream Vera Sans:italic',
                 mathtext_bf = 'Bitstream Vera Sans:bold', font_family = 'serif',
                 font_family_type = 'Computer Modern' , dpi = '100' ,use_tex = True,
                 missing_kwds_color = "whitesmoke", missing_kwds_label = "Missing Values",
                 outline_color = "none", outline_linewidth= 0.5, outline_alpha = 0.15,
                 axis_aspect_ratio = "equal", axis_grid = True, axis_gridcolor = 'gray', 
                 axis_linewidth = 0.25, axis_linestyle = "--", zorder_option = 0,
                 figsize_opt = [10,10], colorbar_pos = [0.94, 0.2, 0.025, 0.6],  
                 cbar_pad = 20, cbar_fontsize = 14, cbar_rotation = 270):
    '''
    This prints a (geographic) heatmap from the geopandas dataframe provided.

    variables you need to pass to make this work:
    df: geopandas dataframe to make map from
    map_var: variable to map
    cmap: Color map of the color bar, defaults to red
    norm_min: min normalised value, in many cases it should be np.min(df[map_var]), defaults to -1
    norm_max: max normalised value, in many cases it should be np.max(df[map_var]), defaults to 1
    cbar_label = label for the colorbar

    (default font options you don't need to worry about, unless you want to)
    Global Font Options
    mathtext_rm/bf/it: font options.
    font_family/_type: set custom font parameters (check this - KJ)
    use_tex: Set latex typeset True(on) or False(off)
    dpi: Set pixel density, default hundered.

    Map Font options
    missing_kwds_color:
    missing_kwds_label:

    Plot options
    outline_color:
    outline_linewidth:
    outline_alpha:
    Axis Options:
    axis_aspect_ratio:
    axis_grid:
    axis_linewidth:
    axis_linestyle:
    zorder_option:

    Colorbar Options:
    colorbar_pos:
    cbar_pad:
    cbar_fontsize:
    cbar_rotation:

    '''


    # Set Master Parameters to make graphs look good
    mpl.rcParams['mathtext.fontset'] = fontset
    mpl.rcParams['mathtext.rm'] = mathtext_rm
    mpl.rcParams['mathtext.it'] = mathtext_it
    mpl.rcParams['mathtext.bf'] = mathtext_bf
    mpl.rc('font', **{'family': font_family , 'serif': [font_family_type]})

    # this turns on latex, which makes font and number look really nice, but also
    # forces latex syntax which can cause problems (can be set to False)
    mpl.rc('text', usetex= use_tex)

    # this sets the dots per inch- it's the resolution the figure will render at.
    # make this larger for more precise rendering, though larger sizes will take longer
    mpl.rcParams['figure.dpi'] = dpi

    # set up figure
    fig, ax = plt.subplots(figsize = figsize_opt)
    plt.close()
    
    # plot data
    df.plot(ax=ax, column=map_var, cmap = cmap, missing_kwds = dict(color = missing_kwds_color, label = missing_kwds_label))
    outline.plot(ax = ax, color = outline_color, linewidth= outline_linewidth , alpha= outline_alpha)

    # axis settings
    ax.set_aspect(axis_aspect_ratio)
    ax.grid(axis_grid)
    ax.yaxis.grid(color= axis_gridcolor, linewidth= axis_linewidth, linestyle= axis_linestyle)
    ax.xaxis.grid(color= axis_gridcolor, linewidth= axis_linewidth, linestyle= axis_linestyle)
    ax.grid(zorder= zorder_option)

    # add custom colorbar
    # l:left, b:bottom, w:width, h:height; in normalized unit (0-1)
    cax = fig.add_axes(colorbar_pos)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=norm_min, vmax=norm_max))
    sm._A = []
    cbar = fig.colorbar(sm, cax=cax)
    cbar.ax.set_ylabel(cbar_label, labelpad= cbar_pad, fontsize= cbar_fontsize, rotation= cbar_rotation)
    
    return fig
