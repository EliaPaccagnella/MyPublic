import argparse

colors = {
    'style':{'reset':'\033[0m',
             'bold':'\033[01m',
             'disable':'\033[02m',
             'underline':'\033[04m',
             'reverse':'\033[07m',
             'strikethrough':'\033[09m',
             'invisible':'\033[08m'},
    'fg':{'black':'\033[30m',
          'red':'\033[31m',
          'green':'\033[32m',
          'orange':'\033[33m',
          'blue':'\033[34m',
          'purple':'\033[35m',
          'cyan':'\033[36m',
          'lightgrey':'\033[37m',
          'darkgrey':'\033[90m',
          'lightred':'\033[91m',
          'lightgreen':'\033[92m',
          'yellow':'\033[93m',
          'lightblue':'\033[94m',
          'pink':'\033[95m',
          'lightcyan':'\033[96m'},
    'bg':{'black':'\033[40m',
          'red':'\033[41m',
          'green':'\033[42m',
          'orange':'\033[43m',
          'blue':'\033[44m',
          'purple':'\033[45m',
          'cyan':'\033[46m',
          'lightgrey':'\033[47m'}
}

def print_color(text, foreground_color='', background_color='', style=''):
    print(
        colors['style'][style],
        colors['fg'][foreground_color],
        colors['bg'][background_color],
        text,
        colors['style']['reset'],
        sep='')
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('text')
    parser.add_argument(
        '-fg',
        '--foreground',
        choices=[
            'black',
            'red',
            'green',
            'orange',
            'blue',
            'purple',
            'cyan',
            'lightgrey'
        ])
    parser.add_argument(
        '-bg',
        '--background',
        choices=[
            'black',
            'red',
            'green',
            'orange',
            'blue',
            'purple',
            'cyan',
            'lightgrey',
            'darkgrey',
            'lightred',
            'lightgree',
            'yellow',
            'lightblue',
            'pink',
            'lightcyan'
        ])
    parser.add_argument(
        '-s',
        '--style',
        choices=[
            'reset',
            'bold',
            'disable',
            'underline',
            'reverse',
            'strikethrough',
            'invisible'
        ])
    
    args = parser.parse_args()

    print_color(
        args.text,
        args.foreground,
        args.background,
        args.style
    )
