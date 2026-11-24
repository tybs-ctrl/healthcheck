# Simple healthcheker api

Simple health checker that uses docker-compose to run 

```yaml
services:
  healthcheck:
    image: tybsct/healthcheck:latest
    ports:
      - "6789:6789"
    configs:
      - healthchecks

configs:
  healthchecks:
    file: ./healthchecks.json
```
Config has this format
```json
[
    {"host": "google.com", "port": 443},
    {"host": "github.com", "port": 443},
    {"host": "1.1.1.1", "port": 53}
]
```

