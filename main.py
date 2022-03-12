import libs.args as args
import tools.tcoder.tcoder as tcoder


execArgs = args.getExecArgs()

# config = args.getConfig()
# configHost = config.get('api', 'host')


if execArgs.tcoder:     # -t / --tcoder
    try:
        if execArgs.encode:     # -e / --encode
            text = input('Input text: ')
            tcoder.runEncoding(text)

        if execArgs.decode:     # -d / --decode
            text = input('Input text: ')
            tcoder.runDecoding(text)

    except Exception as e:
        print(e)
        print('Use --encode or --decode.')

if execArgs.tklog:      # -k / --tklog
    print('TKeyLog under development!')

if execArgs.smbuster:      # -m / --smbuster
    print('Spam mail buster under development!')