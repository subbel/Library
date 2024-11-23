import mysql.connector as mc

def create_db():
    global DB_NAME
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost")
        if con.is_connected(): 
            cur=con.cursor() 
            DB_NAME=input("Enter Database Name : ")
            cur.execute("CREATE DATABASE if NOT Exists {}".format(DB_NAME))
            print(cur.rowcount)
            cur.execute("use {}".format(DB_NAME))
        else:
            print('sorry can\'t connect')
    except: print("some error")
    finally: con.close()
    
def create_tb():
    global TB_NAME
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            cur.execute("use {}".format(DB_NAME))
            TB_NAME=input("Enter Table Name : ")
            cur.execute('''CREATE TABLE if NOT Exists {}(comic_no int Primary key AUTO_INCREMENT, comic_name varchar(100) 
            Primary Key, genre varchar(30), publisher varchar(50), chapters int)'''
                          .format(TB_NAME))
        else:
            print('sorry can\'t connect')
    except: print("some error")
    finally: con.close()

def insert_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor() 
            nm = input("Enter Comic Name : ")
            gn = input("Enter Genre : ")
            pb = input("Enter Publisher : ")
            ch = float(input("Enter No of Chapters : "))
            sql="INSERT INTO MAN(comic_name,genre,publisher,chapters) VALUES(%s,%s,%s,%s)"
            cur.execute(sql,(nm,gn,pb,ch))
            con.commit()
            
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def delete_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            cname=input("Enter Comic Name : ")
            sql="delete FROM MAN WHERE comic_name = %s"
            cur.execute(sql,(cname,))
            con.commit()
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def display_all_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            sql="select * FROM MAN"
            cur.execute(sql)
            while True:
                i=cur.fetchone()
                if not i:
                    break
                print("Comic no {}".format(cur.rowcount))
                print("Comic Name {}".format(i[1]))
                print("Comic Genre {}".format(i[2]))
                print("Publisher {}".format(i[3]))
                print("Chapters {}".format(i[4]))
                print()
                      
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def search_comic_name_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            cname=int(input("Enter Comic Name : "))
            sql="select * FROM MAN where comic_name = %s"
            cur.execute(sql,(cname,))
            while True:
                i=cur.fetchone()
                if not i:
                    if cur.rowcount==-1:
                        print("sorry no such record found with this comic name")
                    break
                print("Comic no {}".format(cur.rowcount))
                print("Comic Name {}".format(i[1]))
                print("Comic Genre {}".format(i[2]))
                print("Publisher {}".format(i[3]))
                print("Chapters {}".format(i[4]))
                print()
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def search_genre_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            gen=input("Enter Genre : ")
            sql="select * FROM MAN where genre = %s"
            cur.execute(sql,(gen,))
            while True:
                i=cur.fetchone()
                if not i:
                    if cur.rowcount==-1:
                        print("sorry no such record found with this genre. ")
                    break
                print("Comic no {}".format(cur.rowcount))
                print("Comic Name {}".format(i[1]))
                print("Comic Genre {}".format(i[2]))
                print("Publisher {}".format(i[3]))
                print("Chapters {}".format(i[4]))
                print()
                      
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def update_name_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            og=input("Enter Comic Name : ")
            Chname=input("Enter Changed Name : ")
            sql="update MAN set comic_name=%s where comic_name = %s"
            cur.execute(sql,(Chname,og))
            con.commit()
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def update_publisher_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            og=input("Enter Comic Name : ")
            pub=input("Enter New Publisher :")
            sql="update MAN set publisher = %s where comic_name = %s"
            cur.execute(sql,(pub,og))
            con.commit()
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error "+str(err))
    finally: con.close()

def update_chapter_rec():
    try:
        con=mc.connect(user="root",password="Password123!",host="localhost",database='Library')
        if con.is_connected(): 
            cur=con.cursor()
            og=input("Enter Comic Name : ")
            chap=input("Enter Updated Chapter :")
            sql="update MAN set chap = %s where comic_name = %s"
            cur.execute(sql,(chap,og))
            con.commit()
        else:
            print('sorry can\'t connect')
    except Exception as err: print("some error "+str(err))
    finally: con.close()

def main():
    while True:
        print("Menu")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert a Record")
        print("4. Delete a Record")
        print("5. Display All Records")
        print("6. Search By Comic Name")
        print("7. Search By Genre")
        print("8. Modify Comic Name")
        print("9. Modify Publisher Name")
        print("10. Modify Chapter Numbers")
        print("11. Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            create_db()
        elif ch==2:
            create_tb()
        elif ch==3:
            insert_rec()
        elif ch==4:
            delete_rec()
        elif ch==5:
            display_all_rec()
        elif ch==6:
            search_comic_name_rec()
        elif ch==7:
            search_genre_rec()
        elif ch==8:
            update_name_rec()
        elif ch==9:
            update_publisher_rec()
        elif ch==10:
            update_chapter_rec()
        elif ch==11:
            quit()
main()

