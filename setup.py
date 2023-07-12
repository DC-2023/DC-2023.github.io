from setuptools import setup, find_packages
'''
# Note: keep requirements here to ease distributions packaging
tests_require = [
    #'pytest',
    #'pytest-httpbin>=0.0.6',
    #'pytest-lazy-fixture>=0.0.6',
    'responses',
    #'pytest-mock',
    'werkzeug<2.1.0'
]
'''
dev_require = [
    #*tests_require,
    'dash',
    'flake8',
    'flake8-comprehensions',
    'flake8-deprecated',
    'flake8-mutable',
    'flake8-tuple',
    'pyopenssl',
    #'pytest-cov',
    'pyyaml',
    'twine',
    'wheel',
    'Jinja2'
]
install_requires = [
    'pip',
    'dash >= 2.10.2',
    'charset_normalizer>=2.0.0',
    'defusedxml>=0.6.0',
    'requests[socks]>=2.22.0',
    'Pygments>=2.5.2',
    'requests-toolbelt>=0.9.1',
    'multidict>=4.7.0',
    'setuptools',
    'rich>=9.10.0'
]

# bdist_wheel
extras_require = {
    'dev': dev_require,
    #'test': tests_require,
    # https://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    #':sys_platform == "win32"': install_requires_win_only,
}


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name = 'SOScar',
    version = '1.0.0',
    description = 'SOScars',
    long_description = long_description(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/DC-2023/DC-2023.github.io',
    author = 'DenCom',
    author_email = '',
    license = 'Apache 2.0',
    #packages = find_packages(include=['uzel', 'truck']),   
    python_requires = '>=3.10',
    extras_require = extras_require,
    install_requires = install_requires,
)
