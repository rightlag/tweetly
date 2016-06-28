# Getting Started

To bootstrap the `tweetly` app, start by cloning the `tweetly` repository:

    $ git clone https://github.com/rightlag/tweetly.git
    $ cd tweetly

Create a Python virtual environment and install the dependences:

    $ virtualenv twitter
    $ source twitter/bin/activate
    $ pip install -r requirements.txt

Then, set the following environment variables:

| Variable        | Description                                                  | Required |
|-----------------|--------------------------------------------------------------|----------|
| `CONSUMER_KEY`    | Your Twitter Consumer Key                                    | **Yes**      |
| `CONSUMER_SECRET` | Your Twitter Consumer Secret                                 | **Yes**      |
| `MYSQL_USER`      | The MySQL database user                                      | **Yes**      |
| `MYSQL_PASSWORD`  | The password for the MySQL database user                     | **Yes**      |
| `MYSQL_DB`        | The name of the MySQL database                               | **Yes**      |
| `PORT`            | The server port for the application to run on (default 3000) | **No**       |

After the environment variables are set, execute the `.sql` script:

    $ mysql -u <USERNAME> -p <PASSWORD> < schema.sql

**Note:** Remove the `<` and `>` symbols before *and* after `USERNAME` and `PASSWORD`.

# Run the Server

    $ python runserver.py

The application *should* be running on `0.0.0.0:3000` or to the port you set for your environment variable.
