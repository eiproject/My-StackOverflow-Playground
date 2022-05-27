companylist=['a','b','c']
sql = ("""select * from company_data cd  where cd.company_id = ANY(ARRAY{})""".format(companylist))
priceItem = connection.execute(sql).fetchAll()