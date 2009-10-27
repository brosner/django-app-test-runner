from distutils.core import setup


setup(
    name = "django-app-test-runner",
    version = "0.1",
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    description = "Run Django app tests standalone",
    long_description = open("README").read(),
    license = "BSD",
    url = "http://github.com/brosner/django-app-test-runner",
    py_modules = [
        "app_test_runner",
    ],
    scripts = [
        "bin/app-test-runner",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)