class FluentSSML(object):

    def __init__(self):
        self.text = ''
        self.tag_stack = []

    def append(self, text, close_tag):
        self.text = '{}{}'.format(self.text, text)
        self.tag_stack.append(close_tag)
        return self

    def append_txt(self, text):
        self.text = '{}{}'.format(self.text, text)
        return self

    def break_str(self, strength):
        return self.append_txt('<break strength="{}" />'.format(strength))

    def break_none(self):
        return self.break_str('none')

    def break_x_w(self):
        return self.break_str('x-weak')

    def break_w(self):
        return self.break_str('weak')

    def break_m(self):
        return self.break_str('medium')

    def break_s(self):
        return self.break_str('strong')

    def break_x_s(self):
        return self.break_str('x-strong')

    def break_ms(self, duration):
        self.text = '<break time="{}ms" />'.format(duration)
        return self

    def break_secs(self, duration):
        self.append_txt('<break time="{}s" />'.format(duration))
        return self

    def paragraph(self):
        self.append('<p>', '</p>')
        return self

    def phoneme_i(self, pronounce):
        self.append('<phoneme alphabet="ipa" ph=\"{}\">'.format(pronounce),
                    '</phoneme>')
        return self

    def phoneme_x(self, pronounce):
        self.append('<phoneme alphabet="x-sampa" ph=\"{}\">'.format(pronounce),
                    '</phoneme>')
        return self

    def sentence(self):
        self.append('<s>', '</s>')
        return self

    def say_as(self, int_as, fmt=None):
        if not fmt:
            self.append('<say-as interpret-as="{}">'.format(int_as),
                        '</say-as>')
        else:
            self.append('<say-as interpret-as="{}" format="{}">'
                        .format(int_as, fmt), '</say-as>')
        return self

    def say_as_spell(self):
        return self.say_as('spell-out')

    def say_as_number(self):
        return self.say_as('number')

    def say_as_ordinal(self):
        return self.say_as('ordinal')

    def say_as_digits(self):
        return self.say_as('digits')

    def say_as_fraction(self):
        return self.say_as('fraction')

    def say_as_unit(self):
        return self.say_as('unit')

    def say_as_date(self, fmt):
        return self.say_as('date', fmt)

    def say_as_time(self):
        return self.say_as('time')

    def say_as_phone(self):
        return self.say_as('telephone')

    def say_as_interjection(self):
        return self.say_as('interjection')

    def audio(self, text):
        self.text = '{}<audio src="{}"/>'.format(self.text, text)
        return self

    def lang(self, code):
        self.append('<lang xml:lang="{}">'.format(code), '</lang>')
        return self

    def prosody(self, attr, val):
        return self.append('<prosody {}="{}">'.format(attr, val), '</prosody>')

    def vol_silent(self):
        return self.prosody('volume', 'silent')

    def vol_x_soft(self):
        return self.prosody('volume', 'x-soft')

    def vol_soft(self):
        return self.prosody('volume', 'soft')

    def vol_loud(self):
        return self.prosody('volume', 'loud')

    def vol_x_loud(self):
        return self.prosody('volume', 'x-loud')

    def rate(self, level):
        self.append('<prosody rate="{}">'.format(level), '</prosody>')
        return self

    def rate_def(self):
        return self.rate("default")

    def rate_inc(self, val):
        return self.rate("+{}%".format(val))

    def rate_dec(self, val):
        return self.rate("-{}%".format(val))

    def txt_x(self, text):
        return self.txt(text, False)

    def txt(self, text, close_tag=True):
        self.text = '{}{}'.format(self.text, text)
        if close_tag:
            while len(self.tag_stack) > 0:
                self.text = '{}{}'.format(self.text, self.tag_stack.pop())
        return self

    @property
    def ssml(self):
        return "<speak>{}</speak>".format(self.text)
