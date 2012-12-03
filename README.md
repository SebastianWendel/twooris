# Description #
Twooris is a simple python script for the raspberry pi plattform to post the attraktors door open or closed status on twitter.

# Requirements #
You need a raspberry pi board, two gpio's and some software packages explained in the following.

## Debian or Ubuntu ##

    sudo aptitude update
    sudo aptitude install git-core python-simplejson python-httplib2 python-oauth2

## CentOS or RedHat ##

    sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-7.noarch.rpm
    sudo yum install git python-simplejson python-httplib2 python-oauth2

## Install the python-twitter library ##

    wget http://python-twitter.googlecode.com/files/python-twitter-0.8.2.tar.gz
    tar xzf python-twitter-0.8.2.tar.gz
    cd python-twitter-0.8.2
    python setup.py build
    sudo python setup.py install

## Create Group and User

    sudo groupadd twooris
    sudo useradd -s /bin/bash -r -m -g twooris twooris

## twitter registration ##
Register your new read- and writable application at twitter and keep the tokens for the configuration.

<https://dev.twitter.com/apps>

# Installation #

    cd /opt
    sudo git clone https://github.com/sebwendel/twooris.git
    sudo chown -R twooris:twooris /opt/twooris

# Configuration #
Now switch the user context and change to the application directory.

    sudo su - twooris
    cd /opt/twooris

Now create the config file, change the twitter tokens you just created, maybe your gpios and the text messeges.

IMPORTANT: Please note that i used the BCM pin layout for the gpio numbers. For more Informations please read <http://elinux.org/RPi_Low-level_peripherals> .

    cat > twooris.cfg << 'EOF'
    [gpios]
    led                 = 18
    switch              = 25
 
    [twitter]
    consumer_key        = A1r2xxgbObRUd5eEFi5TXp4e
    consumer_secret     = sqK5wwXkBKAlLBuP93fu6rDuv6Dt3NtpZWhTUFzU89kxVyMAUp3as9zRjDYCNrok
    access_token_key    = 3nAuU+NvoF3ymMjSaPLgQzQMQbiGRfK39L1wHA1DhjYbMDTx
    access_token_secret = GXFKePckfUvagiAfNxu2cqAjT+ZCFSm6dNh7gXtKkQFbW8M4K7ZBtPbG6duFDG6m
    
    [messeges]
    open                = Der Attraktor ist geöffnet.
    closed              = Der Attraktor ist geschlossen.
    EOF

Please change permissions of the config file to prevent unauthorized access.

    chmod 0600 twooris.cfg

# Usage #

You can start the script or add it to a users crontab like the following:

    crontab -e
    */5 * * * * sudo /opt/twooris/twooris/twooris.py

IMPORTANT: Please note that the script needs root permissions to access '/dev/mem' to manage the raspberry pi gpios.
    
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