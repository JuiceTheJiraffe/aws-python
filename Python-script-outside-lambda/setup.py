from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Jacob Johnson',
    description='Webotron is a python script used to deploy a static website in AWS',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/JuiceTheJiraffe/aws-python/tree/master/Python-script-outside-lambda/webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    webotron=webotron.webotron:cli
    '''
)
