#!/usr/bin/env python3

import os

xref = {
        'WISA22' : ['In Proceedings of the 23rd World Conference on Information Security Applications (WISA)', 2022, 'August', 'Jeju, South Korea'],
        'SEC22' : ['In Proceedings of the 31th USENIX Security Symposium (Security)', 2022, 'August', 'Boston, MA'],
        'DTRAP22' : ['In ACM Journal Digital Threats: Research and Practice (DTRAP)', 2022, 'January', 'ACM'],
        'CCS21' : ['In Proceedings of the 28th ACM Conference on Computer and Communications Security (CCS)', 2021, 'November', 'Seoul, South Korea'],
        'IEEESP21' : ['In IEEE Security & Privacy', 2021, 'March', 'IEEE'],
        'ACSAC20' : ['In Proceedings of the 2020 Annual Computer Security Applications Conference (ACSAC)', 2020, 'December', 'Austin, TX'],
        'FSE20' : ['In Proceedings of the 2020 ACM Joint European Software Engineering Conference and Symposium (ESEC/FSE)', 2020, 'November', 'Sacramento, CA'],
        'SYSTOR20' : ['In Proceedings of the 13th ACM International Systems and Storage Conference (SYSTOR)', 2020, 'October', 'Haifa, Israel'],
        'CODASPY20' : ['In Proceedings of the 10th ACM Conference on Data and Application Security and Privacy (CODASPY)', 2020, 'March', 'New Orleans, LA'],
        'NDSS20' : ['In Proceedings of the 2020 Annual Network and Distributed Systems Security (NDSS)', 2020, 'February', 'San Diego, CA'],
        'BLACKHATEU19' : ['In Black Hat Europe 2019 Briefings', 2019, 'December', 'London, UK'],
        'DC27DML' : ['In DEF CON 27 Demo Labs', 2019, 'August', 'Las Vegas, NV'],
        'PETS19' : ['In Proceedings on Privacy Enhancing Technologies Symposium (PoPETs)', 2019, 'July', 'Stockholm, Sweden'],
        'SEC18' : ['In Proceedings of the 27th USENIX Security Symposium (Security)', 2018, 'August', 'Baltimore, MD'],
        'SYSTEX17' : ['In Proceedings of the 2nd Workshop on System Software for Trusted Execution (SysTEX)', 2017, 'October', 'Shanghai, China'],
        'SEC17' : ['In Proceedings of the 26th USENIX Security Symposium (Security)', 2017, 'August', 'Vancouver, Canada'],
        'CCS16' : ['In Proceedings of the 23rd ACM Conference on Computer and Communications Security (CCS)', 2016, 'October', 'Vienna, Austria'],
        'CSUR16' : ['In ACM Computing Surveys', 2016],
        'BLACKHAT16' : ['In Black Hat USA 2016 Briefings', 2016, 'August', 'Las Vegas, NV'],
        'SEC16' : ['In Proceedings of the 25th USENIX Security Symposium (Security)', 2016, 'August', 'Austin, TX'],
        'CCS15' : ['In Proceedings of the 22nd ACM Conference on Computer and Communications Security (CCS)', 2015, 'October', 'Denver, CO'],
        'NDSS15' : ['In Proceedings of the 2015 Annual Network and Distributed Systems Security (NDSS)', 2015, 'February', 'San Diego, CA'],
        'CCS14' : ['In Proceedings of the 21st ACM Conference on Computer and Communications Security (CCS)', 2014, 'November', 'Scottsdale, AZ'],
        'SEC14' : ['In Proceedings of the 23rd USENIX Security Symposium (Security)', 2014, 'August', 'San Diego, CA'],
        'BLACKHAT14a' : ['In Black Hat USA 2014 Briefings', 2014, 'August', 'Las Vegas, NV'],
        'BLACKHAT14b' : ['In Black Hat USA 2014 Briefings', 2014, 'August', 'Las Vegas, NV'],
        'NDSS14' : ['In Proceedings of the 2014 Annual Network and Distributed Systems Security (NDSS)', 2014, 'February', 'San Diego, CA'],
        'BLACKHAT13a' : ['In Black Hat USA 2013 Briefings', 2013, 'August', 'Las Vegas, NV'],
        }

class BibParser(object):
    _S_NONE_ = 0
    _S_ITEM_STARTED_ = 1

    def __init__(self, fn):
        self._index = 0
        self._end = 0
        self.filename = fn

    def open(self):
        with open(self.filename, 'rt') as f:
            lines = f.readlines()
            self.lines = [l.strip() for l in lines]
            self._end = len(self.lines)

    def next_line(self):
        if self._index >= self._end:
            return None
        prev_index = self._index
        self._index += 1
        return self.lines[prev_index]

    def next_item(self):
        state = BibParser._S_NONE_
        item = {}
        while True:
            l = self.next_line()
            if l == None:
                return None
            if state == BibParser._S_NONE_:
                if '@' in l and l[0] == '@':
                    state = BibParser._S_ITEM_STARTED_
                    item['key'] = l.split('{')[1][:-1]
            elif state == BibParser._S_ITEM_STARTED_:
                if l == '}':
                    state = BibParser._S_NONE_
                    break
                else:
                    if '=' in l:
                        ll = l.split('=')
                        key = ll[0].strip()
                        value = ll[1].strip()[:-1]
                        arr = []
                        for c in value:
                            if c != '{' and c != '}':
                                arr.append(c)
                        item[key] = ''.join(arr)

        return item

    def parse(self):
        bp = BibParser(self.filename)
        bp.open()
        items = []
        while True:
            item = bp.next_item()
            if item == None:
                break
            items.append(item)
        for item in items:
            if 'crossref' in item:
                cross = xref[item['crossref']]
                item['pubstring'] = cross[0]
                item['year'] = cross[1]
                if len(cross) > 2:
                    item['month'] = cross[2]
                if len(cross) > 3:
                    item['venue'] = cross[3]

            if 'url' in item:
                if 'arxiv' in item['url']:
                    if 'howpublished' in item:
                        item['pubstring'] = item['howpublished']
                    else:
                        item['pubstring'] = item['note'].split(',')[0].strip()
                elif 'eprint' in item['url']:
                    item['pubstring'] = item['howpublished']
            if 'note' in item:
                if 'arxiv' in item['note']:
                    if 'howpublished' in item:
                        item['pubstring'] = item['howpublished']
                    else:
                        item['pubstring'] = item['note'].split(',')[0].strip()
                elif 'eprint' in item['note']:
                    item['pubstring'] = item['howpublished']
                elif 'Patent' in item['note']:
                    item['pubstring'] = 'U.S. Patent ' + item['note'].split(',')[1].strip()
                elif 'Thesis' in item['note']:
                    item['pubstring'] = 'Ph.D. Thesis, Georgia Institute of Technology'


        return items


def main():
    bp = BibParser('yeongjin.bib')
    items = bp.parse()
    for item in items:
        key = item['key']
        title = item['title']
        authors = ', '.join(item['author'].split(' and '))
        _in = item['pubstring']
        venue = None
        if 'venue' in item:
            venue = item['venue']
        year = ''
        month = ''
        try:
            year = item['year']
        except:
            pass
        try:
            month = item['month']
        except:
            pass

        s = "%s\n%s\n%s\n%s, %s, %s, %s" % (key, title, authors, _in, venue, month, year)
        print(s)

if __name__ == "__main__":
    main()
