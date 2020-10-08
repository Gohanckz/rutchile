### GENERADOR DE RUTS CHILENOS

```
#------------------------------------------------------------
# ----            GENERADOR DE DÍGITOS RUT CHILENOS     ----|
# ----            Gohanckz                              ----|
# ----            Contact : gohanckz@gmail.cl           ----|
# ----            Version : 2.0                         ----|
#------------------------------------------------------------
```

Genera diccionarios de ruts chilenos con y sin digito verificador para realizar fuerza bruta en tus proyectos de pentesting de manera ética.

#### Instalación

```
pip install -r requirements.txt
```

#### Uso

1. Generar diccionarios sin dígito verificador.

```
python3 rutchile.py -l 
```

2. Generar diccionario con dígito verificador.

```
python3 rutchile.py -d 
```

3. Generar diccionario con dígito verificador y guardar salida en un archivo

```
python3 rutchile.py -d -o <ruta/archivo.txt>
```
