import psycopg2
conn = psycopg2.connect(dbname="qa_db_22_86",
                        user="user_22_86",
                        password="123",
                        host="159.69.151.133",
                        port="5056")

cursor = conn.cursor()

# if conn:
#     print("Connection qa_db_22_86 ")
#
#     select_query = "select * from public.salary_2"
#     execute_q = cursor.execute(select_query)
#     get_query_result = cursor.fetchall()
#
#     print("execute_q = ", execute_q)
#
#     for i in get_query_result:
#         print("id = ", i[0], "salary = ", i[1])
# for i in range(0, 10):
#
#     if conn:
#         print("Connection_insert qa_db_22_86 ")
#
#         salary = str(6000 + i*100)
#         insert_query = "Insert into public.salary_2(monthly_salary)" \
#                         "values (" + salary + ")"
#
#         cursor.execute(insert_query)
#
#         conn.commit()
#
# cursor.close()


# for i in range(1, 10):
#
#     if conn:
#
#         role_name = "'Python_" + str(i) + "'"
#         insert_query = "insert into public.roles_2(role_title)" \
#                        "values (" + role_name + ")"
#
#         print("insert_query", insert_query)
#         cursor.execute(insert_query)
#
#         conn.commit()

cursor.close()

if conn:
    print("Connection qa_db_22_86 ")

    select_query = "select * from public.salary_2;"
    sql = "'select * from salary_2'"

    cursor.execute(sql)
    print(cursor.description[0][1])
    # column_names = [desc(0) for desc in cursor.description]
    # for i in column_names:
    #     print(i)
    conn.commit()
    conn.close()