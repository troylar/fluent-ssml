from fluentssml import FluentSSML


def test_no_text_returns_speak_tag():
    fs = FluentSSML()
    assert fs.ssml == '<speak></speak>'


def test_lang_tag_appends_lang():
    fs = FluentSSML()
    assert fs.lang('fr-FR').txt('le poisson').ssml == \
        '<speak><lang xml:lang="fr-FR">le poisson</lang></speak>'


def test_lang_and_vol_tag_appends_lang_and_vol():
    fs = FluentSSML()
    assert fs.lang('fr-FR').vol_loud().txt('le poisson').ssml == \
        '<speak><lang xml:lang="fr-FR"><prosody volume="loud">le poisson</prosody></lang></speak>'


def test_lang_and_rate_tag_appends_lang_and_rate():
    fs = FluentSSML()
    assert fs.lang('fr-FR').rate('fast').txt('le poisson').ssml == \
        '<speak><lang xml:lang="fr-FR"><prosody rate="fast">le poisson</prosody></lang></speak>'


def test_lang_and_rate_and_vaol_tag_appends_lang_and_rate_and_vol():
    fs = FluentSSML()
    assert fs.vol_x_soft().txt('I love') \
             .lang('fr-FR').rate('fast').vol_loud().txt('le poisson') \
             .ssml == \
        '<speak><prosody volume="x-soft">I love</prosody><lang xml:lang="fr-FR"><prosody rate="fast"><prosody volume="loud">le poisson</prosody></prosody></lang></speak>'


def test_break_secs_adds_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_secs(5).txt('continue').ssml == \
        '<speak>break here<break time="5s" />continue</speak>'


def test_break_none_adds_none_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_none().txt('continue').ssml == \
        '<speak>break here<break strength="none" />continue</speak>'


def test_break_x_w_adds_x_w_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_x_w().txt('continue').ssml == \
        '<speak>break here<break strength="x-weak" />continue</speak>'


def test_break_w_adds_w_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_w().txt('continue').ssml == \
        '<speak>break here<break strength="weak" />continue</speak>'


def test_break_m_adds_m_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_m().txt('continue').ssml == \
        '<speak>break here<break strength="medium" />continue</speak>'


def test_break_s_adds_s_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_s().txt('continue').ssml == \
        '<speak>break here<break strength="strong" />continue</speak>'


def test_break_x_s_adds_x_s_break():
    fs = FluentSSML()
    assert fs.txt('break here').break_x_s().txt('continue').ssml == \
        '<speak>break here<break strength="x-strong" />continue</speak>'


def test_sentence_adds_sentence():
    fs = FluentSSML()
    assert fs.sentence().txt('This is a sentence').ssml == \
        '<speak><s>This is a sentence</s></speak>'


def test_paragraph_adds_paragraph():
    fs = FluentSSML()
    assert fs.paragraph().txt('This is a paragraph').ssml == \
        '<speak><p>This is a paragraph</p></speak>'


def test_phoneme_i_adds_phoneme():
    fs = FluentSSML()
    assert fs.phoneme_i('bad').txt('bed').ssml == \
        '<speak><phoneme alphabet="ipa" ph="bad">bed</phoneme></speak>'


def test_silent_volume_adds_silent():
    fs = FluentSSML()
    assert fs.vol_silent().txt('silent').ssml == \
        '<speak><prosody volume="silent">silent</prosody></speak>'


def test_soft_volume_adds_soft():
    fs = FluentSSML()
    assert fs.vol_soft().txt('this is soft').ssml == \
        '<speak><prosody volume="soft">this is soft</prosody></speak>'


def test_loud_volume_adds_loud():
    fs = FluentSSML()
    assert fs.vol_soft().txt('this is soft').ssml == \
        '<speak><prosody volume="soft">this is soft</prosody></speak>'
