

class ExtractingCommandLineArgs:

    @staticmethod
    def get_hostname(args):
        for i in range(len(args)):
            if args[i] == '--hostname':
                hostname = args[i+1].replace('\'', '')
                return hostname
        raise Exception('Hostname not found use --hostname')

    @staticmethod
    def get_username(args):
        for i in range(len(args)):
            if args[i] == '--username':
                username = args[i + 1].replace('\'', '')
                return username
        raise Exception('Hostname not found use --username')

    @staticmethod
    def get_password(args):
        for i in range(len(args)):
            if args[i] == '--password':
                password = args[i + 1].replace('\'', '')
                return password
        raise Exception('Hostname not found use --password')
