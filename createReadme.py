#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Simple script to auto-generate the README.md file for a til project.
    NOTE: Someone who wanted to be fancy would actually use a template engine
    for this, but this seemed like a task for which it is best to only require
    python.  This is not a general purpose script, but tailored for the format
    being used for "Today I Learned" repos.
    Apply as a git hook by running the following command in linux:
        cd .git/hooks/ && ln -s ../../createReadme.py pre-commit && cd -
'''
from __future__ import print_function
import os

HEADER = '''# TIL

> Today I Learned

그날 공부한 것과 느낀 것들을 기록하는 공간입니다.

아주 간단한 개념이나 소소한 팁들은 [Issues][3]에 남기고있습니다.

기존에는 월별로 나누어 한 주간의 til을 한 파일에 적는 방식으로 작성하였으나
이렇게 날짜만 적어놓은 til은 비효율적이고 나중에 찾아보기도 쉽지 않아 여러가지 방법을 고민을 하던 중에
Simon Wilson님의 [TIL collection][2]을 발견하고 지금의 형식으로 til을 작성하게 되었습니다.

이 곳에 기록하는 내용들 중 일부는 [블로그][1]에 포스팅하고있습니다.
'''

FOOTER = '''
[1]: https://eunbin20.github.io/
[2]: https://github.com/jbranchaud/til
[3]: https://github.com/eunbin20/til/issues
'''


def get_list_of_categories():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs.'''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and
            '.git' not in x]
    return dirs


def get_title(til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open(til_file) as _file:
        for line in _file:
            line = line.strip()
            if line.startswith('#'):
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    ''' For a given category, get the list of TIL titles. '''
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith('.md'):
            title = get_title(fullname)
            titles.append((title, fullname))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(category)
        categories[category] = titles
        count += len(titles)
    return count, categories


def print_file(category_names, count, categories):
    ''' Now we have all the information, print it out in markdown format. '''
    with open('README.md', 'w') as file_:
        file_.write(HEADER)
        file_.write('\n')
        file_.write('_{0} TILs and counting..._'.format(count))
        file_.write('\n')
        file_.write('''
---
### Categories
''')
        # print the list of categories with links
        for category in sorted(category_names):
            file_.write('* [{0}](#{1})\n'.format(category.capitalize(),
                                                 category))

        # print the section for each category
        file_.write('''
---
''')
        for category in sorted(category_names):
            file_.write('### {0}\n'.format(category.capitalize()))
            file_.write('\n')
            tils = categories[category]
            for (title, filename) in tils:
                file_.write('- [{0}]({1})\n'.format(title, filename))
            file_.write('\n')

        file_.write(FOOTER)


def create_readme():
    ''' Create a TIL README.md file with a nice index for using it directly
        from github. '''
    category_names = get_list_of_categories()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)

if __name__ == '__main__':
    create_readme()
    os.system('git add README.md')