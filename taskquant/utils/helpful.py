import os


def dir_path(string):
    """
    Determine if string is a valid directory path
    """
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
        # warnings.warn(
        #     f"{textstyle.WARNING}{string} is not a valid directory, path will be defaulted to ~/.task{textstyle.RESET}",
        # )
