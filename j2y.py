# -*- coding: utf-8 -*-#
#
# May 19 2016, Christian E. Hopps <chopps@dev.terastrm.net>
#
# Copyright (c) 2016, Deutsche Telekom AG.
# All Rights Reserved.
#

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import sys
import yaml


def unicode_representer(unused, uni):
    style = "|" if "\n" in uni else ""
    return yaml.ScalarNode(tag=u'tag:yaml.org,2002:str', value=uni, style=style)

if not (sys.version_info > (3, 0)):
    yaml.add_representer(unicode, unicode_representer)
yaml.add_representer(str, unicode_representer)

if len(sys.argv) > 1 and sys.argv[1] != "-":
    f = open(sys.argv[1], "r")
else:
    f = sys.stdin

print(yaml.dump(json.load(f), allow_unicode=True, indent=4))

__author__ = ''
__date__ = 'May 19 2016'
__version__ = '1.0'
__docformat__ = "restructuredtext en"
