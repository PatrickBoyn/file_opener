import window_conf
from window_conf import (text_variable, text_box,
                         paths, window_conf,
                         root)
import startup


def main():
    # Window title, dimensions.
    window_conf('File Opener', '180x70')

    # Textvariable, index, path, row, column
    text_box(text_variable[0], 0, paths[0], 0, 0)
    text_box(text_variable[1], 1, paths[1], 1, 0)
    text_box(text_variable[2], 2, paths[2], 2, 0)

    window_conf.button('Open', 0, 1, startup.start_file)
    window_conf.button('Add', 1, 1)

    root.mainloop()


if __name__ == '__main__':
    main()
