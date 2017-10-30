class Client:
    def __init__(self):
        print('init')

    def start(self):
        # raise Exception('Test')
        print('start')

    def stop(self):
        raise Exception('Test')
        print('stop')

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        return


if __name__ == "__main__":
    with Client() as client:
        print('with')

