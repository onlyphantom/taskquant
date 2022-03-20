"""
Reference:
# 1. https://i.stack.imgur.com/KTSQa.png
# 2. https://i.stack.imgur.com/9UVnC.png

Usage:
print(f"{textstyle.BOLD}{textstyle.UNDERLINE}Welcome to TaskQuanT{textstyle.RESET}")
-> print(f"\033[1m\033[4mWelcome to TaskQuant\033[0m")
"""


class textstyle:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    # nord colors: https://www.nordtheme.com/docs/colors-and-palettes
    # 38;2 -> foreground rgb // 48;2 -> background rgb
    NORDBG1 = "\033[38;2;67;76;94;48;2;143;188;187m"
    NORDBG2 = "\033[38;2;67;76;94;48;2;136;192;208m"
    NORDBG1BOLD = "\033[38;2;67;76;94;48;2;143;188;187m\033[1m"
    NORDBG2BOLD = "\033[38;2;67;76;94;48;2;136;192;208m\033[1m"
