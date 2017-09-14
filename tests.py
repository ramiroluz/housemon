import unittest

from sensor import Energy


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.energy = Energy()
        self.data = (
            'Device: ID=10; Fw=16071801; Evt=2; Alarms: CoilRevesed=OFF; '
            'Power: Active=289W; Reactive=279var; Appearent=403VA; Line: '
            'Current=1.75A; Voltage=230.08V; Phase=-43,841rad; Peaks: '
            '1041.000; 1051.000; 1058.000; 1051.000; 1049.000; 1047.000; '
            '1054.000; 1059.000; 1057.000; 1060.000; FFT Re: -257863.00; '
            '102815.00; -64043.00; 48516.00; 59599.00; -4223.00; '
            '-43441.00; 23559.00; -24518.00; FFT Img: 481910.00; '
            '-14891.00; 69871.00; -7130.00; 43860.00; 34204.00; 55951.00; '
            '-6945.00; 26131.00; UTC Time: 2016-10-4 16:47:50; hz: 49.87; '
            'WiFi Strength: -62; Dummy: 20'
        )

    def test_groups(self):
        expected = [
            ('Device', '(Device:.*;) Alarms', ('Device: ID=10; Fw=16071801; Evt=2;',)),
            ('Alarms', '^.*(Alarms:.*;) Power', ('Alarms: CoilRevesed=OFF;',)),
            ('Power', '^.*(Power:.*;) Line', (
                'Power: Active=289W; Reactive=279var; Appearent=403VA;',
            )),
            ('Line', '^.*(Line:.*;) Peaks', (
                'Line: Current=1.75A; Voltage=230.08V; Phase=-43,841rad;',
            )),
            ('Peaks', '^.*(Peaks:.*;) FFT Re', (
                'Peaks: 1041.000; 1051.000; 1058.000; 1051.000; 1049.000; '
                '1047.000; 1054.000; 1059.000; 1057.000; 1060.000;',
            )),
            ('FFT Re', '^.*(FFT Re:.*;) FFT Img', (
                'FFT Re: -257863.00; 102815.00; -64043.00; 48516.00; '
                '59599.00; -4223.00; -43441.00; 23559.00; -24518.00;',
            )),
            ('FFT Img', '^.*(FFT Img:.*;) UTC Time', (
                'FFT Img: 481910.00; -14891.00; 69871.00; -7130.00; '
                '43860.00; 34204.00; 55951.00; -6945.00; 26131.00;',)),
            ('UTC Time', '^.*(UTC Time:.*;) hz', ('UTC Time: 2016-10-4 16:47:50;',)),
            ('hz', '^.*(hz:.*;) WiFi Strength', ('hz: 49.87;',)),
            ('Wifi Strength', '^.*(WiFi Strength:.*;) Dummy', (
                'WiFi Strength: -62;',
            )),
            ('Dummy', '^.*(Dummy:.*)', ('Dummy: 20',)),
        ]
        for name, expr, group in expected:
            with self.subTest(name=name):
                self.assertEqual(self.energy.parse_group(expr, self.data), group)

    def test_parse_data(self):
        expected = {
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

        data = self.energy.parse(self.data)
        self.assertEqual(expected, data)
