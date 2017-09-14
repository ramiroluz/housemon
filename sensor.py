import re

class Energy:
    '''
    expressions = ['(Device:.*;) Alarms', '^.*(Alarms:.*;) Power', '^.*(Line:.*;) Peaks', '^.*(Peaks:.*;) FFT Re', '^.*(FFT Re:.*;) FFT Img', '^.*(FFT Img:.*;) UTC Time', '^.*(UTC Time:.*;) hz', '^.*(hz:.*;) Wifi Strength', '^.*(WiFi Strength:.*;)']
    '''
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