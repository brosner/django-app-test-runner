#!/usr/bin/env python

import os
import sys

from optparse import OptionParser

from django.conf import settings
from django.conf import global_settings
from django.core.management import call_command

def main():
    """
    The entry point for the script. This script is fairly basic. Here is a
    quick example of how to use it::
    
        app_test_runner.py [path-to-app]
    
    You must have Django on the PYTHONPATH prior to running this script. This
    script basically will bootstrap a Django environment for you.
    
    By default this script with use SQLite and an in-memory database. If you
    are using Python 2.5 it will just work out of the box for you.
    
        app_test_runner.py
    """
    parser = OptionParser()
    parser.add_option("--DATABASE_ENGINE", dest="DATABASE_ENGINE", default="sqlite3")
    parser.add_option("--DATABASE_NAME", dest="DATABASE_NAME", default="")
    parser.add_option("--DATABASE_USER", dest="DATABASE_USER", default="")
    parser.add_option("--DATABASE_PASSWORD", dest="DATABASE_PASSWORD", default="")
    options, args = parser.parse_args()
    
    sys.path.insert(0, os.path.abspath(os.path.join(os.curdir)))
    settings.configure(**{
        "DATABASE_ENGINE": options.DATABASE_ENGINE,
        "DATABASE_NAME": options.DATABASE_NAME,
        "DATABASE_USER": options.DATABASE_USER,
        "DATABASE_PASSWORD": options.DATABASE_PASSWORD,
        "INSTALLED_APPS": global_settings.INSTALLED_APPS + (
            args[0],
        ),
    })
    call_command("test")

if __name__ == "__main__":
    main()