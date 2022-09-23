#!/usr/bin/env python3

import os
from parse import BibParser

PUB_PATH = '../../content/publication/'

tbl = {
        'jan' : 1,
        'feb' : 2,
        'mar' : 3,
        'apr' : 4,
        'may' : 5,
        'jun' : 6,
        'jul' : 7,
        'aug' : 8,
        'sep' : 9,
        'oct' : 10,
        'nov' : 11,
        'dec' : 12,
        'january' : 1,
        'february': 2,
        'march' : 3,
        'april' : 4,
        'june' : 6,
        'july' : 7,
        'august' : 8,
        'september' : 9,
        'october' : 10,
        'november' : 11,
        'december' : 12,
    }

class PubGenerator(object):
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.args = ['---', "publication_types: ['1']", "publishDate: 1999-01-01T00:00:00Z", '']

    def add_authors(self):
        authors = self.item['author'].split(' and ')
        args = ['authors:']
        for author in authors:
            if author.lower() == 'Yeongjin Jang'.lower():
                args.append('  - %s' % 'admin')
            else:
                args.append('  - %s' % author)
        self.args += args
        self.args.append('')

    def add_date(self):
        print(self.item['key'])
        year = self.item['year']
        month = self.item['month']
        int_y = int(year)
        int_m = int(tbl[month.lower()])
        datestr = "%d-%02d-01T00:00:00Z" % (int_y, int_m)
        self.args.append("date: '%s'" % datestr)
        self.args.append('')

    def add_venue(self):
        self.args.append("publication: '%s'" % self.item['pubstring'])
        self.args.append('')

    def add_title(self):
        print(self.item)
        self.args += ["title: '%s'" % self.item['title'], '']

    def add_abstract(self):
        fn = 'pubs/%s-abstract.md' % self.item['key']
        if not os.path.exists(fn):
            return
        with open(fn) as f:
            abstract = f.read().strip()
            abstract = ' '.join(abstract.split('\n'))
            abstract = '"'.join(abstract.split("'"))
            self.args.append("abstract: '%s'" % abstract)
            self.args.append('')

    def add_slide(self):
        fn = 'pubs/%s-slides.pdf' % self.item['key']
        if not os.path.exists(fn):
            return
        with open(fn, 'rb') as f:
            # copy paper to static
            with open('../../static/uploads/%s-slides.pdf' % self.item['key'], 'wb') as f2:
                f2.write(f.read())
                self.args.append('url_slides: uploads/%s-slides.pdf' % self.item['key'])
                self.args.append('')

    def add_video(self):
        fn = 'pubs/%s-video.link' % self.item['key']
        if not os.path.exists(fn):
            return
        with open(fn, 'rt') as f:
            link = f.read().strip()
            self.args.append('url_video: %s' % link)
            self.args.append('')

    def add_code(self):
        fn = 'pubs/%s-code.link' % self.item['key']
        if not os.path.exists(fn):
            fn = 'pubs/%s-project.link' % self.item['key']
            if not os.path.exists(fn):
                return
        with open(fn, 'rt') as f:
            link = f.read().strip()
            self.args.append('url_source: %s' % link)
            self.args.append('')


    def add_paper(self):
        fn = 'pubs/%s.pdf' % self.item['key']
        if not os.path.exists(fn):
            return
        with open(fn, 'rb') as f:
            # copy paper to static
            with open('../../static/uploads/%s.pdf' % self.item['key'], 'wb') as f2:
                f2.write(f.read())
                self.args.append('url_pdf: uploads/%s.pdf' % self.item['key'])
                self.args.append('')

    def shimai(self):
        self.args += ['', '---', '']

    def generate(self):
        return '\n'.join(self.args)

    def store(self):
        with open("%s%s.md" % (PUB_PATH, self.item['key']), 'wt') as f:
            f.write(self.generate())

    def add_all(self):
        self.add_title()
        self.add_venue()
        self.add_authors()
        self.add_date()
        self.add_abstract()
        self.add_paper()
        self.add_slide()
        self.add_video()
        self.add_code()
        self.shimai()

def main():
    bp = BibParser('yeongjin.bib')
    items = bp.parse()
    for item in reversed(items):
        pg = PubGenerator(item['key'], item)
        pg.add_all()
        pg.store()

if __name__ == '__main__':
    main()
