import os

def populate():
    # Add/create models here
    pass

def add_model():
    # use object.get_or_create here and take the 0th index [0]
    pass

# Start execution here!
if __name__ == '__main__':
    print "Starting database population script"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orthotics_project.settings')
    # from app.models import <model>, <model>
    populate()
