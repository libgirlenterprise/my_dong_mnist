from setuptools import setup, find_packages

setup(
    name='my_dong_mnist',
    version='0.1',
    description='none',
    license='MIT',
    install_requires=[
        'tensorflow',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['my_dong_mnist=my_dong_mnist:main'],
    },
)
