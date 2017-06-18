from email.parser import HeaderParser
from email.utils import getaddresses


def parse_content(content):
    parser = HeaderParser()
    data = dict()

    msg = parser.parsestr(content)
    subject = msg.get_all('subject')
    if subject:
        data['Subject'] = subject

    from_ = getaddresses(msg.get_all('from', []))
    if len(from_) > 0:
        data['From'] = from_

    to_ = getaddresses(msg.get_all('to', []))
    if len(to_) > 0:
        data['To'] = to_

    cc = getaddresses(msg.get_all('cc', []))
    if len(cc) > 0:
        data['Cc'] = cc

    bcc = getaddresses(msg.get_all('bcc', []))
    if len(bcc) > 0:
        data['Bcc'] = bcc

    sender_ip = msg.get_all('x-originating-ip')  # For Microsoft Exchange
    sender_ip_list = list()
    if sender_ip:
        for ips in sender_ip:
            sender_ip_list.append(ips.strip('[]'))
    if len(sender_ip_list) > 0:
        data['Sender IP'] = sender_ip_list

    return data
