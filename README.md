# semilog_blueprint_deploy

## Setup
1. Setup dev environment
```
git clone git@github.com:benber86/semilog_blueprint_deploy.git
uv venv
source .venv/bin/activate
uv install
```

2. Copy `.env.example` to `.env` and set up API keys
3. Update 

## Run tests

```
mox test --network mainnet-fork
```


## Deploy

```
mox run script/deploy.py --network mainnet
```