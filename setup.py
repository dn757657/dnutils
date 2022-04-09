from distutils.core import setup

version = '0.0.1'

setup(name='dnutils',
      version=version,
      packages=['dn_docoptutils'],
      license='MIT',
      description='personal utility funcs',
      author='Dan',
      author_email='daniel.js.campbell@gmail.com',
      url='https://github.com/dn757657/dn_utils.git',
      download_url='https://github.com/dn757657/ct_data/archive/refs/tags/' + version + '.tar.gz',
      keywords=['utility'],
      install_requires=[
      ],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      )
