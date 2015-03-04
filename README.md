# Twog: A simple Twilio powered voice blog

Blog about your daily activities using your voice and a mobile phone. No internet connection needed!

You can find my voice blog on: [https://twog.herokuapp.com](https//:twog.herokuapp.com).

## Usage
1. Create a free [Twilio](https://www.twilio.com) account and a [voice number](https://www.twilio.com/user/account/phone-numbers/incoming).
2. Clone the repository.
3. Change `AUTH_TOKEN` and `ACCOUNT_SID` in `config.py`. You can find them under [account settings](https://www.twilio.com/user/account/settings)
4. Create a [Heroku](https://heroku.com) app and push your code into the app.
5. Change the request url in your [manage number](https://www.twilio.com/user/account/phone-numbers/incoming) page. This should be in the form of yourappname.herokuapp.com.
6. Call the number in [manage number](https://www.twilio.com/user/account/phone-numbers/incoming) to record your first post.
7. Yes it's that simple.

## Is it tested?
Yes, it's that good. You can find tests in `tests.py`

## Is it responsive?
Yes, it uses [Bootstrap](http://getbootstrap.com/).

## Stack?
Bootstrap+Flask+Twilio.