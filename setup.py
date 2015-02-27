from setuptools import setup, find_packages

setup(
    name = "wagtail-blog",
    version = "1.0",
    author = "David Burke",
    author_email = "david@thelabnyc.com",
    description = ("A wordpress like blog app implemented in wagtail"),
    license = "Apache License",
    keywords = "django wagtail blog",
    url = "https://github.com/thelabnyc/wagtail_blog",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: Apache License",
    ],
    install_requires=[
        'wagtail>=0.8.5',
    ]
)
