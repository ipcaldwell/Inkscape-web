#!/usr/bin/env python
# -*- encoding: utf8 -*-

if __name__ == '__main__':
    try:
        from app import db
        from sqlalchemy import event
        db.drop_all()
        db.create_all()
        print("[SUCCESS] Schema created")
    except Exception, err:
        print("[FAIL] Could not create schema. Error: {0}".format(err))
