import argparse
# from configparser import ConfigParser



def getExecArgs():

    parser = argparse.ArgumentParser()

    # parser.add_argument('-c', '--config',
    #                     required=False,
    #                     help="Location of config file - this param is required")

    # parser.add_argument('-d', '--loglevel',
    #                     required=False,
    #                     default='INFO',
    #                     help="optional definition of log level, default is INFO, but WARNING or DEBUG will work as well")
    
    ######### main choice:
    parser.add_argument('-t', '--tcoder',
                        required=False,
                        action='store_true',
                        help="encrypt / decrypt message. Using: python3 main.py -c and -e [encrypt] or -d [decrypt].")
    
    parser.add_argument('-k', '--tklog',
                        required=False,
                        action='store_true',
                        help="keylogger manager - under development.")
    
    parser.add_argument('-m', '--smbuster',
                        required=False,
                        action='store_true',
                        help="smpam mail buster - under development.")

    ######### tcoder:
    parser.add_argument('-e', '--encode',
                        required = False,
                        action='store_true',
                        help = "encode inputed text. Switch -t required!")

    parser.add_argument('-d', '--decode',
                        required = False,
                        action='store_true',
                        help = "decode input text. Switch -t required!")

    return parser.parse_args()



# def getConfig():
#     config = ConfigParser(interpolation=None)
#     try:
#         config.read_file(open(execargs.config, 'r'))
#         return config
#     except Exception:
#         print('Incorrect path to config file!')
#         exit(1)

# execargs = getExecArgs()
# config = getConfig()