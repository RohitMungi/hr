hr
========

Utility to manage users on a server by using a JSON inventory list of users

Preparing the Development
=========================

1. Ensure ``pip`` and ``pipenv`` are installed.

2. Clone the repository: ``git clone git@github.com/RohitMungi/hr.git``

3. ``cd`` into the repository.

4. Fetch development dependencies ``make install``

5. Activate virtualenv: ``pipenv shell``

Usage
=====

Pass in the inventory file with the user names list.

S3 Example w/ bucket name:

::
    $ pgbackup postgres://rohit@example.com:5432/db_one --driver s3 backups

Local example w/ local path:

::

    $ pgbackup postgres://rohit@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
=============

Run tests locally using ``make`` if virtualenv is active:

::
    $ make

If virtualenv isn't active then use:

::
    $ pipenv run make
