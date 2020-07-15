# Multiclip / Edgeless
Multiclip is an application that allows users to copy on one device and paste on another.

In order to identify clipboards, users are required to sign up for an account.

To access a multi-device clipboard, the user must go to a web adress TBD. Currently, the only browsers that 
are known to have the features required to allow multi-device clipboards are Google Chrome and its derivatives. Unfortunately, this means that, initially, only Chrome users will be able to take advantage of multi-device clipboards.

## Installation
Once in its finished state, users will be encouraged to use the official site instead of attempting to set up a local server.

For now, though, those excited to try Multiclip early or those wanting to develop on the code, the following 
instructions should help developers get started.

### Requirements

* Python 3.8
* Pipenv
* Django 2.2 or higher
* Django Channels
* Redis

### Local Development
If you only want to install and run Multiclip for development or demo purposes, the following 
instructions should get you up and running. To enable Multiclip to work across devices, see the following section "Production mode".

#### Setting up the environment
1. Clone this repo to your local machine
2. Navigate to the repo and run `pipenv install` to install the required dependencies.
3. Install Redis. See the Redis docs for details
4. start Redis.
5. Once the installation is complete, run `pipenv shell` to open the environment 
   in a new shell.
6. run `python manage.py runserver` to start the development server.
7. navigate to `localhost:8000/clip/signup` and signup for an account.

You should now be able to synchronize a clipboard across multiple browser tabs and multiple
browser windows. If you want to be able to synchronize a clipboard across devices, read the following 
directions.

### Production mode
In order to allow a clipboard to be synchronized across multiple devices, you 
will need to run Django in a deployment environment. In order for Google Chrome's
Clipboard API to grant sites access to it, the connection must be secure. Django's
development server does not support SSL connections, and as a result Django must be run in 
a deployment environment instead.

In addition to the dependencies described above, you will also need to install Nginx or Apache to 
host static files. If you wish, you can also setup a proxy server for Django, but I will not cover that
here.

When the dependencies were installed, you installed a python library called `daphne`. `daphne` is a production
grade ASGI server, meaning that it is capable of running a Django Channels application in a production
environment.

The essential steps for runnning Multiclip in production mode are as follows:

1. Generate or obtain an SSL certificate and key for use by daphne
2. Change the `STATIC_URL` field in `multiclip/settings.py` to point to the location of the Nginx or Apache
   Static file server.
3. Ensure that the host for static files is configured to serve files via SSL.
4. Make sure that the static file server is running and accessible. 
5. Start `daphne` by running:
```bash
# Make sure that you are using the pipenv environment
pipenv shell

# Start daphne
daphne -e ssl:<SSL_PORT>:privateKey=<SSL_KEY>:certKey=<SSL_CERTIFICATE> multiclip.asgi.application
```
It is easiest to point to the ssl key and ssl certificate if they are placed in the project root directory.

Unfortunately, details for configuring Apache or Nginx are complex and out of the scope of this readme. If you're curious for the details, I can write a short guide for configuring Nginx in the wiki.


Thanks for your interest in multiclip! Let me know if you have any bug reports or feature suggestions.