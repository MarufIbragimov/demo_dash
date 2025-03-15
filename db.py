import duckdb

db_file = 'my.db'

def fetch_date_boundaries():
    with duckdb.connect(db_file) as duck:
        min_date, max_date = duck.query("""
            select
                date_trunc('month', min(order_date))
                , last_day(max(order_date))
            from sales
        """).fetchone()
        return min_date, max_date
    

def fetch_customers(report_date):
    with open('queries/customers.sql') as f:
        custs_query = f.read().format(report_date = report_date)
        print(custs_query)

    with duckdb.connect(db_file) as duck:
        temp_df = duck.query(custs_query).to_df()
    
    return temp_df

print(fetch_customers('2025-02-28'))