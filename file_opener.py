import window_conf
from window_conf import (text_var, text_var2, text_var3,
                         path1, path2, path3, root)
import startup


def main():
    # Window title, dimensions.
    window_conf.window_conf('File Opener', '180x70')

    # Textvariable, index, path, row, column
    window_conf.text_box(text_var, 0, path1, 0, 0)
    window_conf.text_box(text_var2, 1, path2, 1, 0)
    window_conf.text_box(text_var3, 2, path3, 2, 0)

    window_conf.button('Open', 0, 1, startup.start_file)
    window_conf.button('Add', 1, 1)

    root.mainloop()


if __name__ == '__main__':
    main()
