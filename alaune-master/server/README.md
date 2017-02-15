# Serveur

Le serveur est développé à l'aide du [`framework python flask`](http://flask.pocoo.org/). Le serveur sert donc des *routes* (des URLs)

Chaque route  est servie par une fonction dédiée. La fonction ets liée à l'URL et invoquée en utlisant le mécanisme de surcharge "@" de python.

Le serveur apparaît donc comme le contrôleur de l'application. Pour l'hure, il prend aussi en charge le calcul de la vue (les pages HTML) calculée à partir des données fournies par les différents scripts.

Le code contient un script par quotidien qui prend en compte les particularités des pages de ce quotidien. Il ets en effet nécesaire de se plier à la syntaxe particulière de pages d'un quotidien (disposition des unes, etc.).