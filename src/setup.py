from distutils.core import setup


setup(
    name="AVaAoMDTV",
    version="0.1.0",
    description="Applied Visualization and Analysis of Multivariate Datasets - Text Visualization",
    url="https://github.com/Zarnosch/AVaAoMDTV",
    packages=["main", "textparser", "ui"],
    requires=['PyQt5', 'nltk'],
    package_data={"ui": ["ui_files/*.ui"]}
)