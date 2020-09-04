from django.shortcuts import render
from .models import User

# username = None
# Create your views here.
def home(responce):
    return render(responce, 'note_site_home.html')

def signup(responce):
    return render(responce, 'note_site_signup.html', {'is_login_failed': False})

def dashboard(responce):
    # global username
    if responce.method == 'POST':
        username = responce.POST.get('username')
        password = responce.POST.get('password')
        try:
            user = User.objects.get(username=username)
            print(user)
            # print(user)
            notes = user.note_set.all()
            if password == user.password:
                for note in list(notes):
                    if note.note.strip()=='':
                        note.delete()
                user.note_set.create(note='')
                    # pass
                notes = user.note_set.all()
                return render(responce, 'note_site_dashboard.html', {'notes': enumerate(notes), 'username':username})
            else:
                print('failed login')
                return render(responce, 'note_site_home.html', {"is_login_failed": True})
        except:
            print('Failed login')
            return render(responce, 'note_site_home.html', {"is_login_failed": True})

def new_dashboard(responce):
    # global username
    if responce.method == 'POST':
        username = responce.POST.get('username')
        password = responce.POST.get('password')
        confirm_password = responce.POST.get('confirm-password')
        if password != confirm_password:
            print('pass mismatch')
            return render(responce, 'note_site_signup.html', {"is_signup_failed": True})
        for user in User.objects.all():
            if user.username == username:
                print('username already exist')
                return render(responce, 'note_site_signup.html', {"is_signup_failed": True})
        t = User.objects.create(username=username, password=password)
        print(User.objects.all())
        t.note_set.create(note='')
        return render(responce, 'note_site_dashboard.html', {'notes': enumerate([""]), 'username':username})

def save(responce):
    if responce.method == 'POST':
        # print(username) 
        username = responce.POST.get('username')
        user = User.objects.get(username=username)
        # print(user)
        for ind, note in enumerate(user.note_set.all()):
            t = responce.POST.get(f'TA{ind}')
            # print(t)
            note.note = t
            note.save()
            
        for note in list(user.note_set.all()):
            if note.note.strip()=='':
                note.delete()
        user.note_set.create(note='')
    notes = user.note_set.all()
    # print(notes, 'heyyyyyyyyyyyy')
    return render(responce, 'note_site_dashboard.html', {'notes': enumerate(notes), 'username':username})