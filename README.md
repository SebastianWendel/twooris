# Description #
Twooris is a simple python script for the raspberry pi plattform to post the attraktors door open or closed status on twitter.

# Requirements #
You need a raspberry pi board, two gpio's and some packages explained in the following.

## install packages ##

    sudo aptitude update
    sudo aptitude install -y git-core python-virtualenv python-pip


## create credentials and sudo privileges ##

    sudo useradd --user-group --create-home --home-dir /opt/twooris --shell /bin/bash --system twooris
	echo "twooris ALL = NOPASSWD: /opt/twooris/twooris/twooris.py" | sudo tee -a /etc/sudoers  


## install source files ##

    sudo git clone https://github.com/sourceindex/twooris.git /opt/twooris/twooris


## setup python virtualenv and install modules ##

	sudo su - twooris 
	virtualenv /opt/twooris/pyvenv
	source /opt/twooris/pyvenv/bin/activate
	echo "source /opt/twooris/pyvenv/bin/activate" | tee -a /opt/twooris/.profile

    
## install the twitter library ##

    pip install twitter

 
## twitter registration ##
Register your new read- and writable application at twitter and keep the tokens for the configuration.

<https://dev.twitter.com/apps>


# Configuration #
Now change to the application directory.

    cd /opt/twooris/twooris

Create the config file, change the twitter tokens you just created, maybe your gpios and the text messeges.

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
    open                = Die Eingangstür wurde geöffnet.
    closed              = Die Eingangstür wurde geschlossen.
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

Author: Sebastian Wendel, (<packages@sourceindex.de>) Copyright: 2013, Attraktor e.V. Hamburg

Licensed under the GNU GENERAL PUBLIC LICENSE (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.