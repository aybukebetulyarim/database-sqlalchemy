import datetime
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from log_info import *
from library import *


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

def updateRecord():
    idNum = int(input("Please enter a book id for update: "))
    entry = int(input("Please enter a number 1-7 for record to change,\n1: for book name changes,\n2: for edition year changes,\n3: for author changes,\n\
4: for owner name changes,\n5: for category changes,\n6: for translator name changes,\n7: for all data changes for one book: "))

    if entry==1:
        name = input ("Please enter a new book name: ")
        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query1.book_name = name
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum).one()
        owner = query2.owner_name
        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} new book name is {name}",lib_id=idNum)
        session.add(log)
    elif entry==2:
        year = input ("Please enter new edition year: ")
        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query1.edition_year = year
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum)
        owner = query2.owner_name
        query3 = session.query(Library.book_name).filter(Library.book_id==idNum).one()
        bookname = query3.book_name
        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} book name is {bookname} new edition year is {year}",lib_id=idNum)
        session.add(log)
    elif entry==3:
        aut = input ("Please enter new author year: ")
        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum).one()
        owner = query2.owner_name
        query3 = session.query(Library.book_name).filter(Library.book_id==idNum).one()
        bookname = query3.book_name
        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} book name is {bookname} new author is {query1.author}",lib_id=idNum)
        session.add(log)
    elif entry==4:
        new_owner = input ("Please enter new owner name: ")
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum).one()
        owner = query2.owner_name

        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query1.owner_name = new_owner

        query3 = session.query(Library.book_name).filter(Library.book_id==idNum).one()
        bookname=query3.book_name

        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} book name is {bookname} new owner name is {new_owner}",lib_id=idNum)
        session.add(log)
    elif entry==5:
        cat = input ("Please enter new category name: ")
        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query1.category = cat
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum).one()
        owner = query2.owner_name
        query3 = session.query(Library.book_name).filter(Library.book_id==idNum).one()
        bookname=query3.book_name
        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} book name is {bookname} new category name is {cat}",lib_id=idNum)
        session.add(log)
    elif entry==6:
        translatorName = input ("Please enter new translator name: ")
        query1 = session.query(Library).filter(Library.book_id==idNum).one()
        query1.translator = translatorName
        query2 = session.query(Library.owner_name).filter(Library.book_id==idNum).one()
        owner = query2.owner_name
        query3 = session.query(Library.book_name).filter(Library.book_id==idNum).one()
        bookname=query3.book_name
        log = Log_info(process=f"Updated {idNum}.book, owner name is {owner} book name is {bookname} new translator name is {translatorName}",lib_id=idNum)
        session.add(log)
    elif entry==7:
        bookN = input("Please enter a book name: ")
        edition = input("Please enter an edition: ")
        author = input("Please enter author name: ")
        owner = input("Please enter owner name: ")
        category = input("Please enter a category: ")
        translator = input("Please enter a translator name: ")
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        queryBookName = session.query(Library).filter(Library.book_id==idNum).one()
        queryBookName.book_name = bookN
        queryEdition = session.query(Library).filter(Library.book_id==idNum).one()
        queryEdition.edition_year =  edition
        queryAuthor = session.query(Library).filter(Library.book_id==idNum).one()
        queryAuthor.author = author
        queryOwner = session.query(Library).filter(Library.book_id==idNum).one()
        queryOwner.owner_name = owner
        queryCategory = session.query(Library).filter(Library.book_id==idNum).one()
        queryCategory.category = category
        queryTrans = session.query(Library).filter(Library.book_id==idNum).one()
        queryTrans.translator = translator
        log = Log_info(process=f"{idNum}.book all informations about book updated",lib_id=idNum)
        session.add(log)

engine = create_engine('sqlite:////home/turkai/Desktop/database2/librarydatabase.db')

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
book1 = Library(book_name="aa",edition_year=1999,author="aa",owner_name="aa",category="aa",translator="aa")
session.add(book1)

# deleteRecord()

# updateRecord()
# Base.metadata.drop_all(engine)

session.commit()