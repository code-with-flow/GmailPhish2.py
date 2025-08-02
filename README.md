# GmailPhishing Tool
Phishing tool and Email Analysis Tools: A Comprehensive Guide

Table of Contents

- # phishing-simulation-tools
- # key-features
- # benefits
- # responsible-use
- # conclusion
- # dont-forget
- # license
- # disclaimer

Phishing Tools

1. *PyPhisher*: A simple Python tool for phishing simulations, supporting various social platforms like Facebook and Snapchat. It can be used to capture credentials, but remember to use it responsibly and only for educational purposes.
2. *ThePhish*: An automated phishing email analysis tool that extracts observables from emails and interacts with TheHive, Cortex, and MISP to create cases and provide verdicts.
3. *Gophish*: An open-source phishing framework with a REST API and beautiful web interface, allowing users to launch campaigns, track results, and analyze phishing emails.
4. *Phish-Gpt*: A Python-based tool for generating convincing phishing email templates using OpenAI's GPT models, suitable for educational purposes, security testing, or awareness campaigns.

Key Features

1. *Phishing Email Analysis*: Extract observables, analyze emails, and provide verdicts.
2. *Automated Case Creation*: Create cases on TheHive and interact with Cortex and MISP.
3. *Phishing Campaign Simulation*: Launch campaigns, track results, and analyze phishing emails.
4. *Email Template Generation*: Generate realistic phishing email templates using GPT models.

Benefits

1. *Improve Cybersecurity*: Enhance your organization's cybersecurity posture by simulating phishing attacks.
2. *Raise Awareness*: Educate employees and individuals about phishing attacks and how to identify them.
3. *Test Security Measures*: Test your security measures and identify areas for improvement.

Responsible Use

1. *Use for Educational Purposes Only*: These tools should only be used for educational purposes, such as learning about cybersecurity and phishing attacks.
2. *Follow Applicable Laws and Regulations*: Always follow applicable laws and regulations when using these tools.
3. *Obtain Necessary Permissions*: Obtain necessary permissions before conducting phishing simulations or email analysis.

Conclusion

Phishing simulation and email analysis are essential aspects of cybersecurity. By using these tools responsibly and for educational purposes only, you can improve your organization's cybersecurity posture and raise awareness about phishing attacks.

Don't Forget

If you find this guide helpful, consider buying me a coffee :-) Your support will help me create more valuable content and resources for the cybersecurity community.

License

This guide is licensed under the MIT License. Feel free to modify and distribute it as you see fit.

Disclaimer

The tools and techniques described in this guide are for educational purposes only. Use them responsibly and at your own risk.

# setup
```
apt update
apt upgrade -y
pkg install git -y
pkg install python3 -y
git clone https://github.com/code-with-flow/GmailPhish2.py.git
pip install -r requirements.txt
cd GmailPhish2.py
python3 GmailPhish2.py
```
# Usage
```
PHishing EMAIL tool v0.13
Usage: phemail.py [-e <emails>] [-m <mail_server>] [-f <from_address>] [-r <replay_address>] [-s <subject>] [-b <body>]
          -e    emails: File containing list of emails (Default: emails.txt)
          -f    from_address: Source email address displayed in FROM field of the email (Default: Name Surname <name_surname@example.com>)
          -r    reply_address: Actual email address used to send the emails in case that people reply to the email (Default: Name Surname <name_surname@example.com>)
          -s    subject: Subject of the email (Default: Newsletter)
          -b    body: Body of the email (Default: body.txt)
          -p    pages: Specifies number of results pages searched (Default: 10 pages)
          -v    verbose: Verbose Mode (Default: false)
          -l    layout: Send email with no embedded pictures 
          -B    BeEF: Add the hook for BeEF
          -m    mail_server: SMTP mail server to connect to
          -g    Google: Use a google account username:password
          -t    Time delay: Add deleay between each email (Default: 3 sec)
          -R    Bunch of emails per time (Default: 10 emails)
          -L    webserverLog: Customise the name of the webserver log file (Default: Date time in format "%d_%m_%Y_%H_%M")
          -S    Search: query on Google
          -d    domain: of email addresses
          -n    number: of emails per connection (Default: 10 emails)
          -c    clone: Clone a web page
          -w    website: where the phishing email link points to
          -o    save output in a file
          -F    Format (Default: 0): 
                0- firstname surname
                1- firstname.surname@example.com
                2- firstnamesurname@example.com
                3- f.surname@example.com
                4- firstname.s@example.com
                5- surname.firstname@example.com
                6- s.firstname@example.com
                7- surname.f@example.com
                8- surnamefirstname@example.com
                9- firstname_surname@example.com 
          
Examples: phemail.py -e emails.txt -f "Name Surname <name_surname@example.com>" -r "Name Surname <name_surname@example.com>" -s "Subject" -b body.txt
          phemail.py -S example -d example.com -F 1 -p 12
          phemail.py -c https://example.com
```
