# This is purely the result of trial and error.

import sys

from setuptools import setup, find_packages

#import httpie


# Note: keep requirements here to ease distributions packaging
tests_require = [
    'pytest',
    'pytest-httpbin>=0.0.6',
    'pytest-lazy-fixture>=0.0.6',
    'responses',
    'pytest-mock',
    'werkzeug<2.1.0'
]
dev_require = [
    *tests_require,
    'dash',
    #'flake8',
    #'flake8-comprehensions',
    #'flake8-deprecated',
    #'flake8-mutable',
    #'flake8-tuple',
    'pyopenssl',
    'pytest-cov',
    'pyyaml',
    'twine',
    'wheel',
    'Jinja2'
]
install_requires = [
    'dash >= 2.10.2',
    #'pip',
    'charset_normalizer>=2.0.0',
    'defusedxml>=0.6.0',
    'requests[socks]>=2.22.0',
    'Pygments>=2.5.2',
    'requests-toolbelt>=0.9.1',
    'multidict>=4.7.0',
    'setuptools',
    #'importlib-metadata>=1.4.0; python_version < "3.8"',
    'rich>=9.10.0'
]
install_requires_win_only = [
    'colorama>=0.2.4',
]
'''
# Conditional dependencies:

# sdist
if 'bdist_wheel' not in sys.argv:

    if 'win32' in str(sys.platform).lower():
        # Terminal colors for Windows
        install_requires.extend(install_requires_win_only)
'''

# bdist_wheel
extras_require = {
    'dev': dev_require,
    'test': tests_require,
    # https://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    #':sys_platform == "win32"': install_requires_win_only,
}


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name = 'SOScar',
    version = SOScar.__version__,
    #description = SOScar.__doc__.strip(),
    #long_description = long_description(),
    long_description_content_type = 'text/markdown',
    url = 'https://DC-2023.github.io/',
    #download_url=f'https://github.com/httpie/httpie/archive/{httpie.__version__}.tar.gz',
    author = SOScar.__author__,
    author_email = SOScar.__author_email__,
    #license = SOScar.__licence__,
    #packages = find_packages(include=['httpie', 'httpie.*']),   
    python_requires = '>=3.7',
    extras_require = extras_require,
    install_requires = install_requires,
'''    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
   
    project_urls={
        'GitHub': 'https://github.com/httpie/httpie',
        #'Twitter': 'https://twitter.com/httpie',
        #'Discord': 'https://httpie.io/discord',
        #'Documentation': 'https://httpie.io/docs',
        #'Online Demo': 'https://httpie.io/run',
    },
    data_files=[
        ('share/man/man1', ['extras/man/http.1']),
        ('share/man/man1', ['extras/man/https.1']),
        ('share/man/man1', ['extras/man/httpie.1']),
    ]
'''    
)
