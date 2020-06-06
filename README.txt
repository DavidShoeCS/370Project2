README

This program has two functions.  One to generate a one time password QR code
designed to work with the Google Authenticator app, and one to display the 6 digit
one time password.

This program requires pyotp and qrcode which can be downloaded by calling
the following commands via the terminal:
pip3 install pyotp
pip3 install qrcode[PIL]

The script imports:
pyotp
time
qrcode
sys
