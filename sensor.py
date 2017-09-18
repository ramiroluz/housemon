import re

class Energy:
    def __init__(self):
        self.int_regex = re.compile('^[-]?[1-9]\d*$')
        self.float_regex = re.compile('^-?\d+\.\d+$')
        self.datetime_regex = re.compile('^ ?\d{4}-\d{2}-\d{1,2} \d{2}:\d{2}:\d{2};$')
        self.device_regex = '(Device:.*;) Alarms'
        self.alarms_regex = '^.*(Alarms:.*;) Power'
        self.power_regex = '^.*(Power:.*;) Line'
        self.line_regex = '^.*(Line:.*;) Peaks'
        self.peaks_regex = '^.*(Peaks:.*;) FFT Re'
        self.fft_re_regex = '^.*(FFT Re:.*;) FFT Img'
        self.fft_img_regex = '^.*(FFT Img:.*;) UTC Time'
        self.utc_time_regex = '^.*(UTC Time:.*;) hz'
        self.hz_regex = '^.*(hz:.*;) WiFi Strength'
        self.wifi_strength_regex = '^.*(WiFi Strength:.*;) Dummy'
        self.dummy_regex = '^.*(Dummy:.*)'

    def check_value(self, expr, value):
        regex = re.compile(expr)
        return regex.match(value)

    def cast(self, value):
        if self.check_value(self.int_regex, value):
            return int(value)
        elif self.check_value(self.float_regex, value):
            return float(value)
        return value

    def clean_fields(self, value):
        result = value
        expr = re.compile(r'(Active=\d{3})(W)')
        result = expr.sub(r'\1', result)
        expr = re.compile(r'(Reactive=\d{3})(var)')
        result = expr.sub(r'\1', result)
        expr = re.compile(r'(Appearent=\d{3})(VA)')
        result = expr.sub(r'\1', result)
        expr = re.compile(r'(Current=\d\.\d{2})(A)')
        result = expr.sub(r'\1', result)
        expr = re.compile(r'(Voltage=\d{3}\.\d{2})(V)')
        result = expr.sub(r'\1', result)
        return result

    def parse_values(self, group):
        group_name, group_values = group[0].split(':', 1)
        group_values = self.clean_fields(group_values)

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

    def group_as_dict(self, regex, data):
        group_txt = self.parse_group(regex, data)
        group = self.parse_values(group_txt)
        return group

    def parse(self, data):
        result = {}
        result.update(self.group_as_dict(self.device_regex, data))
        result.update(self.group_as_dict(self.alarms_regex, data))
        result.update(self.group_as_dict(self.power_regex, data))
        result.update(self.group_as_dict(self.line_regex, data))
        result.update(self.group_as_dict(self.peaks_regex, data))
        result.update(self.group_as_dict(self.peaks_regex, data))
        result.update(self.group_as_dict(self.fft_re_regex, data))
        result.update(self.group_as_dict(self.fft_img_regex, data))
        result.update(self.group_as_dict(self.utc_time_regex, data))
        result.update(self.group_as_dict(self.hz_regex, data))
        result.update(self.group_as_dict(self.wifi_strength_regex, data))
        result.update(self.group_as_dict(self.dummy_regex, data))

        return result
