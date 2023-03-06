# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

# Generador de Números Primos

Este programa genera una lista de números primos hasta un número dado.

## Uso

Para utilizar esta función, importe el módulo `prime_numbers` y llame la función `generate_primes` con un número entero como argumento:

```python
import prime_numbers

primes = prime_numbers.generate_primes(10)
print(primes)

