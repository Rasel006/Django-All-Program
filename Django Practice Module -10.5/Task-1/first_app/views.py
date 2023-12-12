from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def home(request):
    return render(request, 'PracticesWork/home.html')

def Practices(request):
    dictornary = {
        'namelist':['Rasel', 'is' , 'a', 'simple', 'boy'],
        'datafilter':datetime.now(),
        'fordefaultuse':None,
        'ForAddFilterINT':10,
        'ForCapfirstFilter':'dhaka',
        'ForCutFilter':"R a s e l",
        'ForDictsortFilter':[
            {'name': 'Rasel', 'age': 21},
            {'name': 'Rean', 'age': 29},
            {'name': 'Tahsin', 'age': 23},
            {'name': 'Mahin', 'age': 27},
        ],
        'ForEscapeFilter':"<strong>Rasel</strong> is Good < BOY",
        'ForFirstFilter':['Apple', 'Mango', 'Orenge'],
        'ForLastFilter':['Apple', 'Mango', 'Orenge'],
        'ForLengthFilter':['Apple', 'Mango', 'Orenge','Pinapple','Avacado'],
        'ForLinenumbersFilter':'"First Line \nSecond Line \nThird Line',
        'ForLowerFilter':'RASEL IS DOING WELL IN LOWER',
        'ForUpperFilter':'rasel is doing well in upper',
        'ForTitleFilter':'rasel is doing well in Title',
        'ForRandomFilter':['a','b','c','d','e'],
        'ForSliceFilter':['a','b','c','d','e'],
        'ForTimeFilter': datetime.now(),
        'ForTimesinceFilter':datetime.now() - timedelta(days=2),
        'ForTruncatecharsFilter':"Rasel is simple boy",
        'ForWordcountFilter':"Rasel is a simple boy. He is a university student",
        'ForTruncatewordsFilter':"Mahin is a brilliant boy. He is a university student",
        'ForStriptagsFilter':"<b>I</b> <button>love</button> <span>dogs</span>", 
        'ForPluralizeFilter': 4,
        'ForMake_listFilter': "Rasel",
        'Foraddslashes':"I'm Rasel",
        'ForCenterFilter':"Rasel",
        'Fordivisibleby':7,
        'Forfilesizeformat': 3342323,
        'Forslugify':"Rasel is number 1",
        'ListOfValue':['Course','Price','Seats'],
        'ListOfValueCourseName':['C','Cpp','Python','Django'],
        




        
    }
    return render(request, 'PracticesWork/Pactices.html',dictornary)