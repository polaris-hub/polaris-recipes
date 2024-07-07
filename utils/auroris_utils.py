import os
import fsspec
from PIL.Image import Image as ImageType

import datamol as dm

from auroris.utils import fig2img
from auroris.report import CurationReport
from auroris.report.broadcaster import HTMLBroadcaster

try:
    import jinja2
except ImportError:
    jinja2 = None


class GCP_HTMLBroadcaster(HTMLBroadcaster):
    """
    Render a simple HTML page

    Args:
        report: Curation report object.
        destination: Destination folder for exporting the report.
        embed_images: Whether embed image bytes in HTML report.
    """

    def __init__(
        self,
        report: CurationReport,
        destination: str,
        embed_images: bool = False,
    ):
        super().__init__(report, destination, embed_images)


    def _img_to_html_src(self, path: str):
        """
        Convert a path to a corresponding `src` attribute for an `<img />` tag.
        Currently only supports GCP and local paths.
        """
        protocol = dm.utils.fs.get_protocol(path)
        if protocol == "gs":
            return path.replace("gs://", "https://storage.googleapis.com/")
        elif protocol == "file":
            return os.path.relpath(path, self._destination)
        else:
            raise ValueError("We only support images hosted in GCP or locally")


def save_image(image: ImageType, path: str):
    """Save an image to a fsspec-compatible path"""
    image = fig2img(image)
    with fsspec.open(path, "wb") as fd:
        image.save(fd, format="png")
    protocol = dm.utils.fs.get_protocol(path)
    if protocol == "gs":
        return path.replace("gs://", "https://storage.googleapis.com/")
    return path
    