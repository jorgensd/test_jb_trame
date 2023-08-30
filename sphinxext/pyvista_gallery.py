import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper

# necessary when building the sphinx gallery
def configure_pyvista(app, config):
    pyvista.BUILDING_GALLERY = True
    pyvista.OFF_SCREEN = True

    # Add the PyVista image scraper to SG
    config.sphinx_gallery_conf["image_scrapers"]: (DynamicScraper(), )
    config.sphinx_gallery_conf["examples_dirs"] = "."
    config.sphinx_gallery_conf["filename_pattern"] ="test.ipynb"
    return ()


def setup(app):
    app.connect("config-inited", configure_pyvista)

# import numpy as np
# # Optional - set parameters like theme or window size
# pyvista.set_plot_theme('document')
# pyvista.global_theme.window_size = np.array([1024, 768]) * 2
