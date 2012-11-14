# Description #

Twooris is a simple wrapper script for the attraktor dooris door status system to post open or closed status notification on twitter.

<http://dooris.koalo.de>

# Requirements #

    sudo aptitude install python-simplejson python-httplib2 python-oauth2

    wget http://python-twitter.googlecode.com/files/python-twitter-0.8.2.tar.gz
    tar xzf python-twitter-0.8.2.tar.gz
    cd python-twitter-0.8.2
    python setup.py build
    python setup.py install

<https://dev.twitter.com/apps>

    cat >> twooris.cfg << 'EOF'
    [dooris]
    dooris_url          = http://dooris.koalo.de/door.txt
 
    [twitter]
    consumer_key        =
    consumer_secret     =
    access_token        =
    access_token_secret =
    EOF

# Usage #
Simply include the recipe where you want elasticsearch installed.

# ToDos and Issues #
Have a lock at the github issues section. There's still some work to do, patches are welcome.

# License and Author #

Author: Sebastian Wendel, (<packages@sourceindex.de>)

Copyright: 2012, SourceIndex IT-Serives

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
