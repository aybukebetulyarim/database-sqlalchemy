import datetime 
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from objectrm.loginfo import Log_info
from objectrm.lib import Library


def deleteRecord():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    deleteRec = input("Would you like to delete all records or one record? all/one: ")
    if deleteRec == 'all' or deleteRec == 'ALL':
        records = session.query(Library).all()
        session.delete(records)
        adding = Log_info(process="Library table is deleted.")
        session.add(adding)

    elif deleteRec == 'one' or deleteRec == 'ONE':
        idNum = int(input("Please enter a book id for delete: "))
        session.query(Library).filter(Library.book_id==idNum).delete()
        log = Log_info(process=f"Deleted {Library.book_id}.book, owner name is {Library.owner_name} book name is {Library.book_name}",lib_id=idNum)
        session.add(log)
        session.commit()
    else:
        print("Please JUST write 'one' or 'all'")

def query(id):
    query1 = session.query(Library).filter(Library.book_id==id).one()
    query2 = session.query(Library.owner_name).filter(Library.book_id==id).one()
    owner = query2.owner_name
    query3 = session.query(Library.book_name).filter(Library.book_id==id).one()
    bookname = query3.book_name

def adding(id,var):
    log = Log_info(process=f"book_id:{id}, owner_name:{query.owner}, new:{query.var}",lib_id=id)
    session.add(log)

def updateRecord():
    idNum = int(input("Please enter a book id for update: "))
    entry = int(input("Please enter a number 1-7 for record to change,\n1: for book name changes,\n2: for edition year changes,\n3: for author changes,\n\
4: for owner name changes,\n5: for category changes,\n6: for translator name changes,\n7: for all data changes for one book: "))

    if entry==1:
        name = input ("Please enter a new book name: ")
        query(idNum)
        query.query3.book_name = name
        adding(idNum,name)
    elif entry==2:
        year = input ("Please enter new edition year: ")
        query(idNum)
        query.query1.edition_year = year
        adding(id,year)
    elif entry==3:
        aut = input ("Please enter new author year: ")
        query(idNum)
        query.query1.author = aut
        adding(id,aut)
    elif entry==4:
        new_owner = input ("Please enter new owner name: ")
        query(idNum)
        query.query2.owner_name = new_owner
        adding(id,new_owner)
    elif entry==5:
        cat = input ("Please enter new category name: ")
        query(idNum)
        query.query1.category = cat
        adding(id,cat)
    elif entry==6:
        translatorName = input ("Please enter new translator name: ")
        query(idNum)
        query.query1.translator = translatorName
        adding(id,translatorName)
    elif entry==7:
        bookN      = input("Please enter a book name: ")
        edition    = input("Please enter an edition: ")
        author     = input("Please enter author name: ")
        owner      = input("Please enter owner name: ")
        category   = input("Please enter a category: ")
        translator = input("Please enter a translator name: ")
        date_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        queryall = session.query(Library).filter(Library.book_id==idNum).one()
        queryall.book_name     = bookN
        queryall.edition_year  = edition
        queryall.author        = author
        queryall.owner_name    = owner
        queryall.category      = category
        queryall.translator    = translator
        log = Log_info(process=f"book_id: {idNum}, book_name={bookN}, owner_name={owner}",lib_id=idNum)
        session.add(log)

engine = create_engine('sqlite:///database2.db')

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
book1 = Library(book_name="aa",edition_year=1999,author="aa",owner_name="aa",category="aa",translator="aa")
session.add(book1)
## Update ---> add(book_name, edition_year=1999,author="aa",owner_name="aa",category="aa",translator="aa")  
# deleteRecord()
# updateRecord()
# Base.metadata.drop_all(engine)

session.commit()