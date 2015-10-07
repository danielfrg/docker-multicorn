```
$ docker build -t pandasfdw .
$ docker run -p 5432:5432 -v $(pwd):/src pandasfdw
```

Connect to the Database (using pgadmin for example) create the FDW and Foreign table.

```
CREATE EXTENSION multicorn;

CREATE SERVER pandas_srv foreign data wrapper multicorn options (
    wrapper 'pandasfdw.PandasForeignDataWrapper'
);

CREATE FOREIGN TABLE pandastable (
    sepal_length numeric,
    sepal_width numeric,
    petal_length numeric,
    petal_width numeric,
    species character varying
) server pandas_srv options(
    filename '/src/iris.csv'
);
```

Now is possible to make SQL queries to the table.

```
SELECT * from pandastable;
SELECT * from pandastable where sepal_width < 2.5;
SELECT * from pandastable where sepal_width > 2.5;
```
