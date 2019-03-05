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
    query1 = ''' SELECT title, views FROM logsurvey_story,articles WHERE
    articles.slug = logsurvey_story.slug ORDER BY views desc LIMIT 3; '''
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
            print("""   "{}" - {:,} views
            """.format(tit, vws))
    except:
        print("\nThere is a problem fetching data about the top articles.\n")

# To Print Three Most Favoured Writers


def Favoured_Writers():
    query2 = '''
    SELECT logwriter_title.name AS author,
    sum(logsurvey_story.views) AS views FROM logsurvey_story,logwriter_title
    WHERE logwriter_title.slug=logsurvey_story.slug
    GROUP BY logwriter_title.name ORDER BY views desc limit 4;
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
            print("""   {} - {:,} views
            """.format(aut, all_vws))
    except:
        print("\nThere is problem fetching data about the popular authors.\n")

# To Print Days with more than 1% Faults


def Fault_Survey():
    query3 = '''
    SELECT logfault_abort.date ,
    (logfault_abort.count*100.00 / logsurvey_overall.count)
    AS percentage
    FROM logfault_abort,logsurvey_overall
    WHERE logfault_abort.date = logsurvey_overall.date
    AND (logfault_abort.count*100.00 / logsurvey_overall.count) >1
    ORDER BY (logfault_abort.count*100.00 /logsurvey_overall.count) desc;
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
            print("   %s -- % .1f %% \n" % (date, pctgs))
    except:
        print("\nThere is a problem fetching data",
              "about the percentage of errors\n")


# To Print Out Answers
if __name__ == "__main__":
    Favoured_Stories()
    Favoured_Writers()
    Fault_Survey()
