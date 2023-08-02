from setuptools import setup
import py2exe

setup(console=[{ "script": "main.py"}],
      options={"py2exe": {
            "packages": ['numpy']}})