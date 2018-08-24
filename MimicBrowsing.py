# import pandas
# import psycopg2
# import MimicServer
#
# # NOTE:
# # the events ("shit that happened") are timestamped.
# # the events should be browsed in temporal order
# # REGARDLESS of which table it belongs to.
# # DbBrowser - have multiple cursors associated with a single connection
# # Megacursor will wrap all event cursors - Megacursor will have a method "fetchone()"
# # just like cursor. "fetchone()" will actually not advance any of the cursors
#
# class SubCursor:
#     def __init__(self, _mimicserverplatform=None, _sqlcommand=""):
#         self._mimicserverplatform = _mimicserverplatform
#         self._sqlcommand = _sqlcommand
#
#     @property
#     def sqlcommand(self):
#         return self._sqlcommand
#
#
# class DbBrowser(MimicServer.MimicServerPlatform):
#     def __init__(self):
#         super().__init__()
#         self._cursorcollection = None
#         self._stagingarray = None
#
# class DbBrowserSchema: # describes the variable across which DbBrowser will traverse the database
#     def __init__(self):
#         pass
#
# class
#
#
# # class DbBrowser(MimicServer.MimicServerPlatform):
# #     def __init__(self):
# #         super().__init__()

import pandas
import psycopg2
import MimicServer


class Logical:
    def __init__(self, _intvalue=-1):
        self._intvalue = _intvalue

    def __str__(self):
        if self._intvalue == 0:
            return "AND"
        if self._intvalue == 1:
            return "OR"
        if self._intvalue == 2:
            return "NOT"
        else:
            return ""

    def __repr__(self):
        return self.__str__()

    @property
    def operator(self):
        return self.__str__()

    @operator.setter
    def operator(self, _operatorvalue):
        _tolower = _operatorvalue.lower()
        if _tolower == "and":
            self._intvalue = 0
        if _tolower == "or":
            self._intvalue = 1
        if _tolower == "not":
            self._intvalue = 2
        else:
            self._intvalue = -1


class ConditionUnit:
    def __init__(self, _totalstr):
        if len(_totalstr) > 0:
            abool = ',' in _totalstr
            if abool == True:
                split = _totalstr.split(',')
                self._comparison = split[1]
                self._left = split[0]
                self._right = split[2]
            else:
                self._comparison = ""
                self._left = ""
                self._right = ""
        else:
            self._comparison = ""
            self._left = ""
            self._right = ""

    @classmethod
    def ctor0(cls):
        return cls()

    def __str__(self):
        thestr = ""
        thestr += self._left + self._comparison + self._right
        return thestr

    def __repr__(self):
        return self.__str__()


class ConditionBundle:
    def __init__(self, _conditionunits=None, _logicals=None):
        if _conditionunits != None:
            numunits = len(_conditionunits)
            if numunits > 0:
                self._logicals = [Logical(1)]*(numunits - 1)
            else:
                self._logicals = _logicals
        self._conditionunits = _conditionunits

    def __str__(self):
        thestr = ""
        thestr += "("
        counter = 0
        unitslength = len(self._conditionunits)
        for acondition in self._conditionunits:
            if counter > 0:
                thestr += " "
            thestr += str(acondition)
            if counter < unitslength - 1:
                thestr += " "
                thestr += str(self._logicals[counter])
            counter += 1
        thestr += ")"
        return thestr

    def __repr__(self):
        return self.__str__()


class ConditionCollection:
    def __init__(self, _unitsbundles=None, _logicals=None):
        self._unitsbundles = _unitsbundles
        self._logicals = _logicals

    def __str__(self):
        thestr = ""
        counter = 0
        unitslength = len(self._unitsbundles)
        for acondition in self._unitsbundles:
            if counter > 0:
                thestr += " "
            thestr += str(acondition)
            if counter < unitslength - 1:
                thestr += " "
                thestr += str(self._logicals[counter])
            counter += 1
        return thestr

    def __repr__(self):
        return self.__str__()


cu1 = ConditionUnit('subject_id,=,3015')
cu2 = ConditionUnit('charttime,=,2017-10-28')
cu3 = ConditionUnit('hadm_id,=,100')
cb1 = ConditionBundle([cu1,cu2,cu3])
cu4 = ConditionUnit('dischtime,<,2017-10-30')
cc1 = ConditionCollection([cu4,cb1],['AND'])
print(cc1)

