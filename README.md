# Tell Show

This is a simple script to remind me of when my favorite shows are on. 

Two python scripts (and a single `.tell_show` file) are all that are needed. The `.tell_show` file should be in the users home directory or the same directory as this script is running from and must contain the name of each show in lowercase, each on its own line. 

The script can be run manually, or you can automate the script with `crontab -e` on \*nix systems

You can have the script send you results to your email or phone (Twitter, Pushbullet, etc). I did not want to share my personal API keys, so I use os environment variables. 

Make sure to have `export PUSHBULLET_APIKEY=your_api_key` and `export PUSHBULLET_IPHONE=your_device_key` in your `.bashrc` file. 
