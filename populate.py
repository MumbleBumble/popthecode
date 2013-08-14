from search.models import *

def populate_devices():
    devices = [("IP", "iPhone; CPU iPhone OS 5_0 like Mac OS X", "Mobile/9A334"),
            ("PD", "iPad; CPU OS 5_0 like Mac OS X", "Mobile/9A334"), ("AD", "Linux; U; Android 4.0.3; LG-L160L Build/IML74K", "Mobile"),
            ("OS", "Macintosh; Intel Mac OS X 10_6_8", ""),
            ("PC", "Windows NT 6.2", "" ),
            ("LI", "X11; Linux x86_64", ""),
    ]
    for device in devices:
        Device.objects.create(name=device[0], paren=device[1], mobile=device[2])

def populate_browsers():
    browsers = [("SA", "Mozilla/5.0", "AppleWebKit/537.13+ (KHTML, like Gecko)", "Version/5.1.7 Safari/534.57.2"),
            ("CH", "Mozilla/5.0", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/28.0.1500.95 Safari/537.36" ),
            ("FF", "Mozilla/5.0", "Gecko/20100101", "Firefox/21.0"),
            ("NE", "Mozilla/5.0", "Gecko/20101104", "Netscape/9.1.0285"),
    ]
    for browser in browsers:
        Browser.objects.create(name=browser[0], mozilla=browser[1], render=browser[2], after=browser[3])

def populate():
    populate_devices()
    populate_browsers()
