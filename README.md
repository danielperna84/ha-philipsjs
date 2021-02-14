# ha-philipsjs
Wrapper library to integrate Philips TVs with jointSPACE API into Home-Assistant

This is just being used to wrap the API into a nice object. Nothing fancy.

* Support version 1 and 6 of the jointspace API
* Support pairing process
* Python typing information on endpoints
* NotifyChange support for supported tv's

Print system data
```python
from haphilipsjs import PhilipsTV

tv = PhilipsTV("tv2.ecce.loc", 6)
tv.getSystem()
print(tv.system)
```

Pairing with TV
```python
from haphilipsjs import PhilipsTV

tv = PhilipsTV("tv2.ecce.loc", 6)
tv.getSystem()

state = tv.pairRequest("my_test_app", "My Test App", "mox", "OSX", "native")

pin = input("Enter pin:")

username, password = tv.pairGrant(state, pin)

print(username)
print(password)
```


Command line utility:
```
usage: python -m haphilipsjs [-h] [-d] -i HOST -a API [-u USERNAME] [-p PASSWORD] {status,monitor,ambilight,pair} ...

positional arguments:
  {status,monitor,ambilight,pair}
                        commands
    status              Show current tv status
    monitor             Monitor current tv status
    ambilight           Control ambilight
    pair                Pair with tv

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Debug output
  -i HOST, --host HOST
  -a API, --api API
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        Password
```
