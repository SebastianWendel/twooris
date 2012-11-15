# Description #

Twooris is a simple wrapper script for the attraktor dooris door status system to post open or closed status notification on twitter.

<http://dooris.koalo.de>

# Requirements #

There are no special platform dependencies, but you need to install some python libraries.

## Debian or Ubuntu ##

    sudo aptitude install python-simplejson python-httplib2 python-oauth2

## CentOS or RedHat ##

    wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-7.noarch.rpm
    sudo rpm -Uvh epel-release-6*.rpm
    sudo yum install python-simplejson python-httplib2 python-oauth2

## Install the python-twitter librarie ##

    wget http://python-twitter.googlecode.com/files/python-twitter-x.x.x..tar.gz
    tar xzf python-twitter-x.x.x.tar.gz
    cd python-twitter-x.x.x
    python setup.py build
    python setup.py install

## Twitter registration ##

Register your new read- and writable application at twitter and keep the tokens for the configuration.

<https://dev.twitter.com/apps>

## Twooris Config ##

Now create the config file and append your twitter tokens.

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

You can start the script or add it to a non privileged users crontab like the following:

    crontab -e
    */5 * * * * /opt/twooris/twooris.py

# ToDos and Issues #
Have a lock at the github issues section. There's still some work to do, patches are welcome.

# License and Author #

Author: Sebastian Wendel, (<packages@sourceindex.de>)

Copyright: 2012, SourceIndex IT-Serives

Licensed under the GNU GENERAL PUBLIC LICENSE (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
