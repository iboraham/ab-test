from distutils.core import setup

setup(
    name="ab-test",
    packages=["abtest"],
    version="0.1",
    license="MIT",
    description="A/B testing framework for python",
    author="Ibrahim Onur Serbetci",
    author_email="onurserbetcii@gmail.com",
    url="https://github.com/iboraham/ab-test",
    download_url="https://github.com/iboraham/ab-test/archive/v_01.tar.gz",
    keywords=[
        "ab-testing",
        "hypothesis-testing",
        "z-test",
    ],
    install_requires=[
        "statsmodels",
        "pandas",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
