from flask import Blueprint, jsonify, request, session, copy_current_request_context, Response
import json, requests
from sqlalchemy import inspect
from apps import app

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def objectList_as_dict(objList):
    resultLst = []
    for obj in objList:
        objValue = {c.key: getattr(obj, c.key)
                    for c in inspect(obj).mapper.column_attrs}
        resultLst.append(objValue)
    return resultLst


def rowProxyObjList_as_dic(objList):
    resultLst = []
    for row in objList:
        resultLst.append(dict(zip(row.keys(), row)))
    return resultLst