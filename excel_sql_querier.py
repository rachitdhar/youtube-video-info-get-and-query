import duckdb
from tabulate import tabulate

def main():
    print("**************** SQL Querier for Excel ****************")
    print()
    conn = duckdb.connect()
    
    while True:
        query = input(">> ")
        try:
            query = query.replace("videos", "'videos.xlsx'")
            query = query.replace("Videos", "'videos.xlsx'")
            sql_result = conn.execute(query).fetchall()
            
            cols = [desc[0] for desc in conn.description]
            print(tabulate(sql_result, headers=cols, tablefmt="grid"))
            print()
        except Exception as e:
            print(f"Error occurred in executing the sql query : {e}\n")
            

if __name__ == '__main__':
    main()