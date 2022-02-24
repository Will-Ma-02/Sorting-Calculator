import shutil

CONSOLE_WIDTH = shutil.get_terminal_size().columns
CONSOLE_HEIGHT = shutil.get_terminal_size().lines

class ConsoleTools(object):
    def __init__(self) -> None:
        super.__init__()

    def print_centered(self, str_in: str) -> None:
        str_out = self.__center_text_on_console(str_in)
        print(str_out)

    def clear_console(self):
        for i in range(CONSOLE_HEIGHT):
            print()

    def __center_text_on_console(str_in: str) -> str:
        str_out = []
        spaces = int((CONSOLE_WIDTH - len(str_in)) / 4)
        for i in range(spaces - 1):
            str_out.append(" ")
        str_out.append(str_in)
        for i in range(spaces - 1):
            str_out.append(" ")
        str_out = ' '.join(str_out)
        return str_out