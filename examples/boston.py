from fluentssml import FluentSSML

fs = FluentSSML()

s = fs.txt("if") \
        .phoneme_i('"jO: "kAz "blIN.k@z').txt("your car's blinkers") \
        .phoneme_i('%A').txt('are') \
        .txt('broken, it may be the') \
        .phoneme_i('"blIN.k@').txt('blinker')\
        .txt('relay.') \
        .phoneme_i('"fO.tS@n.@t.li').txt('Fortunately,') \
        .txt('this') \
        .phoneme_i('"kA').txt('car').txt('fix is easy to do.')

print s.ssml
