NumberOfEmployees=int(input('Number of Employees : '))    # تعداد کارمندان
i=1
while i <= NumberOfEmployees :    # اگر شمارنده کوچکتر یا مساوی بود حلقه را ادامه بده
    EmployeePersonalNumber =int(input('Please enter the personnel number of your employee : '))
    HoursOfWork=int(input('How many hours did you work per month? '))
    SalaryPerHour=int(input('What is the salary per hour? '))
    overtimeWork =0   # اضافه کاری
    i=i+1
    if HoursOfWork >40 :
        overtimeWork=(3/2-1)*(HoursOfWork-40)*SalaryPerHour
    salary=HoursOfWork*SalaryPerHour+overtimeWork
    print('The salary of the employee with personnel number ',EmployeePersonalNumber ,
    ' is ',salary ,'$. with ',HoursOfWork, ' working hours and ',overtimeWork,'$ overtime .')
# برنامه ای بنویسید که به تعداد کارمندان ،شماره پرسنلی ،ساعت کاری و دستمزد ساعتی کارمندان را گرفته و حقوق آن را محاسبه کند .
#  اگر کارمند بیش از 40 ساعت اضافه کاری داشته باشد ،اضافه کاری به او تعلق میگیرد .
#  به ازای هر ساعت کاری 2/3 دستمزد ساعتی به عنوان اضافه کاری پرداخت میشود . 