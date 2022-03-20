import os
import warnings
from utils.colors import textstyle


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        # raise NotADirectoryError(string)
        warnings.warn(
            f"{textstyle.WARNING}{string} is not a valid directory, path will be defaulted to ~/.task{textstyle.RESET}",
            # NotADirectoryError,
        )
