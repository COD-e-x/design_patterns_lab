class OldLogger:
    @staticmethod
    def log_message(message):
        print(f'Log: {message}')

class NewLogger:
    @staticmethod
    def write_log(message):
        raise NotImplementedError

class AdapterLogger(NewLogger):
    def __init__(self, old_logger: OldLogger):
        self.__old_logger = old_logger

    def write_log(self, message):
        self.__old_logger.log_message(message)


class ClientCode:
    def __init__(self, logger: NewLogger):
        self.__logger = logger

    def log(self, message):
        self.__logger.write_log(message)

if __name__ == '__main__':
    old_logger_01 = OldLogger()
    adapter = AdapterLogger(old_logger_01)
    client = ClientCode(adapter)

    client.log('Тестовый log')
