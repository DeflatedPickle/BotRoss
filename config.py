import json
from json import JSONDecodeError
from pathlib import Path

import simplejson


def read_id():
    with open("token.txt") as f:
        return f.readline().strip()


def read_config():
    Path("config.json").touch(exist_ok=True)
    with open("config.json", 'r+') as f:
        try:
            pre = json.load(f)
        except JSONDecodeError:
            write_config({})
            pre = json.loads('{}')

        return dict([(int(k), v) for k, v in pre.items()])


def write_config(config):
    with open("config.json", 'w+') as f:
        f.write(simplejson.dumps(config, indent=4, sort_keys=True))
