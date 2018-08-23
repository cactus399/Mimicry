import pandas
import os
import psycopg2
import numpy
import MimicServer




#
# class PgsqlPlatform:
#     def __init__(self):
#         self._psycoConnection = None
#
#     @classmethod
#     def ctor0(cls, _pramConnectionString):
#         thisguy = cls()
#         thisguy._psycoConnection = psycopg2.connect(_pramConnectionString)
#
#     @property
#     def isClosed(self):
#         return self.connection.closed
#
#     @property
#     def connection(self):
#         return self._psycoConnection

# properties - psycopg2.connection
# properties - psycopg2.cursor