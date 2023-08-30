import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from pathlib import Path
# necessary when building the sphinx gallery
def configure_pyvista(app, config):
    pyvista.BUILDING_GALLERY = True
    pyvista.OFF_SCREEN = True

    figure_path = Path.cwd() / "auto-generated/"
    figure_path.mkdir(exist_ok=True)
    pyvista.FIGURE_PATH = str(figure_path)

    readme = Path.cwd() / "auto-generated" / "README.md"
    readme.touch()

    # Add the PyVista image scraper to SG 
    # DynamicScraper()
    config.sphinx_gallery_conf["image_scrapers"]: ("pyvista", )
    config.sphinx_gallery_conf["examples_dirs"] = "auto-generated"
    config.sphinx_gallery_conf["filename_pattern"] = "*"
    return ()


def setup(app):
    app.connect("config-inited", configure_pyvista)

# import numpy as np
# # Optional - set parameters like theme or window size
# pyvista.set_plot_theme('document')
# pyvista.global_theme.window_size = np.array([1024, 768]) * 2
