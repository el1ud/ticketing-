# #!/usr/bin/env python3

from faker import Faker
from app import app, db  # Adjust import based on your app structure
from models import User, Concert, Ticket, ConcertUser

fake = Faker()

def seed_users(n=10):
    for _ in range(n):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password_hash=fake.password()
        )
        user.set_password(fake.password())  # Use the set_password method
        db.session.add(user)
    db.session.commit()

def seed_concerts(n=5):
    for _ in range(n):
        concert = Concert(
            name=fake.company(),
            date=fake.date_time_this_year(),
            venue=fake.city(),
            image_url=fake.image_url()
        )
        db.session.add(concert)
    db.session.commit()

