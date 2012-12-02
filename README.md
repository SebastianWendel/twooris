# Description #

Twooris is a simple wrapper script for the attraktor dooris door status system to post open or closed status notification on twitter.

# Requirements #

There are no special platform dependencies, but you need to install some python librarys.

## Debian or Ubuntu ##
    sudo aptitude update
    sudo aptitude install python-simplejson python-httplib2 python-oauth2

## CentOS or RedHat ##

    wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-7.noarch.rpm
    sudo rpm -Uvh epel-release-6*.rpm
    sudo yum install python-simplejson python-httplib2 python-oauth2

## Install the python-twitter library ##

    wget http://python-twitter.googlecode.com/files/python-twitter-x.x.x..tar.gz
    tar xzf python-twitter-x.x.x.tar.gz
    cd python-twitter-x.x.x
    python setup.py build
    sudo python setup.py install

## Create Group and User
    sudo groupadd twooris
    sudo useradd -s /bin/bash -r -m -g twooris -d /opt/twooris twooris
    sudo su - twooris

## twitter registration ##

Register your new read- and writable application at twitter and keep the tokens for the configuration.

<https://dev.twitter.com/apps>

# Installation #

    git clone https://github.com/sebwendel/twooris.git
    mv twooris /opt
    cd /opt/twooris

# Configuration #

Now create the config file, append the dooris.txt url and your twitter tokens.

    cat > twooris.cfg << 'EOF'
    [gpios]
    led                 = 18
    switch              = 22
 
    [twitter]
    consumer_key        = A1r2xxgbObRUd5eEFi5TXp4e
    consumer_secret     = sqK5wwXkBKAlLBuP93fu6rDuv6Dt3NtpZWhTUFzU89kxVyMAUp3as9zRjDYCNrok
    access_token        = 3nAuU+NvoF3ymMjSaPLgQzQMQbiGRfK39L1wHA1DhjYbMDTx
    access_token_secret = GXFKePckfUvagiAfNxu2cqAjT+ZCFSm6dNh7gXtKkQFbW8M4K7ZBtPbG6duFDG6m
    
    [messeges]
    open                = Der Attraktor ist geöffnet, komm herein und werde Teil.
    closed              = Der Attraktor ist geschlossen, gehen sie weiter es gibt hier nichts mehr zu sehen.
    EOF

Please change permissions of the config file to prevent unauthorized access.

    chmod 0600 twooris.cfg

# Usage #

You can start the script or add it to a non privileged users crontab like the following:

    crontab -e
    */5 * * * * /opt/twooris/twooris.py

# ToDos and Issues #
Have a lock at the github issues section. There's still some work to do, patches are welcome.

# License and Author #

Author: Sebastian Wendel, (<packages@sourceindex.de>) Copyright: 2012, Attraktor e.V. Hamburg

Licensed under the GNU GENERAL PUBLIC LICENSE (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
