# Rabbit hole
RabbitMQ client-server app

## Dependencies
- python 3.8
- docker
- docker-compose

### Run server
`$ docker-compose up`

## Client
### Install dependencies
`$ pip install -r requirements-client.txt`

### Usage
`$ python client/main.py --help`

### Commands
- AddItem --message [message]
- GetItem --id [id]
- RemoveItem --id [id]
- GetAllItems

See `results.log` file in `output` folder

## Code linting
```
$ chmod +x ./lint.sh
$ ./lint.sh
```