# pymongo-api

## Как запустить

Запуск финальной `Mongo` инфраструктуры, `Redis` и `Python` приложения:

```shell
cd mongo-sharding-repl
docker compose up -d
```

> Инициализации реплика сетов и шардирования сделаны в одноразовых `init` контейнерах!

Количество документов в каждом из шардов, а также количество реплик вместе с primary инстансом можно посмотреть
по GET рутовому эндпоинту `/` в поле `shards`, например:

```json
  "shards": {
    "shard1": {
      "instances_count": 4, 
      "primary": "mongo_shard_1:27018",
      "secondaries": [
        "mongo_shard_1_1:27023", 
        "mongo_shard_1_2:27024", 
        "mongo_shard_1_3:27025"
      ],
      "collections": {
        "helloDoc": {
          "documents_count": 492
        }
      }
    },
    "shard2": {
      "instances_count": 4,
      "primary": "mongo_shard_2_3:27028",
      "secondaries": [
        "mongo_shard_2:27019",
        "mongo_shard_2_1:27026",
        "mongo_shard_2_2:27027"
      ],
      "collections": {
        "helloDoc": {
          "documents_count": 508
        }
      }
    }
  },
```

Проверить запись в кэш редиса после ответа эндпоинта `/<collection_name>/users` можно по проброшенному
локальному 6379 порту, сделав коннект через какой либо UI или redis-cli.

- [Итоговая drawio схема](./schema.drawio)
