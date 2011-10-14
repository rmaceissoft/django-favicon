import tldextract


def get_favicon(url):
    result = tldextract.extract(url)
    domain = '.'.join((result.domain, result.tld))
    return 'http://www.google.com/s2/favicons?domain=%s' % domain