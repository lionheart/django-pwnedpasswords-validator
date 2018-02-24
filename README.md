<!-- <p align="center">
  <img width="344" height="225" src="meta/repo-banner-small.png" />
</p> -->

![](meta/repo-banner.png?1)
[![](meta/repo-banner-bottom.png)][lionheart-url]

[![Version][version-badge]][pypi-url]
[![Python Versions][versions-badge]][pypi-url]

`django-pwnedpasswords-validator` is a Django password validator that checks if a user-provided password exists in a data breach using the [Pwned Passwords v2 API](https://haveibeenpwned.com/API/v2#PwnedPasswords). All provided password data is [k-anonymized][k-anonymous-url] before being sent to the API, so plaintext passwords never leave your server.

From https://haveibeenpwned.com/API/v2#PwnedPasswords:

> Pwned Passwords are more than half a billion passwords which have previously been exposed in data breaches. The service is detailed in the [launch blog post](https://www.troyhunt.com/introducing-306-million-freely-downloadable-pwned-passwords/) then [further expanded on with the release of version 2](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2). The entire data set is [both downloadable and searchable online via the Pwned Passwords page](https://haveibeenpwned.com/Passwords).

## Installation

django-pwnedpasswords-validator is available for download through [PyPi][pypi-url]. You can install it right away using pip.

```bash
pip install django-pwnedpasswords-validator
```

Then, add django-pwnedpasswords-validator to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'django_pwnedpasswords_validator'
)
```

Finally, add django-pwnedpasswords-validator to `AUTH_PASSWORD_VALIDATORS`:

```python
AUTH_PASSWORD_VALIDATORS = [
    ...
    {
        'NAME': "django_pwnedpasswords_validator.validation.PwnedPasswordValidator"
    }
]
```

#### Security Note

No plaintext passwords ever leave your server using django-pwnedpasswords-validator.

How does that work? Well, the Pwned Passwords v2 API has a pretty cool [k-anonymity][k-anonymous-url] implementation.

From https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/:

> Formally, a data set can be said to hold the property of k-anonymity, if for every record in a released table, there are k − 1 other records identical to it.

This allows us to only provide the first 5 characters of the SHA-1 hash of the password in question. The API then responds with a list of SHA-1 hash suffixes with that prefix. On average, that list contains 478 results.

People smarter than I am have used [math](https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/) to show that 5-character prefixes are sufficient to maintain k-anonmity.

In short: your plaintext passwords are protected if you use this library. You won't leak any enough data to identity which passwords you're searching for.

## Thanks

Special thanks to [Troy Hunt](https://www.troyhunt.com) for collecting this data and providing this service.

## Authors

[Dan Loewenherz](https://github.com/dlo)

## License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

[ci-badge]: https://img.shields.io/travis/lionheart/django-pwnedpasswords-validator.svg?style=flat
[version-badge]: https://img.shields.io/pypi/v/django-pwnedpasswords-validator.svg?style=flat
[versions-badge]: https://img.shields.io/pypi/pyversions/django-pwnedpasswords-validator.svg?style=flat

[travis-repo-url]: https://travis-ci.org/lionheart/django-pwnedpasswords-validator
[k-anonymous-url]: https://en.wikipedia.org/wiki/K-anonymity
[semver-url]: http://www.semver.org
[pypi-url]: https://pypi.python.org/pypi/django-pwnedpasswords-validator
[lionheart-url]: https://lionheartsw.com/

