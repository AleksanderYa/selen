from .browser_class import Browser


browser = Browser()
browser.connect()

inplay = browser.inplay_market()
soonplay = browser.soonplay_market()

