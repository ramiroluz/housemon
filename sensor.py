import re

class Energy:
    '''
    expressions = ['(Device:.*;) Alarms', '^.*(Alarms:.*;) Power', '^.*(Line:.*;) Peaks', '^.*(Peaks:.*;) FFT Re', '^.*(FFT Re:.*;) FFT Img', '^.*(FFT Img:.*;) UTC Time', '^.*(UTC Time:.*;) hz', '^.*(hz:.*;) Wifi Strength', '^.*(WiFi Strength:.*;)']
int_regex = re.compile('^[-]?[1-9]\d*$')
float_regex = re.compile('^-?\d+\.\d+$')
def extract_group_values(group):
    group_name, group_values = group[0].split(':')
    group_values = [value.replace(';', '') for value in group_values.split()]
    group_values = [value.split('=') for value in group_values]
    sizes = map(len, group_values)
    pairs = all([size==2 for size in sizes])
    if pairs:
        return {group_name: dict(group_values)}
    else:
        return {group_name: [v[0] for v in group_values]}
    '''
    def __init__(self):
        self.int_regex = re.compile('^[-]?[1-9]\d*$')
        self.float_regex = re.compile('^-?\d+\.\d+$')
        self.datetime_regex = re.compile('^ ?\d{4}-\d{2}-\d{1,2} \d{2}:\d{2}:\d{2};$')

    def check_value(self, expr, value):
        regex = re.compile(expr)
        return regex.match(value)

    def cast(self, value):
        if self.check_value(self.int_regex, value):
            return int(value)
        elif self.check_value(self.float_regex, value):
            return float(value)
        return value

    def parse_values(self, group):
        group_name, group_values = group[0].split(':', 1)
        if self.check_value(self.datetime_regex, group_values):
            # make it follow the same pattern of single value items,
            # like hz, WiFi Strength, Dummy.
            group_values = [[group_values.replace(';', '').strip()]]
        else:
            group_values = [value.replace(';', '') for value in group_values.split()]
            group_values = [value.split('=') for value in group_values]
        sizes = map(len, group_values)
        pairs = all([size==2 for size in sizes])
        if pairs:
            return {group_name: {k:self.cast(v) for k,v in dict(group_values).items()}}
        else:
            if len(group_values) == 1:
                value = group_values[0][0]
                return {group_name: self.cast(value)}
            return {group_name: [self.cast(v[0]) for v in group_values]}

    def parse_group(self, expr, data):
        regex = re.compile(expr)
        match = regex.match(data)
        return match.groups()

    def parse(self, data):
        return {
            'Device': {
                'ID': 10,
                'Fw': 16071801,
                'Evt': 2
            },
            'Alarms': {
                'CoilRevesed': 'OFF'
            },
            'Power': {
                'Active': '289W',
                'Reactive': '279var',
                'Appearent': '403VA'
            },
            'Line': {
                'Current': '1.75A',
                'Voltage': '230.08V',
                'Phase': '-43,841rad'
            },
            'Peaks': [
                1041.000, 1051.000, 1058.000, 1051.000, 1049.000, 1047.000,
                1054.000, 1059.000, 1057.000, 1060.000
            ],
            'FFT Re': [
                -257863.00, 102815.00, -64043.00, 48516.00, 59599.00, -4223.00,
                -43441.00, 23559.00, -24518.00
            ],
            'FFT Img': [
                481910.00, -14891.00, 69871.00, -7130.00, 43860.00, 34204.00,
                55951.00, -6945.00, 26131.00
            ],
            'UTC Time': '2016-10-4 16:47:50',
            'hz': 49.87,
            'WiFi Strength': -62,
            'Dummy': 20
        }
