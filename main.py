import config


def open_SMILE():
    import subprocess
    # Smileを実行
    SMILE_EXE_PATH = r"C:\SMILEV\bin\OSK.X1.Client.exe"
    subprocess.run(SMILE_EXE_PATH)


def auto_login():
    # TODO pyautoguiを使ってログインを実行
    pass


def main():
    open_SMILE()


if __name__ == '__main__':
    main()
