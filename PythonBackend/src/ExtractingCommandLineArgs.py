

class ExtractingCommandLineArgs:

    @staticmethod
    def get_hostname(args):
        for i in range(args):
            if args[i] == '--hostname':
                return args[i+1]
        raise Exception('Hostname not found use --hostname')

    @staticmethod
    def get_username(args):
        for i in range(args):
            if args[i] == '--username':
                return args[i+1]
        raise Exception('Hostname not found use --username')

    @staticmethod
    def get_password(args):
        for i in range(args):
            if args[i] == '--password':
                return args[i + 1]
        raise Exception('Hostname not found use --password')
