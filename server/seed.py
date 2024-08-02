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

def seed_tickets(n=20):
    users = User.query.all()
    concerts = Concert.query.all()
    
    for _ in range(n):
        ticket = Ticket(
            seat_number=fake.word(),
            price=fake.random_number(digits=2),
            user_id=fake.random_element(elements=[user.id for user in users]),
            concert_id=fake.random_element(elements=[concert.id for concert in concerts])
        )
        db.session.add(ticket)
    db.session.commit()

def seed_concert_users(n=15):
    users = User.query.all()
    concerts = Concert.query.all()
    
    for _ in range(n):
        concert_user = ConcertUser(
            user_id=fake.random_element(elements=[user.id for user in users]),
            concert_id=fake.random_element(elements=[concert.id for concert in concerts]),
            user_rating=fake.random_number(digits=1)
        )
        db.session.add(concert_user)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_users()
        seed_concerts()
        seed_tickets()
        seed_concert_users()
        print("Database seeded!")
