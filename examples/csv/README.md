```
$ docker run -p 5432:5432 -v $(pwd):/src multicorn
```

Connect to the Database (using pgadmin for example) create the FDW and Foreign table.

```
CREATE EXTENSION multicorn;

CREATE SERVER csv_srv foreign data wrapper multicorn options (
    wrapper 'multicorn.csvfdw.CsvFdw'
);

create foreign table csvtest (
      sepal_length numeric,
      sepal_width numeric,
      petal_length numeric,
      petal_width numeric,
      species character varying
) server csv_srv options (
      filename '/src/iris.csv',
      skip_header '1',
      delimiter ','
);
```

Now is possible to make SQL queries to the table.

```
select * from csvtest;
select sepal_width from csvtest;
```
