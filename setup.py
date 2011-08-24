from distutils.core import setup


package_list = ['mpltex', ]
classifier_list = ['License :: OSI Approved :: MIT License',]

setup(name = 'mpltex', version = '0.0.1',
      description = 'Tools and examples for LaTeX figures using matplotlib.',
      author = 'M J Stanway', author_email = 'm.j.stanway@alum.mit.edu',
      packages = package_list, classifiers = classifier_list,
    )
