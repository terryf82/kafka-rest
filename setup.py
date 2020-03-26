import sys
from setuptools import setup, find_packages

from kafka_rest import __version__

install_requires = [
    'tornado>=4.0.0,<5.0.0',
    'avro_json_serializer>=0.4.1,<0.5.0',
    'avro-python3==1.9.2.1'
]

setup(
    name='kafka-rest',
    version=__version__,
    description="Async client for Confluent's Kafka REST Proxy",
    url='https://github.com/gamechanger/kafka-rest',
    author='GameChanger',
    author_email='travis@gc.io',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=[
        'mock==1.3.0',
        'nose==1.3.7'
    ],
    test_suite="nose.collector",
    zip_safe=False
)
