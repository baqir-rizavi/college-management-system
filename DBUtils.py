class SQLQueryGenerator:
    @staticmethod
    def generate_update_query(table_name: str, sql_condition: str, set_values: dict) -> str:
        query = f"UPDATE {table_name}\nSET"
        for atrib, value in set_values.items():
            if type(value) != str:
                query += f" {atrib} = {value},"
            else:  # for str
                query += f" {atrib} = '{value}',"
        query = query[:-1]
        query += f"\nWHERE {sql_condition};"
        return query
