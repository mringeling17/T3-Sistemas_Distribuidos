# Tarea 3 Sistemas Distribuidos
 
 Sistema Dockerizado con Apache Hadoop MapReduce para contar palabras en Wikipedia como un buscador.

## Herramientas Utilizadas

- [Hadoop](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
- [MongoDB](https://www.mongodb.com/docs/)
- [Docker](https://www.docker.com/get-started/)

## Deployment

To deploy this project run

```bash
  docker-compose build
  docker-compose up
```


## API Reference

#### Listar todas las repeticiones de la palabra encontrada en todas las páginas
```http
  GET localhost:5000/full?search={WORD}
```

#### Listar la URL que contiene el mayor número de repeticiones de la palabra
```http
  GET localhost:5000/max?search={WORD}
```

## Video explicativo

- [Video - Youtube](https://youtu.be/AK_M4xxKiDI)

## Authors

- [@Tukzon](https://www.github.com/Tukzon)
- [@Mringeling17](https://www.github.com/Mringeling17)
