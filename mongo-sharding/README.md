## Как запустить

Запускаем mongo инфраструктуру и приложение

```shell
docker compose up -d
```

> Инициализации реплика сетов и шардирования сделаны в одноразовых `init` контейнерах!

Количество документов в каждом из шардов можно посмотреть по GET рутовому эндпоинту `/` в поле `shards`, например:
```json
  "shards": {
    "shard1": {
      "instances_count": 1, 
      "primary": "mongo_shard_1:27018",
      "secondaries": [],
      "collections": {
        "helloDoc": {
          "documents_count": 492
        }
      }
    },
    "shard2": {
      "instances_count": 1,
      "primary": "mongo_shard_2:27019",
      "secondaries": [],
      "collections": {
        "helloDoc": {
          "documents_count": 508
        }
      }
    }
  },
```
