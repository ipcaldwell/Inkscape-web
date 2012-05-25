#!/bin/bash

pybabel extract -F babel.conf -k __ -o app/translations/messages.pot .
