from django.shortcuts import render
import sqlite3
# Create your views here.
def index(request):
    conn = sqlite3.connect('FFF.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    data = cursor.fetchmany()
    print(data)

    conn.close()
    return render(request, 'index.html',{'data':data})
