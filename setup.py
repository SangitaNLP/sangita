from distutils.core import setup

setup(name='Sangita',
      version='1.0.1dev',
      description='A Natural Language Toolkit for Indian Languages',
      author='Samriddhi Sinha',
      author_email='samriddhidjokestersinha@gmail.com',
      url='https://github.com/djokester/sangita',
      packages=['sangita.hindi', 'sangita.hindi.corpora', '.sangita.hindi.corpora.wordEmbeddings']
      )
