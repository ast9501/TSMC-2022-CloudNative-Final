# General Setting
NUMS_OF_SEARCH_RESULT = 20

# Program Arguments
BLACKLIST = (
    # Google
    'https://www.google.',
    'https://google.',
    'https://webcache.googleusercontent.',
    'http://webcache.googleusercontent.',
    'https://policies.google.',
    'https://support.google.',
    'https://maps.google.'

    # Wikipedia
    'https://en.wikipedia.org',
    'https://zh.wikipedia.org',
)

TARGET_KEYWORDS = {
    "TSMC": (
        'TSMC',
        'Taiwan Semiconductor Manufacturing Co., Ltd.'
        '台積電',
        '台積電 半導體'
        '台灣積體電路製造'
        '2330.TW',
        '台積電 股價'
        'TSMC Report'
    ),
    'ASML': (
        'ASML',
        '艾司摩爾',
        '台灣艾司摩爾科技股份有限公司'
        '荷蘭 ASML',
        'ASML 晶片'
        'ASML AMS',
        'ASML Report'
    ),
    'Applied Materials': (
        'Applied Materials',
        '台灣應用材料股份有限公司',
        '應用材料',
        'NASDAQ: AMAT',
        'Applied Materials 半導體設備',
        'Applied Materials Report'
    ),
    'SUMCO': (
        'SUMCO',
        'SUMCO 日本',
        '勝高',
        'TYO 3436',
        'SUMCO 晶圓'
        'SUMCO Report'
    )
}
