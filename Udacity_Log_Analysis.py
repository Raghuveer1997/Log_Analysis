#!/usr/bin/env python
import psycopg2


def QueryExecute(database_name="news"):
    try:
        link = psycopg2.connect("dbname={}".format(database_name))
        ind = link.cursor()
        return link, ind
    except BaseException:
        print("There is a problem connecting to the database.")

# To Print Three Most Favoured Stories


def Favoured_Stories():
    query1 = ''' SELECT title, topviews FROM popular_views LIMIT 3; '''
    try:
        link, ind = QueryExecute()
        ind.execute(query1)
        ot = ind.fetchall()
        link.close()
        print("--------------------------*----------------------------------")
        print("\n")
        print(" Q1)The Most popular three Stories of all time are:\n\n")
        for p in range(len(ot)):
            tit = ot[p][0]
            vws = ot[p][1]
            print("""   "{}" --> {:,} views
            """.format(tit, vws))
    except:
        print("\nThere is a problem fetching data about the top articles.\n")

# To Print Three Most Favoured Writers


def Favoured_Writers():
    query2 = '''
    SELECT DISTINCT name,
                      sum(topviews) AS topviews
                      FROM popular_views JOIN authors
                      ON (popular_views.author = authors.id)
                      GROUP BY name
                      ORDER BY topviews DESC;
    '''
    try:
        link, ind = QueryExecute()
        ind.execute(query2)
        ot = ind.fetchall()
        link.close()
        print("--------------------------*----------------------------------")
        print("\n")
        print("Q2)The Most popular Story Writers of all time are:\n\n")
        for p in range(len(ot)):
            aut = ot[p][0]
            all_vws = ot[p][1]
            print("""   {} --> {:,} views
            """.format(aut, all_vws))
    except:
        print("\nThere is problem fetching data about the popular authors.\n")

# To Print Days with more than 1% Faults


def Fault_Survey():
    query3 = '''
    select to_char(date,'DD Mon YYYY') as date,fault_prc from fault_perc where fault_prc > 1.0;
    '''
    try:
        link, ind = QueryExecute()
        ind.execute(query3)
        ot = ind.fetchall()
        link.close()
        print("--------------------------*----------------------------------")
        print("\n")
        print("Q3)Day with more than 1% of requests lead to Fault are:\n")
        for p in range(len(ot)):
            date = ot[p][0]
            pctgs = ot[p][1]
            print("   %s --> % .1f %% \n" % (date, pctgs))
    except:
        print("\nThere is a problem fetching data",
              "about the percentage of errors\n")


# To Print Out Answers
if __name__ == "__main__":
    Favoured_Stories()
    Favoured_Writers()
    Fault_Survey()
